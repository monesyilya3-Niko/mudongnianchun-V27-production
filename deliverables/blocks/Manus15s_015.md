# Manus15s_015

> 本文件 = 《120 镜 Manus15 秒满格轨总表》中 **Manus15s_015** 这一块的完整指令，读完即可执行。
> 全局规则（IP 保留 / 五项铁律 / 接力链 / 自检清单）见《Manus执行交接书.md》，此处不重复。
> **执行职责：Manus仅生成本块3840×2160画面（15秒/360帧@24fps）及本块指定尾帧；所有Audio Cue均为声音组与口型时序参考，不生成/交付/嵌入音频。**

## 本块速查

| 项 | 值 |
|:---|:---|
| 块号 | **Manus15s_015**（第 15 / 120 块） |
| 时间码 | `03:30–03:45` |
| 帧区间 | `05041`–`05400` |
| 涵盖镜头 | Shot_022 (0–10s) + Shot_023 (10–15s) |
| 衔接模式 | **B · 末帧接力** |
| 0.0s 首帧 | 承接上一块尾帧 |
| 上一块尾帧 | `Shot_021_LastFrame.png` |
| 主母带 | `07_图3.4_Scene04_4月1日高三同桌竖起DBX与YXP笔记本_3840x2160_4K.jpg`<br>File ID `1jaI5N3jdojN4z2lhQev2EI-GPXgLeuFD` |
| 锁脸图 | `02_图2.1…`<br>File ID `16_EbUVTBnl1JrXxnJQjCG9yg2vVrgB_c`<br>`03a_图2.2L…`<br>File ID `1rw2CxZ5n1dtQJzUY1eQ-aRRa6BvbUJ35` |
| 尾帧导出 | `Manus15s_015_LastFrame_360.png` |

---

## 一、块头与字段（摘自总表）

#### 原始块头：Manus15s_015 | 时间码 03:30–03:45 (15.0s) | 帧区间 05041–05400 | 涵盖 Shot_022 (0–10s) + Shot_023 (10–15s)
- **所属场次**：Scene 04：高三春季分班（4月1日）——笔记本封面上名字与缩写的宿命揭晓 (Cut 04A (2/2) -> Cut 04B (1/3))
- **3:2 跨镜映射关系**：`Shot_022 (全 10.0s · F001–F240) + Shot_023 (前半 5.0s · F241–F360)`
- **光学焦段 / 色温**：35mm f/1.8 -> 50mm f/1.4 双人中景 | 4800K
- **Manus 衔接模式**：**模式B：末帧接力续生 (取 Shot_021 第240帧作0.0s首帧 -> F241(10.0s)跨镜切入 Shot_023 前半程 / Manus Extend 15s)**
- **V27本地参考母带文件**：07_图3.4_Scene04_4月1日高三同桌竖起DBX与YXP笔记本_3840x2160_4K.jpg
- **0.0s 首帧 / 参考槽**：Shot_021_LastFrame.png (USE_SHOT_021_FRAME_240)
- **15.0s（第360帧）尾帧槽**：Manus15s_015_LastFrame_360.png (EXPORT_MANUS15S_015_FRAME_360)
- **辅助锁脸槽（Weight=0.35 仅锁五官骨相，严禁跨场串服）**：02_图2.1_女主角雨绪偏DBX_真人锁脸唯一颜值基准与第219帧_3840x2160_4K.jpg + 03a_图2.2L_男主冬冰絮_春秋季浅灰开衫单人锁脸基准_1916x2160_4K.jpg
- **同步声轨与口型卡点**：【0.0–10.0s (Shot_022)】【SFX】签字笔在笔记本封面书写的清脆沙沙声。 ＋ 【10.0–15.0s (Shot_023前半)】【SFX】笔记本竖立轻叩桌面的清脆声；【男主·冬冰絮】「雨緒偏（あめ おへん / Yu Xu Pian）……中国語読みの頭文字が、Y・X・P！？」（雨绪偏［Ame Ohen / 华语拼音 Yu Xu Pian］……首字母缩写居然是 Y·X·P！？）
- **群像配角画外音（OS）跨镜对位**：无配角画外音（保持男女主原声/VO/环境Foley纯净度）
```text
· 【铁律1 · 光学镜头·画幅·色温死锁】：35mm f/1.8 -> 50mm f/1.4 双人中景 · 色温 4800K · 16:9（3840×2160）全出血无黑边宽银幕 · 18%新海诚式高光柔和辉光（Bloom）与丁达尔体积光。
· 【铁律2 · 角色骨相·颜值·恒定特征死锁】：【双人骨相与恒定特征死锁】女主雨绪偏（DBX）：鹅蛋小V脸、清透冷白瓷肌（Lab L*≥88）、多层星芒琥珀大眼（严禁闭眼）、左眼外下方唯一一颗精致小美人痣、空气感齐刘海+一刀切公主切及腰黑长直发（严禁添加任何头饰发带）；男主冬冰絮（YXP）：同级清透少年冷白皮（Lab L*≥88）、蓬松深棕黑碎盖短发、斯文细黑框眼镜、左右双耳外侧对称佩戴银色双环耳骨夹+小耳圈。
· 【铁律3 · 本镜专属机位景别·服化道·解剖学左右手与防串服分段死锁】：【前半程 0.0–10.0s (Shot_022 · F001–F240)】【同桌低头书写姓名缩写锁（本镜正在桌面写字，尚未竖起笔记本）】4800K春樱教室同桌中近景：冬冰絮（左，浅灰开衫）与雨绪偏（右，条纹领结JK制服，右桌角放粉色相机与粉金星翼彗星挂坠）各自低头握签字笔，在平放于课桌上的科目笔记本封面上认真写下自己的本名与拼音缩写『DBX · 冬冰絮』与『YXP · 雨绪偏』（每人严格两只手，本镜尚未把笔记本竖立举起）。 ＋ 跨镜衔接：【后半程 10.0–15.0s (Shot_023前半 · F241–F360)】【服化道与左右手死锁】4月1日高三教室同桌并排（x=1920拼桌）：左侧男主冬冰絮穿浅灰V领针织开衫配白衬衫，双手将写有大号『DBX · 冬冰絮』的科目笔记本竖立在胸前课桌上；右侧女主雨绪偏穿白衬衫配红蓝白斜条纹领结JK制服（无发箍头饰），双手将写有大号『YXP · 雨绪偏』的科目笔记本竖立在课桌上；右桌角恒定摆放带白猫吊坠的粉色相机与粉金星翼彗星书签挂坠。 【本镜（Manus15s_015 · 03:30–03:45 · 360帧满格 · Shot_022 (0–10s) + Shot_023 (10–15s)）专属五子镜画面边界锁】：前半程与后半程跨镜无缝衔接，严格遵循下方【铁律5】的 Sub-Cut α–ε 五子镜帧级动作轨迹。
· 【铁律4 · 声画同步·配乐SFX·台词口型与声优基频死锁】：【前半程 0.0–10.0s (Shot_022 · F001–F240)】【画外音VO / 内心独白 / 纯配乐SFX·闭口微表情死锁】本镜声轨为画外音（VO）、内心独白或纯配乐/环境音效（SFX），画面中所有在场人物双唇必须保持自然轻抿或温柔浅笑闭合状态，严禁张嘴说话或嘴唇乱动对口型！通过眼神光流转、睫毛轻颤与呼吸起伏传递细腻情绪。 ＋ 【后半程 10.0–15.0s (Shot_023前半 · F241–F360)】【男主现场台词口型死锁】本镜为男主冬冰絮现场同期声开口台词：仅男主冬冰絮在 2.0s–5.0s 区间双唇随日语台词音节自然微张开合对口型；5.0s台词结束后双唇闭合，镜头再环绕至背面；同框倾听的女主雨绪偏必须保持双唇自然轻抿或微笑闭合注视，严禁倾听者乱张嘴！ 【本镜配乐（OST）与侧链锁】：乐章II · 相认 — RADWIMPS《三葉のテーマ》转《糸守高校 (Itomori High School)》（76→108 BPM · G大调 · 宿命相认弦乐渐强）；【声音组完整Cue（非画面生成任务）】：【0.0–10.0s (Shot_022)】【SFX】签字笔在笔记本封面书写的清脆沙沙声。 ＋ 【10.0–15.0s (Shot_023前半)】【SFX】笔记本竖立轻叩桌面的清脆声；【男主·冬冰絮】「雨緒偏（あめ おへん / Yu Xu Pian）……中国語読みの頭文字が、Y・X・P！？」（雨绪偏［Ame Ohen / 华语拼音 Yu Xu Pian］……首字母缩写居然是 Y·X·P！？）；【声优基频与发音死锁】：男主冬冰絮（YXP）声优基频锁定 130Hz 温润少年音（神木隆之介声线），女主雨绪偏（DBX）声优基频锁定 245Hz 清澈少女音（上白石萌音声线），林夏栀锁定 260Hz 明快御姐音（纯OS），陈默野锁定 145Hz 沉稳男中音（纯OS），周凛山教授锁定 95Hz 浑厚低音炮（纯OS），片名「暮冬」严格读作 ぼとう（Botō，严禁误读为くれふゆ）。
· 【铁律5 · Manus 15.0秒（360帧 @24.000fps）五子镜关键帧运镜与动态轨迹死锁】：【Sub-Cut α · 0.0–2.5秒（第001–060帧 · Keyframes F001→F030→F060 · 源自 Shot_022 起幅）】以 `Shot_021_LastFrame.png` 定锚起幅（35mm f/1.8 -> 50mm f/1.4 双人中景，色温 4800K）：雨绪偏偷偷用眼角余光瞥向身旁的新同桌。【Sub-Cut β · 2.5–6.0秒（第061–144帧 · Keyframes F061→F102→F144 · 源自 Shot_022 主动作）】雨绪偏惊讶地认出他正是球场上穿『0401』球衣的少年，心跳骤然加速、白皙耳尖泛起微红。【Sub-Cut γ · 6.0–10.0秒（第145–240帧 · Keyframes F145→F192→F240 · 源自 Shot_022 递进段）】两人各自低头用签字笔在崭新的科目笔记本封面上写下自己的汉字本名与拼音首字母缩写。【Sub-Cut δ · 10.0–13.0秒（第241–312帧 · Keyframes F241→F276→F312 · 跨镜切入 Shot_023 前半程）】第241帧无缝切入 `Shot_023`（50mm f/1.4 双人中景，4800K）：承接前镜写名字末帧；摄影机平滑切入50mm双人中景：冬冰絮与雨绪偏同时把写好名字的科目笔记本在胸前课桌上竖立起来互相自我介绍。【Sub-Cut ε · 13.0–15.0秒（第313–360帧 · Keyframes F313→F336→F360）Manus 15秒满格阻尼稳像与第360帧锁】F313起按24fps院线阻尼曲线平稳减速，于第15.00秒（第360帧）零动态模糊定格并导出 `Manus15s_015_LastFrame_360.png`（`EXPORT_MANUS15S_015_FRAME_360`）供 `Manus15s_016` 第001帧无缝接力。
· 【铁律6 · Manus 15秒满格视频生成平台首尾帧槽位与多图权重死锁】：【Manus衔接模式】模式B：末帧接力续生 (取 Shot_021 第240帧作0.0s首帧 -> F241(10.0s)跨镜切入 Shot_023 前半程 / Manus Extend 15s)；【0.0s(第001帧)首帧/参考槽位】`Shot_021_LastFrame.png (USE_SHOT_021_FRAME_240)`；【15.0s(第360帧)尾帧槽位】`Manus15s_015_LastFrame_360.png (EXPORT_MANUS15S_015_FRAME_360)`；【辅助锁脸槽位（Weight=0.35 仅锁五官骨相，严禁跨场串服）】02_图2.1_女主角雨绪偏DBX_真人锁脸唯一颜值基准与第219帧_3840x2160_4K.jpg + 03a_图2.2L_男主冬冰絮_春秋季浅灰开衫单人锁脸基准_1916x2160_4K.jpg。
· 【铁律7 · 单镜靶向负面提示词分段死锁（Negative）】：【前半程 0.0–10.0s (Shot_022 · F001–F240)】变形的手指、多余的手臂（严禁三只手）、手指粘连或缺失、左右手镜像颠倒、闭眼或半眯眼、斗鸡眼、偏黄偏暗肤色（严禁面部脏暗阴影）、多余黑边或画中画内框、画面闪烁伪影、文字乱码、廉价3D塑料感、左眼外下方美人痣缺失或移位、男主双耳银色耳骨夹缺失、严禁在女主头上添加任何发箍或蝴蝶结发带头饰、严禁出现垂直分屏黑线或左右双屏割裂画面、严禁人物张嘴说话或嘴唇乱动对口型、画面内严禁出现任何扭曲乱码文字、除参考图既有道具与商标外的其他商标Logo或多余水印、严禁笔记本封面与后墙黑板出现扭曲乱码字迹或除参考图既有周边外的其他动漫商标 (deformed fingers, extra arms, three hands, fused or missing fingers, reversed left/right hands, closed or half-shut eyes, crossed eyes, dark or yellowish skin shadow, black letterbox/pillarbox borders, picture-in-picture frames, flickering artifacts, garbled text, cheap 3D CGI plastic look, missing or misplaced left under-eye beauty mole, missing symmetrical silver ear cuffs on boy, any hairband, headband, or hair ribbon on heroine, vertical split-screen black line or split-panel frame, open mouth speaking, random lip movement or lip-syncing) ＋ 【后半程 10.0–15.0s (Shot_023前半 · F241–F360)】变形的手指、多余的手臂（严禁三只手）、手指粘连或缺失、左右手镜像颠倒、闭眼或半眯眼、斗鸡眼、偏黄偏暗肤色（严禁面部脏暗阴影）、多余黑边或画中画内框、画面闪烁伪影、文字乱码、廉价3D塑料感、左眼外下方美人痣缺失或移位、男主双耳银色耳骨夹缺失、严禁在女主头上添加任何发箍或蝴蝶结发带头饰、严禁出现垂直分屏黑线或左右双屏割裂画面、画面内严禁出现任何扭曲乱码文字、除参考图既有道具与商标外的其他商标Logo或多余水印、严禁笔记本封面与后墙黑板出现扭曲乱码字迹或除参考图既有周边外的其他动漫商标 (deformed fingers, extra arms, three hands, fused or missing fingers, reversed left/right hands, closed or half-shut eyes, crossed eyes, dark or yellowish skin shadow, black letterbox/pillarbox borders, picture-in-picture frames, flickering artifacts, garbled text, cheap 3D CGI plastic look, missing or misplaced left under-eye beauty mole, missing symmetrical silver ear cuffs on boy, any hairband, headband, or hair ribbon on heroine, vertical split-screen black line or split-panel frame)
```
