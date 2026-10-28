#!/usr/bin/env python3
"""
V27 Prompt Optimizer (v2): 5s-slice strategy for MiniMax.
- Keeps original EN prompt integrity
- Trims to ~2500-4000 chars by extracting only the relevant Sub-Cut window
- Adds clip-specific focus + continuity instruction
"""
import re
from pathlib import Path

WORK = Path(__file__).resolve().parents[2]
FENCE = "```text"


def extract_prompt_body(text: str) -> str:
    m = re.search(re.escape(FENCE) + r"\n(.*?)\n```", text, re.S)
    return m.group(1) if m else text


def slice_for_5s(prompt_body: str, clip_in_unit: int) -> str:
    """
    Extract only the relevant portion of a 15s prompt for a 5s sub-clip.
    clip_in_unit: 1 (0-5s), 2 (5-10s), 3 (10-15s)
    """
    # The prompt has Sub-Cut α-ε mapped to frame ranges
    # For 5s clips, we need to extract the relevant Sub-Cuts

    # Keep: canonical + optics + character (always) + relevant Sub-Cut + negative
    # Identify all Sub-Cut sections
    subcut_pattern = r"Sub-Cut\s+[α-ε][^:]*:\s*[^\n]+\n(.*?)(?=Sub-Cut\s+[α-ε]|Iron Rule 6|Iron Rule 7|\Z)"
    subcuts = re.findall(subcut_pattern, prompt_body, re.S)

    # If we have Sub-Cuts, slice by clip index
    # Clip 1 (0-5s): Sub-Cuts α, β (frames 001-120)
    # Clip 2 (5-10s): Sub-Cuts γ (frames 121-240)
    # Clip 3 (10-15s): Sub-Cuts δ, ε (frames 241-360)
    clip_map = {
        1: [0, 1],    # α, β
        2: [2],       # γ
        3: [3, 4],    # δ, ε
    }

    if subcuts and clip_in_unit in clip_map:
        indices = clip_map[clip_in_unit]
        relevant = [subcuts[i] for i in indices if i < len(subcuts)]

        # Build sliced prompt: canonical + optics + character + relevant subcuts + negative
        parts = []

        # Canonical style (keep full)
        canon = re.search(r"Film-Wide Canonical.*?(?=Iron Rule 1|Ironclad Rule)", prompt_body, re.S)
        if canon:
            parts.append(canon.group(0).strip())

        # Optics + character (first Iron Rules)
        optics = re.search(r"(Iron Rule 1.*?)(?=Iron Rule [23]|Ironclad)", prompt_body, re.S)
        if optics:
            parts.append(optics.group(1).strip()[:800])

        # Relevant Sub-Cut(s)
        for rc in relevant:
            parts.append(rc.strip()[:1500])

        # Negative prompt (always)
        neg = re.search(r"Iron Rule 7.*", prompt_body, re.S)
        if not neg:
            neg = re.search(r"Ironclad Rule.*", prompt_body, re.S)
        if neg:
            parts.append(neg.group(0).strip()[:600])

        result = "\n\n".join(parts)
        # Ensure reasonable length
        if 800 < len(result) < 5000:
            return result

    # Fallback: just trim to 4000 chars, keeping head + tail (canonical + negative)
    if len(prompt_body) > 4000:
        head = prompt_body[:2500]
        tail_match = re.search(r"Iron Rule 7.*|Ironclad Rule.*", prompt_body, re.S)
        tail = tail_match.group(0)[:600] if tail_match else ""
        return f"{head}\n\n{tail}"

    return prompt_body


def build_minimax_prompt(prompt_body: str, clip: dict) -> str:
    """Build final MiniMax prompt for a 5s clip."""
    clip_idx = int(clip["clip_in_unit"])
    adapter = clip.get("prompt_adapter_instruction", "")
    continuity = clip.get("continuity_input", "")

    sliced = slice_for_5s(prompt_body, clip_idx)

    # Add adapter instruction
    header = f"[TASK] Generate exactly 5 seconds of video for {clip['clip_id']} ({clip['film_start_tc']} — {clip['film_end_tc']}).\n"
    header += f"[INSTRUCTION] {adapter}\n\n"

    # Add continuity
    footer = ""
    if continuity and "LastFrame" in continuity:
        footer = f"\n\n[CONTINUITY] Previous clip last frame: {continuity} — maintain seamless transition."

    return header + sliced + footer


if __name__ == "__main__":
    import sys
    print("=== V27 Prompt Optimizer v2 (5s-slice) ===")

    for n in [1, 2, 3, 30, 60, 90, 120]:
        en_path = WORK / f"deliverables/model_prompts_en/Unit15s_{n:03d}.md"
        if not en_path.exists():
            continue
        text = en_path.read_bytes().decode("utf-8")
        body = extract_prompt_body(text)
        # Fake clips for each sub-segment
        for clip_idx in [1, 2, 3]:
            clip = {
                "clip_id": f"V27_U{n:03d}_C0{clip_idx}",
                "film_start_tc": f"00:{(n-1)*15//60:02d}:{(n-1)*15%60:02d}",
                "film_end_tc": "",
                "clip_in_unit": str(clip_idx),
                "prompt_adapter_instruction": f"Extract unit-relative seconds {(clip_idx-1)*5}-{clip_idx*5}s; keep only action/camera/sub-cut in this interval.",
                "continuity_input": "V27_U001_C01_LastFrame.png" if clip_idx > 1 else "source refs",
            }
            result = build_minimax_prompt(body, clip)
            print(f"  Unit15s_{n:03d} C{clip_idx}: {len(body)} -> {len(result)} ({len(result)/len(body):.0%})")
        print()
