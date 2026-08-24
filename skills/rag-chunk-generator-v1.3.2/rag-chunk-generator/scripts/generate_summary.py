"""
generate_summary.py — 為每切片產生一句話 summary，供 hypothetical
question embedding 使用。

摘要模式（v1.3）：
  1. 抽取式：預設，不需網路或 API 金鑰
  2. 生成式：只有明確指定 mode="api" 才呼叫 Claude API
     API 失敗時仍降級為抽取式摘要
  絕不再把「（summary 生成失敗：…）」這種錯誤字串寫進交付物。

若跳過（--skip_summary），不呼叫 API 也不做抽取，summary 留空字串。
"""
import json
import re
import sys
import time
import urllib.request
import urllib.error
from typing import Any


_API_URL = "https://api.anthropic.com/v1/messages"
_MODEL = "claude-sonnet-4-6"
_MAX_TOKENS = 100


def _call_api(text: str, lang: str = "auto") -> str:
    lang_hint = {
        "zh": "請用繁體中文",
        "en": "Please respond in English",
        "auto": "請用與原文相同語言",
    }.get(lang, "請用與原文相同語言")

    prompt = (
        f"以下是一段文字切片，{lang_hint}，"
        f"用一句話（20～40 字）總結這段切片的核心主題，"
        f"語句完整、資訊密度高，適合作為 RAG 向量嵌入的 hypothetical question 描述。\n\n"
        f"切片內容：\n{text[:800]}"
    )

    payload = json.dumps({
        "model": _MODEL,
        "max_tokens": _MAX_TOKENS,
        "messages": [{"role": "user", "content": prompt}],
    }).encode("utf-8")

    req = urllib.request.Request(
        _API_URL,
        data=payload,
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data["content"][0]["text"].strip()
    except Exception as e:
        raise RuntimeError(f"summary API 不可用：{e}") from e


def extractive_summary(chunk: dict[str, Any]) -> str:
    """抽取式降級摘要：章節標題 ＋ 一句核心句。"""
    title = chunk.get("section_title") or "未分節內容"
    body = chunk.get("text", "")
    sents = [s.strip() for s in re.split(r"(?<=[。！？])", body) if len(s.strip()) >= 12]
    core = ""
    # 首句常是 overlap 帶進來的殘句，優先取第二句起
    for s in (sents[1:] or sents):
        if 15 <= len(s) <= 60:
            core = s
            break
    if not core and sents:
        core = sents[0][:60]
    if not core:
        core = re.sub(r"\s+", " ", body)[:50]
    return f"{title}：{core.rstrip('。')}。"


def generate_summaries(
    chunks: list[dict[str, Any]],
    lang: str = "auto",
    mode: str = "extractive",
    skip: bool = False,
    batch_delay: float = 0.3,
) -> list[dict[str, Any]]:
    if skip:
        return chunks
    if mode not in {"extractive", "api"}:
        raise ValueError(f"不支援的 summary mode：{mode}")
    if mode == "extractive":
        for chunk in chunks:
            if chunk.get("text", "").strip():
                chunk["summary"] = extractive_summary(chunk)
        print(f"[summary] 共 {len(chunks)} 個切片使用抽取式摘要。", flush=True)
        return chunks

    total = len(chunks)
    for i, chunk in enumerate(chunks):
        if not chunk.get("text", "").strip():
            continue
        if mode == "api":
            try:
                print(f"[summary] {i + 1}/{total} {chunk['chunk_id']}", flush=True)
                chunk["summary"] = _call_api(chunk["text"], lang=lang)
                if batch_delay and i < total - 1:
                    time.sleep(batch_delay)
                continue
            except RuntimeError as e:
                mode = "extractive"
                print(
                    f"[summary] 降級：{e}。改用抽取式摘要（章節標題＋核心句），"
                    f"品質低於生成式，請知悉。",
                    flush=True,
                )
        chunk["summary"] = extractive_summary(chunk)
    print(f"[summary] 共 {total} 個切片使用抽取式摘要。", flush=True)
    return chunks


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="chunks JSON 檔路徑")
    parser.add_argument("--output", required=True, help="輸出 JSON 檔路徑")
    parser.add_argument("--lang", default="auto")
    parser.add_argument("--skip", action="store_true")
    args = parser.parse_args()

    from pathlib import Path
    chunks = json.loads(Path(args.input).read_text(encoding="utf-8"))
    result = generate_summaries(chunks, lang=args.lang, skip=args.skip)
    Path(args.output).write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"完成，{len(result)} 個切片 summary 已寫入 {args.output}")
