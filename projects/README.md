# Projects｜Phase II Empirical Projects

Phase II 不再继续增加 worldview。

当前项目池：

1. **[Recession Scar Half-life](recession_scar_half_life/README.md)** — R3 — **ACTIVE / first comparative results available**
2. **Mortgage Reset Clock** — R4 — queued
3. **AI Apprenticeship Panel** — R2 / R3 — long-horizon
4. **Customer Beta Validation** — R1 / R4 — queued
5. **Binding Stock Substitution Map** — R2 — queued

详细优先级与 falsifier：

[PHASE_II_ROADMAP.md](../PHASE_II_ROADMAP.md)

项目进入 active 状态前必须先建立：

```text
Research Question
Treatment / Exposure
Outcome
Comparison Group
Identification
Falsifier
Data Provenance
```

没有 identification plan 的项目保持：

```text
Idea
```

而不是：

```text
Empirical Result
```


## Active Project 01

Recession Scar Half-life 已完成 design lock：

```text
Research Question ✅
Falsifier ✅
Metric Spec ✅
Data-access audit ✅
Study registry ✅
Effect extraction schema ✅
Estimator skeleton ✅
CI checks ✅
```

下一步不再改 research question，而是开始：

```text
paper-level coefficient extraction
→ normalized scar curves
```


### Project 01 当前进展

~~~text
Japan     exact table extraction ✅
US        exact fitted-effect extraction ✅
Canada    Table 2 earnings / employer-quality extraction ✅
Finland   exact annual earnings extraction ✅
Netherlands published summary verified; exact curve source gap documented
~~~

当前最重要的 working result：

> **Scar half-life 不是 country constant；同一制度内部的 worker type、re-matching access、sample 和 identification specification 就能产生非常大的 persistence heterogeneity。**

详见：

[Comparative Results](recession_scar_half_life/COMPARATIVE_RESULTS.md)
