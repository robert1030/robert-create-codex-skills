"""
chunk_mp4.py — MP4 Whisper 逾字稿 RAG 切片引擎（v1.0 凍結）
策略：Whisper word-level timestamps → 語意段落切 ＋ 時間戳記保留
"""
import re
import sys
import tempfile
from pathlib import Path
from typing import Any

import bootstrap

bootstrap.ensure_mp4()
bootstrap.ensure_tiktoken()

import whisper   # noqa: E402
import enc_compat  # noqa: E402

_ENC = enc_compat.get_encoding()


def _count_tokens(text: str) -> int:
    return len(_ENC.encode(text))


def _seconds_to_hms(seconds: float) -> str:
    h = int(seconds // 3600)
    m = int((seconds % 3600) // 60)
    s = int(seconds % 60)
    return f"{h:02d}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


def chunk_mp4(
    path: Path,
    chunk_size: int = 256,
    overlap: int = 40,
    min_len: int = 30,
    whisper_model: str = "base",
) -> list[dict[str, Any]]:
    slug_file = re.sub(r"[^\w]", "_", path.stem)[:40]

    print(f"[chunk_mp4] 載入 Whisper 模型：{whisper_model}", flush=True)
    model = whisper.load_model(whisper_model)

    print(f"[chunk_mp4] 轉逾字稿中：{path.name}", flush=True)
    result = model.transcribe(str(path), word_timestamps=True)

    # 從 segments 建立 word list：[{word, start, end}]
    words: list[dict] = []
    for seg in result.get("segments", []):
        for w in seg.get("words", []):
            words.append({
                "word": w["word"].strip(),
                "start": w["start"],
                "end": w["end"],
            })

    # 若無 word-level，降級用 segment-level
    if not words:
        for seg in result.get("segments", []):
            words.append({
                "word": seg["text"].strip(),
                "start": seg["start"],
                "end": seg["end"],
            })

    # 以靜音（gap > 1.0s）或達 chunk_size 切段
    raw_blocks: list[dict] = []
    buf_words: list[dict] = []
    for i, w in enumerate(words):
        if buf_words:
            gap = w["start"] - buf_words[-1]["end"]
            buf_text = " ".join(x["word"] for x in buf_words)
            if gap > 1.0 and _count_tokens(buf_text) >= min_len:
                raw_blocks.append({
                    "text": buf_text,
                    "start_time": buf_words[0]["start"],
                    "end_time": buf_words[-1]["end"],
                })
                buf_words = []
        buf_words.append(w)
        buf_text = " ".join(x["word"] for x in buf_words)
        if _count_tokens(buf_text) >= chunk_size:
            raw_blocks.append({
                "text": buf_text,
                "start_time": buf_words[0]["start"],
                "end_time": buf_words[-1]["end"],
            })
            # overlap：保留末尾 overlap tokens 的 words
            tail_text = ""
            tail_words = []
            for bw in reversed(buf_words):
                candidate = bw["word"] + " " + tail_text
                if _count_tokens(candidate) <= overlap:
                    tail_text = candidate
                    tail_words.insert(0, bw)
                else:
                    break
            buf_words = tail_words

    if buf_words:
        buf_text = " ".join(x["word"] for x in buf_words)
        if buf_text.strip():
            raw_blocks.append({
                "text": buf_text,
                "start_time": buf_words[0]["start"],
                "end_time": buf_words[-1]["end"],
            })

    # 合併過短
    merged: list[dict] = []
    for blk in raw_blocks:
        if _count_tokens(blk["text"]) < min_len and merged:
            merged[-1]["text"] += " " + blk["text"]
            merged[-1]["end_time"] = blk["end_time"]
        else:
            merged.append(blk)

    # 建 chunks
    chunks: list[dict[str, Any]] = []
    for i, blk in enumerate(merged):
        ts = _seconds_to_hms(blk["start_time"]).replace(":", "")
        chunk_id = f"{slug_file}_{ts}_{i:04d}"
        chunks.append({
            "chunk_id": chunk_id,
            "text": blk["text"],
            "source_file": path.name,
            "file_type": "mp4",
            "chunk_index": i,
            "page_number": None,
            "start_time": round(blk["start_time"], 2),
            "end_time": round(blk["end_time"], 2),
            "section_title": None,
            "token_count": _count_tokens(blk["text"]),
            "summary": "",
        })

    for i, c in enumerate(chunks):
        c["prev_chunk_id"] = chunks[i - 1]["chunk_id"] if i > 0 else None
        c["next_chunk_id"] = chunks[i + 1]["chunk_id"] if i < len(chunks) - 1 else None

    return chunks


if __name__ == "__main__":
    path = Path(sys.argv[1])
    model = sys.argv[2] if len(sys.argv) > 2 else "base"
    result = chunk_mp4(path, whisper_model=model)
    print(f"切片完成，共 {len(result)} 個切片。")
