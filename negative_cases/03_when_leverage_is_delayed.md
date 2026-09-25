# Negative Case 03｜高杠杆为什么有时不会立刻爆：固定利率与 adjustment delay

> 目标：攻击 R4 的“即时放大”直觉。  
> 结论：Leverage 可以很高，但 contract structure 会把 shock 从 **immediate amplification** 改成 **delayed repricing**。

## 1. UK mortgage tightening：rate shock 不等于 contemporaneous cash-flow shock

Bank of England 在 2023–24 的分析中强调：

```text
UK residential mortgage stock
大部分已经变成 fixed-rate
```

2023Q1：

```text
约 87% outstanding residential mortgage value
on fixed rate
```

这和 2000s early period 的 under 30% 非常不同。

因此：

```text
Bank Rate ↑ today
```

不会立即让所有 household：

```text
mortgage payment ↑ today
```

而是：

```text
wait until refix / refinance date
```

才逐步传导。

BoE 2024 进一步指出，fixed-term mortgage prevalence 已经让 cash-flow transmission 相比过去 tightening cycle 更慢。

### 来源

- Bank of England, **Financial Stability in Focus: Interest rate risk**, July 2023.  
  https://www.bankofengland.co.uk/financial-stability-in-focus/2023/july-2023

- Bank of England, **Monetary Policy Report**, August 2024.  
  https://www.bankofengland.co.uk/monetary-policy-report/2024/august-2024

---

## 2. 这不是“杠杆没风险”，而是 risk 被重新安排到时间轴上

Fixed rate 做的事情是：

```text
Shock
→ Delay
→ Refix Cliff / Staggered Reset
```

而不是：

```text
Shock
→ No Effect
```

所以：

```text
Leverage Risk
```

需要加入：

```text
Maturity / Reset Schedule
```

---

## 3. 2024 的现实验证：很多 mortgagor 仍未完成 repricing

BoE June 2024 FSR 记录：

```text
超过 300 万 mortgage accounts
仍支付低于 3% 的利率
```

很多会在 2026 年底前到期。

November 2024 FSR 又指出：

```text
37% fixed-rate mortgage accounts
自 2021H2 rates 开始上升后
仍未 re-fix
```

这意味着：

> **宏观 rate shock 与 household cash-flow shock 可以相隔数年。**

### 来源

- Bank of England, **Financial Stability Report**, June 2024.  
  https://www.bankofengland.co.uk/financial-stability-report/2024/june-2024

- Bank of England, **Financial Stability Report**, November 2024.  
  https://www.bankofengland.co.uk/financial-stability-report/2024/november-2024

---

## 4. 为什么这对 R4 很重要

原始直觉：

```text
High Leverage
→ Shock Amplification
```

不够。

必须写成：

```text
High Leverage
× Contract State
→ Timing + Form of Amplification
```

同样 high debt：

### Floating / short reset

```text
cash-flow shock 早
```

### Long fixed rate

```text
cash-flow shock 晚
```

### Marginable debt

```text
market-price shock 可立即变 margin call
```

所以：

```text
Leverage
```

不是单一 scalar。

---

## 5. Negative case 的真正含义

这个案例不是说：

```text
R4 错了
```

而是说：

```text
Leverage Amplification
```

若忽略：

```text
maturity
rate fixation
refinancing schedule
```

就会错误预测 shock 的时点。

这正是 R4 V2 改成：

# State-Contingent Leverage Amplification

的原因。
