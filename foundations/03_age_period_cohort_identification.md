# Foundation 03｜Age–Period–Cohort：为什么“某一代人更惨”不是一个容易识别的命题

> 研究状态：**A（成熟人口学 / 统计学方法论）**

Life Is Timing 经常使用：

```text
Age
Period
Cohort
```

三个概念。

但这三者之间存在一个著名、而且不能靠“更复杂回归”自动消失的问题：

# APC Identification Problem

---

## 1. 三个变量分别是什么意思

### Age

```text
你现在几岁
```

可能对应：

- 生理年龄；
- career stage；
- family stage；
- retirement stage。

### Period

```text
现在是哪一年 / 哪个历史时期
```

例如：

- 2008 financial crisis；
- 2020 pandemic；
- 2022 inflation shock；
- 2025–26 AI adoption wave。

### Cohort

```text
你是哪一年出生 / 哪一年毕业 / 哪一年买房
```

最常见的是 birth cohort，但研究问题也可以定义：

- graduation cohort；
- mortgage origination cohort；
- fund vintage；
- project vintage。

---

## 2. 为什么它们不能被简单“拆开”

因为：

```text
Cohort = Period - Age
```

如果你知道：

```text
年龄
+
当前年份
```

出生年份就已经确定。

所以在传统 additive model：

```text
Y
=
Age Effect
+
Period Effect
+
Cohort Effect
```

中，三个时间维度存在完全线性依赖。

因此：

> **不存在仅靠数据本身就能唯一恢复三条独立线性 trend 的办法。**

多种不同的：

```text
Age slope
Period slope
Cohort slope
```

可以产生完全相同 fitted values。

这不是 sample size 不够。

而是：

# Identification

本身不存在。

---

## 3. 为什么这对 Life Is Timing 特别重要

如果我们观察到：

```text
1990s-born
homeownership 更低
```

至少有三种解释：

### Age Effect

```text
他们只是还年轻
```

### Period Effect

```text
所有年龄的人在这个时期都面对更贵住房 / 更紧 mortgage
```

### Cohort Effect

```text
这批人因为在特定历史窗口进入 housing market
留下持续差异
```

如果不做识别，就很容易把：

```text
“今天年轻人”
```

误写成：

```text
“这一代人的永久特征”
```

---

## 4. 一个最常见的错误

错误写法：

```text
1993 cohort 资产更少
→ 1993 cohort 天生更不擅长积累财富
```

更合理的研究步骤：

```text
先控制 / 描述 Age
再识别 Period shock
再问 Cohort 是否存在持续 deviation
```

也就是说：

```text
Observed Cohort Difference
≠ Pure Cohort Effect
```

---

## 5. 为什么“加固定效应”也不能自动解决

传统 APC 文献几十年来提出过许多办法：

- constrained generalized linear model；
- intrinsic estimator；
- hierarchical APC / CCREM；
- ridge / regularisation；
- detrending；
- estimable functions；
- APC-I。

但核心纪律是：

> **任何声称同时给出独立 Age / Period / Cohort effect 的方法，都必须说明它额外加入了什么 assumption。**

如果 assumption 没有 substantive justification：

```text
统计模型给出的唯一答案
```

不等于：

```text
经济世界里存在唯一答案
```

---

## 6. 对本仓库更合适的思路：Event × Age-at-Exposure

Life Is Timing 的研究问题通常并不需要硬拆：

```text
全局 Age trend
+
全局 Period trend
+
全局 Cohort trend
```

我们真正关心的往往是：

```text
一个可定义 historical shock
×
不同年龄 / life stage 的 exposure
```

例如：

```text
2008 recession
×
22 岁 graduate
vs
32 岁 mortgagor
vs
55 岁 pre-retiree
```

或者：

```text
1998 China housing reform
×
首次购房窗口
```

这比抽象地说：

```text
“1970 cohort effect”
```

更容易形成可反驳假设。

---

## 7. APC-I 给出的一个有价值视角

Luo 与 Hodges 的 APC-I 思路不再把：

```text
Cohort
```

视为独立于 Age 与 Period 的第三个 additive main effect。

而把 cohort meaning 理解为：

```text
Age × Period Interaction
```

也就是说：

> 社会变化对不同年龄的人影响不同，并且这种差异可能持续。

这与 Life Course Theory 的直觉非常接近：

```text
Historical Change
×
Life Stage
→
Cohort Pattern
```

我们不需要把 APC-I 当作唯一“正确方法”。

但它提醒我们：

> **cohort 的经济含义本来就来自人在特定年龄经历了特定历史变化。**

---

## 8. 本仓库以后如何使用 cohort

### 可以直接说

```text
“2008 recession entrants”
“1993-born housing-entry window”
“1998 housing reform occurred when 1970 cohort was around 28”
```

这些是在描述 exposure。

### 需要谨慎说

```text
“1993 cohort 的某结果完全是 cohort effect”
```

除非有可信 identification。

### 尽量不要说

```text
“这一代人就是更保守 / 更懒 / 更不会理财”
```

除非能排除 Age 与 Period。

---

## 9. 最推荐的识别策略

对于本项目，我们优先：

### 1. 明确 shock

```text
Recession
Policy Reform
Credit Tightening
Technology Adoption
Asset Bust
```

### 2. 明确 exposure window

```text
Age at Shock
Graduation Year
Purchase Vintage
Loan Vintage
```

### 3. 找 comparison group

```text
adjacent cohort
adjacent region
different exposure intensity
different institution
```

### 4. 看 persistence

```text
冲击后的差异是否持续
```

### 5. 找 mechanism

```text
first-job quality?
LTV?
OJT?
asset entry price?
mobility?
```

而不是只画一条 cohort trend 然后给故事。

---

## 10. 核心结论

> **Cohort 是非常有用的历史定位工具，但不是一个可以脱离 Age 与 Period 随意解释的魔法变量。**

对 Life Is Timing 来说，最重要的不是证明：

```text
“某代人天生不同”
```

而是识别：

```text
某个历史变化
在某个人生阶段
留下了什么持续影响
```

---

## 11. 证据与来源

1. Luo, L. & Warren, J. R., **Describing and explaining age, period, and cohort trends in Americans’ vocabulary knowledge**, 2023.  
   https://pmc.ncbi.nlm.nih.gov/articles/PMC10119018/

2. Nielsen, B., **Age-period-cohort models in a two-sample setting**, Nuffield College Economics Discussion Paper.  
   https://www.nuffield.ox.ac.uk/economics/papers/2022/2022-W03apc_2sample.pdf

3. Luo, L. & Hodges, J. S., APC-I framework, discussed and implemented in the literature summarized above.

4. Ryder, N. B., **The Cohort as a Concept in the Study of Social Change**, *American Sociological Review*, 1965.
