#!/usr/bin/env python3
"""
V27 Batch Generator: Parallel MiniMax 5s clip generation with Claude-assisted QC.
Usage:
  python tools/pipeline/batch_generate.py --clips 001-003     # first 3 Unit units (9 clips)
  python tools/pipeline/batch_generate.py --clips 001-120     # full batch
  python tools/pipeline/batch_generate.py --clips 001         # single unit
  python tools/pipeline/batch_generate.py --dry-run           # preview prompts only
"""
import argparse
import csv
import json
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

WORK = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(WORK / "tools/pipeline"))
from prompt_optimizer_v2 import build_minimax_prompt, extract_prompt_body

# MiniMax API config (set via env or config file)
MINIMAX_API_KEY = ""
MINIMAX_API_URL = "https://api.minimax.chat/v1/video_generation"

# Generation settings
MODEL = "MiniMax-Hailo-02"  # or MiniMax-H3 / H3-Lite
RESOLUTION = "768P"
DURATION = 5  # seconds per clip
MAX_WORKERS = 3  # concurrent requests
MAX_RETRIES = 2  # per-clip retry on failure


def load_clip_plan(clip_range: str) -> list[dict]:
    """Load clips from 5s ledger filtered by manus unit range."""
    ledger = WORK / "V27_5秒视频生成台账.csv"
    with open(ledger, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))

    if clip_range:
        # Parse range like "001-003" or "001" or "001,003,005"
        if "-" in clip_range and "," not in clip_range:
            start, end = clip_range.split("-")
            start, end = int(start), int(end)
            keep = set(range(start, end + 1))
        elif "," in clip_range:
            keep = set(int(x) for x in clip_range.split(","))
        else:
            keep = {int(clip_range)}

        filtered = []
        for r in rows:
            unit_num = int(r["manus_unit"].replace("Unit15s_", ""))
            if unit_num in keep:
                filtered.append(r)
        return filtered

    return rows


def build_prompt(clip: dict) -> str:
    """Build MiniMax-ready prompt for a single 5s clip."""
    manus_unit = clip["manus_unit"]
    text = (WORK / f"deliverables/model_prompts_en/{manus_unit}.md").read_bytes().decode("utf-8")
    body = extract_prompt_body(text)
    return build_minimax_prompt(body, clip)


def generate_clip(clip: dict, prompt: str) -> dict:
    """Generate a single 5s clip via MiniMax API."""
    clip_id = clip["clip_id"]
    print(f"  [{clip_id}] Generating... ({len(prompt)} chars prompt)")

    # TODO: Replace with actual MiniMax API call
    # For now, dry-run returns prompt info
    return {
        "clip_id": clip_id,
        "manus_unit": clip["manus_unit"],
        "clip_in_unit": clip["clip_in_unit"],
        "prompt_length": len(prompt),
        "prompt": prompt,
        "status": "dry_run",
        "output_file": clip["output_file"],
    }


def batch_generate(clips: list[dict], dry_run: bool = False) -> list[dict]:
    """Generate all clips with parallel execution."""
    print(f"Batch: {len(clips)} clips, dry_run={dry_run}")
    print(f"Model: {MODEL} @ {RESOLUTION}, {DURATION}s/clip")
    print(f"Workers: {MAX_WORKERS}, Retries: {MAX_RETRIES}")
    print("-" * 60)

    results = []

    if dry_run:
        for clip in clips:
            prompt = build_prompt(clip)
            result = {
                "clip_id": clip["clip_id"],
                "prompt_length": len(prompt),
                "prompt_preview": prompt[:200],
                "status": "dry_run",
            }
            results.append(result)
            print(f"  {clip['clip_id']}: {len(prompt)} chars — {prompt[:80]}...")
        return results

    # Real generation with parallel execution
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {}
        for clip in clips:
            prompt = build_prompt(clip)
            fut = pool.submit(generate_clip, clip, prompt)
            futures[fut] = clip

        for fut in as_completed(futures):
            try:
                result = fut.result()
                results.append(result)
                print(f"  DONE: {result['clip_id']} -> {result['status']}")
            except Exception as e:
                clip = futures[fut]
                print(f"  FAIL: {clip['clip_id']} -> {e}")
                results.append({"clip_id": clip["clip_id"], "status": "failed", "error": str(e)})

    return results


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="V27 Batch Generate via MiniMax")
    parser.add_argument("--clips", type=str, default="", help="Clip range e.g. 001-003 or 001")
    parser.add_argument("--dry-run", action="store_true", help="Preview prompts without generating")
    parser.add_argument("--output", type=str, default="", help="Save results JSON to file")
    args = parser.parse_args()

    clips = load_clip_plan(args.clips)
    print(f"Loaded {len(clips)} clips from ledger (filter: {args.clips or 'all'})")

    results = batch_generate(clips, dry_run=args.dry_run)

    print("-" * 60)
    print(f"Done: {len(results)} clips processed")
    passed = sum(1 for r in results if r.get("status") in ("done", "dry_run"))
    print(f"  Success: {passed}/{len(results)}")

    if args.output:
        Path(args.output).write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"  Saved to: {args.output}")
