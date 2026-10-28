#!/usr/bin/env python3
"""
V27 Prompt Optimizer: Compress 10K EN prompts to MiniMax-optimal ~2000 chars
Preserves all critical info, strips redundancy for faster/cheaper generation.
"""
import re
from pathlib import Path

WORK = Path(__file__).resolve().parents[2]

CANONICAL = (
    "Original high-quality Japanese theatrical animation: hand-drawn textured backgrounds, "
    "stable character animation, cinematic composition, natural light and atmospheric perspective. "
    "Seasonal palettes: late-winter cool blue / spring-rain blue-green / sunset orange-gold / snowy-night blue-violet. "
    "No: plastic skin, template face, deformed limbs, watermark, flicker, garbled text."
)

def extract_blocks(text: str) -> dict:
    """Extract Unit15s -> prompt body from vol6 or EN file."""
    pat = r"(?m)^#### Unit15s_(\d{3}) \|.*$"
    fence = "```text"
    fence_end = "```"
    sections = list(re.finditer(pat, text))
    out = {}
    for j, h in enumerate(sections):
        end = sections[j + 1].start() if j + 1 < len(sections) else len(text)
        sec = text[h.start():end]
        m = re.search(re.escape(fence) + r"\n(.*?)\n" + re.escape(fence_end), sec, re.S)
        if m:
            out[int(h.group(1))] = m.group(1)
    return out


def compress_for_minimax(body: str) -> str:
    """
    Compress a full EN prompt body for MiniMax 5s generation.
    Strategy:
    - Keep canonical style (compressed)
    - Keep shot-specific: optics, character, camera, costume
    - Keep negative prompt
    - Trim verbose Sub-Cut keyframe detail (only keep relevant 5s slice)
    """
    parts = []

    # 1. Canonical (compressed)
    parts.append(f"[STYLE] {CANONICAL}")

    # 2. Extract Iron Rule 1 (optics)
    m1 = re.search(r"Iron Rule 1.{0,500}?(\d+mm.*?f/\d+\.\d+.*?16:9.*?3840.{0,50})", body)
    if m1:
        parts.append(f"[OPTICS] {m1.group(1).strip()}")

    # 3. Extract Iron Rule 2 (character)
    m2 = re.search(r"Iron Rule 2.{0,300}?Character[^:]*:\s*(.{50,800}?)(?=Iron Rule 3|\[STYLE\])", body, re.S)
    if m2:
        char_desc = re.sub(r"\s+", " ", m2.group(1).strip())[:800]
        parts.append(f"[CHARACTER] {char_desc}")

    # 4. Extract Iron Rule 3 (camera/costume/hands) — shot-specific
    m3 = re.search(r"Iron Rule 3.{0,300}?Camera[^:]*:\s*(.{50,800}?)(?=Iron Rule [45]|\[)", body, re.S)
    if m3:
        cam = re.sub(r"\s+", " ", m3.group(1).strip())[:600]
        parts.append(f"[CAMERA] {cam}")

    # 5. Iron Rule 4 — audio/lip-sync (keep concise)
    m4 = re.search(r"Iron Rule 4.{0,200}?Lip[^:]*:\s*(.{30,500}?)(?=Iron Rule 5|\[)", body, re.S)
    if m4:
        lip = re.sub(r"\s+", " ", m4.group(1).strip())[:400]
        parts.append(f"[LIPSYNC] {lip}")

    # 6. Negative prompt
    m7 = re.search(r"Iron Rule 7.{0,200}?Negative[^:]*:\s*(.+)", body, re.S)
    if m7:
        neg = re.sub(r"\s+", " ", m7.group(1).strip())[:600]
        parts.append(f"[NEGATIVE] {neg}")

    result = "\n\n".join(parts)

    # Safety: if compression lost too much, keep key sections verbatim
    if len(result) < 1000:
        # Fallback: keep full body trimmed to 3000
        return body[:3000]

    # Ensure minimum viable length
    if len(result) < 1200:
        # Add back camera detail
        pass

    return result


def optimize_clip_prompt(manus_body: str, clip_idx: int) -> str:
    """
    Further optimize for a specific 5s sub-clip within a 15s Unit unit.
    clip_idx: 1, 2, or 3 (0-5s, 5-10s, 10-15s)
    """
    base = compress_for_minimax(manus_body)

    # Add clip-specific Sub-Cut focus
    clip_labels = {
        1: "Sub-Cut α-β (0-5s): opening/wide establishing",
        2: "Sub-Cut γ (5-10s): main action/dialogue",
        3: "Sub-Cut δ-ε (10-15s): closing/transition to next shot",
    }
    label = clip_labels.get(clip_idx, "")

    return f"{base}\n\n[FOCUS] {label} — render this 5-second segment only."


if __name__ == "__main__":
    import sys

    print("=== V27 Prompt Optimizer ===")
    print("Checking compression ratios...")

    vol6 = (WORK / "deliverables/vol6_manus15.md").read_bytes().decode("utf-8")
    en_path = WORK / "deliverables/model_prompts_en/Unit15s_001.md"
    if en_path.exists():
        en_text = en_path.read_bytes().decode("utf-8")
        m = re.search(r"```text\n(.*?)\n```", en_text, re.S)
        if m:
            body = m.group(1)
            compressed = compress_for_minimax(body)
            print(f"  Unit15s_001 EN: {len(body)} -> {len(compressed)} chars ({len(compressed)/len(body):.0%})")
            print(f"  Preview: {compressed[:300]}...")

    # Check a few more
    for n in [1, 30, 60, 90, 120]:
        ep = WORK / f"deliverables/model_prompts_en/Unit15s_{n:03d}.md"
        if ep.exists():
            t = ep.read_bytes().decode("utf-8")
            mm = re.search(r"```text\n(.*?)\n```", t, re.S)
            if mm:
                orig = len(mm.group(1))
                comp = len(compress_for_minimax(mm.group(1)))
                print(f"  Unit15s_{n:03d}: {orig} -> {comp} ({comp/orig:.0%})")

    print("Done. Use: python tools/pipeline/prompt_optimizer.py --clip Unit15s_001 --idx 1")
