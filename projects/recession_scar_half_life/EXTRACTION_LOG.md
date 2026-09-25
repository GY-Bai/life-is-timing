# Extraction Log｜Project 01

> 作用：记录每一次从论文表格进入 machine-readable data 的变更，尤其是纠错。

## 2026-09-25｜Kondo 2024 Tables 2–3

Source:

Ayako Kondo, **Scars of the job market “ice-age”**, *Social Science Japan Journal* 27(2), 2024.

https://academic.oup.com/ssjj/article/27/2/133/7727749

### 已核对

#### Table 2 — High school graduates, full-time annual earnings

1984–2004 subsample：

```text
Experience 1–3   -0.040  [0.003]
Experience 4–6   -0.030  [0.004]
Experience 7–9   -0.021  [0.004]
Experience 10–12 -0.012  [0.005]
```

1993–2013 subsample：

```text
Experience 1–3   -0.016  [0.008]
Experience 4–6   -0.004  [0.007]
Experience 7–9   +0.005  [0.009]
Experience 10–12 +0.010  [0.009]
```

### 纠错记录

早期 extraction 曾把：

```text
1993–2013 high-school / experience 4–6
```

误写成：

```text
+0.013
```

该数字属于 **Table 3 college younger subsample** 的 4–6 earnings coefficient，而不是 Table 2 high-school coefficient。

已修正为：

```text
-0.004
```

这是一个典型 cross-table transcription error，因此以后所有 effect-curve extraction 都必须在本文件留下核验记录。

---

#### Table 3 — Four-year college graduates, full-time annual earnings

1984–2004 subsample：

```text
Experience 1–3   -0.030  [0.007]
Experience 4–6   -0.018  [0.006]
Experience 7–9   -0.005  [0.007]
Experience 10–12 +0.006  [0.009]
```

1993–2013 subsample：

```text
Experience 1–3   +0.004  [0.008]
Experience 4–6   +0.013  [0.010]
Experience 7–9   +0.022  [0.012]
Experience 10–12 +0.024  [0.013]
```

Kondo 本文结论与这些表格一致：

```text
older cohorts:
entry unemployment has persistent negative earnings effects

younger / post-ice-age cohorts:
negative entry-unemployment earnings effect is no longer statistically significant
```

---

## Derived metric rule

当前只对：

```text
方向稳定
且至少有 3 个可比较 event-time 点
```

计算 descriptive magnitude half-life。

使用 grouped bin midpoint：

```text
1–3  → 2
4–6  → 5
7–9  → 8
10–12 → 11
```

这只是 descriptive approximation，不把 bin midpoint 当成论文实际逐年估计。


---

## 2026-09-25｜Kahn 2010 Table 4

Source:

Lisa B. Kahn, **The Long-Term Labor Market Consequences of Graduating from College in a Bad Economy**, *Labour Economics* 17(2), 2010.

Published article:
https://doi.org/10.1016/j.labeco.2009.09.002

Table extraction source used for exact cells:
pre-publication manuscript, Table 4, printed p. 37.  
The published article narrative reports the same qualitative path and near-identical headline magnitudes.

### National OLS fitted effects

```text
Year 1   -0.059  [0.020]
Year 5   -0.050  [0.014]
Year 10  -0.038  [0.010]
Year 15  -0.026  [0.012]
```

Underlying Table 4 coefficients:

```text
College UE Rate  -0.062
College × exp    +0.002
```

### National IV fitted effects

```text
Year 1   -0.074  [0.030]
Year 5   -0.059  [0.025]
Year 10  -0.040  [0.020]
Year 15  -0.022  [0.021]
```

IV uses birth-year indicators for national unemployment exposure.

### State OLS fitted effects

```text
Year 1   -0.023
Year 5   -0.022
Year 10  -0.020
Year 15  -0.018
```

These point estimates are not statistically significant.

### State IV fitted effects

```text
Year 1   -0.105
Year 5   -0.103
Year 10  -0.100
Year 15  -0.097
```

The state IV uses unemployment in the state of residence at age 14 in the modal graduation year as the proxy/instrument structure.

### Derived descriptive half-life

Using year-1 fitted effect as reference:

```text
National OLS  ≈ 13.54 years
National IV   ≈ 10.83 years
State OLS     > 15 years (right-censored by magnitude)
State IV      > 15 years (right-censored by magnitude)
```

These are **magnitude half-lives**, not significance horizons.

### Important interpretation boundary

The four specifications are not four independent estimates of the same estimand.

In particular:

```text
national exposure
state exposure
OLS
IV
```

use different variation and can imply different local treatment effects.

Therefore Project 01 keeps them as:

```text
within-paper specification sensitivity
```

rather than averaging them.


---

## 2026-09-25｜Päällysaho 2017 Tables 2–3

Source:

Miika Päällysaho, **The Short- and Long-Term Effects of Graduating During a Recession: Evidence from Finland**, VATT Working Paper 96, 2017.

PDF:
https://www.doria.fi/bitstream/handle/10024/148933/wp96.pdf

### Table 2 — All graduation cohorts 1988–2004

Outcome:

```text
log real annual earnings
per +1pp regional unemployment at graduation
```

Exact annual coefficients:

```text
1  -0.0210
2  -0.0178
3  -0.0163
4  -0.0151
5  -0.0148
6  -0.0140
7  -0.0125
8  -0.0115
9  -0.0105
10 -0.0099
```

Year-1 magnitude:

```text
0.0210
```

Half target:

```text
0.0105
```

Year 9 coefficient is exactly:

```text
-0.0105
```

so descriptive magnitude half-life is:

```text
9.0 years
```

The earnings effect remains statistically significant through year 10.

---

### Table 3 — Depression cohorts 1988–1995

```text
-0.0103
-0.0073
-0.0065
-0.0059
-0.0064
-0.0061
-0.0049
-0.0042
-0.0034
-0.0027
```

The path is negative but mildly non-monotone.

First half-magnitude crossing:

```text
≈ 6.79 years
```

This is descriptive only.

---

### Table 3 — Post-depression cohorts 1996–2004

```text
-0.0237
-0.0152
-0.0123
-0.0106
-0.0087
-0.0074
-0.0058
-0.0044
-0.0043
-0.0049
```

Half target:

```text
0.01185
```

First crossing is between years 3 and 4:

```text
descriptive half-life ≈ 3.26 years
```

The paper reports statistical significance at the 5% level only through year 5.

### Identification warning

The three curves are **not** simple “same treatment, different macro severity” clones.

Restricting to 1988–1995 changes the identifying variation:

```text
many cohorts share the aggregate depression
→ regional unemployment variation within those cohorts becomes relatively more important
```

Therefore:

> **All-cohort persistence minus depression-only persistence cannot be interpreted as a causal estimate of “depression severity”.**

This is exactly why Project 01 stores exposure definition and sample window alongside every half-life.


---

## 2026-09-25｜Oreopoulos, von Wachter & Heisz 2012 Table 2

Source:

Philip Oreopoulos, Till von Wachter & Andrew Heisz, **The Short- and Long-Term Career Effects of Graduating in a Recession**, *American Economic Journal: Applied Economics* 4(1), 2012.

Published PDF:
https://oreopoulos.faculty.economics.utoronto.ca/wp-content/uploads/2020/05/oreopoulos-et-al-the-short-and-long-term-career-effects-of-graduating-in-a-recession-aej-applied-2012.pdf

DOI:
https://doi.org/10.1257/app.4.1.1

### Table 2 — Full sample annual earnings

Regional unemployment rate at graduation, grouped experience effects:

```text
Experience 0–1   -0.0183  [0.0020]
Experience 4–5   -0.0089  [0.0016]
Experience 9–10  -0.0042  [0.0016]
```

Using bin midpoints:

```text
0–1   → 0.5
4–5   → 4.5
9–10  → 9.5
```

and the first effect as reference:

```text
half target = 0.00915
```

the descriptive magnitude half-life is:

```text
≈ 4.39 years
```

This lines up with the authors' narrative that a typical recession's initial earnings loss halves within roughly five years and fades by about ten years, but our 4.39-year value is a separate grouped-bin interpolation metric.

### Employer quality — average firm median log earnings

```text
0–1   -0.0096  [0.0012]
4–5   -0.0042  [0.0011]
9–10  -0.0028  [0.0012]
```

descriptive magnitude half-life:

```text
≈ 4.06 years
```

This gives a direct mechanism comparison:

```text
employer-quality gap
and
earnings gap
```

both shrink strongly during the first several years.

The paper's text also reports that firm quality improves especially quickly during the first 3–5 years, when job mobility is elevated.

---

### Skill heterogeneity

Annual earnings:

#### Bottom predicted-earnings quintile

```text
0–1   -0.0277
4–5   -0.0167
9–10  -0.0161
```

By 9–10 years, magnitude is still above half the initial value:

```text
half-life > 9.5 years
```

(right-censored in our grouped metric).

#### Middle quintile

```text
-0.0232
-0.0124
-0.0039
```

descriptive half-life:

```text
≈ 4.97 years
```

#### Top quintile

```text
-0.0147
-0.0042
-0.0024
```

descriptive half-life:

```text
≈ 3.30 years
```

So within the same institutional environment:

```text
Top skill
→ faster recovery

Bottom skill
→ much more persistent scar
```

This is stronger identification for R3 than a naïve cross-country comparison, because treatment definition, data system and broad institutional setting are held much more constant.

---

### Employer-quality heterogeneity

Average firm median log earnings:

```text
Full sample:
-0.0096 → -0.0042 → -0.0028

Bottom:
-0.0111 → -0.0087 → -0.0126

Middle:
-0.0128 → -0.0050 → -0.0043

Top:
-0.0082 → -0.0004 → +0.0010
```

The top group closes the employer-quality gap rapidly and then changes sign.

The bottom group does **not** monotonically catch up: by 9–10 years the employer-quality gap is again larger in magnitude.

Therefore no single employer-quality half-life is reported for the top sign-reversal path, while the bottom group is right-censored.

### Interpretation

This table directly strengthens the mechanism:

```text
Re-matching Capacity
→ Employer Upgrading
→ Scar Decay
```

but does not prove that employer mobility is the only channel.

The authors explicitly describe both:

```text
mobility toward better firms
+
recovery within firms
```

as adjustment margins.
