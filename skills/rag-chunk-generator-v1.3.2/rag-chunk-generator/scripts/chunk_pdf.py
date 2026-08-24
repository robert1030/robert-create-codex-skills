"""
chunk_pdf.py — PDF 高細緻度 RAG 切片引擎（v1.0 凍結）
策略：語意段落切 ＋ 標題階層感知
"""
import re
import sys
from pathlib import Path
from typing import Any

import bootstrap
import preprocess

bootstrap.ensure_pdf()
bootstrap.ensure_tiktoken()

import logging  # noqa: E402

import pdfplumber  # noqa: E402

# pdfminer 對字型子集 PDF 會刷 FontBBox 警告，與切片正確性無關，靜音
logging.getLogger("pdfminer").setLevel(logging.ERROR)
import enc_compat  # noqa: E402

_ENC = enc_compat.get_encoding()


def _count_tokens(text: str) -> int:
    return len(_ENC.encode(text))


def _split_by_sentences(text: str, chunk_size: int) -> list[str]:
    """把超長段落以句號切成 ≤ chunk_size 的片段。"""
    sentences = re.split(r"(?<=[。！？\.!?])\s*", text)
    chunks, buf = [], ""
    for s in sentences:
        candidate = buf + s
        if _count_tokens(candidate) <= chunk_size:
            buf = candidate
        else:
            if buf:
                chunks.append(buf.strip())
            buf = s
    if buf.strip():
        chunks.append(buf.strip())
    return chunks


def chunk_pdf(
    path: Path,
    chunk_size: int = 256,
    overlap: int = 40,
    min_len: int = 30,
) -> list[dict[str, Any]]:
    slug = re.sub(r"[^\w]", "_", path.stem)[:40]
    raw_blocks: list[dict] = []  # {page, heading, text}

    with pdfplumber.open(path) as pdf:
        current_chapter = None
        current_section = None
        for page_num, page in enumerate(pdf.pages, 1):
            text = preprocess.normalize_text(page.extract_text() or "")
            para_buf = ""
            for line in text.splitlines():
                stripped = line.strip()
                if preprocess.is_footer(stripped):
                    stripped = ""
                if not stripped:
                    if para_buf.strip():
                        raw_blocks.append({
                            "page": page_num,
                            "heading": preprocess.compose_heading(current_chapter, current_section),
                            "text": para_buf.strip(),
                        })
                    para_buf = ""
                    continue
                kind, htext = preprocess.heading_kind(stripped)
                if kind:
                    if para_buf.strip():
                        raw_blocks.append({
                            "page": page_num,
                            "heading": preprocess.compose_heading(current_chapter, current_section),
                            "text": para_buf.strip(),
                        })
                        para_buf = ""
                    if kind == "chapter":
                        current_chapter = htext
                        current_section = None
                    else:
                        current_section = htext
                else:
                    para_buf += stripped + " "
            if para_buf.strip():
                raw_blocks.append({
                    "page": page_num,
                    "heading": preprocess.compose_heading(current_chapter, current_section),
                    "text": para_buf.strip(),
                })

    # 細切超長、合併過短
    fine_blocks: list[dict] = []
    for blk in raw_blocks:
        if _count_tokens(blk["text"]) > chunk_size:
            for sub in _split_by_sentences(blk["text"], chunk_size):
                fine_blocks.append({**blk, "text": sub})
        else:
            fine_blocks.append(blk)

    # 合併過短（< min_len）到前一塊
    merged: list[dict] = []
    for blk in fine_blocks:
        if _count_tokens(blk["text"]) < min_len and merged:
            merged[-1]["text"] += " " + blk["text"]
        else:
            merged.append(blk)

    # 加 overlap 並建 chunk list
    chunks: list[dict[str, Any]] = []
    prev_tail = ""
    for i, blk in enumerate(merged):
        text = (prev_tail + " " + blk["text"]).strip() if prev_tail else blk["text"]
        tok = _count_tokens(text)
        # 計算 overlap tail（下一切片的開頭）
        enc_ids = _ENC.encode(blk["text"])
        prev_tail = _ENC.decode(enc_ids[-overlap:]) if len(enc_ids) > overlap else blk["text"]

        page_str = f"p{blk['page']:03d}"
        chunk_id = f"{slug}_{page_str}_{i:04d}"
        chunks.append({
            "chunk_id": chunk_id,
            "text": text,
            "source_file": path.name,
            "file_type": "pdf",
            "chunk_index": i,
            "page_number": blk["page"],
            "start_time": None,
            "end_time": None,
            "section_title": blk["heading"],
            "token_count": tok,
            "summary": "",  # 由 generate_summary.py 填入
        })

    # 填 prev／next
    for i, c in enumerate(chunks):
        c["prev_chunk_id"] = chunks[i - 1]["chunk_id"] if i > 0 else None
        c["next_chunk_id"] = chunks[i + 1]["chunk_id"] if i < len(chunks) - 1 else None

    return chunks


if __name__ == "__main__":
    path = Path(sys.argv[1])
    result = chunk_pdf(path)
    print(f"切片完成，共 {len(result)} 個切片。")
