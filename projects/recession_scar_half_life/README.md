# Project 01｜Recession Scar Half-life

> Phase II status: **ACTIVE — Japan / US / Canada / Finland table-level extraction verified; Netherlands in progress**  
> Primary target: **R3 Entry–Re-entry Hysteresis**

这个项目不再问：

```text
“recession graduates 有没有 scar？”
```

已有大量文献已经回答：

```text
有，而且存在明显异质性。
```

真正的问题是：

> **为什么 scar 在不同国家、教育轨道和制度环境中的衰减速度不同？**

---

## 研究对象

第一轮固定四个比较单元：

```text
Japan
United States / Canada
Netherlands
Finland
```

其中 Canada 被保留在 North American mechanism block，因为 Oreopoulos–von Wachter–Heisz 的 employer-upgrading 机制对 R3 特别重要。

---

## 研究目标

把：

```text
Bad Entry
→ Persistent Scar
```

拆成：

```text
Initial Shock
× State Dependence
× Re-entry Friction
÷ Alternative Adjustment Routes
→ Scar Decay Path
```

并研究：

```text
scar half-life
fade-out horizon
long-run asymptote
```

分别由什么决定。

---

## 当前阶段

### 已完成

- research question；
- falsifier；
- metric specification；
- cross-study comparability rules；
- data-access audit；
- source registry；
- effect-curve extraction schema；
- Kondo 2024 Tables 2–3 exact extraction；
- Kahn 2010 Table 4 fitted wage curves；
- Päällysaho 2017 Tables 2–3 annual earnings curves；
- Oreopoulos–von Wachter–Heisz 2012 Table 2 earnings / employer-quality / skill-quintile curves；
- descriptive scar half-life metrics；
- extraction correction log；
- half-life estimator skeleton；
- local metadata audit。

### 尚未完成

- 从 van den Berge 提取更完整的 academic / vocational event-time coefficients；
- cross-study normalized path；
- US public-data replication；
- restricted-microdata replication；
- cross-study descriptive synthesis。

---

## 目录

- [RESEARCH_DESIGN.md](RESEARCH_DESIGN.md)
- [METRIC_SPEC.md](METRIC_SPEC.md)
- [DATA_ACCESS.md](DATA_ACCESS.md)
- [../../data/projects/recession_scar_half_life/study_registry.csv](../../data/projects/recession_scar_half_life/study_registry.csv)
- [../../data/projects/recession_scar_half_life/effect_curve_template.csv](../../data/projects/recession_scar_half_life/effect_curve_template.csv)
- [../../data/projects/recession_scar_half_life/effect_curves.csv](../../data/projects/recession_scar_half_life/effect_curves.csv)
- [../../data/projects/recession_scar_half_life/derived_metrics.csv](../../data/projects/recession_scar_half_life/derived_metrics.csv)
- [EXTRACTION_LOG.md](EXTRACTION_LOG.md)
- [FIRST_RESULTS.md](FIRST_RESULTS.md)
- [BASELINE_SYNTHESIS.md](BASELINE_SYNTHESIS.md)

---

## Falsifier

R3 的强版本会被削弱，如果：

```text
high entry rigidity
+
low re-entry flexibility
+
large entry shock
```

并没有对应：

```text
longer scar persistence
```

或者 scar persistence 主要由：

```text
shock severity / composition / measurement
```

解释，而制度变量没有额外解释力。

---

## 最重要的研究纪律

这个项目**不直接比较论文里的“显著到第几年”**。

因为 statistical significance 同时由：

```text
effect size
sample size
standard error
specification
```

决定。

真正比较的对象优先是：

```text
normalized effect path
```

而不是 p-value path。
