"""
render_md.py — 輸出單檔彙整 .md ＋ zip 多檔包
交付契約（v1.0 凍結）：
  {filename}_chunks.md     — 所有切片彙整，頂部附統計摘要
  {filename}_chunks.zip    — 每切片 chunk_{id}.md ＋ index.md
"""
import io
import json
import sys
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Any


def _null_str(v) -> str:
    return str(v) if v is not None else "null"


def _chunk_to_md(chunk: dict[str, Any]) -> str:
    """單切片 → YAML frontmatter ＋ 正文。"""
    meta_lines = [
        "---",
        f"chunk_id: {chunk['chunk_id']}",
        f"source_file: {chunk['source_file']}",
        f"file_type: {chunk['file_type']}",
        f"chunk_index: {chunk['chunk_index']}",
        f"page_number: {_null_str(chunk['page_number'])}",
        f"start_time: {_null_str(chunk['start_time'])}",
        f"end_time: {_null_str(chunk['end_time'])}",
        f"section_title: {_null_str(chunk.get('section_title'))}",
        f"prev_chunk_id: {_null_str(chunk.get('prev_chunk_id'))}",
        f"next_chunk_id: {_null_str(chunk.get('next_chunk_id'))}",
        f"token_count: {chunk['token_count']}",
        *[
            f"{key}: {_null_str(chunk.get(key))}"
            for key in ("source_locator", "block_type", "extraction_backend", "quality_status")
            if key in chunk
        ],
        f"summary: {chunk.get('summary', '')}",
        "---",
        "",
        chunk["text"],
    ]
    return "\n".join(meta_lines)


def _index_md(chunks: list[dict[str, Any]], params: dict) -> str:
    source = chunks[0]["source_file"] if chunks else "（無）"
    total = len(chunks)
    tokens = [c["token_count"] for c in chunks]
    avg = round(sum(tokens) / total, 1) if total else 0
    mn, mx = (min(tokens), max(tokens)) if tokens else (0, 0)
    now = datetime.now().strftime("%Y-%m-%d %H：%M：%S")

    rows = []
    for c in chunks:
        loc = f"p.{c['page_number']}" if c["page_number"] else (
            f"{c['start_time']}s" if c["start_time"] is not None else "—"
        )
        title = c.get("section_title") or "—"
        rows.append(
            f"| {c['chunk_id']} | {loc} | {title} | {c['token_count']} | chunk_{c['chunk_id']}.md |"
        )

    lines = [
        f"# RAG 切片索引｜{source}",
        "",
        "## 切片統計",
        f"- 來源格式：{chunks[0]['file_type'] if chunks else '—'}",
        f"- 切片總數：{total}",
        f"- 平均 token 數：{avg}",
        f"- 最小／最大 token：{mn} ／ {mx}",
        f"- chunk_size：{params.get('chunk_size', 256)}｜overlap：{params.get('overlap', 40)}｜min_len：{params.get('min_len', 30)}",
        f"- 處理時間：{now}",
        "",
        "## 切片目錄",
        "| chunk_id | 頁碼／時間戳 | 所屬標題 | token 數 | 檔案 |",
        "|---|---|---|---|---|",
        *rows,
    ]
    return "\n".join(lines)


def _combined_md(chunks: list[dict[str, Any]], params: dict) -> str:
    source = chunks[0]["source_file"] if chunks else "（無）"
    total = len(chunks)
    tokens = [c["token_count"] for c in chunks]
    avg = round(sum(tokens) / total, 1) if total else 0
    now = datetime.now().strftime("%Y-%m-%d %H：%M：%S")

    header = "\n".join([
        f"# RAG 切片彙整｜{source}",
        "",
        f"> 切片總數：{total}｜平均 token：{avg}｜chunk_size：{params.get('chunk_size', 256)}｜overlap：{params.get('overlap', 40)}｜產出時間：{now}",
        "",
        "---",
        "",
    ])

    body_parts = []
    for c in chunks:
        body_parts.append(_chunk_to_md(c))

    return header + "\n\n---\n\n".join(body_parts)


def render(
    chunks: list[dict[str, Any]],
    output_dir: Path,
    source_stem: str,
    params: dict | None = None,
) -> tuple[Path, Path]:
    """
    回傳 (combined_md_path, zip_path)
    """
    params = params or {}
    output_dir.mkdir(parents=True, exist_ok=True)

    # 單檔彙整
    combined_path = output_dir / f"{source_stem}_chunks.md"
    combined_path.write_text(_combined_md(chunks, params), encoding="utf-8")

    # 多檔 zip
    zip_path = output_dir / f"{source_stem}_chunks.zip"
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for c in chunks:
            fname = f"chunk_{c['chunk_id']}.md"
            zf.writestr(fname, _chunk_to_md(c))
        zf.writestr("index.md", _index_md(chunks, params))

    return combined_path, zip_path


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output_dir", default="/home/claude/output")
    parser.add_argument("--stem", required=True)
    args = parser.parse_args()

    chunks = json.loads(Path(args.input).read_text(encoding="utf-8"))
    md, zp = render(chunks, Path(args.output_dir), args.stem)
    print(f"單檔：{md}")
    print(f"ZIP：{zp}")
