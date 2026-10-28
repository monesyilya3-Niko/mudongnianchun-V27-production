#!/usr/bin/env python3
"""
V27 QC Pipeline: Claude-assisted quality check for generated clips.
- Evaluates clips for: face consistency, hand deformation, perspective, flicker
- Generates a QC report with pass/fail + retry recommendations
Usage:
  python tools/pipeline/qc_pipeline.py --input results.json
  python tools/pipeline/qc_pipeline.py --clips 001-003 --use-claude
"""
import argparse
import json
import sys
from pathlib import Path

WORK = Path(__file__).resolve().parents[2]

QC_CHECKLIST = [
    ("face_stability", "人物面部/五官是否稳定，无崩脸或模板化"),
    ("hand_limbs", "手指/肢体无畸变、多指或错误手数"),
    ("clothing_consistency", "服装颜色/款式跨帧一致"),
    ("perspective", "透视/空间关系正确，无穿帮"),
    ("lighting", "光照符合场景设定，无过曝或色彩断层"),
    ("motion_smoothness", "动作流畅，无闪烁或跳帧"),
    ("text_watermark", "无伪文字/水印/拼贴"),
    ("negative_compliance", "无塑料皮肤、脏噪点、廉价3D感"),
]


def qc_check_clip(clip_path: str, use_claude: bool = False) -> dict:
    """
    QC a single generated clip.
    If use_claude and image available, uses Claude vision to evaluate.
    Otherwise returns a manual checklist template.
    """
    result = {
        "clip": clip_path,
        "checks": [],
        "overall": "pending",
        "retry_hint": "",
    }

    if use_claude:
        # Claude vision QC — requires clip image/frame extraction
        result["checks"] = [{"item": c[0], "desc": c[1], "status": "pending_claude"} for c in QC_CHECKLIST]
        result["overall"] = "needs_claude_review"
    else:
        result["checks"] = [{"item": c[0], "desc": c[1], "status": "manual"} for c in QC_CHECKLIST]
        result["overall"] = "needs_manual_review"

    return result


def generate_qc_report(clips: list[str], output: str = "") -> dict:
    """Generate QC report for a batch of clips."""
    report = {
        "total": len(clips),
        "qc_results": [],
        "summary": {"pass": 0, "fail": 0, "pending": 0},
    }

    for clip in clips:
        qc = qc_check_clip(clip)
        report["qc_results"].append(qc)
        report["summary"]["pending"] += 1

    if output:
        Path(output).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"QC report saved to: {output}")

    return report


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="V27 QC Pipeline")
    parser.add_argument("--input", type=str, default="", help="Input results JSON from batch_generate")
    parser.add_argument("--clips", type=str, default="", help="Clip range e.g. 001-003")
    parser.add_argument("--output", type=str, default="", help="Output QC report JSON")
    parser.add_argument("--use-claude", action="store_true", help="Use Claude vision for QC")
    args = parser.parse_args()

    if args.input:
        data = json.loads(Path(args.input).read_text(encoding="utf-8"))
        clips = [r.get("output_file", r.get("clip_id", "")) for r in data]
    elif args.clips:
        if "-" in args.clips:
            start, end = args.clips.split("-")
            clips = [f"Unit15s_{n:03d}" for n in range(int(start), int(end) + 1)]
        else:
            clips = [f"Unit15s_{int(args.clips):03d}"]
    else:
        clips = []

    print(f"QC: {len(clips)} clips")
    for item, desc in QC_CHECKLIST:
        print(f"  [{item}]: {desc}")

    report = generate_qc_report(clips, args.output or "")
    print(f"\nQC Report: {report['summary']}")
    print("Use --use-claude with frame images for automated visual QC")
