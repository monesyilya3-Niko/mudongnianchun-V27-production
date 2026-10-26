# Manus15s_105

> 本文件 = 《120 镜 Manus15 秒满格轨总表》中 **Manus15s_105** 这一块的完整指令，读完即可执行。
> 全局规则（IP 保留 / 五项铁律 / 接力链 / 自检清单）见《Manus执行交接书.md》，此处不重复。
> **执行职责：Manus仅生成本块3840×2160画面（15秒/360帧@24fps）及本块指定尾帧；所有Audio Cue均为声音组与口型时序参考，不生成/交付/嵌入音频。**

## 本块速查

| 项 | 值 |
|:---|:---|
| 块号 | **Manus15s_105**（第 105 / 120 块） |
| 时间码 | `26:00–26:15` |
| 帧区间 | `37441`–`37800` |
| 涵盖镜头 | Shot_157 (0–10s) + Shot_158 (10–15s) |
| 衔接模式 | **B · 末帧接力** |
| 0.0s 首帧 | 承接上一块尾帧 |
| 上一块尾帧 | `Shot_156_LastFrame.png` |
| 主母带 | `26_图3.21_Scene21_火锅店庆生宴帝王蟹螺蛳粉与左手银戒剥虾_3840x2160_4K.jpg`<br>File ID `1gQKEb8vorW3xmlepV5RuFSlDOIp-NhC1` |
| 锁脸图 | `02_图2.1…`<br>File ID `16_EbUVTBnl1JrXxnJQjCG9yg2vVrgB_c`<br>`03b_图2.2R…`<br>File ID `1xs8JeeE86UUaUtlD2mUY0auSXY278fFk` |
| 尾帧导出 | `Manus15s_105_LastFrame_360.png` |

---

## 一、块头与字段（摘自总表）

#### 原始块头：Manus15s_105 | 时间码 26:00–26:15 (15.0s) | 帧区间 37441–37800 | 涵盖 Shot_157 (0–10s) + Shot_158 (10–15s)
- **所属场次**：Scene 21：帝王蟹海鲜锅、炸腐竹红油螺蛳粉与戴银戒全程宠溺剥虾 (Cut 21C (3/5) -> Cut 21C (4/5))
- **3:2 跨镜映射关系**：`Shot_157 (全 10.0s · F001–F240) + Shot_158 (前半 5.0s · F241–F360)`
- **光学焦段 / 色温**：85mm f/1.4 | 3400K
- **Manus 衔接模式**：**模式B：末帧接力续生 (取 Shot_156 第240帧作0.0s首帧 -> F241(10.0s)跨镜切入 Shot_158 前半程 / Manus Extend 15s)**
- **V27本地参考母带文件**：26_图3.21_Scene21_火锅店庆生宴帝王蟹螺蛳粉与左手银戒剥虾_3840x2160_4K.jpg
- **0.0s 首帧 / 参考槽**：Shot_156_LastFrame.png (USE_SHOT_156_FRAME_240)
- **15.0s（第360帧）尾帧槽**：Manus15s_105_LastFrame_360.png (EXPORT_MANUS15S_105_FRAME_360)
- **辅助锁脸槽（Weight=0.35 仅锁五官骨相，严禁跨场串服）**：02_图2.1_女主角雨绪偏DBX_真人锁脸唯一颜值基准与第219帧_3840x2160_4K.jpg + 03b_图2.2R_男主冬冰絮_初雪夜黑夹克双层银链单人锁脸基准_1916x2160_4K.jpg
- **同步声轨与口型卡点**：【0.0–10.0s (Shot_157)】【女主·雨绪偏】「でもやっぱり、氷絮が剥いてくれたエビが世界一甘いね！」（但果然还是冰絮帮我剥的虾，是全世界第一甜呢！） ＋ 【10.0–15.0s (Shot_158前半)】【SFX】茶百道奶茶杯轻碰声与欢快笑声。
- **群像配角画外音（OS）跨镜对位**：无配角画外音（保持男女主原声/VO/环境Foley纯净度）
```text
· 【铁律1 · 光学镜头·画幅·色温死锁】：85mm f/1.4 · 色温 3400K · 16:9（3840×2160）全出血无黑边宽银幕 · 18%新海诚式高光柔和辉光（Bloom）与丁达尔体积光。
· 【铁律2 · 角色骨相·颜值·恒定特征死锁】：【双人骨相与恒定特征死锁】女主雨绪偏（DBX）：鹅蛋小V脸、清透冷白瓷肌（Lab L*≥88）、多层星芒琥珀大眼（严禁闭眼）、左眼外下方唯一一颗精致小美人痣、空气感齐刘海+一刀切公主切及腰黑长直发（佩戴本场专属粉白蕾丝双蝴蝶结发带）；男主冬冰絮（YXP）：同级清透少年冷白皮（Lab L*≥88）、蓬松深棕黑碎盖短发、斯文细黑框眼镜、左右双耳外侧对称佩戴银色双环耳骨夹+小耳圈。
· 【铁律3 · 本镜专属机位景别·服化道·解剖学左右手与防串服死锁】：【服化道与解剖学左右手死锁·换装与美食重点】全景落地窗火锅卡座（图3.21）：左椅背搭着男主黑色工装夹克，右椅背搭着女主樱花粉大衣与纯白围巾；左侧男主冬冰絮穿修身深色黑衬衫配双层银链，解剖学左手无名指清晰佩戴银色情侣戒，正用双手专注为女主剥大明虾壳；右侧女主雨绪偏身穿粉白洛丽塔蕾丝公主裙、头戴粉白蕾丝双蝴蝶结发带（严禁穿回冬装或缺失蕾丝发带！），双手持木筷与白瓷勺；餐桌恒定锁定：帝王蟹鲍鱼碎冰船、沸腾黄铜烟囱火锅、铺满金黄炸腐竹卷的青花瓷碗红油螺蛳粉、两杯蓝白熊猫杯手作奶茶。 【本镜（Manus15s_105 · 26:00–26:15 · 360帧满格 · Shot_157 (0–10s) + Shot_158 (10–15s)）专属五子镜画面边界锁】：前半程与后半程跨镜无缝衔接，严格遵循下方【铁律5】的 Sub-Cut α–ε 五子镜帧级动作轨迹。
· 【铁律4 · 声画同步·配乐SFX·台词口型与声优基频死锁】：【前半程 0.0–10.0s (Shot_157 · F001–F240)】【女主现场台词口型死锁】本镜为女主雨绪偏现场同期声开口台词：仅女主雨绪偏在 2.0s–8.0s 区间朱唇随日语台词音节自然微张开合对口型；同框倾听的男主冬冰絮必须保持双唇自然轻抿或微笑闭合注视，严禁倾听者乱张嘴！ ＋ 【后半程 10.0–15.0s (Shot_158前半 · F241–F360)】【画外音VO / 内心独白 / 纯配乐SFX·闭口微表情死锁】本镜声轨为画外音（VO）、内心独白或纯配乐/环境音效（SFX），画面中所有在场人物双唇必须保持自然轻抿或温柔浅笑闭合状态，严禁张嘴说话或嘴唇乱动对口型！通过眼神光流转、睫毛轻颤与呼吸起伏传递细腻情绪。 【本镜配乐（OST）与侧链锁】：乐章VII · 火锅庆生 — RADWIMPS《なんでもないや (Nandemonaiya - movie ver.)》（78 BPM · C大调 · 温暖木吉他与人声主歌慢板）；【声音组完整Cue（非画面生成任务）】：【0.0–10.0s (Shot_157)】【女主·雨绪偏】「でもやっぱり、氷絮が剥いてくれたエビが世界一甘いね！」（但果然还是冰絮帮我剥的虾，是全世界第一甜呢！） ＋ 【10.0–15.0s (Shot_158前半)】【SFX】茶百道奶茶杯轻碰声与欢快笑声。；【声优基频与发音死锁】：男主冬冰絮（YXP）声优基频锁定 130Hz 温润少年音（神木隆之介声线），女主雨绪偏（DBX）声优基频锁定 245Hz 清澈少女音（上白石萌音声线），林夏栀锁定 260Hz 明快御姐音（纯OS），陈默野锁定 145Hz 沉稳男中音（纯OS），周凛山教授锁定 95Hz 浑厚低音炮（纯OS），片名「暮冬」严格读作 ぼとう（Botō，严禁误读为くれふゆ）。
· 【铁律5 · Manus 15.0秒（360帧 @24.000fps）五子镜关键帧运镜与动态轨迹死锁】：【Sub-Cut α · 0.0–2.5秒（第001–060帧 · Keyframes F001→F030→F060 · 源自 Shot_157 起幅）】以 `Shot_156_LastFrame.png` 定锚起幅（85mm f/1.4，色温 3400K）：85mm近景特写穿粉色洛丽塔公主裙的雨绪偏，她幸福地细细品尝冬冰絮亲手剥好的虾仁。【Sub-Cut β · 2.5–6.0秒（第061–144帧 · Keyframes F061→F102→F144 · 源自 Shot_157 主动作）】白皙脸颊漾起甜甜的酒窝，眉眼弯弯地对冬冰絮说出“冰絮剥的虾是全世界第一甜”。【Sub-Cut γ · 6.0–10.0秒（第145–240帧 · Keyframes F145→F192→F240 · 源自 Shot_157 递进段）】她左眼外下方的小美人痣在水晶暖光下熠熠生辉，说话者口型开合严格匹配日语台词音节节奏，眼神高光与面部微表情细腻传神。【Sub-Cut δ · 10.0–13.0秒（第241–312帧 · Keyframes F241→F276→F312 · 跨镜切入 Shot_158 前半程）】第241帧无缝切入 `Shot_158`（85mm f/1.4，3400K）：冬冰絮看着她大快朵颐的可爱模样；左手银戒微闪，又宠溺地夹起一块帝王蟹腿肉放到她碗里。【Sub-Cut ε · 13.0–15.0秒（第313–360帧 · Keyframes F313→F336→F360）Manus 15秒满格阻尼稳像与第360帧锁】F313起按24fps院线阻尼曲线平稳减速，于第15.00秒（第360帧）零动态模糊定格并导出 `Manus15s_105_LastFrame_360.png`（`EXPORT_MANUS15S_105_FRAME_360`）供 `Manus15s_106` 第001帧无缝接力。
· 【铁律6 · Manus 15秒满格视频生成平台首尾帧槽位与多图权重死锁】：【Manus衔接模式】模式B：末帧接力续生 (取 Shot_156 第240帧作0.0s首帧 -> F241(10.0s)跨镜切入 Shot_158 前半程 / Manus Extend 15s)；【0.0s(第001帧)首帧/参考槽位】`Shot_156_LastFrame.png (USE_SHOT_156_FRAME_240)`；【15.0s(第360帧)尾帧槽位】`Manus15s_105_LastFrame_360.png (EXPORT_MANUS15S_105_FRAME_360)`；【辅助锁脸槽位（Weight=0.35 仅锁五官骨相，严禁跨场串服）】02_图2.1_女主角雨绪偏DBX_真人锁脸唯一颜值基准与第219帧_3840x2160_4K.jpg + 03b_图2.2R_男主冬冰絮_初雪夜黑夹克双层银链单人锁脸基准_1916x2160_4K.jpg。
· 【铁律7 · 单镜靶向负面提示词分段死锁（Negative）】：【前半程 0.0–10.0s (Shot_157 · F001–F240)】变形的手指、多余的手臂（严禁三只手）、手指粘连或缺失、左右手镜像颠倒、闭眼或半眯眼、斗鸡眼、偏黄偏暗肤色（严禁面部脏暗阴影）、多余黑边或画中画内框、画面闪烁伪影、文字乱码、廉价3D塑料感、左眼外下方美人痣缺失或移位、男主双耳银色耳骨夹缺失、严禁遗漏女主粉白蕾丝双蝴蝶结发带、严禁出现垂直分屏黑线或左右双屏割裂画面、画面内严禁出现任何扭曲乱码文字、除参考图既有道具与商标外的其他商标Logo或多余水印、严禁奶茶杯身出现除参考图既有字样外的其他商标汉字；餐具严禁出现乱码标识 (deformed fingers, extra arms, three hands, fused or missing fingers, reversed left/right hands, closed or half-shut eyes, crossed eyes, dark or yellowish skin shadow, black letterbox/pillarbox borders, picture-in-picture frames, flickering artifacts, garbled text, cheap 3D CGI plastic look, missing or misplaced left under-eye beauty mole, missing symmetrical silver ear cuffs on boy, missing pink-and-white lace double-bow headband on heroine, vertical split-screen black line or split-panel frame) ＋ 【后半程 10.0–15.0s (Shot_158前半 · F241–F360)】变形的手指、多余的手臂（严禁三只手）、手指粘连或缺失、左右手镜像颠倒、闭眼或半眯眼、斗鸡眼、偏黄偏暗肤色（严禁面部脏暗阴影）、多余黑边或画中画内框、画面闪烁伪影、文字乱码、廉价3D塑料感、左眼外下方美人痣缺失或移位、男主双耳银色耳骨夹缺失、严禁遗漏女主粉白蕾丝双蝴蝶结发带、严禁出现垂直分屏黑线或左右双屏割裂画面、严禁人物张嘴说话或嘴唇乱动对口型、画面内严禁出现任何扭曲乱码文字、除参考图既有道具与商标外的其他商标Logo或多余水印、严禁奶茶杯身出现除参考图既有字样外的其他商标汉字；餐具严禁出现乱码标识 (deformed fingers, extra arms, three hands, fused or missing fingers, reversed left/right hands, closed or half-shut eyes, crossed eyes, dark or yellowish skin shadow, black letterbox/pillarbox borders, picture-in-picture frames, flickering artifacts, garbled text, cheap 3D CGI plastic look, missing or misplaced left under-eye beauty mole, missing symmetrical silver ear cuffs on boy, missing pink-and-white lace double-bow headband on heroine, vertical split-screen black line or split-panel frame, open mouth speaking, random lip movement or lip-syncing)
```
