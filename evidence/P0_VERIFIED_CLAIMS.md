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
L2 DESIGN-VERIFIED
```

**Primary research**

Atif Mian & Amir Sufi,  
**Household Leverage and the Recession of 2007 to 2009**, NBER WP 15896.

https://www.nber.org/papers/w15896

**Empirical design**

论文以约 450 个美国 counties 为主要 cross-section，研究：

```text
2002Q4–2006Q4 debt-to-income growth
→ 2006–2009 local outcomes
```

并在 Tables 4–6 使用 first-difference regressions；IV specification 用 Saiz housing-supply inelasticity instrument household leverage growth。

**Exact design-level support**

- Table 4：一标准差 leverage growth 与约 **1/2 标准差** auto-sales decline 相关；IV coefficient 更大但更不精确；
- Table 5：一标准差 leverage growth 对应约 **1/3 标准差** new-housing-permit decline；
- Table 6：一标准差 leverage growth 对应约 **1/3 标准差** unemployment increase。

**Language discipline**

即便有 IV，repo 仍区分：

```text
cross-county causal mechanism evidence
```

与：

```text
“household leverage 单独解释整个 aggregate Great Recession”
```

后者并不由这篇论文单独建立。

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
L2 DESIGN-VERIFIED
```

**Published research**

Chodorow-Reich, Nenov & Simsek,  
**Stock Market Wealth and the Real Economy: A Local Labor Market Approach**,  
*American Economic Review* 111(5), 2021, 1613–1657.  
DOI: 10.1257/aer.20200208

https://www.aeaweb.org/articles?id=10.1257/aer.20200208

**Empirical design**

利用 county-level stock-wealth exposure 与 aggregate stock-price movements 构造 local wealth shock；Equation (1) 估计动态 county response。Published article 同时提供 replication package。

**Design-level support**

AER Table 2（h = 7 baseline）显示：

- total employment / payroll response 为正；
- nontradable employment / payroll response 更明显；
- tradable employment response 接近零。

论文模型把这些 local responses 映射为：

```text
MPC = 3.2 cents
per $1 stock wealth
per year
```

因此 Customer Beta 文档可以用它支持：

```text
stock-wealth shock
→ local nontradable demand / employment
```

但不能直接把 3.2 cents 当成任何具体餐馆的 MPC。

---

## C025｜Generative AI at Work：published version

**Claim**

```text
GenAI assistant：
preferred specification average productivity ≈ +15.2%
low-skill / low-experience workers gain much more
```

**Status**

```text
L2 DESIGN-VERIFIED
```

**Published research**

Brynjolfsson, Li & Raymond,  
**Generative AI at Work**, *Quarterly Journal of Economics*, 2025, 140(2): 889–942.  
DOI: 10.1093/qje/qjae044

https://doi.org/10.1093/qje/qjae044

**Population / design**

```text
5,172 customer-support agents
3,006,395 chats
staggered AI rollout
agent-month outcomes
```

Section IV 使用 standard difference-in-differences framework；preferred specification 包含：

```text
year-month FE
agent FE
agent-tenure FE
```

standard errors clustered at agent level。

**Design-level support**

Table II, preferred specification：

```text
Post AI × Ever treated
= +0.301 resolutions/hour
≈ +15.2% relative to pre-treatment baseline
```

Figure III：

```text
lowest pre-treatment skill quintile
≈ +36% resolutions/hour
```

最高技能组 productivity effect 接近零。

经验曲线分析还显示：

```text
2 months tenure + AI
≈
>6 months tenure without AI
```

在多项 productivity outcome 上成立。

**Version note**

2023 NBER working-paper 版本曾报告：

```text
5,179 agents
+14% average
+34% novice / low-skilled
```

2025 *QJE* final version 更新了 sample 与 estimates。核心 repo 从现在起优先使用 published version。

**Boundary**

这是：

```text
single firm
single occupation
particular AI tool
```

不能把 +15% 或 +36% 机械外推到所有职业。

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

本轮 10 条 P0 claim 均已完成至少 L1 source verification。

其中：

```text
C014
C020
C025
```

已进一步达到 **L2 design-level verification**。

同时本轮发现并修复了一个典型的 version drift：

```text
C025
2023 working paper: 5,179 / +14% / +34%
→
2025 QJE final: 5,172 / +15.2% preferred spec / low-skill quintile ≈ +36%
```

这正说明为什么 repo 需要 claim-level source version control。

下一步：

1. 检查其他 working-paper citation 是否已有 published version；
2. 将更多 derived values 转成 data artifact；
3. 继续对 P1 synthesis 建立 direct-evidence / falsification link。
