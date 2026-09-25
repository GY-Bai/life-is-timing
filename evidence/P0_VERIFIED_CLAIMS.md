# P0 Verified Claims｜第一轮定量与强断言核验

> 核验日期：2026-09-25  
> 目标：对 Claims Ledger 中 P0 claims 建立“原始值 → 来源位置 → 推导”的最短可复核链条。

---

## C008｜中国住宅平均销售价格：1995 / 1998

**Claim**

```text
1995 全国住宅平均销售价格：1509 元/㎡
1998 全国住宅平均销售价格：1854 元/㎡
```

**Status**

```text
VERIFIED
```

**Primary source**

国家统计局，《中国统计年鉴 2005》表 6-38：  
“按用途分的商品房屋平均销售价格”。

URL:

https://www.stats.gov.cn/sj/ndsj/2005/html/F0638C.HTM

**Exact location**

```text
1995 row:
房屋平均销售价格 1591
住宅 1509

1998 row:
房屋平均销售价格 2063
住宅 1854
```

**Important boundary**

这里引用的是：

```text
住宅
```

列，不是：

```text
全部商品房屋平均销售价格
```

因此 1995 的正确住宅数字是 1509，不是 1591。

---

## C009｜中国住宅价格指数 2021Q3 → 2026Q1

**Claim**

```text
2021Q3 至 2026Q1
名义住宅价格指数约 -21.9%
```

**Status**

```text
VERIFIED / DERIVED
```

**Primary data**

BIS Residential Property Price database，经 FRED 发布：

https://fred.stlouisfed.org/series/QCNN628BIS

Series:

```text
QCNN628BIS
Residential Property Prices for China
Index 2010=100
Quarterly
Not Seasonally Adjusted
```

**Raw values**

```text
2021Q3 = 145.9129
2026Q1 = 113.9785
```

**Formula**

```text
113.9785 / 145.9129 - 1
= -0.218859...
≈ -21.89%
```

**Reported value**

```text
约 -21.9%
```

**Series boundary**

FRED / BIS notes:

```text
2007Q1–2015Q4:
new dwellings in 70 cities

from 2016Q1:
existing buildings in 70 cities
```

因此：

```text
2018–2026 内部比较
```

可作为当前 regime path 的观察，

但不能把整个 2007–2026 序列不加说明地当成完全一致口径的 repeat-sales series。

---

## C014｜Household leverage 与 2007–09 recession severity

**Claim**

```text
危机前 household leverage 越高 / 增长越快的美国地区，
2007–09 recession 中 durable consumption、default、
house price、unemployment、residential investment 等恶化更明显。
```

**Status**

```text
VERIFIED
```

**Primary research**

Atif Mian & Amir Sufi,  
**Household Leverage and the Recession of 2007 to 2009**, NBER WP 15896.

https://www.nber.org/papers/w15896

**Exact support**

Abstract 明确指出：

- 2002–06 household leverage 增长大的 counties；
- 从 2006Q3 起 durable consumption 相对下降更明显；
- household leverage / credit-card dependence 可以解释 recession 中相当部分：
  - consumer default；
  - house price；
  - unemployment；
  - residential investment；
  - durable consumption pattern。

**Language discipline**

论文 abstract 使用：

```text
powerful statistical predictor
```

因此本 repo 不应仅凭这一篇写成：

```text
“所有 leverage 差异都被完全因果识别”
```

更强 causal wording 应搭配后续 identification papers。

---

## C015｜2009 net worth 已反弹，但 household deleveraging 仍继续

**Claim**

```text
2009Q2–Q3 household net worth 已转为回升，
很大部分来自 equity-price rebound；
与此同时 household deleveraging 仍继续，
2009 total household debt 为该序列 1951 年开始以来首次年度下降。
```

**Status**

```text
VERIFIED
```

**Primary source**

Federal Reserve,  
**Monetary Policy Report, February 24, 2010 — Recent Financial and Economic Developments**

https://www.federalreserve.gov/monetarypolicy/mpr_20100224_part2.htm

**Exact support**

报告明确写到：

```text
household net worth turned up in 2009Q2 and Q3
much of the recovery reflected a rebound in equity prices
```

同时：

```text
households began to deleverage around 2008Q3
process continued during 2009H2
total household debt declined in 2009
for the first time since the series began in 1951
```

这直接支持：

```text
Asset / Net-worth Recovery
≠ Debt Repair Completed
```

---

## C016｜UK 高负债 household crisis 后 spending cut 更大

**Claim**

```text
UK 高 mortgage debt household 在 crisis 后 spending cut 更大；
与 debt 相关的 spending cuts 可能使 aggregate private consumption
在 2007 后降低最多约 2%。
```

**Status**

```text
VERIFIED
```

**Primary source**

Philip Bunn & May Rostom,  
**Household debt and spending in the United Kingdom**,  
Bank of England Working Paper No. 554, 2015.

https://www.bankofengland.co.uk/working-paper/2015/household-debt-and-spending-in-the-uk

**Exact support**

BoE summary：

```text
more highly indebted households
made larger cuts in spending

debt-associated spending cuts
may have reduced aggregate private consumption
by up to 2% after 2007
```

**Wording**

使用：

```text
up to 2%
```

不要改成：

```text
exactly 2%
```

---

## C020｜Stock wealth → local nontradable employment / payroll

**Claim**

```text
local stock wealth shock 会提高 local nontradable employment / payroll；
模型隐含 stock-wealth MPC 约 3.2 cents per dollar per year。
```

**Status**

```text
VERIFIED
```

**Primary research**

Chodorow-Reich, Nenov & Simsek,  
**Stock Market Wealth and the Real Economy: A Local Labor Market Approach**,  
NBER WP 25959.

https://www.nber.org/papers/w25959

**Exact support**

Abstract：

```text
aggregate stock-price-driven local stock wealth increase
→ local employment and payroll ↑
in nontradable industries and total
→ no effect on tradable-industry employment
```

模型 implied:

```text
MPC = 3.2 cents
per $1 stock wealth
per year
```

---

## C025｜Generative AI at Work：14% / 34%

**Claim**

```text
GenAI assistant：
average productivity +14%
novice / low-skilled workers +34%
experienced / highly skilled workers impact minimal
```

**Status**

```text
VERIFIED
```

**Primary research**

Brynjolfsson, Li & Raymond,  
**Generative AI at Work**, NBER WP 31161.

https://www.nber.org/papers/w31161

**Population**

```text
5,179 customer-support agents
```

**Exact support**

NBER abstract reports:

```text
+14% average
+34% novice / low-skilled
minimal impact on experienced / highly skilled
```

**Boundary**

这是：

```text
customer-support setting
```

不能直接外推为：

```text
所有职业 novice 都 +34%
```

---

## C029｜Northern Rock：约 75% funding 来自 non-retail money markets

**Claim**

```text
截至 2007-06-30，
Northern Rock 约 75% total funding
来自 non-retail money markets。
```

**Status**

```text
VERIFIED
```

**Primary source**

Northern Rock written evidence / UK House of Commons Treasury Committee:

https://publications.parliament.uk/pa/cm200708/cmselect/cmtreasy/536/536we06.htm

**Exact support**

```text
As at 30 June 2007
around 75% of total funding
was sourced from non-retail money markets.
```

同时记录：

```text
total non-retail funding balance = £80.5bn
£53.8bn (about two thirds of non-retail funding)
raised from securitisations and covered bonds
```

**Related turning point**

同一证据记录：

```text
2007-08-09
serious disruption in medium-term funding markets

then
severe restrictions in short-term wholesale liquidity
```

---

## C031｜英国 1980s cohort 30 岁时 homeownership 40% vs 1970s 55%

**Claim**

```text
1980s-born cohort @ age 30:
homeownership ≈ 40%

1970s cohort @ age 30:
≈ 55%
```

**Status**

```text
VERIFIED
```

**Primary / authoritative research source**

Jonathan Cribb, IFS / Fiscal Studies, 2019:

https://ifs.org.uk/journals/intergenerational-differences-income-and-wealth-evidence-britain

**Exact support**

IFS summary reports：

```text
1980s cohort:
homeownership 40% at age 30

1970s cohort:
55% at age 30
```

并报告：

```text
1980s cohort median wealth
in early 30s
≈ 20% lower than 1970s cohort
```

**Version note**

IFS 2016 的更早数据曾用“early-1980s cohort wealth about half”的表述。

2019 updated article 报告：

```text
20% lower median wealth in early 30s
```

因此核心 repo 应优先采用：

```text
2019 updated estimate
```

而把 2016 “about half”保留为旧 data vintage，不混用。

---

## C034｜2020 upstream oil & gas investment

**Claim**

```text
2020 global upstream oil & gas investment
相较 2019 下降接近三分之一。
```

**Status**

```text
VERIFIED
```

**Primary source**

IEA,  
**World Energy Investment 2020 — Fuel supply**

https://www.iea.org/reports/world-energy-investment-2020/fuel-supply

**Exact support**

IEA：

```text
upstream spending in 2020
is set to be down almost one-third from 2019
```

并说明：

```text
initial capex revisions averaged around -25%
likely net global upstream result
≈ almost one-third decline
```

**Boundary**

这是：

```text
2020 pandemic shock
```

不能单独证明：

```text
之后任何 oil-price increase 都由 underinvestment 导致
```

---

# P0 第一轮结论

本轮 10 条：

```text
C008
C009
C014
C015
C016
C020
C025
C029
C031
C034
```

均已完成第一层 source verification。

下一步仍需进一步提高 reproducibility：

1. 把 C009 的 raw series 写入 data；
2. 对论文类 claim 保存 DOI / published version；
3. 对 C014 等强机制命题定位到具体 table / empirical design，而不仅是 abstract；
4. 检查所有 case 文档是否使用了与本文件完全一致的数字与措辞。
