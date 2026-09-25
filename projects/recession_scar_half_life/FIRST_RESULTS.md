# First Results｜Project 01

> 状态：**Japan / US / Finland / Canada 已有 verified table-level extraction；Netherlands 仍以 published summary 为主。**  
> 这不是国家排名，也不是 R3 的最终检验。

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

Japan、US、Finland 与 Canada 已经有可核验的 effect path。

下一步优先：

```text
van den Berge 2018
→ 尽量取得 academic / vocational annual wage path
→ 再做 normalized within-study comparison
```

在 treatment / specification 没有被明确记录前，不做 pooled cross-country regression。


---

# 5. United States｜Kahn 2010 exact Table 4 extraction

Kahn 的 Table 4 现在已经进入 machine-readable curve。

### National OLS

```text
year 1   -0.059
year 5   -0.050
year 10  -0.038
year 15  -0.026
```

以 year-1 magnitude 为 reference：

```text
half target = 0.0295
```

在 year 10 与 15 之间做 descriptive linear interpolation：

```text
half-life ≈ 13.54 years
```

### National IV

```text
-0.074
-0.059
-0.040
-0.022
```

descriptive half-life：

```text
≈ 10.83 years
```

### State IV

```text
-0.105
-0.103
-0.100
-0.097
```

到 year 15 magnitude 仍远高于 year-1 的一半，因此：

```text
half-life > 15 years
```

是 right-censored。

## 6. 一个新的方法论结果：half-life 对 specification 很敏感

同一篇论文、同一批 NLSY79 white male college graduates：

```text
National OLS  ≈ 13.54 years
National IV   ≈ 10.83 years
State IV      >15 years
```

所以“美国 scar 的 half-life 是多少”本身就是一个过度简化的问题。

更准确：

> **Scar decay 取决于 exposure definition 与 identification variation。**

这意味着未来 cross-country synthesis 必须同时保存：

```text
country
+
sample
+
treatment
+
specification
```

不能只保存：

```text
country → one number
```

这也是为什么 Project 01 不会做国家 ranking。


---

# 7. Finland｜exact annual curve 已经改变了我们对“shock severity”的表述

Päällysaho 2017 Table 2 给出 1988–2004 全部 cohort 的 annual earnings curve：

```text
year 1   -0.0210
year 2   -0.0178
year 3   -0.0163
year 4   -0.0151
year 5   -0.0148
year 6   -0.0140
year 7   -0.0125
year 8   -0.0115
year 9   -0.0105
year 10  -0.0099
```

year-1 magnitude 的一半是：

```text
0.0105
```

而 year 9 恰好是：

```text
-0.0105
```

所以：

```text
descriptive magnitude half-life = 9.0 years
```

这一次不需要 interpolation。

## 8. 1996–2004 cohort 的 half-life 明显更短

Table 3 中 post-depression cohorts：

```text
year 1   -0.0237
year 2   -0.0152
year 3   -0.0123
year 4   -0.0106
year 5   -0.0087
...
```

half target：

```text
0.01185
```

因此：

```text
half-life ≈ 3.26 years
```

而作者报告：

```text
5% significance horizon ≈ 5 years
```

再次验证：

```text
magnitude half-life
≠
significance horizon
```

## 9. 一个更重要的识别提醒

表面上：

```text
All cohorts half-life = 9y
Post-depression = 3.26y
```

很容易被写成：

```text
deep depression
→ scar persistence × 3
```

但这还不能成立。

因为 Table 3 的 sample restriction 同时改变了：

```text
cohort composition
aggregate historical contrast
regional identifying variation
```

所以目前只能说：

> **Finland 提供了强烈的 persistence heterogeneity evidence，但还不能把 9.0 / 3.26 的差完全解释成 shock severity 的 causal effect。**

这一步让 R3 的 Phase II 研究问题进一步收缩：

```text
不是：
“哪个国家 scar 更久？”

而是：
“在什么 identification design 下，
哪一部分 persistence 可以归因于 shock，
哪一部分来自 institution / composition / exposure construction？”
```


---

# 10. Canada｜同一制度内部，re-matching speed 已经表现出巨大异质性

Oreopoulos、von Wachter、Heisz 2012 Table 2 的 full-sample annual-earnings effects：

```text
experience 0–1   -0.0183
experience 4–5   -0.0089
experience 9–10  -0.0042
```

以 grouped midpoint：

```text
0.5, 4.5, 9.5
```

构造 descriptive magnitude half-life：

```text
≈ 4.39 years
```

这与作者的文字结论——典型 recession 的初始 earnings loss 大约五年减半、十年左右消退——在量级上相容。

## 11. Employer quality 的恢复几乎同步发生

Average firm median log earnings：

```text
-0.0096
-0.0042
-0.0028
```

descriptive half-life：

```text
≈ 4.06 years
```

论文同时指出，毕业时受到坏 labor-market shock 的人更可能先进入低质量 employer；之后前 3–5 年 employer quality 改善最快，而这一阶段也正是 job mobility 较高的时候。

所以 Canada 目前是 R3 最直接的 mechanism case：

```text
Bad Entry
→ Lower-quality Employer
→ Job Mobility
→ Employer Upgrading
→ Partial Earnings Catch-up
```

## 12. 最重要的结果其实来自 skill heterogeneity

Annual earnings 的 grouped path：

```text
Bottom quintile:
-0.0277 → -0.0167 → -0.0161
half-life > 9.5y

Middle:
-0.0232 → -0.0124 → -0.0039
half-life ≈ 4.97y

Top:
-0.0147 → -0.0042 → -0.0024
half-life ≈ 3.30y
```

于是同一个国家、同一套数据、同一种 regional-unemployment exposure 下：

> **recovery speed 的差异已经可以在 worker type 内部出现，而不需要先诉诸“日本制度 vs 美国制度”。**

这对 R3 是一个重要收缩：

```text
Re-entry Flexibility
```

不能只定义成国家制度变量。

它还必须包含：

```text
worker-specific access to better offers
mobility cost
initial employer quality
search capacity
```

## 13. Bottom group 是一个真正的 persistence case

Bottom predicted-earnings quintile 的 employer-quality path：

```text
-0.0111
-0.0087
-0.0126
```

并没有表现出单调 catch-up。

这与作者的解释一致：较弱势毕业生的 job mobility 更有限，更可能长期停留在 lower-paying employer / sector。

所以 Project 01 到这里出现了一个比“国家 half-life”更有价值的研究对象：

```text
Who gets access to re-matching?
```

而不是只问：

```text
How flexible is the country?
```
