# Verification Levels｜核验等级

为避免“Verified”含义过宽，Phase I 以后统一使用以下等级。

## L0 — Indexed

只知道来源存在，尚未核对 claim。

## L1 — Source-Verified

已经回到 primary / authoritative source，并确认它明确支持该 claim。

L1 再细分：

- **L1-primary-exact-value**：官方原始数字；
- **L1-primary-exact-statement**：官方 / 原始来源明确措辞；
- **L1-primary-abstract**：论文原始摘要明确支持；
- **L1-authoritative-exact-statement**：权威研究机构明确给出结果；
- **L1-primary-plus-derived**：原始数据已核，repo 自己做数学推导。

## L2 — Design-Verified

不仅核到来源，还核到：

- sample；
- identification strategy；
- table / figure / equation；
- exact outcome；
- confidence interval / specification（如适用）。

对于强因果措辞，目标至少是 L2。

## L3 — Reproduced

使用可获取 raw inputs / public data，在 repo 中重新计算出同一关键结果。

L3 不要求复制整篇论文，只要求复现 repo 实际引用的数字或图。

---

## 当前状态

第一批 P0 claims 主要达到：

```text
L1
```

其中：

```text
C009
```

已经具备小型：

```text
L3-derived
```

链条：

```text
BIS/FRED raw observations
→ CSV
→ local verification script
→ -21.8859%
```

后续强因果 claim：

```text
C014
C020
C025
```

优先向 L2 推进。
