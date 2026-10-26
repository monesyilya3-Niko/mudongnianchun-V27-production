#!/usr/bin/env python3
"""Deterministic structural audit of the local V27 script candidate; no cloud writes."""
from pathlib import Path
import hashlib, json, re, sys
ROOT = Path(__file__).resolve().parent
D = ROOT / 'deliverables'
issues=[]; checks=[]
def check(name, ok, detail):
    checks.append({'check':name,'status':'pass' if ok else 'issue','detail':detail})
    if not ok: issues.append(name)
def payloads(text):
    hs=list(re.finditer(r'(?m)^#### Manus15s_(\d{3}) \|.*$',text)); out={}
    for j,h in enumerate(hs):
        end=hs[j+1].start() if j+1<len(hs) else len(text)
        sec=text[h.start():end]; m=re.search(r'```text\n(.*?)\n```',sec,re.S)
        if m: out[int(h.group(1))]=m.group(1)
    return hs,out
v6=(D/'vol6_manus15.md').read_text(encoding='utf-8')
bible=(D/'vol_bible.md').read_text(encoding='utf-8')
v5=(D/'vol5_voice.md').read_text(encoding='utf-8')
cue=(D/'voice_cue.md').read_text(encoding='utf-8')
_,master=payloads(v6); _,bible_blocks=payloads(bible)
expected=set(range(1,121))
check('Manus15s block coverage',set(master)==expected,f'{len(master)}/120 prompt bodies in vol6')
check('Bible prompt coverage',set(bible_blocks)==expected,f'{len(bible_blocks)}/120 embedded prompt bodies')
parity=[]; duty=[]
for n in range(1,121):
    p=D/'blocks'/f'Manus15s_{n:03d}.md'
    if not p.exists(): parity.append(f'missing {n:03d}'); continue
    s=p.read_text(encoding='utf-8'); m=re.search(r'```text\n(.*?)\n```',s,re.S)
    if not m or m.group(1)!=master.get(n): parity.append(f'prompt mismatch {n:03d}')
    if '执行职责：Manus仅生成本块' not in s: duty.append(f'missing responsibility note {n:03d}')
check('stand-alone prompt parity',not parity,f'{120-len(parity)}/120 match; errors={parity[:8]}')
check('per-block audio boundary',not duty,f'{120-len(duty)}/120 notes; errors={duty[:8]}')
# Compare Bible inlines to the authoritative master.
bi=[n for n in range(1,121) if bible_blocks.get(n)!=master.get(n)]
check('Bible-to-master prompt parity',not bi,f'{120-len(bi)}/120 equal; mismatches={bi[:8]}')
# The plot's documented photo count and generated-frame distinction must remain explicit.
asset_ok=('218 张历史实拍照片' in bible and '第 219 帧' in bible and '不是相机拍摄的原片' in bible and '216 张四季日常照' in bible)
check('218+1 asset accounting',asset_ok,'Bible states 218 historical photographs + AI-generated frame 219')
old_terms=['1+1+217=219','最后的第219张照片','最後の219枚目','そして四季の217枚','この十日間、君の誘いを断ったり','这十天推掉你的约会','219张照片（1+1+217=219）']
files=[D/'vol_bible.md',D/'vol5_voice.md',D/'voice_cue.md',D/'vol6_manus15.md']
left=[]
for p in files:
    t=p.read_text(encoding='utf-8')
    for term in old_terms:
        if term in t:left.append(f'{p.name}: {term}')
check('legacy contradiction sweep',not left,'no targeted legacy phrases' if not left else '; '.join(left[:8]))
check('Shot_123 corrected timeline/dialogue','この間、君の誘いを断ったり' in v6 and 'この十日間、君の誘いを断ったり' not in v6,'date scope no longer falsely covers earlier refusal')
check('Shot_124/128 revised frame wording','218枚の実写写真' in v6 and '最後の219フレーム目' in v6,'key Japanese lines distinguish real photos and generated frame')
check('Manus audio generation boundary','Manus仅生成画面' in v6 and '声音组完整Cue（非画面生成任务）' in v6,'master assigns all audio to sound department')
shot_count=len(re.findall(r'(?m)^#### Shot_\d{3} \|',bible))
check('180-shot structure',shot_count==180,f'{shot_count}/180 Shot headings')
block101=master.get(101,'')
check('Manus15s_101 food-only shot',('女主座位前方桌面上的螺蛳粉碗' in block101 and '人物不入画且不得出现头、脸、手或身体' in block101),'food close-up is not directed at an off-camera character')
block102=master.get(102,'')
check('Manus15s_102 tail-frame contract',('Manus15s_102_LastFrame_360.png (EXPORT_MANUS15S_102_FRAME_360)' in block102 and 'Shot_153_LastFrame.png (EXPORT_SHOT_153_FRAME_240)' not in block102),'Manus F360 is the required output; Shot F240 is not mislabelled as it')
block119=master.get(119,'')
check('Manus15s_119 VO closed-mouth direction',('画外合声VO' in block119 and '全程闭口、不做口型' in block119),'final chorus is off-screen voice-over; visible backs remain closed-mouth')
style_tag='【全片统一视觉风格与语言总则】'
style_counts={n:master.get(n,'').count(style_tag) for n in range(1,121)}
style_ok=all(v==1 for v in style_counts.values())
check('uniform style/language rule in every prompt',style_ok,f'{sum(v==1 for v in style_counts.values())}/120 prompts contain exactly one canonical rule')
named_style=any(t in '\n'.join(master.values()) for t in ['新海诚','新海誠','京阿尼','Shinkai'])
check('original style language without artist-name prompts',not named_style,'prompts use shared original art-direction language rather than named creator/studio imitation')
language_rule='画面生成描述、动作、机位、光线和场景执行语统一使用简体中文'
language_ok=all(language_rule in master.get(n,'') for n in range(1,121))
check('consistent Chinese image-instruction language',language_ok,'all 120 prompts declare Chinese visual directions; Japanese dialogue and technical IDs remain fixed exceptions')
visual_standard=(ROOT/'V27_统一视觉与语言规范.md').read_text(encoding='utf-8')
visual_ok=all(x in visual_standard for x in ['原创','简体中文','试片','塑料皮肤'])
check('visual and language standard available',visual_ok,'stand-alone art-direction and language bible is present')
all_text='\n'.join(p.read_text(encoding='utf-8') for p in ROOT.rglob('*.md'))
clean_ok=('drive.google.com' not in all_text and 'File ID:' not in all_text and 'Folder ID:' not in all_text and not re.search(r'(?<!\w)V(?:0?[1-9]|1\d|2[0-6])(?!\w)',all_text))
check('single clean V27 environment',clean_ok,'no Drive URLs/IDs or prior version labels in project markdown')
source_count=len(list((D/'source_masters').glob('*.jpg')))
candidate_count=len(list((D/'selected_images').glob('*.png')))
check('local image asset set',source_count==40 and candidate_count==10,f'{source_count}/40 source masters; {candidate_count}/10 selected image candidates')
platform=(ROOT/'V27_制作与发布流程.md').read_text(encoding='utf-8')
platform_ok=all(x in platform for x in ['哔哩哔哩','抖音','AI内容标识','5秒'])
check('platform production workflow',platform_ok,'Bilibili, Douyin, AI disclosure, and current five-second generation adaptation documented')
# A passed package is ready for the user's video production stage, not a finished film or publication.
result={'audit':'V27 clean production script package audit','script_package_ready_to_start_video':not issues,'final_video_delivered':False,'platform_publication_performed':False,'checks':checks,'issue_count':len(issues)}
(ROOT/'V27_audit_results.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(result,ensure_ascii=False,indent=2))
sys.exit(1 if issues else 0)
