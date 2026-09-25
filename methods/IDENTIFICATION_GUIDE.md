# Identification Guide｜这个 repo 如何避免把故事当因果

Life Is Timing 天生容易产生漂亮故事。

因此研究纪律必须比一般叙事更严格。

本文件定义以后所有 case study 的最低识别标准。

---

## 1. 四层语言必须分开

### Observation

```text
我们看到了什么？
```

例如：

```text
2021 之后某地房价下跌
```

### Association

```text
哪些变量一起变化？
```

例如：

```text
高杠杆地区消费下降更多
```

### Causal Evidence

```text
有没有可信设计说明 X 导致 Y？
```

例如：

- natural experiment；
- instrument；
- discontinuity；
- difference-in-differences；
- adjacent cohort design。

### Synthesis / Hypothesis

```text
我们把多个领域拼起来后提出什么更一般的解释？
```

这层可以原创。

但必须明确不是：

```text
已经被单篇论文证明
```

---

## 2. 每个 Cohort Case 必须问

```text
Age effect?
Period effect?
Cohort exposure?
Selection?
Composition?
```

不能因为：

```text
某一代今天表现不同
```

就直接称为：

```text
cohort scar
```

---

## 3. 每个 Timing Case 必须问

### Timing 是外生的吗？

如果一个人：

```text
自己选择在 2021 买房
```

那么：

```text
2021 buyer
```

和：

```text
2018 buyer
```

可能本来就是不同类型的人。

所以 purchase timing difference 可能包含：

```text
Selection
```

### 有没有制度 / 历史事件提供 quasi-exogenous variation？

例如：

- graduation recession；
- policy reform；
- mortgage rule change；
- local shock；
- plant closure。

---

## 4. 每个 Asset / Household Case 必须区分

```text
Price
Equity
Net Worth
Cash Flow
Consumption
```

例如：

```text
House Price -20%
```

不等于：

```text
Household Net Worth -20%
```

也不等于：

```text
Negative Equity
```

必须考虑：

```text
LTV
Principal Repayment
Other Assets
Income
Transfers
```

---

## 5. 每个 Recovery Case 必须区分 level 与 path

```text
GDP 回到危机前水平
```

不等于：

```text
GDP 回到危机前趋势线
```

同理：

```text
Employment Level Recovered
```

不等于：

```text
Cohort Career Path Recovered
```

需要区分：

```text
Level Recovery
Growth Recovery
Trend Recovery
Distributional Recovery
```

---

## 6. 每个“机制类比”都必须提供断点

如果我们说：

```text
Oil Capacity
≈ Human Capital Stock
```

必须同时写：

### 相似点

```text
都需要长期投资
都存在 lead time
都可能因 underinvestment 出现 scarcity
```

### 不同点

```text
human capital 有 agency
skills 可迁移
technology 可替代
workers 会退出 / 移民
training capacity 不是固定物理产能
```

类比是为了生成 hypothesis。

不是为了替代证据。

---

## 7. 每个 Case 最低模板

```text
1. Historical Timeline
2. Shock
3. Adjustment Margin
4. Stock Constraint
5. Life-stage Exposure
6. Optionality
7. Direct Evidence
8. Counter-evidence
9. Boundary Conditions
10. What Would Falsify This?
```

如果一个 case 没有第 8–10 项：

```text
还不能算研究稿
```

最多只是 narrative note。

---

## 8. “What Would Falsify This?” 是硬要求

例：

### Hypothesis

```text
长期 junior hiring decline
会导致 future senior shortage
```

可反驳数据：

```text
AI-intensive firms
长期 junior share 降低
但 8–12 年后
experienced-worker supply 没有下降
甚至更高
```

那么：

```text
Human-capital Cannibalization
```

至少需要大幅修改。

---

## 9. Repo 的目标

不是：

```text
证明 Life Is Timing 永远正确
```

而是：

```text
找到在哪些条件下 timing matter
在哪些条件下不 matter
以及为什么
```

真正好的理论应该：

```text
允许自己失败
```

---

## 10. 核心纪律

> **先找 identification，再找故事；先找反例，再扩大理论。**

这会让 Life Is Timing 从：

```text
一个有吸引力的世界观
```

变成：

```text
一个可以被数据攻击、修正和保留下来的研究框架
```
