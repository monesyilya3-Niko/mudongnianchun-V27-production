# V27 快速制作指南 — MiniMax + Muse 快做方案

> 状态: 脚本包出版级就绪 (23/23 PASS) | 工具链就绪 | 可直接开干

---

## 一、整体思路

```
Muse (策划+质检+自动化)  +  MiniMax 3000积分(执行)  +  4账号12000积分(补量)
       ↓                        ↓                      ↓
  提示词5秒切片              批量生成               轮换补量
  失败自动重试              并行加速               分月完成
  生成后质检                省积分                 保底交付
```

- **不重写提示词**: 原EN提示词已是出版级, 只做5秒切片 (2700-4300字/条, MiniMax最优区间)
- **不盲烧积分**: 单镜试探 → 单元验证 → 批量, 每步有质检闸门
- **不手工搬运**: 脚本自动处理360条台账

---

## 二、快速开始 (3步)

### Step 1: 预览提示词 (0积分)

```bash
# 看Unit15s_001的3个5秒切片长什么样
python -I tools/pipeline/batch_generate.py --clips 001 --dry-run

# 看前3个单元(9条)的全部预览
python -I tools/pipeline/batch_generate.py --clips 001-003 --dry-run
```

### Step 2: 单镜试探 (约45积分/条)

1. 从`tools/pipeline/batch_generate.py`导出的第一条提示词复制
2. 在MiniMax桌面版粘贴 + 挂上对应参考图:
   - `V27_U001_C01` → `04_图3.1_Scene01_暮冬之雪与春雨之窗_3840x2160_4K.jpg` (scene ref, Weight 0.65)
3. 生成5秒, 看效果
4. 用Muse帮你质检: 把生成的帧截图发给Muse, 问"脸崩了吗? 手正常吗?"

### Step 3: 批量 (试探通过后)

```bash
# 生成前3个单元(试片45秒 = 9条) — 约405积分
python -I tools/pipeline/batch_generate.py --clips 001-003

# 试片通过后, 全量360条 — 分批执行
python -I tools/pipeline/batch_generate.py --clips 001-030  # 第一批
python -I tools/pipeline/batch_generate.py --clips 031-060  # 第二批
# ...以此类推
```

---

## 三、积分规划

| 阶段 | 内容 | 积分消耗 | 建议账号 |
|------|------|----------|----------|
| 试探 | 1条5秒 x 2-3次重试 | ~135 | 主账号 |
| 试片 | 9条5秒 (Unit15s_001-003) x 平均2次 | ~810 | 主账号 |
| 批量 | 360条 x 平均2次 (H3 768P 45积分/条) | ~32,400 | 4账号轮换 |
| 节省 | 用H3 Max 480P批量(30积分/条), 择优768P精修 | ~21,600 | — |
| 分月 | 本月60% + 下月40% + 免费额度续命 | 分摊 | — |

**3000积分够**: 试探 + 试片 + 约40条批量
**12000积分够**: 480P完整版 或 768P分月完成

---

## 四、工具链

| 工具 | 作用 | 命令 |
|------|------|------|
| `prompt_optimizer_v2.py` | 5秒切片(10K→3K字) | `python -I tools/pipeline/prompt_optimizer_v2.py` |
| `batch_generate.py` | 批量生成(并行+重试) | `python -I tools/pipeline/batch_generate.py --clips 001-003 --dry-run` |
| `qc_pipeline.py` | 质检清单(8项) | `python -I tools/pipeline/qc_pipeline.py --clips 001-003` |
| `audit_v27_candidate.py` | 脚本包验证(23项) | `python -I audit_v27_candidate.py` |
| `validate_en_prompt.py` | 英译验证(120项) | `python -I validate_en_prompt.py` |

---

## 五、质检8项 (每条必查)

1. `face_stability` — 面部/五官稳定
2. `hand_limbs` — 手指/肢体无畸变
3. `clothing_consistency` — 服装跨帧一致
4. `perspective` — 透视正确
5. `lighting` — 光照符合场景
6. `motion_smoothness` — 动作流畅无闪烁
7. `text_watermark` — 无伪文字/水印
8. `negative_compliance` — 无塑料皮肤/廉价3D

---

## 六、常见问题

**Q: 提示词太长会被MiniMax截断吗?**
A: v2切片后每条2700-4300字, 在MiniMax H3的5000字限制内, 不会截断。

**Q: 失败率高怎么办?**
A: 单条失败2次就换写法 — 调整负面提示词或换参考图, 比硬烧省积分。

**Q: 4账号会被封吗?**
A: 主号付费+小号薅免费是常见做法, 避免4号同时高频生成。详看MiniMax用户协议。

**Q: 可以用Muse直接生成视频吗?**
A: 不能。Muse是文字/代码模型, 不生成视频。它帮你做策划、转换、质检, 执行靠MiniMax。

---

*生成时间: 2026-10-27 | 脚本版本: V27 RELEASED 23/23 PASS*
