#!/usr/bin/env python3
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
import os, re, json, time, sys, urllib.request

ROOT = Path(__file__).resolve().parent
SRC = ROOT / 'deliverables' / 'blocks'
OUT = ROOT / 'deliverables' / 'model_prompts_en'
OUT.mkdir(parents=True, exist_ok=True)
MODEL = os.environ.get('V27_TRANSLATION_MODEL', 'gpt-6.1-sol')
MAX_WORKERS = int(os.environ.get('V27_TRANSLATION_WORKERS', '5'))
API_URL = os.environ['OPENAI_API_BASE'].rstrip('/') + '/chat/completions'
API_KEY = os.environ['OPENAI_API_KEY']

SYSTEM = '''You are the senior localization editor for a precision-controlled animated-film video-generation package.
Translate the supplied Chinese Markdown production prompt into precise, natural English for a video model.
This is NOT a summary and NOT a rewrite. Preserve the complete Markdown structure, all headings, tables, bullets, code fences, ordering, and every production constraint.
Hard invariants:
- Keep every identifier, Shot_###, Unit15s_###, frame number, timestamp, FPS, resolution, focal length, color temperature, unit, filename, export token, weight, numeric value, and backticked token exactly unchanged.
- Keep all Japanese dialogue, Japanese on-screen text, exact quoted text, proper names, asset filenames, and technical codes verbatim. Preserve Chinese source text only when it is an exact in-frame text/asset label or a quoted Japanese translation note; otherwise translate it.
- Translate director labels, section labels, audio-cue prose, technical instructions, negative prompts, and the canonical visual/language rule into English.
- Do not introduce artist/studio names or change the style direction. Render the style as original, high-quality Japanese theatrical animation-film visual language, with the stated anti-cheap-AI constraints.
- Keep the opening title as '# Unit15s_###' and keep the English output self-contained.
- Output only the translated Markdown file, with no preface, explanation, or code-fence wrapper around the whole file.'''

def quoted_japanese(text):
    vals=[]
    for pat in [r'「[^」]+」', r'『[^』]+』']:
        vals += re.findall(pat, text)
    return vals

def backticks(text):
    return re.findall(r'`[^`\n]+`', text)

def invariants(src, out, n):
    errs=[]
    if not out.lstrip().startswith(f'# Unit15s_{n:03d}'):
        errs.append('bad title')
    if out.count('```text') != src.count('```text'):
        errs.append('code-fence count')
    for tok in backticks(src):
        if tok not in out: errs.append(f'missing backtick {tok}')
    for tok in quoted_japanese(src):
        if tok not in out: errs.append(f'missing quoted text {tok[:30]}')
    for tok in re.findall(r'\b(?:Shot|Unit15s)_\d{3}\b', src):
        if out.count(tok) < src.count(tok): errs.append(f'identifier count {tok}')
    for tok in re.findall(r'\b\d+(?:\.\d+)?(?:fps|mm|K|dB|Hz|BPM|px|s)\b', src):
        if tok not in out: errs.append(f'missing tech token {tok}')
    if '【全片统一视觉风格与语言总则】' in out:
        errs.append('Chinese canonical heading remained')
    if re.search(r'(?m)^\s*[一二三四五六七]、', out):
        errs.append('Chinese section label remained')
    return errs

def translate_one(path):
    n=int(path.stem.split('_')[-1])
    src=path.read_text(encoding='utf-8')
    # Resume only if an existing output passes the deterministic gate.
    existing=OUT/f'Unit15s_{n:03d}.md'
    if existing.exists():
        txt=existing.read_text(encoding='utf-8')
        e=invariants(src,txt,n)
        if not e:
            return n,'skipped',[]
    prompt='Translate this complete source file faithfully. Preserve all invariants listed above.\n\nSOURCE FILE:\n'+src
    last=[]
    for attempt in range(3):
        body={
            'model': MODEL,
            'messages': [{'role':'system','content':SYSTEM},{'role':'user','content':prompt}],
            'reasoning': {'effort':'medium'},
            'max_completion_tokens': 16000,
        }
        req=urllib.request.Request(API_URL, data=json.dumps(body).encode('utf-8'), headers={'Authorization':'Bearer '+API_KEY,'Content-Type':'application/json'})
        with urllib.request.urlopen(req, timeout=300) as response:
            payload=json.loads(response.read().decode('utf-8'))
        if payload.get('error'):
            raise RuntimeError(payload['error'])
        out=((payload.get('choices') or [{}])[0].get('message') or {}).get('content') or ''
        last=invariants(src,out,n)
        if not last:
            existing.write_text(out.rstrip()+'\n',encoding='utf-8')
            return n,'written',[]
        prompt += '\n\nYour previous output failed these deterministic checks: '+json.dumps(last,ensure_ascii=False)+'. Return the complete corrected file only. Do not omit any section.'
    return n,'failed',last

def main():
    files=sorted(SRC.glob('Unit15s_*.md'))
    results=[]
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as ex:
        futs={ex.submit(translate_one,p):p for p in files}
        for fut in as_completed(futs):
            try: r=fut.result()
            except Exception as e:
                p=futs[fut]; r=(int(p.stem.split('_')[-1]),'error',[repr(e)])
            results.append(r); print(json.dumps(r,ensure_ascii=False),flush=True)
    results.sort()
    (ROOT/'translation_run_results.json').write_text(json.dumps({'model':MODEL,'results':results},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    bad=[r for r in results if r[1] not in ('written','skipped')]
    print(json.dumps({'total':len(results),'written_or_skipped':len(results)-len(bad),'failed':bad},ensure_ascii=False,indent=2))
    return 1 if bad else 0
if __name__=='__main__': sys.exit(main())
