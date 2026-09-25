# Source Verification Protocol｜来源核验规范

> 目标：让每一个定量或强因果 claim 都能从 repo 回到原始证据。

## 1. 四级来源优先级

### Tier 1 — Primary / Official

- original paper；
- official statistics；
- legislation；
- central bank；
- government report；
- regulator filing。

### Tier 2 — Authoritative secondary

- NBER version；
- IFS / major research institute；
- university publication page；
- peer-reviewed review。

### Tier 3 — High-quality explanatory

- major financial press；
- reputable long-form analysis。

### Tier 4 — Discovery only

- search snippet；
- blog；
- forum；
- social media；
- unsourced secondary quote。

核心 claim 不应只停留在 Tier 4。

---

## 2. 每条数字必须保存五件事

```text
Claim ID
Exact Value
Unit
Period / Population
Source Location
```

如果数字由我们计算：

```text
Derived Value
=
Raw Inputs
+
Formula
```

必须同时保存 raw inputs。

---

## 3. “原文支持大方向”不等于支持具体数字

错误：

```text
文章讨论 housing decline
→ 就引用它支持 -21.9%
```

正确：

```text
原始 series：
2021Q3 = x
2026Q1 = y

Derived:
(y / x - 1) = -21.9%
```

---

## 4. 因果措辞等级

### Descriptive

```text
X 与 Y 同时发生
```

### Associational

```text
X 与 Y 显著相关
```

### Quasi-causal

```text
利用 IV / DiD / RD / natural experiment
识别 X 对 Y 的影响
```

### Structural / Model-based

```text
模型中 X 可生成 Y
```

不能把：

```text
model result
```

写成：

```text
observed causal fact
```

---

## 5. 版本与日期

对：

- working paper；
- report；
- official data series；

必须保存：

```text
version / publication date / retrieval date
```

因为之后可能修订。

---

## 6. Verification Record 模板

```text
Claim ID:
Claim:
Status:
Source:
Exact location:
Population:
Period:
Method:
Raw value(s):
Transformation:
Counterevidence:
Notes:
```

---

## 7. 当前 Phase I 的目标

先完成：

```text
P0 claims
```

即所有：

- 具体数字；
- 明确 cohort 范围；
- 强因果措辞；
- 关键 turning-point date。

完成后再进入 reproducibility。
