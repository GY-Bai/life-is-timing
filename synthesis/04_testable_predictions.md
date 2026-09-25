# Testable Predictions｜六条候选规律如何被数据攻击

> 目标：把 Candidate Regularities 从“解释框架”推进到“可证伪命题”。

## P1｜Fastest Adjustable Margin：低调整成本变量应更早响应 shock

### 命题

如果多个变量共同吸收同一 shock，那么：

```text
Adjustment Cost / Time 越低
→ Response Lag 越短
```

### 可测试设计

对同一 shock 做 event study，比较：

- market price；
- funding spread；
- hiring；
- hours；
- headcount；
- wage；
- capital stock。

例如 recession：

```text
spread
→ hiring
→ headcount
→ wage
```

是否存在稳定 lead-lag。

### 会推翻什么

如果高承诺 slow variable 系统性先于 liquid / reversible variable 调整，而且这种顺序无法由政策冻结、价格管制或 measurement lag 解释，那么 R1 需要收缩。

---

## P2｜Slow Stock Persistence：恢复半衰期应随 stock rebuild time 增加

### 命题

```text
Recovery Persistence
↑
when
Rebuilding Lead Time ↑
```

### 可测试设计

跨行业比较：

```text
short-cycle software / service
vs
skilled labor
vs
housing
vs
mining / energy capacity
```

在类似 demand shock 后，估计：

```text
time-to-50%-recovery
time-to-trend-recovery
```

并与：

```text
training / construction / project lead time
```

做关系。

### 反证

如果 rebuild lead time 很长，但 recovery 总是极快，则说明：

```text
substitution / imports / idle capacity / migration
```

比 stock rigidity 更重要。

---

## P3｜Entry × Re-entry：制度越前置，recession-entry scar 应越持久

### 命题

```text
Same Macro Shock
× More Front-loaded Entry
→ Larger / More Persistent Cohort Scar
```

条件：

```text
Re-entry Flexibility 较低
```

### 可测试设计

跨国家 / 跨制度比较：

- Japan-style new-graduate hiring；
- more flexible US-style employer switching；
- occupation licensing differences；
- apprenticeship-heavy vs open-entry occupations。

核心 outcome：

- earnings；
- regular employment；
- employer quality；
- occupation quality；
- recovery half-life。

### 反证

如果 entry gate 很强但后续 scar 不更持久，说明：

```text
policy / re-entry channel
```

能够完全抵消 entry rigidity。

---

## P4｜Leverage Nonlinearity：同一资产价格 shock 对高杠杆主体的行为反应应凸性更强

### 命题

```text
|Behavioral Response|
↑ nonlinearly with LTV / leverage
```

例如：

```text
House Price -10%
```

对：

```text
LTV 20%
```

与：

```text
LTV 80%
```

不应只是按比例不同。

### 可测试设计

按 initial LTV / debt-service ratio 分组：

- consumption；
- default；
- mobility；
- refinancing；
- job search；
- asset sale。

### 反证

如果控制 income / liquidity 后，高低 leverage 的 response 完全相同，则 R4 的 household 版本需要重估。

---

## P5｜Optionality Buffers Scarring：更多可退出选项应降低 shock persistence

### 命题

```text
Scar Persistence
↓
when
Optionality ↑
```

可观测 proxy：

- cash buffer；
- transferable skill；
- geographic mobility；
- employer switching；
- refinancing access；
- stable long-term funding；
- family transfer。

### 可测试设计

对相同 shock exposure 的人 / 企业做匹配：

```text
same shock
different optionality
```

比较：

- recovery speed；
- long-run income；
- default；
- occupational upgrade；
- relocation；
- firm survival。

### 关键识别难点

Optionality 往往与：

```text
ability
wealth
network
management quality
```

内生相关。

因此需要：

- policy discontinuity；
- exogenous mobility change；
- refinancing eligibility cutoff；
- visa / licensing rule；
- liquidity rule change。

### 反证

如果外生增加 optionality 后，长期 scar 没有下降，则统一的 Historical Optionality 概念需要缩小适用范围。

---

## P6｜Experience Effects：belief 应对亲历历史呈 recency-weighted、domain-specific 反应

### 命题

```text
Belief
=
f(Experienced History)
```

而且：

```text
recent experience weight > distant experience weight
```

### 可测试设计

观察：

- local house-price history → national housing expectations；
- experienced inflation → inflation expectations；
- experienced returns → portfolio choice；
- experienced unemployment → labor-market beliefs。

### 更强预测

如果 regime 改变，但个人 experience 更新较慢，则：

```text
old-cohort beliefs
```

应比：

```text
new information implied beliefs
```

更持久。

### 反证

如果控制公开信息后，personal experience 完全没有额外解释力，则 R6 失败。

---

# 跨规律交互预测

真正有价值的可能不是 R1–R6 单独成立，而是它们的 interaction。

## P7｜High Leverage × Low Optionality

```text
Leverage ↑
+
Optionality ↓
→ Scar Persistence sharply ↑
```

比两者单独作用更强。

这可以在：

- mortgage household；
- leveraged firm；
- bank；
- fund；

中分别测试。

---

## P8｜Bad Entry × Slow Stock

如果 bad entry 打到一个重建很慢的 stock：

```text
Entry Shock
× Long Rebuild Time
→ Long Scar
```

例如：

```text
graduation recession
× apprenticeship-heavy occupation
```

应比：

```text
graduation recession
× easily certifiable / open-entry occupation
```

留下更久影响。

---

## P9｜Experience Bias × Irreversible Decision

如果个人把有限 sample path 过度外推，同时做：

```text
High Leverage
+
High Irreversibility
```

则 belief error 的长期成本应更大。

住房是最自然的测试场景：

```text
local boom experience
→ optimistic belief
→ high-LTV purchase
→ later regime shift
```

---

# 数据优先级

如果未来真正做 empirical project，优先寻找能够同时提供：

```text
Timing
Exposure
Initial State
Adjustment
Long-run Outcome
```

的数据。

最有价值的组合包括：

### Labor

```text
graduation year
local unemployment
first employer
job switching
earnings panel
```

### Housing

```text
purchase vintage
initial LTV
city price path
income
principal repayment
net worth
```

### Firms

```text
funding structure
shock date
investment / hiring
liquidity buffer
survival
```

### AI

```text
AI adoption date
junior hiring
task mix
training
promotion
senior stock
```

---

# 核心纪律

> **一个好 framework 的下一步，不是继续解释更多故事，而是主动设计最容易让自己失败的测试。**
