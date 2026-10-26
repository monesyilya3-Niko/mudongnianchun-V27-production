#!/usr/bin/env python3
from pathlib import Path
import re
ROOT=Path(__file__).resolve().parent
D=ROOT/'deliverables'
STYLE=(
'【全片统一视觉风格与语言总则】全片采用原创、高品质日本剧场版动画电影视觉语言：'
'手绘质感的精细环境背景与稳定、自然的角色动画相结合；构图有电影感，透视、景深与空间关系准确；'
'以可信自然光和大气透视塑造暮冬冷蓝、春雨青绿、黄昏橙金、雪夜蓝紫等分场色彩，跨镜保持同一调色逻辑；'
'云层、雨雪、水面、玻璃反光与城市灯光层次丰富但不过曝，辉光克制，粒子有明确环境来源；'
'角色线条干净、五官与服装跨帧稳定，手指肢体比例正确，发丝、布料、雨雪运动连续可信；'
'拒绝廉价AI观感：塑料皮肤、模板化五官、过度锐化、随机纹理、脏噪点、过强Bloom、过饱和霓虹、'
'透视错乱、肢体畸变、角色/服装漂移、伪文字、水印、画面拼贴、闪烁和不必要的镜头抖动。'
'画面生成描述、动作、机位、光线和场景执行语统一使用简体中文；日语对白必须按剧本原文保留，'
'Shot/Manus编号、F帧号、时间码、镜头光学缩写、单位、文件名等固定技术标记保留原文，不自行翻译或改写。'
)
REPLACES=[
 ('新海诚×京阿尼电影集级超清实景与静物微距光影镜头','原创高品质日本剧场版动画电影级背景与静物微距光影镜头'),
 ('新海诚式高光柔和辉光（Bloom）与丁达尔体积光','克制高光辉光（Bloom）与自然大气体积光'),
 ('新海诚式体积光束','自然大气体积光束'),
 ('新海诚式高光','克制、连续的电影级高光'),
 ('新海诚式光影','统一视觉总则规定的电影级光影'),
 ('新海诚式','统一视觉总则规定的电影级'),
 ('新海诚','原创动画电影视觉'),
 ('新海誠','原创动画电影视觉'),
 ('京阿尼','日本剧场版动画电影'),
]
# Update all Markdown copies so there is no conflicting named-style reference in prose or duplicate blocks.
for p in ROOT.rglob('*.md'):
 s=p.read_text(encoding='utf-8')
 for a,b in REPLACES:s=s.replace(a,b)
 if s!=p.read_text(encoding='utf-8'):p.write_text(s,encoding='utf-8')
# Add one exact canonical style/language instruction to each authoritative embedded prompt and the 120 stand-alone prompt bodies.
def update_payloads(p):
 s=p.read_text(encoding='utf-8')
 pat=re.compile(r'(?P<open>```text\n)(?P<body>.*?)(?P<close>\n```)',re.S)
 def sub(m):
  body=m.group('body')
  if '【全片统一视觉风格与语言总则】' in body:return m.group(0)
  return m.group('open')+STYLE+'\n'+body+m.group('close')
 out,n=pat.subn(sub,s)
 p.write_text(out,encoding='utf-8')
 return n
for p in [D/'vol_bible.md',D/'vol6_manus15.md',*sorted((D/'blocks').glob('Manus15s_*.md'))]:
 update_payloads(p)
print('Updated named style references and inserted uniform visual/language rule into 120 prompts and mirrored copies.')
