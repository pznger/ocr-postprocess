"""OCR 后处理流水线 —— 一键入口。

使用方法（最简）：
    # 把 md（和对应的 pdf）丢进 input/，然后：
    python ocr-postprocess/pipeline.py

    # 只处理单个文件：
    python ocr-postprocess/pipeline.py --md raw/民用建筑设计统一标准.md

流程：
  1. strip_frontmatter    剥离前言/目录
  2. text_normalize       OCR 噪声规则归一化
  2b. page_break_join     检测/拼接被页码截断的句子（可选 LLM 确认）
  3. text_clean_llm       （可选）调 LLM 修复规则处理不了的乱码段落
  4. normalize_headings   标题层级统一到 # / ##
  4a. strip_bare_number_bold  清理 OCR 原材料自带的 **1** / **2** 裸数字加粗
  4b. bold_clause_numbers     x.y.z 条款编号加粗
  5. formula_verify + symbol_verify + table_verify
                          默认 dry-run 出复核清单；
                          当 input/ 有同名 PDF 时自动启用 VLM 校对；
                          符号定义错误自动检测修复；
                          生成 summary-report.md 汇总所有修改
  6. splitter -> wiki/

输出：ocr-postprocess/output/<规范名>/
"""

from __future__ import annotations

import argparse
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
REPO_ROOT = ROOT.parent
INPUT_DIR = ROOT / "input"
OUTPUT_ROOT = ROOT / "output"

sys.path.insert(0, str(ROOT))

from postprocess.strip_frontmatter import strip_frontmatter
from postprocess.normalize_headings import normalize_headings
from postprocess.text_normalize import normalize_text, strip_bare_number_bold, bold_clause_numbers
from postprocess.page_break_join import find_candidates, join_with_llm, write_dry_run_report as write_pb_report
from postprocess.checkpoint import Checkpoint
from postprocess.text_clean_llm import clean_with_llm, write_dry_run_report
from postprocess.formula_verify import FormulaChange, write_formula_report, verify_with_vlm as verify_formulas
from postprocess.table_verify import write_table_report, verify_with_vlm as verify_tables
from postprocess.symbol_verify import write_symbol_report, verify_symbols_with_vlm
from postprocess.summary_report import SummaryReport
from postprocess.splitter import split_to_wiki


# ── PDF 自动配对 ───────────────────────────────────────

def _find_pdf(md_path: Path) -> Path | None:
    """在 md 同级目录找同名 PDF（允许文件名微小偏差）。"""
    candidates = list(md_path.parent.glob(md_path.stem + ".pdf"))
    if candidates:
        return candidates[0]
    # 尝试去掉括号里的内容再匹配，比如 "GB 50017-2017 钢结构设计标准（含条文说明）"
    stem_short = md_path.stem.split("（")[0].split("(")[0].strip()
    if stem_short != md_path.stem:
        candidates = list(md_path.parent.glob(stem_short + ".pdf"))
        if candidates:
            return candidates[0]
    return None


# ── 单文件流水线 ────────────────────────────────────────

def process_one(
    md_path: Path,
    *,
    output_root: Path = OUTPUT_ROOT,
    pdf_path: Path | None = None,
    use_vlm: bool = True,
    use_llm_clean: bool = False,
    api_key: str | None = None,
    base_url: str | None = None,
    model: str | None = None,
    skip_split: bool = False,
) -> Path:
    spec_name = md_path.stem
    work_dir = output_root / spec_name
    work_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n{'='*60}")
    print(f"  {spec_name}")
    print(f"{'='*60}")

    # 自动配对 PDF
    if pdf_path is None:
        pdf_path = _find_pdf(md_path)
    has_pdf = pdf_path is not None and pdf_path.exists()
    if has_pdf:
        print(f"  [pdf] 自动配对 -> {pdf_path.name}")
    else:
        print("  [pdf] 未找到同名 PDF（VLM 阶段将仅生成复核清单）")

    text = md_path.read_text(encoding="utf-8")

    # 断点续跑
    ck = Checkpoint(work_dir / "checkpoint.json")

    # ── 1. 剥离前言 / 目录 ──
    text, meta = strip_frontmatter(text)
    print(f"  [1] strip_frontmatter: -{meta['dropped_lines']} 行, 首章 -> {meta['marker']}")
    (work_dir / "01-stripped.md").write_text(text, encoding="utf-8")

    # ── 2. OCR 噪声归一化（规则） ──
    text = normalize_text(text)
    print("  [2] text_normalize: 规则归一化完成")
    (work_dir / "02-normalized.md").write_text(text, encoding="utf-8")

    # ── 2b. 跨页断句拼接 ──
    n_pb = write_pb_report(text, work_dir / "page-break-report.md")
    if n_pb > 0 and use_llm_clean:
        text, n_joined = join_with_llm(
            text,
            api_key=api_key, base_url=base_url, model=model,
            dry_run=False, checkpoint=ck,
            on_progress=lambda c, t, j: print(f"\r  [2b] 跨页断句 {c}/{t}（已拼接 {j}）", end="", flush=True),
        )
        print(f"\r  [2b] page_break_join: {n_joined}/{n_pb} 处已拼接")
    else:
        print(f"  [2b] page_break_join: {n_pb} 处候选（dry-run，加 --llm-clean 启用 LLM 确认）")
    (work_dir / "02b-page-joined.md").write_text(text, encoding="utf-8")

    # ── 3. LLM 段落清洗（可选） ──
    if use_llm_clean:
        n_suspicious = write_dry_run_report(text, work_dir / "text-clean-report.md")
        if n_suspicious > 0:
            text, repaired = clean_with_llm(
                text,
                api_key=api_key,
                base_url=base_url,
                model=model,
                dry_run=False, checkpoint=ck,
                on_progress=lambda c, t, f: print(f"\r  [3] 段落清洗 {c}/{t}（已修复 {f}）", end="", flush=True),
            )
            print(f"\r  [3] text_clean_llm: {repaired}/{n_suspicious} 段已修复")
        else:
            print("  [3] text_clean_llm: 无可疑段落，跳过")
        (work_dir / "02c-llm-cleaned.md").write_text(text, encoding="utf-8")
    else:
        print("  [3] text_clean_llm: 跳过（--no-llm-clean）")

    # ── 4. 标题归一化 ──
    text = normalize_headings(text)
    print("  [4] normalize_headings: 层级折叠为 # / ##")
    (work_dir / "04-headings.md").write_text(text, encoding="utf-8")

    # ── 4a. 清理 OCR 自带的裸数字加粗 ──
    text = strip_bare_number_bold(text)
    print("  [4a] strip_bare_bold: **1** / **2** 裸数字加粗已清理")

    # ── 4b. 条款编号加粗 ──
    text = bold_clause_numbers(text)
    print("  [4b] bold_clause: x.y.z 条款编号加粗完成")
    (work_dir / "04b-clause-bold.md").write_text(text, encoding="utf-8")

    # ── 5. 公式 / 符号 / 表格复核 ──
    n_formula = write_formula_report(text, work_dir / "formula-report.md")
    n_symbol = write_symbol_report(text, work_dir / "symbol-report.md")
    n_table = write_table_report(text, work_dir / "table-report.md")
    print(f"  [5a] 公式 {n_formula} 处 -> formula-report.md")
    print(f"  [5b] 符号 {n_symbol} 处 -> symbol-report.md")
    print(f"  [5c] 表格 {n_table} 张  -> table-report.md")

    formula_changes: list[FormulaChange] = []
    symbol_hits: list = []
    table_hits: list = []

    vlm_ran = False
    if use_vlm and has_pdf and (n_formula > 0 or n_symbol > 0 or n_table > 0):
        if n_formula > 0:
            text, _ = verify_formulas(
                text, pdf_path,
                api_key=api_key, base_url=base_url, model=model, dry_run=False, checkpoint=ck,
                on_progress=lambda c, t: print(f"\r  [5a] 公式复核 {c}/{t}", end="", flush=True),
                changes=formula_changes,
            )
            print(f"\r  [5a] 公式复核完成（修正 {len(formula_changes)} 处）")
        if n_symbol > 0:
            text, symbol_hits = verify_symbols_with_vlm(
                text, pdf_path,
                api_key=api_key, base_url=base_url, model=model, dry_run=False, checkpoint=ck,
                on_progress=lambda c, t: print(f"\r  [5b] 符号复核 {c}/{t}", end="", flush=True),
            )
            modified = len([h for h in symbol_hits if h.suggested_line])
            print(f"\r  [5b] 符号复核完成（修正 {modified} 处）")
        if n_table > 0:
            text, table_hits = verify_tables(
                text, pdf_path,
                api_key=api_key, base_url=base_url, model=model, dry_run=False, checkpoint=ck,
                on_progress=lambda c, t: print(f"\r  [5c] 表格复核 {c}/{t}", end="", flush=True),
            )
            print(f"\r  [5c] 表格复核完成")
        vlm_ran = True

        # 重新写入带修改标记的报告
        write_formula_report(text, work_dir / "formula-report.md", changes=formula_changes)
        write_symbol_report(text, work_dir / "symbol-report.md")
        write_table_report(text, work_dir / "table-report.md")

        print("  [5d] VLM 校验完成")
    elif use_vlm and not has_pdf:
        print("  [5d] VLM 跳过（无 PDF）")
    else:
        print("  [5d] VLM 跳过")

    # 始终生成汇总报告（dry-run 时显示待复核清单，VLM 后展示修改详情）
    summary = SummaryReport(spec_name=spec_name)
    summary.formula_total = n_formula
    summary.symbol_total = n_symbol
    summary.table_total = n_table
    if formula_changes:
        summary.add_formula_changes(formula_changes)
    if symbol_hits:
        summary.add_symbol_changes(symbol_hits)
    if table_hits:
        summary.add_table_changes(table_hits)
    if not vlm_ran:
        summary.add_extra(
            "说明",
            "当前为 **dry-run 模式**（未启用 VLM），上列数据为疑似 OCR 错误清单，"
            "去除 `--no-vlm` 参数运行流水线将自动调用 VLM 修正。",
        )
    summary.write(work_dir / "summary-report.md")
    print(f"  [5e] 汇总报告 -> summary-report.md")

    final_md = work_dir / "05-final.md"
    final_md.write_text(text, encoding="utf-8")

    # ── 6. 拆分 ──
    if not skip_split:
        wiki_root = work_dir / "wiki"
        if wiki_root.exists():
            shutil.rmtree(wiki_root)
        wiki_root.mkdir(parents=True, exist_ok=True)
        tmp_input = work_dir / f"{spec_name}.md"
        shutil.copy(final_md, tmp_input)
        split_to_wiki(tmp_input, wiki_root=wiki_root, repo_root=REPO_ROOT, spec_name=spec_name)
        print(f"  [6] split_wiki -> {wiki_root}")
    else:
        print("  [6] split 跳过")

    return final_md


# ── CLI ─────────────────────────────────────────────────

def main() -> None:
    p = argparse.ArgumentParser(
        description="OCR 后处理流水线 —— 一键清洗 + 拆分",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""\
示例:
  python pipeline.py                          # 处理 input/ 下所有 .md
  python pipeline.py --md raw/xxx.md          # 只处理单个
  python pipeline.py --no-vlm                 # 即使有 PDF 也不调 VLM
  python pipeline.py --llm-clean              # 额外启用 LLM 段落清洗
  python pipeline.py --skip-split             # 只出清洗结果，不拆 wiki
""",
    )
    p.add_argument("--md", type=Path, default=None, help="单文件模式")
    p.add_argument("--input-dir", type=Path, default=INPUT_DIR)
    p.add_argument("--output-root", type=Path, default=OUTPUT_ROOT)
    p.add_argument("--no-vlm", action="store_true", help="禁止 VLM 校验")
    p.add_argument("--llm-clean", action="store_true", help="启用 LLM 段落级 OCR 修复")
    p.add_argument("--skip-split", action="store_true", help="跳过 wiki 拆分")
    p.add_argument("--api-key", default=None, help="覆盖默认 API key")
    p.add_argument("--base-url", default=None, help="覆盖默认 base URL")
    p.add_argument("--model", default=None, help="覆盖默认模型")
    args = p.parse_args()

    args.output_root.mkdir(parents=True, exist_ok=True)

    if args.md:
        if not args.md.exists():
            print(f"[error] {args.md} 不存在")
            sys.exit(1)
        md_paths = [args.md]
    else:
        md_paths = sorted(args.input_dir.glob("*.md"))
        if not md_paths:
            print(f"[warn] {args.input_dir} 中没有 .md 文件")
            return
        print(f"发现 {len(md_paths)} 个 .md 文件")

    for md in md_paths:
        process_one(
            md,
            output_root=args.output_root,
            use_vlm=not args.no_vlm,
            use_llm_clean=args.llm_clean,
            api_key=args.api_key,
            base_url=args.base_url,
            model=args.model,
            skip_split=args.skip_split,
        )

    print(f"\n完成。输出 -> {args.output_root}")


if __name__ == "__main__":
    main()
