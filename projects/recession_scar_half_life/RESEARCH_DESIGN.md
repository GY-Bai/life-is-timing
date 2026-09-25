# Research Design｜Recession Scar Half-life

## 1. Estimand

核心不是一个统一的跨国 causal coefficient。

第一阶段 estimand 是每篇研究内部的：

```text
dynamic response curve

β_s
=
effect of adverse entry condition
at s years after labor-market entry
```

其中：

```text
s = potential experience / years since graduation
```

然后才讨论：

```text
β_s 的 decay shape
```

是否与制度环境一致。

---

## 2. 为什么不能直接做“国际系数排行榜”

四个国家的论文 treatment 并不一致：

- unemployment rate at graduation；
- field-specific employment decline；
- cohort-group indicator；
- national / state unemployment；
- instrumented unemployment；
- recession dummy。

outcome 也不一致：

- wage；
- annual earnings；
- employment；
- regular employment；
- mismatch；
- employer quality。

因此：

```text
raw β
```

不可直接横向比较。

本项目禁止：

```text
Japan coefficient > Netherlands coefficient
→ Japan institution scar 更强
```

这种 naïve ranking。

---

## 3. 两阶段设计

### Stage A｜Within-study decay extraction

对每篇论文提取：

```text
β_0, β_1, ... β_T
SE / CI
outcome
treatment unit
sample
specification
```

然后在**同一篇论文内部**构造：

```text
Normalized Effect_s
=
β_s / β_reference
```

其中 reference 优先：

```text
first reliable post-entry coefficient
```

避免不同 treatment unit 造成量纲混淆。

### Stage B｜Cross-study mechanism comparison

比较：

- half-life；
- fade-out horizon；
- asymptotic persistence；
- employer / sector switching；
- mismatch persistence；
- heterogeneity by education / advantage。

这一步是：

```text
descriptive mechanism synthesis
```

不是跨国 causal meta-regression。

---

## 4. Identification buckets

每项研究必须标注设计等级。

### Bucket A｜Within-cohort / regional or field variation

例如：

- van den Berge：field-specific employment conditions；
- Kahn：state / national unemployment，另有 IV。

### Bucket B｜Cohort × region exposure construction

例如：

- Schwandt–von Wachter：birth cohort × state-of-birth 的 entry condition。

### Bucket C｜Administrative longitudinal cohort design

例如：

- Oreopoulos–von Wachter–Heisz：university-employer-employee longitudinal data。

### Bucket D｜Repeated cross-section / cohort profile

例如：

- Kondo 2024 的 cohort profiles + unemployment-at-entry specification。

不同 bucket 不应假装 identification strength 完全相同。

---

## 5. Primary outcome hierarchy

为了减少 researcher degrees of freedom，优先级预注册为：

```text
1. earnings / wage
2. employment / regular employment
3. employer quality
4. mismatch / occupation
5. switching / migration
```

其中：

```text
scar half-life
```

主要基于 1–2。

3–5 用于解释：

```text
为什么 decay 快 / 慢
```

而不是重新定义主结果。

---

## 6. Core explanatory variables

先只保留六个制度 /机制变量：

```text
Entry Gate Rigidity
Re-entry Flexibility
Employer Switching
Sector Switching
Education Track
Shock Severity
```

任何新增 explanatory variable 必须说明：

```text
它改变的是 R3 哪一个乘数？
```

否则放 notes，不进入主模型。

---

## 7. Main hypotheses

### H1｜Re-entry

```text
Re-entry Flexibility ↑
→ Scar Half-life ↓
```

### H2｜Mobility

```text
Employer / Sector Mobility ↑
→ Employer-quality mismatch decays faster
→ Wage scar decays faster
```

### H3｜Entry gate

```text
Front-loaded Entry Gate ↑
→ State Dependence ↑
→ Persistence ↑
```

### H4｜Shock severity

```text
Shock Severity ↑
→ Initial Effect ↑
and possibly
→ Persistence ↑
```

但 H4 必须和 institution effect 分开。

---

## 8. Falsification design

### F1

如果 Netherlands academic graduates 的快速 recovery：

```text
并不是 job / sector mobility
```

而主要来自 sample composition 或 macro rebound，则 H2 收缩。

### F2

如果 Japan 的 persistence 在控制 shock severity 后并不高于高-mobility systems，则 H3 收缩。

### F3

如果 Finland 1990s depression 只是把 initial effect 放大，但 normalized decay rate 与后续 cohorts 一样，则：

```text
Shock Severity
```

主要影响 level，不影响 half-life。

### F4

如果 low-advantage groups scar 更久，但 mobility 指标不能解释差异，则需要增加：

```text
credit / family / credential / network
```

等机制，而不是硬塞进 R3。

---

## 9. Selection risks

必须逐项记录：

- endogenous graduation timing；
- endogenous location；
- further schooling；
- labor-force non-entry；
- selective migration；
- sample attrition；
- unemployment-rate measurement；
- occupation / wage coding changes。

跨论文综合中：

```text
different correction strategies
```

本身就是解释变量，而不是 nuisance。

---

## 10. Phase II-1 的最小成功标准

不是发表一个跨国 causal coefficient。

而是完成：

```text
4-country source registry
+
paper-level effect extraction
+
normalized scar curves
+
censoring-aware half-life estimates
+
mechanism table
+
explicit null / contradiction log
```

只要最终发现：

```text
R3 无法跨制度稳定成立
```

项目仍然算成功。
