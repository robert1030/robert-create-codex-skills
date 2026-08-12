#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MP4 adapter for subtitles, offline transcription, and frame OCR degradation."""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
from pathlib import Path

from adapters.base import AdapterContext
from models import AttemptRecord, DocumentIR, Location
from ocr import ocr_image
from utils import normalize_nfc

TIMESTAMP_RE = re.compile(r"(?P<h>\d{2}):(?P<m>\d{2}):(?P<s>\d{2})[,.](?P<ms>\d{3})")


def _seconds(value: str) -> float:
    match = TIMESTAMP_RE.search(value)
    if not match:
        return 0.0
    return int(match.group("h")) * 3600 + int(match.group("m")) * 60 + int(match.group("s")) + int(match.group("ms")) / 1000


def _probe(path: Path) -> dict:
    executable = shutil.which("ffprobe")
    if not executable:
        raise RuntimeError("ffprobe_not_available")
    completed = subprocess.run(
        [executable, "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
        timeout=60,
    )
    if completed.returncode != 0:
        raise RuntimeError(f"ffprobe_failed:{completed.stderr}")
    return json.loads(completed.stdout)


def _extract_subtitles(path: Path, work_dir: Path) -> list[tuple[float, float, str]]:
    executable = shutil.which("ffmpeg")
    if not executable:
        return []
    output = work_dir / "subtitles.srt"
    completed = subprocess.run(
        [executable, "-y", "-v", "error", "-i", str(path), "-map", "0:s:0", str(output)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
        timeout=120,
    )
    if completed.returncode != 0 or not output.is_file():
        return []
    text = output.read_text(encoding="utf-8", errors="replace")
    entries: list[tuple[float, float, str]] = []
    for section in re.split(r"\n\s*\n", text.strip()):
        lines = [line.strip() for line in section.splitlines() if line.strip()]
        if len(lines) < 3 or "-->" not in lines[1]:
            continue
        start_text, end_text = [value.strip() for value in lines[1].split("-->", 1)]
        body = normalize_nfc(" ".join(lines[2:]))
        if body:
            entries.append((_seconds(start_text), _seconds(end_text), body))
    return entries


def _transcribe(path: Path) -> tuple[list[tuple[float, float, str]], list[AttemptRecord]]:
    attempts: list[AttemptRecord] = []
    try:
        from faster_whisper import WhisperModel  # type: ignore
    except Exception as exc:
        attempts.append(AttemptRecord(1, "faster-whisper", "offline_transcription", "failed", error=f"unavailable:{exc}"))
        return [], attempts
    try:
        model = WhisperModel("tiny", device="cpu", compute_type="int8")
        segments, _info = model.transcribe(str(path), beam_size=1)
        entries = []
        for segment in segments:
            text = normalize_nfc(segment.text)
            if text:
                entries.append((float(segment.start), float(segment.end), text))
        attempts.append(AttemptRecord(1, "faster-whisper", "offline_transcription", "success" if entries else "failed", parameters={"model": "tiny", "device": "cpu"}))
        return entries, attempts
    except Exception as exc:
        attempts.append(AttemptRecord(1, "faster-whisper", "offline_transcription", "failed", error=str(exc)))
        return [], attempts


def _extract_frame(path: Path, timestamp: float, output: Path) -> bool:
    executable = shutil.which("ffmpeg")
    if not executable:
        return False
    completed = subprocess.run(
        [executable, "-y", "-v", "error", "-ss", f"{timestamp:.3f}", "-i", str(path), "-frames:v", "1", str(output)],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        check=False,
        timeout=60,
    )
    return completed.returncode == 0 and output.is_file() and output.stat().st_size > 0


def parse(path: Path, context: AdapterContext) -> DocumentIR:
    title = path.stem
    blocks = [context.block(
        "heading", title, heading_path=[title], content_origin="derived_normalization",
        required=True, critical=True, verbatim=False, metadata={"level": 1, "title_from_filename": True},
    )]
    try:
        probe = _probe(path)
    except Exception as exc:
        blocks.append(context.block(
            "placeholder", "", heading_path=[title], content_origin="placeholder",
            required=True, critical=True, status="failed", verbatim=False,
            metadata={"reason": str(exc)},
        ))
        return DocumentIR(context.provenance.source_id, title, context.provenance, blocks, metadata={"adapter": "video_adapter"}, errors=[str(exc)])

    duration = float(probe.get("format", {}).get("duration") or 0.0)
    context.provenance.source_dimensions["media_duration_seconds"] = duration
    streams = probe.get("streams", [])
    has_audio = any(stream.get("codec_type") == "audio" for stream in streams)
    has_video = any(stream.get("codec_type") == "video" for stream in streams)
    subtitles = _extract_subtitles(path, context.work_dir)
    transcript_attempts: list[AttemptRecord] = []
    transcript_source = "embedded_subtitle"
    if not subtitles and has_audio:
        subtitles, transcript_attempts = _transcribe(path)
        transcript_source = "offline_whisper"
    for index, (start, end, text) in enumerate(subtitles, start=1):
        block = context.block(
            "transcript", text, location=Location(time_start=start, time_end=end), heading_path=[title],
            content_origin="transcript", required=True, critical=False,
            metadata={"segment_index": index, "transcript_source": transcript_source},
        )
        block.attempts = list(transcript_attempts)
        blocks.append(block)

    frame_text_count = 0
    if has_video:
        frame_times = [0.0]
        if duration > 4:
            frame_times.append(duration / 2)
        if duration > 10:
            frame_times.append(max(0.0, duration - 1.0))
        for frame_index, timestamp in enumerate(sorted(set(frame_times)), start=1):
            output = context.work_dir / f"frame-{frame_index:03d}.png"
            if not _extract_frame(path, timestamp, output):
                continue
            frame_sha256 = hashlib.sha256(output.read_bytes()).hexdigest()
            visual_review = (
                context.visual_semantics.lookup(output.name, frame_sha256)
                if context.visual_semantics is not None
                else None
            )
            route, admission = context.visual_route(
                output.name, frame_sha256, review_present=visual_review is not None,
                visual_class="screen_capture", native_structured_parser_status="not_applicable",
            )
            if visual_review is not None and visual_review.review_mode == "semantic_summary":
                blocks.append(context.block(
                    "image", visual_review.summary,
                    location=Location(time_start=timestamp, time_end=timestamp, asset_id=f"frame-{frame_index:03d}"),
                    heading_path=[title], content_origin="llm_visual_summary", required=False, critical=False,
                    verbatim=False,
                    metadata={
                        "reference": output.name,
                        "asset_sha256": frame_sha256,
                        "visual_class": "screen_capture",
                        "visual_summary_evidence": visual_review.evidence(),
                        "capability_route": route,
                    },
                ))
                continue
            result = ocr_image(output, admission=admission, languages=context.ocr_languages)
            if result.status != "success" or not result.text:
                continue
            frame_text_count += 1
            block = context.block(
                "image", result.text, location=Location(time_start=timestamp, time_end=timestamp, asset_id=f"frame-{frame_index:03d}"),
                heading_path=[title], content_origin="ocr", required=False, critical=False,
                metadata={
                    "reference": output.name,
                    "asset_sha256": frame_sha256,
                    "visual_class": "screen_capture",
                    "ocr_confidence": result.confidence,
                    "ocr_quality": result.quality,
                    "ocr_semantic_status": "accepted",
                    "capability_route": route,
                },
            )
            block.attempts = result.attempts
            blocks.append(block)

    if not subtitles:
        reason = "no_audio_stream" if not has_audio else "transcription_unavailable_or_empty"
        blocks.append(context.block(
            "placeholder", "", heading_path=[title], content_origin="placeholder",
            required=True, critical=False, status="failed", verbatim=False,
            metadata={"reason": reason, "frame_ocr_success_count": frame_text_count},
        ))
    return DocumentIR(
        source_id=context.provenance.source_id,
        title=title,
        provenance=context.provenance,
        blocks=blocks,
        metadata={
            "adapter": "video_adapter",
            "duration_seconds": duration,
            "has_audio": has_audio,
            "has_video": has_video,
            "subtitle_or_transcript_segment_count": len(subtitles),
            "frame_ocr_success_count": frame_text_count,
        },
    )
