"""剥离 OCR md 文档开头的前言、目录、版权、出版信息，只从规范正文第一章开始保留。

策略：
1. 自顶向下扫描，找出"第一个看起来像正文章节标题"的位置。
   章节标题判定 (compact_no_space)：
       ^1总则$, ^1基本规定$, ^[0-9]{1,2}<中文章节名>$
   或者 markdown 行本身就是 `# 1 ...` / `# 1<chinese>` / `##? 1总则`。
   仅当章节号是 1 (或编号最小的)时才作为切入点，避免误把 `5.1` 当成章节 1。

2. 同时也支持在前言区识别 `# 前 言` / `# 目 次` / `# 目 录` 等显式段落，
   出现这些标题后到下一个正文一级章节之间的所有内容都丢弃。

3. 输出从第一章开始到文末的所有行（页码标记保留）。

不做：
- 不处理结尾的"本标准用词说明 / 引用标准名录"——这些由后续拆分阶段统一处理。
"""

from __future__ import annotations

import re

# 用于判断"明显是第一章正文标题"的紧凑表达（去掉空格、井号、全角空格之后）
# 命中规则:
#   1总则 / 1总 则 / 1基本规定 / 1范围 ...
_FIRST_CHAPTER_RE = re.compile(r"^#{0,6}\s*1\s*[一-鿿]")
_PAGE_RE = re.compile(r"^<!--\s*[·•.\s]*\d+[·•.\s]*-->$")


def _strip_compact(line: str) -> str:
    return re.sub(r"\s+", "", line)


def _looks_like_first_chapter(line: str) -> bool:
    """章节 1 的标题。允许各种井号层级 / OCR 把"总 则"分开。"""
    stripped = line.strip()
    if not stripped:
        return False
    # 去掉前导井号
    text = re.sub(r"^#{1,6}\s*", "", stripped)
    compact = _strip_compact(text)
    # 形如 1总则 / 1基本规定 / 1范围
    if re.match(r"^1[一-鿿]{2,8}$", compact):
        # 排除：1.0.1 / 1.1 这种条款
        if "." in stripped[:6]:
            return False
        return True
    # 也允许 "# 1 总则" 这种正常写法
    if _FIRST_CHAPTER_RE.match(stripped) and "." not in stripped.split()[1] if len(stripped.split()) > 1 else False:
        return True
    return False


def strip_frontmatter(text: str) -> tuple[str, dict]:
    """
    返回 (剥离后的文本, 元数据 dict)。
    元数据包含：dropped_lines, first_chapter_line_index, marker（用作日志）
    """
    lines = text.splitlines()
    cut_idx = None
    for i, line in enumerate(lines):
        if _looks_like_first_chapter(line):
            cut_idx = i
            break

    if cut_idx is None:
        # 找不到第一章，原样返回，避免破坏文档
        return text, {"dropped_lines": 0, "first_chapter_line_index": None, "marker": None}

    # 把第一章首行强制规范为 `# 1 <章节名>`，方便后续标题归一化阶段
    head = lines[cut_idx].strip().lstrip("#").strip()
    # 去掉总则中的空格："1总 则" -> "1总则"
    head = re.sub(r"^(\d+)\s*([一-鿿])", r"\1\2", head)
    m = re.match(r"^(\d+)([一-鿿].+?)$", _strip_compact(head))
    if m:
        ch_no = m.group(1)
        ch_name = m.group(2)
        normalized_first = f"# {ch_no} {ch_name}"
    else:
        normalized_first = f"# {head}"

    kept = [normalized_first] + lines[cut_idx + 1 :]
    return "\n".join(kept), {
        "dropped_lines": cut_idx,
        "first_chapter_line_index": cut_idx,
        "marker": normalized_first,
    }


def is_page_marker(line: str) -> bool:
    return bool(_PAGE_RE.match(line.strip()))
