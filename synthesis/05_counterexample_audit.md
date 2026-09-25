# Counterexample Audit｜六条候选规律的反例与失效边界

> 目标：不是继续证明 R1–R6，而是主动寻找它们在哪里会失败。  
> 结论：六条规律大多仍然保留，但都必须从“绝对规律”收缩为 **conditional regularity**。

---

# R1｜Fastest Adjustable Margin：反例是“最容易动的变量，也可能被粘住”

原版：

```text
Shock
→ 最容易调整的变量先动
```

这个方向总体成立，但“最容易”不能只按物理流动性判断。

## 反例 A：住房 downturn 中，volume 可以先于 price 调整

Housing market 里，seller 可能因为：

- loss aversion；
- reservation price；
- negative equity；
- search friction；

不愿意立刻接受更低价格。

Genesove & Mayer 对 Boston condo market 的研究发现，面临 nominal loss 的 seller：

```text
asking price 更高
sale hazard 更低
```

因此 downturn 中可以出现：

```text
transaction volume ↓↓↓
price ↓ relatively slowly
```

也就是说：

```text
Price
```

虽然“可报价”，却不一定是实际最快清算的 margin。

### 来源

- Genesove & Mayer, **Loss Aversion and Seller Behavior: Evidence from the Housing Market**, QJE / NBER.  
  https://www.nber.org/papers/w8143

---

## 反例 B：工资 sticky 时，企业可能先裁人而不是降工资

美国与丹麦的研究都显示：

```text
Nominal Wage Cut
```

并不是一个低成本 adjustment margin。

工资下降可能带来：

- morale cost；
- quits；
- fairness concern；
- internal wage structure disruption。

Ehrlich & Montes（2024）估计 wage rigidity 与：

```text
higher layoff rate
lower hiring rate
```

相关。

Davis & Krolikowski（2025）则发现，很多失业者事后愿意接受工资下降来保住岗位，但雇主与员工在 layoff 前实际讨论 wage / hour cuts 的情况极少。

所以 shock 可能走：

```text
Demand Shock
→ Employment Quantity ↓
```

而不是：

```text
Wage Price ↓
```

### 来源

- Ehrlich & Montes, **Wage Rigidity and Employment Outcomes**, AEJ: Macro, 2024.  
  https://www.aeaweb.org/articles?id=10.1257/mac.20200125

- Davis & Krolikowski, **Sticky Wages on the Layoff Margin**, AER, 2025.  
  https://pubs.aeaweb.org/doi/10.1257/aer.20240309

---

## R1 修正版

```text
Shock
→ Lowest-cost AVAILABLE adjustment margin
```

其中 available 由：

```text
Liquidity
+ Contract
+ Norms
+ Regulation
+ Loss Aversion
+ Search Friction
```

共同决定。

所以不再写：

```text
“Price always moves first”
```

而写：

> **压力会优先进入当时实际调整成本最低、制度上可执行的 margin。**

---

# R2｜Slow Stock Persistence：反例是“慢 stock 可能被替代，而不是被重建”

原版：

```text
Persistence
∝ Rebuilding Time of Binding Stock
```

问题在于：

```text
slow stock
```

不一定真的需要原地重建。

---

## 反例 A：short-cycle supply 可以绕过 long-cycle capacity

IEA 记录 2014 downturn 以后 oil industry 明显转向：

```text
shorter-cycle
smaller
modular
faster-payback
```

项目。

美国 shale 尤其具有：

```text
shorter investment cycle
```

因此，即使传统 deepwater / megaproject 是慢 stock，系统仍可能通过：

```text
shale
brownfield
inventory
OPEC spare capacity
```

绕开一部分重建时间。

### 来源

- IEA, **World Energy Investment 2019 — Fuel supply**.  
  https://www.iea.org/reports/world-energy-investment-2019/fuel-supply

- IEA, **World Energy Investment 2022**.  
  https://www.iea.org/reports/world-energy-investment-2022/overview-and-key-findings

---

## 反例 B：human-capital shortage 可以通过 immigration 缓解

如果本地 skilled-worker stock 很慢：

```text
training takes years
```

并不意味着一定要等本地新人全部培养出来。

可以：

```text
import labor
```

2026 年关于美国 2021–24 labor shortage 的研究发现，immigration 能帮助填补 vacancy，并缓和 wage pressure。

### 来源

- Mandelman, Yu & Zanetti, **Immigration, labor shortages, and labor market dynamics**, Oxford, 2026.  
  https://www.economics.ox.ac.uk/publication/2388644/ora-hyrax

---

## R2 修正版

```text
Persistence
∝
Rebuild Time of
SLOWEST BINDING NON-SUBSTITUTABLE Stock
```

必须加：

```text
non-substitutable
```

否则 imports、migration、technology、idle capacity 都可能绕过原来的 slow stock。

---

# R3｜Entry × Re-entry：反例是“bad entry 不一定留下长期 scar”

原版：

```text
Bad Entry
× Low Re-entry
→ Persistent Scar
```

这个结构仍然强，但不同 institution / skill group 的 scar 可以非常短。

---

## 反例 A：荷兰 academic graduates 可以较快追平

Van den Berge 对 Netherlands 1996–2012 graduates 的研究发现：

```text
academic graduates
初始 wage loss 较大
但约 6 年后消失
```

主要恢复机制是：

```text
job / sector mobility
→ better-paying employer
```

而 vocational graduates 的 mismatch 更持久。

这意味着：

```text
same recession
× different educational track
→ different scar half-life
```

### 来源

- van den Berge, **Bad start, bad match?**, Labour Economics, 2018.  
  https://research-portal.uu.nl/en/publications/bad-start-bad-match-the-early-career-effects-of-graduating-in-a-r/

---

## 反例 B：Finland 的 effect 会随 macro regime 改变

Päällysaho 的 Finland 研究发现：

```text
全样本：
earnings scar 可达约 10 年

但排除异常深的 1990s depression 后：
earnings effect 约 5 年
unemployment effect 很小
```

说明：

```text
Scar Persistence
```

不仅由 entry institution 决定，还受：

```text
shock severity
macro regime
```

影响。

### 来源

- Päällysaho, **The Short- and Long-Term Effects of Graduating During a Recession: Evidence from Finland**.  
  https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3050444

---

## 反例 C：labor-market scar 不一定转化为 wealth / family scar

Kawaguchi（2020）研究 NLSY79 发现：

```text
bad labor-market entry
→ persistent wage penalty
```

但长期：

```text
home ownership
car ownership
net asset holdings
family formation
```

并没有显著受影响。

一个适应机制是：

```text
搬到生活成本更低的州
```

这直接提醒：

```text
Career Scar
≠ Automatically Wealth Scar
```

### 来源

- Kawaguchi, **The Effects of Graduating from College During a Recession on Living Standards**, Economic Inquiry, 2020.  
  https://onlinelibrary.wiley.com/doi/10.1111/ecin.12835

---

## R3 修正版

```text
Persistent Entry Scar
≈
Entry Shock Severity
× State Dependence
× Re-entry Friction
÷ Alternative Adjustment Routes
```

其中 Alternative Routes 包括：

- employer switching；
- sector switching；
- migration；
- further education；
- lower-cost location；
- family risk sharing。

---

# R4｜Leverage Nonlinearity：反例是“杠杆不一定马上表现为 cash-flow crisis”

原版：

```text
Price Shock
× Leverage
→ Nonlinear State Change
```

这个机制对 marginable / refinancing-sensitive balance sheet 很强。

但 household mortgage 有特殊制度。

---

## 反例 A：fixed-rate mortgage 会延迟 shock transmission

英国 2023–24 的高利率阶段，大量 household 当时处于 fixed-rate mortgage。

Bank of England 明确指出：

```text
fixed-rate structure
→ higher Bank Rate 向 household debt service 的传导被延迟
```

因此：

```text
Rate Shock Today
```

不会立刻变成：

```text
Cash-flow Shock Today
```

而是等：

```text
refinancing / reset date
```

才释放。

### 来源

- Bank of England, **Financial Stability in Focus: Interest rate risk**, July 2023.  
  https://www.bankofengland.co.uk/financial-stability-in-focus/2023/july-2023

- Bank of England, **Monetary Policy Report**, August 2024.  
  https://www.bankofengland.co.uk/monetary-policy-report/2024/august-2024

---

## 反例 B：negative equity 可能表现为“锁住”，而不是“强制卖出”

Ferreira、Gyourko、Tracy 的研究发现：

```text
negative equity
→ mobility 显著下降
```

也就是说 household mortgage 不像 margin account：

```text
asset price ↓
→ immediately liquidate
```

更可能是：

```text
asset price ↓
→ household remains in place
→ mobility / reallocation ↓
```

但这里甚至存在 measurement controversy：Schulhofer-Wohl 曾得到 negative equity 并不降低 mobility 的不同结论；之后 FGT 更新数据与 move coding 后再次得到 lock-in。

这本身说明：

> **leverage 的行为结果高度依赖 contract 与 measurement。**

### 来源

- Ferreira, Gyourko & Tracy, **Housing Busts and Household Mobility: An Update**.  
  https://www.nber.org/papers/w17405

- Schulhofer-Wohl, **Negative Equity Does Not Reduce Homeowners' Mobility**.  
  https://www.nber.org/papers/w16701

---

## R4 修正版

```text
Leverage Amplification
=
f(
LTV,
Debt-Service,
Maturity,
Rate Fixation,
Recourse,
Marginability,
Refinancing Need,
Liquidity
)
```

因此不能把：

```text
high leverage
```

当成单一 scalar risk。

它可能表现为：

- default；
- consumption cut；
- margin call；
- refinancing risk；
- mobility lock-in；
- delayed adjustment。

---

# R5｜Optionality Buffers Scarring：反例是“Option 本身也有成本”

原版：

```text
Optionality ↑
→ Scar Persistence ↓
```

这是目前 repo 最重要的 strategy synthesis。

但它绝不是：

```text
more options always better
```

---

## 反例 A：mobility 可能销毁 specific human capital

Neal 的 displaced-worker 研究显示：

```text
switch industry
→ loss of industry-specific human capital
→ wage loss
```

后续研究也发现 occupation / industry-specific experience 有显著价值。

所以：

```text
“能换行业”
```

是 option。

但：

```text
“真的换行业”
```

可能有 exercise cost。

### 来源

- Neal, **Industry-Specific Human Capital: Evidence from Displaced Workers**, Journal of Labor Economics, 1995.  
  https://www.journals.uchicago.edu/doi/10.1086/298388

---

## 反例 B：更多等待时间不一定自动改善 match

UI 是一个很好的 real-options analogue。

Nekoei & Weber（Austria）发现：

```text
longer UI
→ longer unemployment
但也可通过更好的 employer match
→ higher reemployment wage
```

说明 wait option 有价值。

但 Washington Work Search experiment 的长期跟踪发现：

```text
取消 work-search requirement
```

对 permanent job losers 反而带来：

- 更长 reemployment time；
- 更低 earnings；
- 更短 first post-claim tenure。

也就是说：

```text
More Time / Less Pressure
```

并不自动产生更好结果。

### 来源

- Nekoei & Weber, **Does Extending Unemployment Benefits Improve Job Quality?**, AER, 2017.  
  https://swlb1.aeaweb.org/articles?id=10.1257/aer.20150528

- U.S. Department of Labor, **Effects of Eliminating the Work Search Requirement**, 2015.  
  https://www.dol.gov/agencies/eta/research/publications/effects-eliminating-work-search-requirement-job-match-quality

---

## R5 修正版

真正有用的不是：

```text
Raw Optionality
```

而是：

# Exercisable Optionality

可以写成：

```text
Effective Optionality
=
Option Set
× Exercisability
× Value Preservation
- Exercise Cost
- Carrying Cost
```

例如：

```text
能搬家
```

如果会失去 occupation-specific capital、family support、visa、childcare：

```text
nominal option 很大
effective option 很小
```

---

# R6｜Experience ≠ Historical Distribution：反例是“重视近期经验有时恰恰是合理的”

原版：

```text
Personal Experience
≠ Historical Distribution
```

这个事实不需要修改。

但容易被误读成：

```text
使用个人近期经验
= irrational bias
```

这不成立。

---

## 反例 A：结构变化环境中，近期数据本来就应该权重更高

Adaptive-learning literature 里：

```text
constant-gain learning
```

会主动降低很久以前数据的权重。

原因是：

```text
如果 data-generating process 在变化
full-history average 反而追不上 regime shift
```

Evans / Honkapohja 传统明确指出：

```text
optimal gain
取决于 perceived structural change
```

structural change 越大：

```text
更高 gain
→ 更快追踪新参数
```

### 来源

- Evans & Honkapohja learning framework summary.  
  https://darkwing.uoregon.edu/~gevans/LearningMacroOxford_RedForm_4Sept2020.pdf

- Markiewicz & Pick, **Adaptive learning and survey data**, 2014.  
  https://ideas.repec.org/a/eee/jeborg/v107y2014ipbp685-707.html

---

## 反例 B：Experience-based learning 本身可以接近 Bayesian updating

Nagel（2026）的综述强调：

```text
experience-based model
closely resembles Bayesian updating
```

真正偏离 full-information rational expectation 的地方，是：

```text
对自己 lifetime 内的数据给予更高权重
```

所以 experience effect 不应简单写成：

```text
irrationality
```

而应写成：

```text
locally adaptive
but historically incomplete
```

### 来源

- Stefan Nagel, **Experiences, Expectations, and Asset Prices**, 2026.  
  https://www.nber.org/papers/w34675

---

## R6 修正版

```text
Experience-based Learning
=
Useful Adaptation
when regime is changing

but

Dangerous Compression
when local sample is mistaken for universal law
```

真正的问题不是：

```text
“你有没有使用自己的经验”
```

而是：

> **你有没有把经验的适用边界一起保存下来。**

---

# 六条规律经过 Red Team 后的 V2

```text
R1
Shock first hits the lowest-cost AVAILABLE margin,
not necessarily the most liquid-looking variable.

R2
Persistence is governed by the slowest BINDING,
NON-SUBSTITUTABLE stock.

R3
Entry shocks become scars when state dependence
and re-entry friction exceed alternative adjustment routes.

R4
Leverage is a state-contingent amplifier whose effect
depends on maturity, cash flow, recourse, marginability and refinancing.

R5
EXERCISABLE optionality buffers scarring;
nominal options can be costly, unusable or value-destroying.

R6
Experience-based learning can be locally adaptive
while remaining globally incomplete.
```

---

# 最重要的变化

Red Team 之后，整个 framework 从：

```text
“系统总是这样运行”
```

收缩成：

```text
“当这些边界条件成立时，
这个 mechanism 更可能出现”
```

这是进步，而不是削弱。

如果一个框架只能靠忽略反例来维持，它没有研究价值。
