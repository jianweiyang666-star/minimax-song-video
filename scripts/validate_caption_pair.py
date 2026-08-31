#!/usr/bin/env python3
"""Validate one primary Caption JSON file and an optional translation file."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


CJK = re.compile(r"[\u3400-\u9fff]")
LATIN_WORD = re.compile(r"[A-Za-z]{2,}")
REQUIRED = {"text", "startMs", "endMs", "timestampMs", "confidence"}


def load(path: Path) -> list[dict]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, list) or not value:
        raise ValueError(f"{path}: expected a non-empty JSON array")
    return value


def check_language(text: str, language: str, label: str) -> None:
    if language == "zh" and not CJK.search(text):
        raise ValueError(f"{label}: expected Chinese text: {text!r}")
    if language == "zh" and LATIN_WORD.search(text):
        raise ValueError(f"{label}: unexpected English word in Chinese text: {text!r}")
    if language == "en" and CJK.search(text):
        raise ValueError(f"{label}: unexpected Chinese character in English text: {text!r}")
    if language == "en" and not LATIN_WORD.search(text):
        raise ValueError(f"{label}: expected English text: {text!r}")


def validate_track(
    captions: list[dict], path: Path, language: str, duration_ms: int | None
) -> None:
    previous_start = -1.0
    for index, caption in enumerate(captions):
        missing = REQUIRED - set(caption)
        if missing:
            raise ValueError(f"{path}[{index}]: missing fields {sorted(missing)}")
        text = caption["text"]
        start = caption["startMs"]
        end = caption["endMs"]
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"{path}[{index}]: empty caption text")
        if not isinstance(start, (int, float)) or not isinstance(end, (int, float)):
            raise ValueError(f"{path}[{index}]: startMs/endMs must be numeric")
        if start < 0 or end <= start or start <= previous_start:
            raise ValueError(f"{path}[{index}]: invalid timing {start}-{end}")
        if duration_ms is not None and end > duration_ms:
            raise ValueError(f"{path}[{index}]: caption ends after media duration")
        check_language(text, language, f"{path}[{index}]")
        previous_start = start


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary", type=Path, required=True)
    parser.add_argument("--primary-language", choices=["zh", "en"], required=True)
    parser.add_argument("--translation", type=Path)
    parser.add_argument("--translation-language", choices=["zh", "en"])
    parser.add_argument("--duration-ms", type=int)
    args = parser.parse_args()

    if bool(args.translation) != bool(args.translation_language):
        parser.error("--translation and --translation-language must be used together")

    primary = load(args.primary)
    validate_track(primary, args.primary, args.primary_language, args.duration_ms)

    translation: list[dict] | None = None
    if args.translation:
        translation = load(args.translation)
        validate_track(
            translation,
            args.translation,
            args.translation_language,
            args.duration_ms,
        )
        if len(primary) != len(translation):
            raise ValueError("primary and translation caption counts differ")
        for index, (left, right) in enumerate(zip(primary, translation)):
            if left["startMs"] != right["startMs"] or left["endMs"] != right["endMs"]:
                raise ValueError(f"caption timing differs at index {index}")

    print(
        json.dumps(
            {
                "primaryCaptions": len(primary),
                "translationCaptions": len(translation) if translation else 0,
                "durationMs": args.duration_ms,
                "status": "ok",
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
