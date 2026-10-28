#!/usr/bin/env python3
"""Validation gate for English model-execution prompts."""
from pathlib import Path
import json, re, sys

ROOT = Path(__file__).resolve().parent
D = ROOT / "deliverables"

def quoted_japanese(text):
    vals = []
    for pat in [r'「[^」]+」', r'『[^』]+』']:
        vals += re.findall(pat, text)
    return vals

def backticks(text):
    return re.findall(r'`[^`\n]+`', text)

def invariants(src, out, n):
    errs = []
    if not out.lstrip().startswith(f'# Manus15s_{n:03d}'):
        errs.append('bad title')
    if out.count('```text') != src.count('```text'):
        errs.append('code-fence count')
    for tok in backticks(src):
        if tok not in out:
            errs.append(f'missing backtick {tok}')
    for tok in quoted_japanese(src):
        if tok not in out:
            errs.append(f'missing quoted text {tok[:30]}')
    for tok in re.findall(r'\b(?:Shot|Manus15s)_\d{3}\b', src):
        if out.count(tok) < src.count(tok):
            errs.append(f'identifier count {tok} (src={src.count(tok)}, out={out.count(tok)})')
    for tok in re.findall(r'\b\d+(?:\.\d+)?(?:fps|mm|K|dB|Hz|BPM|px|s)\b', src):
        if tok not in out:
            errs.append(f'missing tech token {tok}')
    if '【全片统一视觉风格与语言总则】' in out:
        errs.append('Chinese canonical heading remained')
    if re.search(r'(?m)^\s*[一二三四五六七]、', out):
        errs.append('Chinese section label remained')
    return errs

def check_unit(n):
    sp = D / "blocks" / f"Manus15s_{n:03d}.md"
    ep = D / "model_prompts_en" / f"Manus15s_{n:03d}.md"
    if not sp.exists():
        return False, [f"source Manus15s_{n:03d}.md does not exist"]
    if not ep.exists():
        return False, [f"english Manus15s_{n:03d}.md does not exist"]
    src = sp.read_text(encoding="utf-8")
    out = ep.read_text(encoding="utf-8")
    errs = invariants(src, out, n)
    return len(errs) == 0, errs

if __name__ == "__main__":
    if len(sys.argv) > 1:
        args = sys.argv[1:]
        all_ok = True
        for a in args:
            if "-" in a:
                start, end = map(int, a.split("-"))
                units = range(start, end + 1)
            else:
                units = [int(a)]
            for u in units:
                ok, errs = check_unit(u)
                if ok:
                    print(f"Manus15s_{u:03d}: PASS")
                else:
                    all_ok = False
                    print(f"Manus15s_{u:03d}: FAIL -> {errs}")
        sys.exit(0 if all_ok else 1)
    else:
        # Check all present in model_prompts_en
        files = sorted((D / "model_prompts_en").glob("Manus15s_*.md"))
        print(f"Checking {len(files)} English prompt files...")
        failures = 0
        for f in files:
            m = re.fullmatch(r"Manus15s_(\d{3})\.md", f.name)
            if not m:
                continue
            u = int(m.group(1))
            ok, errs = check_unit(u)
            if not ok:
                failures += 1
                print(f"Manus15s_{u:03d}: FAIL -> {errs[:3]}")
        print(f"Result: {len(files) - failures}/{len(files)} passed.")
        sys.exit(0 if failures == 0 else 1)
