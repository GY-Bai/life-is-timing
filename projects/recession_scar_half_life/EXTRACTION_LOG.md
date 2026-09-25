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
