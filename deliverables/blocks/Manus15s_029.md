# Manus15s_029

> 本文件 = 《120 镜 Manus15 秒满格轨总表》中 **Manus15s_029** 这一块的完整指令，读完即可执行。
> 全局规则（IP 保留 / 五项铁律 / 接力链 / 自检清单）见《Manus执行交接书.md》，此处不重复。
> **执行职责：Manus仅生成本块3840×2160画面（15秒/360帧@24fps）及本块指定尾帧；所有Audio Cue均为声音组与口型时序参考，不生成/交付/嵌入音频。**

## 本块速查

| 项 | 值 |
|:---|:---|
| 块号 | **Manus15s_029**（第 29 / 120 块） |
| 时间码 | `07:00–07:15` |
| 帧区间 | `10081`–`10440` |
| 涵盖镜头 | Shot_043 (0–10s) + Shot_044 (10–15s) |
| 衔接模式 | **C · 前导留空** |
| 0.0s 首帧 | 留空（挂场景参考 Weight=0.65） |
| 上一块尾帧 | `Shot_042_EndHold_Frame240.png` |
| 主母带 | `10_图3.7a_Scene07_私人放映室同看你的名字双色彗星_3840x2160_4K.jpg`<br>File ID `14v7v3IDOO1ZBNAjk-8L4KD40DmLf1piD` |
| 锁脸图 | `02_图2.1…`<br>File ID `16_EbUVTBnl1JrXxnJQjCG9yg2vVrgB_c`<br>`03b_图2.2R…`<br>File ID `1xs8JeeE86UUaUtlD2mUY0auSXY278fFk` |
| 尾帧导出 | `Manus15s_029_LastFrame_360.png` |

---

## 一、块头与字段（摘自总表）

#### 原始块头：Manus15s_029 | 时间码 07:00–07:15 (15.0s) | 帧区间 10081–10440 | 涵盖 Shot_043 (0–10s) + Shot_044 (10–15s)
- **所属场次**：Scene 07：十日温柔证明（Day 9）——私人放映室里的《你的名字。》与丝绒扶手十指紧扣 (Cut 07A (1/4) -> Cut 07A (2/4))
- **3:2 跨镜映射关系**：`Shot_043 (全 10.0s · F001–F240) + Shot_044 (前半 5.0s · F241–F360)`
- **光学焦段 / 色温**：35mm Anamorphic f/1.4 | 6200K
- **Manus 衔接模式**：**模式C-前导：场景/角色参考起幅 (0.0s首帧槽留空，防提前锁死高潮定格 -> F241(10.0s)跨镜切入 Shot_044 前半程 / Manus Reference Lead-In)**
- **V27本地参考母带文件**：10_图3.7a_Scene07_私人放映室同看你的名字双色彗星_3840x2160_4K.jpg
- **0.0s 首帧 / 参考槽**：NONE_SCENE_REF_LEAD_IN (0.0s首帧槽留空，挂载 10_图3.7a_Scene07_私人放映室同看你的名字双色彗星_3840x2160_4K.jpg 至场景参考槽 Weight=0.65) (SCENE_REF_ONLY_LOCAL_ASSET)
- **15.0s（第360帧）尾帧槽**：Manus15s_029_LastFrame_360.png (EXPORT_MANUS15S_029_FRAME_360)
- **辅助锁脸槽（Weight=0.35 仅锁五官骨相，严禁跨场串服）**：02_图2.1_女主角雨绪偏DBX_真人锁脸唯一颜值基准与第219帧_3840x2160_4K.jpg + 03b_图2.2R_男主冬冰絮_初雪夜黑夹克双层银链单人锁脸基准_1916x2160_4K.jpg
- **同步声轨与口型卡点**：【0.0–10.0s (Shot_043)】【SFX】放映机轻微的胶片光束声；【BGM】RADWIMPS《デート (Date)》温柔的钢琴独奏在影厅内流淌。 ＋ 【10.0–15.0s (Shot_044前半)】【男主·冬冰絮】「九日目の証明は、僕たちを繋いでくれたこの映画。」（第九天的证明，是这部把我们连在一起的电影。）
- **群像配角画外音（OS）跨镜对位**：无配角画外音（保持男女主原声/VO/环境Foley纯净度）
```text
· 【铁律1 · 光学镜头·画幅·色温死锁】：35mm Anamorphic f/1.4 · 色温 6200K · 16:9（3840×2160）全出血无黑边宽银幕 · 18%新海诚式高光柔和辉光（Bloom）与丁达尔体积光。
· 【铁律2 · 角色骨相·颜值·恒定特征死锁】：【双人骨相与恒定特征死锁】女主雨绪偏（DBX）：鹅蛋小V脸、清透冷白瓷肌（Lab L*≥88）、多层星芒琥珀大眼（严禁闭眼）、左眼外下方唯一一颗精致小美人痣、空气感齐刘海+一刀切公主切及腰黑长直发（严禁添加任何头饰发带）；男主冬冰絮（YXP）：同级清透少年冷白皮（Lab L*≥88）、蓬松深棕黑碎盖短发、斯文细黑框眼镜、左右双耳外侧对称佩戴银色双环耳骨夹+小耳圈。
· 【铁律3 · 本镜专属机位景别·服化道·解剖学左右手与防串服死锁】：【服化道与左右手死锁】私人放映室双人深红丝绒座椅（左扶手杯托插着冷饮杯）：女主雨绪偏坐在左侧（图3.7a），身穿黑白横条纹宽松毛衣（无发箍头饰，严禁穿JK制服或粉大衣），右膝/右扶手前侧平放樱花粉浮雕随身圆镜；男主冬冰絮坐在右侧，身穿黑色拉链工装夹克内搭纯白无字棉质T恤、颈戴双层银链；在图3.7b越轴手部微距中，左侧为男主黑夹克白内衬袖口伸出的左手，右侧为女主黑白条纹毛衣袖口伸出的右手，两手在深红丝绒扶手上十指紧扣。 【本镜（Manus15s_029 · 07:00–07:15 · 360帧满格 · Shot_043 (0–10s) + Shot_044 (10–15s)）专属五子镜画面边界锁】：前半程与后半程跨镜无缝衔接，严格遵循下方【铁律5】的 Sub-Cut α–ε 五子镜帧级动作轨迹。
· 【铁律4 · 声画同步·配乐SFX·台词口型与声优基频死锁】：【前半程 0.0–10.0s (Shot_043 · F001–F240)】【画外音VO / 内心独白 / 纯配乐SFX·闭口微表情死锁】本镜声轨为画外音（VO）、内心独白或纯配乐/环境音效（SFX），画面中所有在场人物双唇必须保持自然轻抿或温柔浅笑闭合状态，严禁张嘴说话或嘴唇乱动对口型！通过眼神光流转、睫毛轻颤与呼吸起伏传递细腻情绪。 ＋ 【后半程 10.0–15.0s (Shot_044前半 · F241–F360)】【男主现场台词口型死锁】本镜为男主冬冰絮现场同期声开口台词：仅男主冬冰絮在 2.0s–5.0s 区间双唇随日语台词音节自然微张开合对口型；5.0s台词结束后双唇闭合，镜头再环绕至背面；同框倾听的女主雨绪偏必须保持双唇自然轻抿或微笑闭合注视，严禁倾听者乱张嘴！ 【本镜配乐（OST）与侧链锁】：乐章III · 影院牵手 — RADWIMPS《デート (Date)》（68 BPM · 降B大调 · 温柔钢琴独奏与大提琴低吟）；【声音组完整Cue（非画面生成任务）】：【0.0–10.0s (Shot_043)】【SFX】放映机轻微的胶片光束声；【BGM】RADWIMPS《デート (Date)》温柔的钢琴独奏在影厅内流淌。 ＋ 【10.0–15.0s (Shot_044前半)】【男主·冬冰絮】「九日目の証明は、僕たちを繋いでくれたこの映画。」（第九天的证明，是这部把我们连在一起的电影。）；【声优基频与发音死锁】：男主冬冰絮（YXP）声优基频锁定 130Hz 温润少年音（神木隆之介声线），女主雨绪偏（DBX）声优基频锁定 245Hz 清澈少女音（上白石萌音声线），林夏栀锁定 260Hz 明快御姐音（纯OS），陈默野锁定 145Hz 沉稳男中音（纯OS），周凛山教授锁定 95Hz 浑厚低音炮（纯OS），片名「暮冬」严格读作 ぼとう（Botō，严禁误读为くれふゆ）。
· 【铁律5 · Manus 15.0秒（360帧 @24.000fps）五子镜关键帧运镜与动态轨迹死锁】：【Sub-Cut α · 0.0–2.5秒（第001–060帧 · Keyframes F001→F030→F060 · 源自 Shot_043 起幅）】以 `NONE_SCENE_REF_LEAD_IN (0.0s首帧槽留空，挂载 10_图3.7a_Scene07_私人放映室同看你的名字双色彗星_3840x2160_4K.jpg 至场景参考槽 Weight=0.65)` 定锚起幅（35mm Anamorphic f/1.4，色温 6200K）：4月10日（Day 9，周日）。【Sub-Cut β · 2.5–6.0秒（第061–144帧 · Keyframes F061→F102→F144 · 源自 Shot_043 主动作）】6200K星空蓝紫光影下的私人放映室全景（图3.7a，全出血无黑边16:9画幅）：前方巨幕正在放映《暮冬》蓝粉双色彗星划破夜空的经典画面。【Sub-Cut γ · 6.0–10.0秒（第145–240帧 · Keyframes F145→F192→F240 · 源自 Shot_043 递进段）】双人深红丝绒座椅左扶手杯托里插着带吸管的冷饮杯，穿黑白横条纹毛衣的雨绪偏（右膝平放樱花粉浮雕随身圆镜）与穿黑夹克配纯白无字棉质T恤双层银链的冬冰絮并肩而坐。【Sub-Cut δ · 10.0–13.0秒（第241–312帧 · Keyframes F241→F276→F312 · 跨镜切入 Shot_044 前半程）】第241帧无缝切入 `Shot_044`（35mm Anamorphic f/1.4，6200K）：银幕上双色彗星的璀璨流光溢满影厅；银幕双色彗星的蓝粉流光在雨绪偏多层星芒琥珀色大眼睛里投下梦幻星点，左眼外下方唯一的小美人痣清晰精致。【Sub-Cut ε · 13.0–15.0秒（第313–360帧 · Keyframes F313→F336→F360）Manus 15秒满格阻尼稳像与第360帧锁】F313起按24fps院线阻尼曲线平稳减速，于第15.00秒（第360帧）零动态模糊定格并导出 `Manus15s_029_LastFrame_360.png`（`EXPORT_MANUS15S_029_FRAME_360`）供 `Manus15s_030` 第001帧无缝接力。
· 【铁律6 · Manus 15秒满格视频生成平台首尾帧槽位与多图权重死锁】：【Manus衔接模式】模式C-前导：场景/角色参考起幅 (0.0s首帧槽留空，防提前锁死高潮定格 -> F241(10.0s)跨镜切入 Shot_044 前半程 / Manus Reference Lead-In)；【0.0s(第001帧)首帧/参考槽位】`NONE_SCENE_REF_LEAD_IN (0.0s首帧槽留空，挂载 10_图3.7a_Scene07_私人放映室同看你的名字双色彗星_3840x2160_4K.jpg 至场景参考槽 Weight=0.65) (SCENE_REF_ONLY_LOCAL_ASSET)`；【15.0s(第360帧)尾帧槽位】`Manus15s_029_LastFrame_360.png (EXPORT_MANUS15S_029_FRAME_360)`；【辅助锁脸槽位（Weight=0.35 仅锁五官骨相，严禁跨场串服）】02_图2.1_女主角雨绪偏DBX_真人锁脸唯一颜值基准与第219帧_3840x2160_4K.jpg + 03b_图2.2R_男主冬冰絮_初雪夜黑夹克双层银链单人锁脸基准_1916x2160_4K.jpg。
· 【铁律7 · 单镜靶向负面提示词分段死锁（Negative）】：【前半程 0.0–10.0s (Shot_043 · F001–F240)】变形的手指、多余的手臂（严禁三只手）、手指粘连或缺失、左右手镜像颠倒、闭眼或半眯眼、斗鸡眼、偏黄偏暗肤色（严禁面部脏暗阴影）、多余黑边或画中画内框、画面闪烁伪影、文字乱码、廉价3D塑料感、左眼外下方美人痣缺失或移位、男主双耳银色耳骨夹缺失、严禁在女主头上添加任何发箍或蝴蝶结发带头饰、严禁出现垂直分屏黑线或左右双屏割裂画面、严禁人物张嘴说话或嘴唇乱动对口型、画面内严禁出现任何扭曲乱码文字、除参考图既有道具与商标外的其他商标Logo或多余水印、严禁大银幕出现片名文字或T恤胸口出现Vintage News印字（银幕仅呈现纯净双色彗星星空，内搭为纯白无字T恤） (deformed fingers, extra arms, three hands, fused or missing fingers, reversed left/right hands, closed or half-shut eyes, crossed eyes, dark or yellowish skin shadow, black letterbox/pillarbox borders, picture-in-picture frames, flickering artifacts, garbled text, cheap 3D CGI plastic look, missing or misplaced left under-eye beauty mole, missing symmetrical silver ear cuffs on boy, any hairband, headband, or hair ribbon on heroine, vertical split-screen black line or split-panel frame, open mouth speaking, random lip movement or lip-syncing) ＋ 【后半程 10.0–15.0s (Shot_044前半 · F241–F360)】变形的手指、多余的手臂（严禁三只手）、手指粘连或缺失、左右手镜像颠倒、闭眼或半眯眼、斗鸡眼、偏黄偏暗肤色（严禁面部脏暗阴影）、多余黑边或画中画内框、画面闪烁伪影、文字乱码、廉价3D塑料感、左眼外下方美人痣缺失或移位、男主双耳银色耳骨夹缺失、严禁在女主头上添加任何发箍或蝴蝶结发带头饰、严禁出现垂直分屏黑线或左右双屏割裂画面、画面内严禁出现任何扭曲乱码文字、除参考图既有道具与商标外的其他商标Logo或多余水印、严禁大银幕出现片名文字或T恤胸口出现Vintage News印字（银幕仅呈现纯净双色彗星星空，内搭为纯白无字T恤） (deformed fingers, extra arms, three hands, fused or missing fingers, reversed left/right hands, closed or half-shut eyes, crossed eyes, dark or yellowish skin shadow, black letterbox/pillarbox borders, picture-in-picture frames, flickering artifacts, garbled text, cheap 3D CGI plastic look, missing or misplaced left under-eye beauty mole, missing symmetrical silver ear cuffs on boy, any hairband, headband, or hair ribbon on heroine, vertical split-screen black line or split-panel frame)
```
