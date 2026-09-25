# Claims Ledger｜核心命题台账

> 状态：Phase I claim-level audit。  
> 目标：把“文档”拆成可独立核验的 claims，防止同一个数字或因果措辞在不同文件中漂移。

## 字段

- **ID**：稳定编号；
- **Claim**：一句话命题；
- **Type**：Fact / Evidence / Synthesis / Hypothesis / Boundary；
- **Verification**：Verified / Partial / Pending / Rejected；
- **Population / Period**：适用对象与时间；
- **Source**：当前主要来源；
- **Used In**：主要文档。

| ID | Claim | Type | Verification | Population / Period | Source | Used In |
|---|---|---|---|---|---|---|
| C001 | 日本 job-market “ice-age” cohorts 可大致界定为 1993–2004 labor-market entrants | Fact | Verified | Japan, 1993–2004 entrants | Kondo 2024 | Case 01 |
| C002 | 日本毕业时未进入 regular employment 会提高后续非 regular 状态持续概率 | Evidence | Verified | Japan | Kondo 2007 | Case 01 / Doc 04 |
| C003 | 日本后冰河期 cohort 的 entry-unemployment scarring 不再与冰河期同样显著 | Boundary | Verified | Japan, post-ice-age cohorts | Kondo 2024 | Case 01 |
| C004 | 美国/加拿大 recession entry 会造成初始 earnings / wage penalty | Evidence | Verified | North America, multiple cohorts | Kahn; Oreopoulos et al.; Schwandt-von Wachter | Case 02 |
| C005 | recession-entry scar 可通过 employer upgrading / switching 部分修复 | Evidence | Verified | Canada / flexible labor markets | Oreopoulos et al. | Case 02 / Doc 01 |
| C006 | labor-market scar 不必然转化为长期 housing / net-worth scar | Boundary | Verified | NLSY79 | Kawaguchi 2020 | Counterexample Audit |
| C007 | 中国 1998 年住房改革明确推动停止住房实物分配并实行货币化 | Fact | Verified | China, 1998 | 国发〔1998〕23号 | Case 03 |
| C008 | 全国住宅平均销售价格：1995 年约 1509 元/㎡，1998 年约 1854 元/㎡ | Fact | Verified | China, national transaction averages | NBS historical tables | Case 03 |
| C009 | 中国住宅价格指数 2021Q3 至 2026Q1 约下跌 21.9%（名义） | Derived Fact | Verified | BIS China index | BIS/FRED series | Case 03 |
| C010 | 全国价格下跌不能推出某 birth cohort 多数家庭 negative equity | Boundary | Verified conceptually | China households | LTV / repayment requirement | Case 03 / Evidence Ledger |
| C011 | Nick Hitchon 1982 年加入 UW–Madison，并长期从事 plasma / fusion research | Fact | Verified | Individual case | UW biography | Case 04 |
| C012 | Nick 进入职业市场时英国 aggregate unemployment 很高 | Fact | Verified | UK, early 1980s | ONS | Case 04 |
| C013 | Nick 案例只能支持 mechanism plausibility，不能做 population causal inference | Boundary | Verified methodologically | Individual case | case-study limitation | Case 04 |
| C014 | 高 household leverage 会放大 2007–09 recession 中的 consumption / employment decline | Evidence | Verified | US regions | Mian & Sufi | Case 05 |
| C015 | 2009 美国 household net worth 已部分反弹，但 deleveraging 仍继续 | Fact / Synthesis | Verified | US, 2009 | Federal Reserve | Case 05 |
| C016 | UK 高负债家庭在 crisis 后 spending cut 更大 | Evidence | Verified | UK households | Bunn & Rostom | Case 05 |
| C017 | market liquidity 与 funding liquidity 可形成自我强化 spiral | Evidence / Theory | Verified | Financial markets | Brunnermeier-Pedersen | Case 06 / Doc 05 |
| C018 | private-market reported volatility 较低可能部分来自低频估值 / price-discovery lag | Synthesis | Partial | Private markets | BoE + illiquidity literature | Case 06 |
| C019 | private-credit redemption pressure 必然触发 public-market fire sale | Hypothesis | Rejected as universal | Fund-specific | conditional only | Case 06 / Counterevidence |
| C020 | local stock wealth shocks 会影响 nontradable employment / payroll | Evidence | Verified | US local labor markets | Chodorow-Reich et al. | Case 07 |
| C021 | housing wealth / collateral shock 可进入 household consumption | Evidence | Verified | US / UK | Mian-Sufi; BoE | Case 07 |
| C022 | Customer Beta 可稳定预测单家 local business revenue | Hypothesis | Pending | Firm-level | needs POS / customer mix | Doc 07 / Case 07 |
| C023 | New Zealand 自 1970s 中期长期存在 current-account deficit | Fact | Verified | NZ | RBNZ | Case 08 |
| C024 | current-account identity 成立不代表 funding regime 稳定 | Synthesis | Verified conceptually | Open economy | accounting + RBNZ history | Case 08 |
| C025 | GenAI 在客服场景平均提高 productivity 约 15%，且低经验 / 低技能 worker 的增益显著更大 | Evidence | L2 Design-Verified | 5,172 support agents | Brynjolfsson-Li-Raymond, QJE 2025 | Case 09 |
| C026 | AI adoption 已导致全面 junior employment collapse | Claim | Rejected as universal | Current labor market | Stanford review | Case 09 |
| C027 | AI adoption 可能改变 junior / senior workforce composition | Emerging Evidence | Partial | 41-country affiliate data | Chandar & Klein Teeselink | Case 09 |
| C028 | AI 最终会造成 future senior shortage | Hypothesis | Pending | Long horizon | no long-run panel yet | Case 09 / Doc 04 |
| C029 | Northern Rock 约 75% funding 来自 non-retail money markets | Fact | Verified | Northern Rock, 2007H1 | UK Parliament evidence | Case 10 |
| C030 | Northern Rock crisis 的关键 early break 是 wholesale funding freeze，而非等到全部 mortgage losses realized | Evidence + Synthesis | Verified | UK, 2007 | Treasury Committee / BoE | Case 10 |
| C031 | UK later cohorts 在相同年龄的 homeownership 较 earlier cohorts 更低 | Evidence | Verified | Britain | IFS / Resolution Foundation | Case 11 |
| C032 | UK later-cohort wealth stagnation 不需要假设年轻人储蓄偏好恶化 | Model Evidence | Verified within model | Britain | Crawford-Sturrock | Case 11 |
| C033 | wealth amount 与 wealth timing 对 life-course outcome 不等价 | Synthesis | Partial | Households | inheritance timing logic | Case 11 |
| C034 | 2014–20 oil upstream investment weakness 降低了 future supply elasticity | Evidence + Synthesis | Verified directionally | Global oil | IEA | Case 12 |
| C035 | 2021–22 oil price spike 可全部由 underinvestment 解释 | Claim | Rejected | Global oil | multiple competing shocks | Case 12 |
| C036 | Great Depression 对不同 cohort 的影响取决于 age-at-exposure / developmental stage | Evidence | Verified | Oakland / Berkeley cohorts | Elder | Case 13 |
| C037 | local house-price experience 会影响 aggregate house-price expectations | Evidence | Verified | US households | Kuchler-Zafar | Case 14 |
| C038 | US housing-experience effect 已在所有国家严格 replication | Claim | Rejected / Pending | Cross-country | insufficient comparable designs | Case 14 |
| C039 | Age、Period、Cohort 三条独立线性趋势可仅靠观测数据唯一识别 | Claim | Rejected | APC models | identification identity | Foundation 03 |
| C040 | cohort difference 可以直接解释为 causal cohort effect | Claim | Rejected | Any cohort comparison | APC discipline | Foundation 03 |
| C041 | shock 总是先让最“流动”的变量动 | Claim | Rejected as absolute | Cross-domain | wage / housing counterexamples | Synthesis V2 |
| C042 | shock 倾向先进入最低成本且可执行的 adjustment margin | Candidate Regularity | Partial | Cross-domain | multiple cases | Canonical Model R1 |
| C043 | 最慢、binding 且不可替代的 stock 决定 recovery persistence | Candidate Regularity | Partial | Cross-domain | labor / housing / energy | Canonical Model R2 |
| C044 | bad entry 在 re-entry friction 高时更容易固化成 scar | Candidate Regularity | Strong Partial | Labor markets strongest | Japan / US / NL / Finland | Canonical Model R3 |
| C045 | leverage amplification 取决于 maturity / rate / recourse / marginability 等 contract state | Candidate Regularity | Strong Partial | Household / financial balance sheets | BoE / housing / banking | Canonical Model R4 |
| C046 | nominal optionality 与 effective exercisable optionality 不等价 | Candidate Regularity | Partial | Cross-domain | mobility / UI / refinancing | Canonical Model R5 |
| C047 | experience-based learning 可能 locally adaptive，但不能代表 full historical distribution | Candidate Regularity | Strong Partial | Expectations / beliefs | Malmendier-Nagel / adaptive learning | Canonical Model R6 |
| C048 | “被周期拷打过”必然形成更正确的 macro model | Claim | Rejected | General | experience-effects literature | Foundation 02 |
| C049 | Path dependence 等于 path determinism | Claim | Rejected | General | re-entry / turning-point evidence | Canonical Model |
| C050 | Life Is Timing 可以用一个统一结构方程直接估计 | Claim | Rejected | Framework | decomposition only | Canonical Model |

---

# 下一轮核验优先级

## P0｜定量 / 强断言核验

第一轮 L1 已全部完成；其中以下三条已进一步达到 L2 design-level：

```text
C014
C020
C025
```

其余 P0 维持 L1 / derived verification：

```text
C008 C009 C015 C016 C029 C031 C034
```

这些含明确数字或较强经验断言。

## P1｜需要补更强直接识别

```text
C018
C022
C027
C033
C042
C043
C046
```

## P2｜长期等待数据

```text
C028
```

AI → future senior shortage 暂时不能升级。

---

# 规则

以后任何核心文档新增一个：

```text
具体数字
具体 cohort 定义
强因果措辞
跨领域 generalization
```

必须先在本 ledger 分配 claim ID。
