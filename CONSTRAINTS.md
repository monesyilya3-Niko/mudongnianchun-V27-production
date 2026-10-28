# 《暮冬念春》V27 工程约束与质量门禁规范 (CONSTRAINTS.md)

> 本文件定义了 V27 制作交付包的**物理约束、确定性门禁、审计判定与阻断条件**。

---

## 一、唯一物理放行门禁 (Single Source of Truth)

本工程状态由 `audit_v27_candidate.py` 仲裁，严禁任何人工或口头绕过。

```bash
python audit_v27_candidate.py
```

### 放行合格判据（必须同时满足，缺一不可）：
1. 退出码（Exit Code）严格为 `0`；
2. `"script_package_ready_to_start_video": true`；
3. `"blocking_checks": []` 为空；
4. `"issue_count": 0`；
5. 23 项检查全部为 `pass`。

---

## 二、23 项自动化审计项说明与容忍度

| 序号 | 检查项 (Check Name) | 校验标准 | 容忍度 |
| :---: | :--- | :--- | :---: |
| 1 | `Unit15s block coverage` | `vol6_unit15s.md` 包含完整的 120 个提示词块正文 | 零容忍 |
| 2 | `Bible prompt coverage` | `vol_bible.md` 包含完整的 120 个内嵌提示词块正文 | 零容忍 |
| 3 | `stand-alone prompt parity` | `blocks/Unit15s_NNN.md` 120 块与总表正文 100% 逐字相同 | 零容忍 |
| 4 | `per-block audio boundary` | 120 块必须均声明“Unit仅生成本块3840×2160画面...不生成/交付/嵌入音频” | 零容忍 |
| 5 | `Bible-to-master prompt parity` | 圣经内嵌 120 块与总表 120 块 100% 逐字相同 | 零容忍 |
| 6 | `218+1 asset accounting` | 圣经必须明确写明“218 张历史实拍照片”与“第 219 帧合成” | 零容忍 |
| 7 | `legacy contradiction sweep` | 严禁残留历史错误表述（如 1+1+217=219、最后219张照片、这十天推掉你的约会等） | 零容忍 |
| 8 | `Shot_123 corrected timeline` | 正确限定日期范围，消除既有拒绝约会的时序矛盾 | 零容忍 |
| 9 | `Shot_124/128 revised frame` | 核心日文台词准确区分实拍照片（218枚の実写写真）与合成帧（最後の219フレーム目） | 零容忍 |
| 10 | `Unit audio generation boundary`| 明确声画职责分离，声音工作全部归入声音组 | 零容忍 |
| 11 | `180-shot structure` | 严格保持 180 个 `#### Shot_### \|` 镜头标题 | 零容忍 |
| 12 | `Unit15s_101 food-only shot` | 螺蛳粉特写镜头必须明确“人物不入画且不得出现头、脸、手或身体” | 零容忍 |
| 13 | `Unit15s_102 tail-frame contract`| 必须导出 `Unit15s_102_LastFrame_360.png`，严禁误标为 Shot F240 | 零容忍 |
| 14 | `Unit15s_119 VO direction` | 终幕画外合声 VO 必须明确背影人物“全程闭口、不做口型” | 零容忍 |
| 15 | `uniform style rule in prompt` | 120 块必须有且仅有一次【全片统一视觉风格与语言总则】标签 | 零容忍 |
| 16 | `Shinkai-anchored style` | 120块提示词正典段须含 Makoto Shinkai 导演锚点及《你的名字。》《天气之子》《铃芽之旅》质感锚点 | 零容忍 |
| 17 | `English execution layer declared`| 120 块中文源提示必须声明面向视频模型使用英文并忠实表达 | 零容忍 |
| 18 | `visual and language standard` | `V27_统一视觉与语言规范.md` 存在且包含关键规范关键词 | 零容忍 |
| 19 | `legacy cloud references` | 全项目文本中 Google Drive ID、Drive URL、File ID 残留必须严格为 0 | 零容忍 |
| 20 | `local image asset set` | 40 张源母带 (`source_masters`) + 10 张选定候选 (`selected_images`) 全部在位 | 零容忍 |
| 21 | `platform production workflow` | `V27_制作与发布流程.md` 包含 B站、抖音、AI标识、5秒适配 | 零容忍 |
| 22 | `English prompt coverage` | `deliverables/model_prompts_en/` 必须存在完整的 120 份编号文件 | **当前阻断** |
| 23 | `English review ledger approval` | `V27_英译执行提示审校台账.csv` 120 项哈希绑定、三项检查 PASS、导演 APPROVED | **当前阻断** |

---

## 三、英文模型执行层不变量语法 (Deterministic Invariants)

在生成或审核 `deliverables/model_prompts_en/Unit15s_NNN.md` 时，必须通过以下确定性不变量测试：

1. **Title 校验**：以 `# Unit15s_NNN` 开头。
2. **代码块数量一致**：Markdown 内部 ````text` 块计数与中文源稿严格相等。
3. **资产标识符保真**：反引号包含的所有标记（`` `token` ``）必须 100% 在英文稿中存在。
4. **镜号与块号完整**：`Shot_###` 与 `Unit15s_###` 出现次数不得少于源稿。
5. **技术 Token 原样保留**：数值+单位（`fps|mm|K|dB|Hz|BPM|px|s`）必须原样存在，如 `3840×2160`、`24mm Anamorphic f/2.8`、`6500K`、`111.9Hz`、`Lab L*≥88`。
6. **日文对白逐字保留**：引号包含的原版日文对白（`「...」` 与 `『...』`）原样保留，严禁擅自翻译或删减。
7. **彻底清除中文结构标签**：严禁残留“【全片统一视觉风格与语言总则】”或“一、二、三”中文章节前缀，必须翻译为严谨电影专业术语。

---

## 四、跨 Shot 口型绝对时码基准

配音窗口必须以对应 `Shot` 起点为零点，跨 15 秒块连续映射，严禁在块边界截断：

- **Shot_014 (02:10–02:20)**：口型窗口全片 02:12–02:18（跨 `Unit15s_009` 局部 12–15s 与 `Unit15s_010` 局部 0–3s）。
- **Shot_026 (04:10–04:20)**：口型窗口全片 04:12–04:18（跨 `Unit15s_017` 局部 12–15s 与 `Unit15s_018` 局部 0–3s），04:18 口型结束后再安排镜头运动。
- **Shot_027 (04:20–04:30)**：口型窗口全片 04:22–04:28（对应 `Unit15s_018` 局部 7–13s），男主为唯一说话者，女主全程闭口。
