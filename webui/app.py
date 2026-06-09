"""OCR 后处理 Web UI —— Flask 应用。

启动：
    python ocr-postprocess/webui/app.py
    # 浏览器打开 http://127.0.0.1:5000

功能：
  - 上传 MD + PDF，自动配对
  - 分步执行流水线（前置剥离 → 文本归一化 → 标题折叠 → 编号加粗 → 拆分）
  - 每一步产出可预览
  - PDF ↔ MD 左右对照查看（按页码同步）
"""

from __future__ import annotations

import base64
import io
import json
import os
import queue
import re
import shutil
import sys
import threading
import time
import uuid
from pathlib import Path

from flask import (
    Flask, render_template, request, jsonify, send_file,
    Response, stream_with_context,
)

# ── 路径 ────────────────────────────────────────────────
WEBUI_DIR = Path(__file__).resolve().parent
ROOT_DIR = WEBUI_DIR.parent
REPO_ROOT = ROOT_DIR.parent
UPLOAD_DIR = WEBUI_DIR / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

sys.path.insert(0, str(ROOT_DIR))

from postprocess.strip_frontmatter import strip_frontmatter
from postprocess.text_normalize import normalize_text, strip_bare_number_bold, bold_clause_numbers
from postprocess.page_break_join import join_with_llm, find_candidates
from postprocess.normalize_headings import normalize_headings
from postprocess.splitter import split_to_wiki

app = Flask(__name__)
app.config["MAX_CONTENT_LENGTH"] = 500 * 1024 * 1024  # 500 MB

# ── 进度事件队列 ─────────────────────────────────────────
_progress_queues: dict[str, queue.Queue] = {}


def _emit(job_id: str, stage: str, msg: str, pct: int = 0):
    q = _progress_queues.get(job_id)
    if q:
        q.put({"stage": stage, "msg": msg, "pct": pct})


# ── 路由 ─────────────────────────────────────────────────

@app.route("/")
def index():
    """主页面：上传 + 流水线控制"""
    return render_template("index.html")


@app.route("/viewer/<job_id>")
def viewer(job_id):
    """对照查看页面"""
    return render_template("viewer.html", job_id=job_id)


# ── API：上传 ────────────────────────────────────────────

@app.route("/api/upload", methods=["POST"])
def api_upload():
    """上传 MD + PDF，返回 job_id。"""
    md_file = request.files.get("md")
    if not md_file or not md_file.filename.endswith(".md"):
        return jsonify({"error": "请上传 .md 文件"}), 400

    job_id = uuid.uuid4().hex[:12]
    job_dir = UPLOAD_DIR / job_id
    job_dir.mkdir(parents=True)

    md_path = job_dir / md_file.filename
    md_file.save(md_path)

    pdf_path = None
    pdf_file = request.files.get("pdf")
    if pdf_file and pdf_file.filename.endswith(".pdf"):
        pdf_path = job_dir / pdf_file.filename
        pdf_file.save(pdf_path)

    # 每个 job 独立进度队列
    _progress_queues[job_id] = queue.Queue()

    return jsonify({
        "job_id": job_id,
        "md_name": md_path.name,
        "has_pdf": pdf_path is not None,
        "pdf_name": pdf_path.name if pdf_path else None,
    })


# ── API：流水线 ──────────────────────────────────────────

@app.route("/api/run", methods=["POST"])
def api_run():
    """启动流水线（异步）。"""
    data = request.get_json()
    job_id = data.get("job_id")
    stage = data.get("stage", "all")  # all | single stage name
    job_dir = UPLOAD_DIR / job_id
    md_files = list(job_dir.glob("*.md"))
    if not md_files:
        return jsonify({"error": "未找到 md 文件"}), 400
    md_path = md_files[0]

    # 自动找 PDF
    pdf_files = list(job_dir.glob("*.pdf"))
    pdf_path = pdf_files[0] if pdf_files else None

    if job_id not in _progress_queues:
        _progress_queues[job_id] = queue.Queue()

    thread = threading.Thread(
        target=_run_pipeline, args=(job_id, md_path, pdf_path, job_dir, stage),
        daemon=True,
    )
    thread.start()
    return jsonify({"status": "started"})


@app.route("/api/progress/<job_id>")
def api_progress(job_id):
    """SSE 端点：推送流水线进度。"""
    q = _progress_queues.get(job_id)
    if not q:
        return Response("data: {}\n\n", mimetype="text/event-stream")

    def stream():
        while True:
            try:
                msg = q.get(timeout=30)
                yield f"data: {json.dumps(msg, ensure_ascii=False)}\n\n"
                if msg.get("stage") == "done" or msg.get("stage") == "error":
                    break
            except queue.Empty:
                yield f"data: {json.dumps({'stage': 'ping'})}\n\n"

    return Response(stream_with_context(stream()), mimetype="text/event-stream")


def _run_pipeline(job_id: str, md_path: Path, pdf_path: Path | None, job_dir: Path, stage: str):
    """后台执行流水线。"""
    try:
        text = md_path.read_text(encoding="utf-8")

        # 1. 剥离前置
        _emit(job_id, "strip", "剥离前言/目录...", 5)
        text, meta = strip_frontmatter(text)
        (job_dir / "01-stripped.md").write_text(text, encoding="utf-8")
        _emit(job_id, "strip", f"完成：丢弃 {meta['dropped_lines']} 行", 10)

        # 2. 文本归一化
        _emit(job_id, "normalize", "OCR 噪声归一化...", 15)
        text = normalize_text(text)
        (job_dir / "02-normalized.md").write_text(text, encoding="utf-8")
        _emit(job_id, "normalize", "完成：规则归一化", 25)

        # 2b. 跨页断句拼接（dry-run 出报告，LLM 确认需 --llm-clean）
        _emit(job_id, "pagebreak", "检测跨页断句...", 28)
        candidates = find_candidates(text)
        if candidates:
            text, n_joined = join_with_llm(text, dry_run=False)
            _emit(job_id, "pagebreak", f"完成：{n_joined}/{len(candidates)} 处拼接", 32)
        else:
            _emit(job_id, "pagebreak", "无跨页断句", 32)

        # 3. 标题归一化
        _emit(job_id, "headings", "标题层级折叠...", 30)
        text = normalize_headings(text)
        (job_dir / "03-headings.md").write_text(text, encoding="utf-8")
        _emit(job_id, "headings", "完成：只保留 # / ##", 45)

        # 4. 清理裸数字加粗
        _emit(job_id, "bare-bold", "清理 OCR 自带裸数字加粗...", 50)
        text = strip_bare_number_bold(text)

        # 5. 条款编号加粗
        _emit(job_id, "clause-bold", "条款编号加粗...", 55)
        text = bold_clause_numbers(text)
        (job_dir / "04-clause-bold.md").write_text(text, encoding="utf-8")
        _emit(job_id, "clause-bold", "完成：x.y.z 编号加粗", 65)

        # 6. 公式/表格报告（dry-run）
        _emit(job_id, "report", "生成公式/表格复核清单...", 70)
        from postprocess.formula_verify import write_formula_report
        from postprocess.table_verify import write_table_report
        n_f = write_formula_report(text, job_dir / "formula-report.md")
        n_t = write_table_report(text, job_dir / "table-report.md")
        _emit(job_id, "report", f"完成：{n_f} 公式 + {n_t} 表格", 80)

        # 7. 拆分
        _emit(job_id, "split", "章节拆分...", 85)
        final_md = job_dir / "final.md"
        final_md.write_text(text, encoding="utf-8")
        tmp_input = job_dir / f"{md_path.stem}.md"
        shutil.copy(final_md, tmp_input)
        wiki_root = job_dir / "wiki"
        if wiki_root.exists():
            shutil.rmtree(wiki_root)
        wiki_root.mkdir(parents=True, exist_ok=True)
        split_to_wiki(tmp_input, wiki_root=wiki_root, repo_root=REPO_ROOT, spec_name=md_path.stem)
        _emit(job_id, "split", f"完成", 95)

        # 保存最终产物路径
        (job_dir / "meta.json").write_text(
            json.dumps({
                "final_md": str(final_md),
                "wiki_root": str(wiki_root),
                "has_pdf": pdf_path is not None,
                "pdf_path": str(pdf_path) if pdf_path else None,
                "pages": _count_pages(pdf_path) if pdf_path else 0,
                "formula_count": n_f,
                "table_count": n_t,
            }, ensure_ascii=False),
            encoding="utf-8",
        )

        _emit(job_id, "done", "全部完成", 100)

    except Exception as e:
        _emit(job_id, "error", str(e), 0)


def _count_pages(pdf_path: Path) -> int:
    if not pdf_path or not pdf_path.exists():
        return 0
    try:
        import fitz
        doc = fitz.open(pdf_path)
        n = len(doc)
        doc.close()
        return n
    except Exception:
        return 0


# ── API：PDF 页面 / MD 内容 ──────────────────────────────

@app.route("/api/pdf-page/<job_id>/<int:page>")
def api_pdf_page(job_id, page):
    """返回 PDF 单页 PNG。"""
    job_dir = UPLOAD_DIR / job_id
    pdf_files = list(job_dir.glob("*.pdf"))
    if not pdf_files:
        return "no pdf", 404
    pdf_path = pdf_files[0]
    try:
        import fitz
        doc = fitz.open(pdf_path)
        if page < 1 or page > len(doc):
            doc.close()
            return "page out of range", 404
        pix = doc[page - 1].get_pixmap(dpi=150)
        doc.close()
        return Response(pix.tobytes("png"), mimetype="image/png")
    except Exception as e:
        return str(e), 500


@app.route("/api/md-content/<job_id>")
def api_md_content(job_id):
    """返回当前阶段 MD 内容。"""
    stage = request.args.get("stage", "04-clause-bold")
    job_dir = UPLOAD_DIR / job_id
    stage_files = {
        "stripped": "01-stripped.md",
        "normalized": "02-normalized.md",
        "headings": "03-headings.md",
        "final": "04-clause-bold.md",
    }
    filename = stage_files.get(stage, "04-clause-bold.md")
    path = job_dir / filename
    if not path.exists():
        return "", 404
    text = path.read_text(encoding="utf-8")
    return Response(text, mimetype="text/plain; charset=utf-8")


@app.route("/api/page-markers/<job_id>")
def api_page_markers(job_id):
    """返回 MD 中的页码标记列表 [{page, line}, ...]"""
    stage = request.args.get("stage", "04-clause-bold")
    job_dir = UPLOAD_DIR / job_id
    stage_files = {
        "stripped": "01-stripped.md",
        "normalized": "02-normalized.md",
        "headings": "03-headings.md",
        "final": "04-clause-bold.md",
    }
    filename = stage_files.get(stage, "04-clause-bold.md")
    path = job_dir / filename
    if not path.exists():
        return jsonify([])

    markers = []
    page_re = re.compile(r"^<!--\s*(\d+)\s*-->$")
    for i, line in enumerate(path.read_text(encoding="utf-8").splitlines()):
        m = page_re.match(line.strip())
        if m:
            markers.append({"page": int(m.group(1)), "line": i})
    return jsonify(markers)


@app.route("/api/job-info/<job_id>")
def api_job_info(job_id):
    """返回 job 元数据。"""
    meta_path = UPLOAD_DIR / job_id / "meta.json"
    md_files = list((UPLOAD_DIR / job_id).glob("*.md"))
    if meta_path.exists():
        return jsonify(json.loads(meta_path.read_text(encoding="utf-8")))
    return jsonify({"md_name": md_files[0].name if md_files else "unknown", "has_pdf": False})


@app.route("/api/wiki-tree/<job_id>")
def api_wiki_tree(job_id):
    """返回 wiki 目录树。"""
    wiki_root = UPLOAD_DIR / job_id / "wiki"
    if not wiki_root.exists():
        return jsonify([])

    def walk(path: Path) -> list:
        items = []
        for p in sorted(path.iterdir()):
            if p.is_dir():
                items.append({"name": p.name, "type": "dir", "children": walk(p)})
            else:
                items.append({"name": p.name, "type": "file", "path": str(p.relative_to(wiki_root))})
        return items
    return jsonify(walk(wiki_root))


@app.route("/api/wiki-file/<job_id>/<path:rel_path>")
def api_wiki_file(job_id, rel_path):
    """返回 wiki 下某个文件的内容。"""
    file_path = UPLOAD_DIR / job_id / "wiki" / rel_path
    if not file_path.exists() or not file_path.is_file():
        return "", 404
    return Response(file_path.read_text(encoding="utf-8"), mimetype="text/plain; charset=utf-8")


# ── API：已有 output 目录挂载 ─────────────────────────────

@app.route("/api/existing-jobs")
def api_existing_jobs():
    """列出 output/ 中已有的处理结果。"""
    output_root = ROOT_DIR / "output"
    if not output_root.exists():
        return jsonify([])
    jobs = []
    for d in sorted(output_root.iterdir()):
        if d.is_dir():
            final = d / "05-final.md" if (d / "05-final.md").exists() else (
                d / "04-clause-bold.md" if (d / "04-clause-bold.md").exists() else None
            )
            if not final:
                final = d / "04-headings.md" if (d / "04-headings.md").exists() else None
            if final:
                jobs.append({"name": d.name, "has_wiki": (d / "wiki").exists(), "has_final": True})
    return jsonify(jobs)


@app.route("/api/load-existing/<name>")
def api_load_existing(name):
    """把 output/<name> 的内容映射为一个虚拟 job，供 viewer 使用。"""
    src = ROOT_DIR / "output" / name
    if not src.exists():
        return jsonify({"error": "not found"}), 404

    # 产生一个稳定的虚拟 job_id
    job_id = "existing-" + name.replace(" ", "_")[:40]
    job_dir = UPLOAD_DIR / job_id
    # 清理旧缓存，重新复制（保证和 output/ 同步）
    if job_dir.exists():
        shutil.rmtree(job_dir)
    job_dir.mkdir(parents=True)
    # 复制各阶段产物（统一命名为 04-clause-bold.md，匹配 viewer 查找逻辑）
    for fname in ["01-stripped.md", "02-normalized.md", "04-headings.md"]:
        src_file = src / fname
        if src_file.exists():
            shutil.copy(src_file, job_dir / fname)
    for candidate in ["05-final.md", "04b-clause-bold.md"]:
        c = src / candidate
        if c.exists():
            shutil.copy(c, job_dir / "04-clause-bold.md")
            break

    # 查找 PDF
    pdf_candidates = list(ROOT_DIR.glob(f"input/{name}*.pdf")) + list(ROOT_DIR.glob(f"input/*{name}*.pdf"))
    pdf_path = pdf_candidates[0] if pdf_candidates else None

    (job_dir / "meta.json").write_text(
        json.dumps({
            "final_md": str(job_dir / "04-clause-bold.md"),
            "wiki_root": str(src / "wiki") if (src / "wiki").exists() else "",
            "has_pdf": pdf_path is not None,
            "pdf_path": str(pdf_path) if pdf_path else None,
            "pages": _count_pages(pdf_path) if pdf_path else 0,
            "source": "existing",
        }, ensure_ascii=False),
        encoding="utf-8",
    )
    return jsonify({"job_id": job_id, "name": name})


# ── API：wiki 下载 ────────────────────────────────────────

@app.route("/api/download-wiki/<job_id>")
def api_download_wiki(job_id):
    """打包下载 wiki 目录。"""
    import zipfile
    wiki_root = UPLOAD_DIR / job_id / "wiki"
    if not wiki_root.exists():
        return "no wiki", 404
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in wiki_root.rglob("*"):
            if f.is_file():
                zf.write(f, f.relative_to(wiki_root))
    buf.seek(0)
    return Response(buf.getvalue(), mimetype="application/zip",
                    headers={"Content-Disposition": f"attachment; filename=wiki-{job_id[:8]}.zip"})


# ── 启动 ─────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"Web UI 启动: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000, debug=True)
