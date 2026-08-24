"""
chunk_docx.py — DOCX heading-aware RAG 切片引擎（v1.0 凍結）
策略：Heading 1/2/3 結構樹切片，超長段落再細切
"""
import re
import sys
from pathlib import Path
from typing import Any

import bootstrap

bootstrap.ensure_docx()
bootstrap.ensure_tiktoken()

from docx import Document  # noqa: E402
import enc_compat          # noqa: E402

_ENC = enc_compat.get_encoding()


def _count_tokens(text: str) -> int:
    return len(_ENC.encode(text))


def _heading_level(para) -> int | None:
    """回傳段落的 heading level（1/2/3），非 heading 回 None。"""
    style = para.style.name
    m = re.match(r"Heading (\d)", style)
    if m:
        return int(m.group(1))
    if style.startswith("標題") or style.startswith("heading"):
        return 1
    return None


def _slug(text: str) -> str:
    return re.sub(r"[^\w]", "_", text.strip())[:30]


def chunk_docx(
    path: Path,
    chunk_size: int = 256,
    overlap: int = 40,
    min_len: int = 30,
) -> list[dict[str, Any]]:
    slug_file = re.sub(r"[^\w]", "_", path.stem)[:40]
    doc = Document(str(path))

    # 建立結構：[(heading_text, level, [para_text, ...])]
    sections: list[dict] = []
    current_heading = None
    current_level = 0
    buf_paras: list[str] = []
    has_headings = False

    for para in doc.paragraphs:
        text = para.text.strip()
        if not text:
            continue
        lvl = _heading_level(para)
        if lvl is not None:
            has_headings = True
            if buf_paras:
                sections.append({
                    "heading": current_heading,
                    "level": current_level,
                    "text": " ".join(buf_paras),
                })
            current_heading = text
            current_level = lvl
            buf_paras = []
        else:
            buf_paras.append(text)

    if buf_paras:
        sections.append({
            "heading": current_heading,
            "level": current_level,
            "text": " ".join(buf_paras),
        })

    if not has_headings:
        print("[chunk_docx] 警告：未偵測到 heading，退回純段落切片。", file=sys.stderr)

    # 細切超長段落
    fine_blocks: list[dict] = []
    for sec in sections:
        if _count_tokens(sec["text"]) > chunk_size:
            sentences = re.split(r"(?<=[。！？\.!?])\s*", sec["text"])
            buf = ""
            for s in sentences:
                if _count_tokens(buf + s) <= chunk_size:
                    buf += s
                else:
                    if buf.strip():
                        fine_blocks.append({**sec, "text": buf.strip()})
                    buf = s
            if buf.strip():
                fine_blocks.append({**sec, "text": buf.strip()})
        else:
            fine_blocks.append(sec)

    # 合併過短
    merged: list[dict] = []
    for blk in fine_blocks:
        if _count_tokens(blk["text"]) < min_len and merged:
            merged[-1]["text"] += " " + blk["text"]
        else:
            merged.append(blk)

    # 建 chunks ＋ overlap
    chunks: list[dict[str, Any]] = []
    prev_tail = ""
    for i, blk in enumerate(merged):
        text = (prev_tail + " " + blk["text"]).strip() if prev_tail else blk["text"]
        enc_ids = _ENC.encode(blk["text"])
        prev_tail = _ENC.decode(enc_ids[-overlap:]) if len(enc_ids) > overlap else blk["text"]

        heading_slug = _slug(blk["heading"]) if blk["heading"] else "no_heading"
        chunk_id = f"{slug_file}_{heading_slug}_{i:04d}"
        chunks.append({
            "chunk_id": chunk_id,
            "text": text,
            "source_file": path.name,
            "file_type": "docx",
            "chunk_index": i,
            "page_number": None,
            "start_time": None,
            "end_time": None,
            "section_title": blk["heading"],
            "token_count": _count_tokens(text),
            "summary": "",
        })

    for i, c in enumerate(chunks):
        c["prev_chunk_id"] = chunks[i - 1]["chunk_id"] if i > 0 else None
        c["next_chunk_id"] = chunks[i + 1]["chunk_id"] if i < len(chunks) - 1 else None

    return chunks


if __name__ == "__main__":
    path = Path(sys.argv[1])
    result = chunk_docx(path)
    print(f"切片完成，共 {len(result)} 個切片。")
