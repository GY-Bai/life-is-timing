# Case 07｜Local Business Customer Beta：为什么宏观复苏穿过客群以后才变成营业额

> 研究状态：**A（wealth / balance-sheet effect）+ B（Customer Beta 框架）**

我们此前用一个没有线上外卖、依赖社区老客的餐馆做过 thought experiment。

真正值得保留的不是那家店的具体权重，而是一个一般方法：

```text
Macro Recovery
→ Customer Balance Sheet
→ Customer Spending
→ Local Business Revenue
```

也就是：

# Customer Beta

---

## 1. 为什么“经济恢复”对不同店不是同一件事

假设同一条街有两家餐馆。

### Restaurant A

客群主要是：

```text
shareholders
high-income professionals
bonus-dependent workers
homeowners
```

### Restaurant B

客群主要是：

```text
wage earners
service workers
renters
local employees
```

那么危机后的恢复变量可能完全不同。

A 更可能暴露于：

```text
Stock Price
Bonus
Housing Wealth
```

B 更可能暴露于：

```text
Employment
Hours
Wage
Disposable Income
```

所以：

```text
Same ZIP
Same Cuisine
Same Recession
≠ Same Recovery Curve
```

---

## 2. Stock wealth 真的会进入 local economy

Chodorow-Reich、Nenov 与 Simsek 使用美国地区股票财富差异研究发现：

```text
local stock wealth ↑
→ local nontradable employment ↑
→ local payroll ↑
```

模型对应的 stock-wealth MPC 约为：

```text
每增加 $1 stock wealth
→ 每年约 3.2 cents consumption
```

关键是：

```text
影响主要出现在 nontradable local industries
```

这正是：

- 餐馆；
- 本地服务；
- 零售；
- leisure；

这类 customer-beta 行业。

---

## 3. Housing wealth 往往更直接

Case、Quigley、Shiller 的长期州级研究发现：

```text
housing wealth
```

与 consumption 的关系通常比：

```text
stock-market wealth
```

更强。

Mian 与 Sufi 更进一步显示：

```text
house-price gain
→ home-equity borrowing
→ spending
```

尤其在低收入 ZIP code 中更强。

所以 local business 不能只看：

```text
附近房价涨没涨
```

还要看：

```text
谁持有房
有没有 mortgage
能否 equity extraction
收入是否稳定
```

---

## 4. Great Recession 为什么验证了“反向链条”

高 housing leverage 地区在 2007–2009：

```text
住房净值跌得更多
→ consumption cut 更大
→ unemployment 更差
```

因此：

```text
Asset Shock
```

可以通过 customer balance sheet，进入：

```text
Main Street Revenue
```

而不需要先经过全国工资统计。

---

## 5. Customer Beta 的最简模型

```text
Revenue_t
=
Σ_i
CustomerShare_i
× ShockExposure_i
× MPC_i
× CategoryElasticity_i
```

其中：

### CustomerShare

某类顾客占多少营业额。

### ShockExposure

他们主要暴露于：

- wage；
- employment；
- bonus；
- stock；
- housing；
- pension；
- business income。

### MPC

资产 / 收入变化后，他们会改变多少消费。

### CategoryElasticity

这类消费有多容易被削减。

---

## 6. 为什么不能直接用 ZIP code 平均收入

因为：

```text
ZIP Demographics
≠ Actual Customer Mix
```

一家餐馆可能：

- 靠周边退休居民；
- 靠办公楼午餐；
- 靠某个族群；
- 靠周末家庭聚餐；
- 靠少数高消费 regular customer。

所以 Census / ACS 只能提供：

```text
Prior
```

真正需要验证的是：

- POS；
- customer ZIP；
- average ticket；
- weekday / weekend；
- lunch / dinner；
- reservation；
- foot traffic；
- delivery share；
- card transaction；
- nearby employers。

---

## 7. 2026 英国研究为什么进一步强化这个框架

Bank of England 2026 的 mortgage / consumption 研究使用约六百万 household-level natural experiments，发现：

```text
mortgage rate ↓
→ consumption ↑
```

而很大部分作用并不是单纯来自：

```text
monthly payment 下降
```

而是：

```text
house price ↑
→ collateral ↑
→ borrowing ↑
→ consumption ↑
```

这再次说明：

```text
Household Balance Sheet
```

是宏观政策进入 local demand 的重要通道。

---

## 8. 五层映射

### Shock

```text
Stock Crash
Housing Crash
Unemployment
Inflation
Mortgage Reset
```

### Adjustment Margin

```text
Discretionary Consumption
Restaurant Frequency
Ticket Size
```

### Stock

```text
Household Wealth
Housing Equity
Savings
Debt
```

### Life Stage

```text
Retiree
Young Renter
Young Family
Peak-earner
```

MPC 与 shock exposure 完全不同。

### Optionality

```text
Savings
Credit Access
Housing Equity
Second Income
Transfer
```

决定消费者能否平滑支出。

---

## 9. 核心结论

> **商户没有“宏观 beta”；商户拥有的是“客群 beta”。**

宏观指标只有穿过：

```text
Customer Mix
```

以后，才会变成具体营业额。

---

## 10. 证据与来源

1. Gabriel Chodorow-Reich, Plamen T. Nenov & Alp Simsek, **Stock Market Wealth and the Real Economy: A Local Labor Market Approach**, NBER / AER.  
   https://www.nber.org/papers/w25959

2. Karl E. Case, John M. Quigley & Robert J. Shiller, **Wealth Effects Revisited: 1975–2012**, NBER.  
   https://www.nber.org/papers/w18667

3. Atif Mian & Amir Sufi, **House Price Gains and U.S. Household Spending from 2002 to 2006**, NBER.  
   https://www.nber.org/papers/w20152

4. Atif Mian & Amir Sufi, **Who Bears the Cost of Recessions?**, NBER.  
   https://www.nber.org/papers/w22256

5. Angus Foulis, Jonathan Hazell, Atif Mian & Belinda Tracey, **How do interest rates affect consumption? Household debt and the role of asset prices**, Bank of England, 2026.  
   https://www.bankofengland.co.uk/working-paper/2026/how-do-interest-rates-affect-consumption-household-debt-and-the-role-of-asset-prices
