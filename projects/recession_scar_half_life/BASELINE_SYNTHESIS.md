# Baseline Synthesis｜Recession Scar Half-life

> 状态：**Phase II working synthesis**  
> 只使用目前已经回到 published / authoritative source 的结果。  
> 不做“哪个国家最差”的排名，不把不同 treatment unit 的 raw coefficient 直接比较。

## 1. 当前最可靠的横向事实

### Japan｜同一制度里，cohort regime 发生了变化

Kondo 2024 覆盖 graduation cohorts 1984–2013。

Older subsample 中，entry unemployment 对 full-time annual earnings 的负面影响清楚存在。

以四年制大学毕业生为例：

```text
experience 1–3   -0.030
experience 4–6   -0.018
experience 7–9   -0.005
experience 10–12 +0.006
```

而 1993–2013 younger subsample：

```text
+0.004
+0.013
+0.022
+0.024
```

Kondo 的核心结论也是：

```text
entry-unemployment effects on employment / earnings
are no longer statistically significant
for cohorts entering after the job-market ice age
```

因此：

> **“日本 entry gate rigid”本身不足以解释 scar persistence。**

同一个国家的 historical labor-market regime 也会改变 R3。

Source:  
https://academic.oup.com/ssjj/article/27/2/133/7727749

---

### United States｜Kahn Table 4 已经进入 exact fitted curve

Kahn 2010 Table 4 的 national OLS fitted effects：

```text
year 1   -0.059
year 5   -0.050
year 10  -0.038
year 15  -0.026
```

对应 descriptive magnitude half-life：

```text
≈ 13.54 years
```

National IV：

```text
-0.074
-0.059
-0.040
-0.022
```

对应：

```text
≈ 10.83 years
```

而 state IV 到 year 15 仍约：

```text
-0.097
vs year-1 -0.105
```

因此 magnitude half-life：

```text
> 15 years
```

这说明同一篇论文内部：

> **exposure definition + identification variation 本身就会显著改变 decay estimate。**

所以 US 不能被压成一个“13 年 scar”数字。

Source:  
https://doi.org/10.1016/j.labeco.2009.09.002

---

### Canada｜re-matching mechanism 最直接

Oreopoulos、von Wachter、Heisz 2012 的最终 AEJ 版本：

```text
unlucky graduates
→ persistent earnings declines lasting about ten years
```

其关键机制不是：

```text
same employer slowly restores wage
```

而是：

```text
start at lower-paying employers
→ gradual mobility
→ better firms
→ partial catch-up
```

作者早期 / complementary working-paper summary 进一步估计：

```text
firm quality + job mobility
can account for roughly 40–50%
of losses and catch-up
```

这使 Canada 成为 R3 中：

# Alternative Adjustment Routes

最直接的 mechanism anchor。

Sources:

https://www.aeaweb.org/articles?id=10.1257/app.4.1.1  
https://www.iza.org/publications/dp/3578/privacy-policy

---

### Netherlands｜同一国不同 education track，scar half-life 明显不同

van den Berge 2018：

#### Academic graduates

```text
~10% initial wage loss
per 1pp decline in field-specific employment
```

作者报告：

```text
wage loss fades after roughly 6 years
```

#### Higher vocational graduates

```text
~6% initial loss
```

但：

```text
~1% remains after 8 years
```

论文还指出：

```text
job / sector mobility
→ better-paying employers
```

是主要 catch-up mechanism。

因此：

> **initial damage 大，不代表 persistence 一定更长。**

Academic group：

```text
larger initial hit
but faster recovery
```

Vocational group：

```text
smaller initial hit
but more persistent mismatch
```

Source:  
https://www.wiljanvandenberge.com/research/bad-start-bad-match

---

### Finland｜exact annual curves 显示 persistence heterogeneity，但不能直接叫“severity effect”

Päällysaho 2017 Table 2：

```text
all cohorts 1988–2004
year 1  -0.0210
...
year 9  -0.0105
year 10 -0.0099
```

descriptive magnitude half-life：

```text
9.0 years
```

Table 3 的 1996–2004 cohorts：

```text
year 1 -0.0237
year 3 -0.0123
year 4 -0.0106
```

对应：

```text
half-life ≈ 3.26 years
```

差异很大。

但 sample restriction 同时改变：

```text
cohort composition
aggregate historical contrast
regional identifying variation
```

所以目前最稳妥的结论不是：

```text
“deep recession causally triples scar duration”
```

而是：

> **同一国家、同一数据框架中，persistence 对 cohort window / historical regime 极其敏感；shock severity 是候选解释，但不能单独从这个对比识别。**

Source:  
https://www.doria.fi/bitstream/handle/10024/148933/wp96.pdf

---

## 2. 第一轮 mechanism map## 2. 第一轮 mechanism map

目前五组 evidence 更像：

```text
Japan:
same country, later cohorts → scarring weakens

US:
long right-tail persistence

Canada:
employer upgrading is a major recovery route

Netherlands:
education track changes decay speed

Finland:
extreme recession changes persistence horizon
```

这意味着 R3 暂时应该进一步展开成：

```text
Scar Persistence
=
f(
Initial Shock Severity,
Entry-State Dependence,
Re-entry Flexibility,
Employer / Sector Mobility,
Education Track,
Historical Labor-market Regime
)
```

注意：

```text
Historical Labor-market Regime
```

目前只是一个 placeholder。

它必须继续被拆成可观察变量，不能成为“解释不了就归因于 regime”的垃圾桶。

---

## 3. 当前最重要的反直觉结果

### A. initial loss 与 persistence 可以分离

Netherlands：

```text
academic initial loss > vocational
```

但：

```text
academic recovery faster
```

所以：

```text
Scar Severity
≠ Scar Half-life
```

---

### B. institution 不应被当成 time-invariant constant

Japan younger cohorts 的结果说明：

```text
same national labor-market label
```

不等于：

```text
same transition matrix
```

企业 hiring、nonregular employment、demography、re-entry practice 都可能变化。

---

### C. “十年 scar”不是统一自然常数

目前 literature 已经同时出现：

```text
~5 years
~6 years
8–10 years
15+ year residual effect
```

它们来自不同 sample / outcome / treatment / institution。

所以本项目的目标绝不能变成：

```text
找一个 universal scar duration
```

真正目标是：

```text
解释 decay heterogeneity
```

---

## 4. 下一轮 extraction 优先级

### Priority 1

Kahn 2010：

```text
找到 / 提取 annual experience interaction coefficients
```

### Priority 2

Oreopoulos et al. 2012：

```text
earnings
employer quality
mobility
```

三条 curve 尽量来自同一 published specification。

### Priority 3

van den Berge 2018：

```text
academic vs vocational
annual wage curve
+
mismatch / employer-quality curve
```

### Priority 4

Päällysaho 2017：

```text
all cohorts
vs
1996–2004
```

用同一 outcome 比较 normalized decay。

---

## 5. 当前不做的事情

暂时不做：

```text
cross-country regression
institution score ranking
pooled meta-analysis
one-number international half-life
```

因为当前 study count 太少、treatment 与 outcome 不够统一。

先把：

```text
paper-level curves
```

做好，再决定下一步。
