# Case 06｜Private Credit 与 Liquidity Mismatch：慢资产的压力为什么会泄到快市场

> 研究状态：**A（成熟 liquidity 机制）+ B（当前 private-market 应用）**

Private credit 是 Adjustment Margin 框架非常好的现代案例。

核心不是：

```text
private credit 一定会爆
```

而是：

> **当底层资产很慢、投资者或融资端很快时，系统会把压力转移到最能动的地方。**

---

## 1. 经典机制：Market Liquidity × Funding Liquidity

Brunnermeier 与 Pedersen（2009）把：

```text
Market Liquidity
```

和：

```text
Funding Liquidity
```

放在同一个反馈回路中。

典型链条：

```text
价格下跌
→ volatility ↑
→ margin / haircut ↑
→ funding capacity ↓
→ forced selling
→ market depth ↓
→ price further ↓
```

于是产生：

```text
Liquidity Spiral
```

这就是：

```text
快变量之间的正反馈
```

---

## 2. Private Market 为什么特殊

private credit / private equity 的底层资产通常：

- 不连续交易；
- 定价频率低；
- 退出耗时；
- loan / deal 高度 bespoke；
- price discovery 较弱。

这给它一个优势：

```text
closed-ended long-term capital
→ 不必每天 mark-to-market 卖出
```

但也带来另一个问题：

```text
Illiquid Asset
+
Fast Redemption / Leverage / Refinancing Need
```

会制造 liquidity mismatch。

---

## 3. 2026 年英国央行已经把这个问题当成正式金融稳定主题

Bank of England 2026 年的 private-markets system-wide exploratory scenario（SWES）明确要研究：

```text
banks + NBFIs + private markets
在 downturn 中如何互动
以及是否会放大 stress
```

原因包括：

- private markets 规模快速增长；
- leverage；
- opacity；
- valuation uncertainty；
- banks / insurers / leveraged finance 之间的 interconnectedness。

这不是说系统已经发生危机。

恰恰相反：

> 监管者关心的是，这套系统在当前规模下还没有经历过一次完整 broad-based macro stress。

---

## 4. 2026 年已经出现了一个很有意思的局部样本

Bank of England July 2026 FSR 记录：

```text
部分美国 non-traded BDCs
→ redemption requests elevated
→ several funds limited redemptions
```

很多这类 vehicle：

```text
quarterly redemption
通常有约 5% cap
```

这种 gate 本来就是为了让：

```text
fast investor withdrawal
```

不要直接逼迫：

```text
slow underlying loans
```

被迫 fire sale。

但它也会产生新的行为：

```text
担心以后拿不出来
→ investors pre-emptively redeem
```

这就是：

```text
Liquidity Protection
```

与：

```text
Run Incentive
```

之间的张力。

---

## 5. 为什么压力可能泄到 public markets

假设底层 private loans 无法快速出售，而 fund / sponsor / connected institution 需要现金。

最容易动的可能是：

```text
cash
public credit
leveraged loans
HY bonds
listed equity
bank facilities
```

所以：

```text
Stress Origin
≠ Price Adjustment Location
```

这就是我们此前总结的：

```text
Slow Asset Pressure
→ Fast Asset Price
```

但必须强调：

是否真的发生 cross-asset forced selling，取决于具体 fund structure、redemption terms、bank facilities、collateral 和 mandate，不能把它当成所有 private-credit fund 的必然行为。

---

## 6. 为什么 private NAV 可能看起来更稳定

如果一个资产：

```text
daily traded
```

它会迅速显示新价格。

如果另一个资产：

```text
季度估值
模型估值
缺少交易
```

其 NAV 调整可能更慢。

于是：

```text
Public Asset Volatility
>
Private Asset Reported Volatility
```

不一定意味着：

```text
Private Asset Fundamental Risk 更低
```

其中一部分可能只是：

```text
Price Discovery Lag
```

---

## 7. 2025–2026 当前风险为什么值得继续追踪

Bank of England 2025–2026 的 FSR 持续指出：

- private markets 与 banks 的 direct / indirect links 在增加；
- leverage 与 valuation opacity 是主要 vulnerability；
- 一部分 UK private debt / leveraged loans 在未来数年面临 refinancing；
- 2021 低利率环境下形成的一批 debt 将逐步进入更高融资成本的再融资环境。

这正好是：

```text
Action | Funding Regime
```

的例子。

同一笔 leverage：

```text
2021 @ cheap funding
```

和：

```text
2026 @ tighter refinancing conditions
```

不是同一笔经济交易。

---

## 8. 五层映射

### Shock

```text
Credit deterioration
Rate Shock
Redemption Shock
Refinancing Shock
```

### Adjustment Margin

```text
Public Spread
Liquid Credit
Redemption Gate
Bank Facility
```

### Stock

```text
Illiquid Loans
Private Equity Stakes
Highly Levered Portfolio Companies
```

### Life Stage / Institutional Stage

在企业与基金层面对应：

```text
Loan Vintage
Fund Vintage
Refinancing Year
```

本质上和人的 cohort timing 相同：

```text
同一结构
× 不同历史融资窗口
→ 不同结果
```

### Optionality

```text
Cash Buffer
Uncalled Capital
Long-dated Funding
Closed-end Structure
Refinancing Capacity
Asset Sale Options
```

---

## 9. 核心结论

> **流动性危机最重要的问题不是“哪里看起来最波动”，而是“哪里必须先动、哪里暂时动不了”。**

这也是为什么：

```text
Selling Order
≠ Fundamental Damage Order
```

---

## 10. 证据与来源

1. Markus Brunnermeier & Lasse Heje Pedersen, **Market Liquidity and Funding Liquidity**, *Review of Financial Studies*, 2009.  
   https://markus.scholar.princeton.edu/publications/market-liquidity-and-funding-liquidity

2. Bank of England, **Private Markets System-Wide Exploratory Scenario (SWES)**, 2026.  
   https://www.bankofengland.co.uk/financial-stability/boe-system-wide-exploratory-scenario-exercise/boe-private-markets-swes

3. Bank of England, **Financial Stability Report — December 2025**.  
   https://www.bankofengland.co.uk/financial-stability-report/2025/december-2025

4. Bank of England, **Financial Stability Report — July 2026**.  
   https://www.bankofengland.co.uk/financial-stability-report/2026/july-2026

5. Bank of England, **Financial Policy Committee Record — April 2026**.  
   https://www.bankofengland.co.uk/financial-policy-committee-record/2026/april-2026
