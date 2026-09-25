# Metric Specification｜如何定义 Scar Half-life

## 1. 为什么不能用“显著到第几年”

错误定义：

```text
Half-life
=
最后一个 p < 0.05 的年份
```

因为它把：

```text
effect magnitude
```

和：

```text
statistical power
```

混在一起。

---

## 2. Primary metric：normalized magnitude half-life

设同一 study / outcome 的 event-time effect 为：

```text
β_s
```

选择 reference：

```text
β_ref
=
first reliable post-entry effect
```

定义：

```text
m_s
=
|β_s| / |β_ref|
```

Scar Half-life：

```text
h_0.5
=
first s where m_s <= 0.5
```

如果年度点稀疏：

```text
linear interpolation
```

仅用于 descriptive estimate，并标记：

```text
interpolated = true
```

---

## 3. Persistent asymptote

有些 scar 不回到 0。

因此更合理的 decay model 是：

```text
β_s
=
β_inf
+
(β_0 - β_inf) exp(-λs)
```

对应：

```text
half-life
=
ln(2) / λ
```

但只有在：

- event-time points 足够；
- 方向稳定；
- fit 不明显失真；

时才估计。

否则只报告 empirical crossing。

---

## 4. Right censoring

如果论文观察到 T 年时：

```text
|β_T| > 0.5 |β_ref|
```

则：

```text
half-life > T
```

不能偷偷写成：

```text
half-life = T
```

例如 Kahn 2010 的 wage effect 在约 15 年仍显著为负，因此其 scar path 需要视为：

```text
right-censored
```

直到完整 curve extraction 后再估计。

---

## 5. Fade-out horizon

单独记录：

```text
H_zero
=
first event time authors describe effect as faded / near zero
```

这是：

```text
author-reported descriptive metric
```

不能和 half-life 混用。

已知例子：

- Netherlands academic wage loss：约 6 年 fade out；
- Canada：earnings losses约 8–10 年 fade；
- Finland post-1990s-depression subsample：earnings effects约前 5 年；
- Kahn US sample：15 年后仍有 wage loss，属于长期右删失型路径。

这些 summary 必须在 effect extraction 中回到 table / figure 后才能进入定量比较。

---

## 6. Sign reversal

如果 β_s：

```text
negative
→ zero
→ positive
```

不能简单继续套 exponential decay。

需要标记：

```text
path_type = reversal
```

并单独分析 turning point。

---

## 7. Multiple outcomes

同一个 cohort 可能：

```text
wage scar ↓
但
employment scar ≈ 0
```

或者：

```text
wage recovery
但
mismatch persists
```

因此每个 outcome 单独计算 decay。

禁止创造：

```text
one synthetic scar score
```

除非未来有明确 measurement model。

---

## 8. 最终输出格式

每条 curve 至少输出：

```text
study_id
country
outcome
sample_group
treatment_unit
reference_event_time
reference_beta
half_life_empirical
half_life_model
fade_out_horizon
right_censored
path_type
source_table
source_page
```
