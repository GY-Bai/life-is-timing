# First Results｜Project 01

> 状态：**只包含 Japan Kondo 2024 的首批 verified extraction。**  
> 这不是跨国结论，也不是 R3 的最终检验。

## 1. 首个可计算结果

对 Kondo 2024 的 older subsample，使用：

```text
full-time annual earnings
per +1pp unemployment rate at labor-market entry
```

并以 grouped experience bin midpoint 作为 descriptive event time。

### High school：1984–2004 cohort window

原始 effect：

```text
1–3 years    -0.040
4–6 years    -0.030
7–9 years    -0.021
10–12 years  -0.012
```

如果以第一组：

```text
-0.040
```

作为 reference，则 half magnitude target 是：

```text
-0.020
```

它位于 7–9 与 10–12 两个 bin midpoint 之间。

线性插值：

```text
descriptive half-life ≈ 8.33 years
```

但论文在 10–12 years 的 coefficient 仍然显著为负。

因此：

> **Half-life ≠ Fade-out horizon。**

这是本项目 metric design 的第一个实际验证。

---

### Four-year college：1984–2004 cohort window

原始 effect：

```text
1–3 years    -0.030
4–6 years    -0.018
7–9 years    -0.005
10–12 years  +0.006
```

为避免 sign reversal 扭曲 decay metric，只使用前三个单调负值 bin。

reference：

```text
-0.030
```

half magnitude：

```text
-0.015
```

位于 4–6 与 7–9 bin midpoint 之间。

descriptive half-life：

```text
≈ 5.69 years
```

这和论文文字结论：

```text
college full-time annual earnings effect
statistically negative for six years
```

在量级上相容，但两者不是同一个统计量。

---

## 2. Younger cohort 是更重要的边界案例

1993–2013 younger subsample：

### High school

```text
-0.016
-0.004
+0.005
+0.010
```

### College

```text
+0.004
+0.013
+0.022
+0.024
```

这里不应该强行计算一个“scar half-life”。

因为：

```text
initial negative scar
```

本身已经明显减弱、消失或发生 sign reversal。

这比多算一个 half-life 更有研究价值：

> **同一个国家、相似的 labor-market institution，scar mechanism 本身也会随 historical period 改变。**

因此 R3 不能只依赖：

```text
Japan = rigid entry
```

还需要解释：

```text
为什么同样是 Japan，
post-ice-age cohorts 的 entry-unemployment effect 变弱了？
```

---

## 3. 当前对 R3 的影响

首批 extraction 暂时支持：

```text
Entry rigidity
不是充分条件。
```

更可能是：

```text
Persistent Scar
=
Entry Shock
× State Dependence
× Re-entry Friction
× Historical Labor-market Regime
```

其中最后一项目前只是：

```text
mechanism placeholder
```

不能因为 Japan younger cohort 结果改变，就立刻发明一个新 regularity。

下一步应该从 Kondo 本文讨论与其他国家材料中寻找具体机制：

- nonregular-to-regular transition 是否改变；
- cohort labor supply / demography；
- hiring practices；
- female / sector composition；
- prolonged stagnation 是否改变相对比较基准。

---

## 4. 下一步

接下来优先完成：

```text
Kahn 2010
Oreopoulos et al. 2012
van den Berge 2018
Päällysaho 2017
```

的 event-time extraction。

只有在至少三种制度环境存在可比较 curve 后，才开始画 cross-study normalized paths。
