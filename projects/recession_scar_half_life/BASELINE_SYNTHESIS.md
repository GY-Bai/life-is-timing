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

### United States｜Kahn 路径是明显的长期右尾

Kahn 2010 的 published text 报告：

```text
national unemployment rate +1pp
→ initial wage loss about 6–7%
```

并且：

```text
effect magnitude falls by roughly 0.25 percentage point per year
```

但到毕业后约 15 年：

```text
wage loss still about 2.5%
and statistically significant
```

所以在我们还没有完整年度 coefficient curve 前，最安全的标签是：

```text
long-persistence / right-tail case
```

而不是人为指定一个精确 half-life。

Source:  
https://www.sciencedirect.com/science/article/pii/S0927537109001018

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

### Finland｜shock severity 是不能忽略的变量

Päällysaho 2017：

全 graduation cohorts：

```text
annual earnings effect
lasts at least first 10 years

unemployment effect
roughly 7 years
```

但如果只看：

```text
1996–2004 cohorts
```

即排除 exceptionally deep early-1990s Finnish depression 后：

```text
earnings effect
only first ~5 years

unemployment effect
little to none
```

这说明：

> **Shock Severity 可能同时改变 initial loss 与 persistence。**

所以不能看到：

```text
Finland long scar
```

就全部归因于 labor-market institution。

Source:  
https://www.doria.fi/handle/10024/148933

---

## 2. 第一轮 mechanism map

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
