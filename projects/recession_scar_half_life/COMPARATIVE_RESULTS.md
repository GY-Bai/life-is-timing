# Comparative Results｜Recession Scar Half-life 第一轮横向结果

> 状态：**Phase II working result**  
> 这些数字是 study-internal descriptive metrics，不是国家排名，也不是可直接 pooled 的 causal estimates。

## 1. 当前可核验的 half-life map

| Study / sample | Outcome / specification | Descriptive magnitude half-life | 关键边界 |
|---|---|---:|---|
| Japan — high school, older cohorts | full-time annual earnings | ≈ 8.33y | grouped experience bins |
| Japan — four-year college, older cohorts | full-time annual earnings | ≈ 5.69y | 10–12y 后 sign reversal，half-life 只用前三个负值 bin |
| US — Kahn national OLS | wage | ≈ 13.54y | national unemployment exposure |
| US — Kahn national IV | wage | ≈ 10.83y | 不同 identifying variation |
| US — Kahn state IV | wage | > 15y | right-censored；不能和 national estimate 平均 |
| Canada — full sample | annual earnings | ≈ 4.39y | grouped 0–1 / 4–5 / 9–10 bins |
| Canada — bottom skill quintile | annual earnings | > 9.5y | right-censored |
| Canada — middle skill quintile | annual earnings | ≈ 4.97y | same paper / same treatment framework |
| Canada — top skill quintile | annual earnings | ≈ 3.30y | fastest within-paper recovery |
| Canada — full sample | employer quality | ≈ 4.06y | firm median log earnings |
| Finland — all 1988–2004 cohorts | annual earnings | 9.00y | exact annual curve |
| Finland — 1988–1995 | annual earnings | ≈ 6.79y | sample / identifying variation changes |
| Finland — 1996–2004 | annual earnings | ≈ 3.26y | sample / historical window changes |
| Netherlands — academic | wage | summary: fade ≈ 6y | exact curve not yet publicly extracted |
| Netherlands — vocational | wage | summary: ≈1% remains at 8y | exact curve not yet publicly extracted |

## 2. 第一条真正稳定的结果：Country 不是一个 scar parameter

如果把 literature 压成：

~~~text
Japan = X years
US = Y years
Canada = Z years
~~~

会立刻丢掉最重要的信息。

同一个国家内部已经存在：

### Canada

~~~text
Top skill     ≈ 3.30y
Middle        ≈ 4.97y
Bottom        > 9.5y
~~~

### Finland

~~~text
all cohorts   = 9.0y
1996–2004     ≈ 3.26y
~~~

### Japan

~~~text
older cohorts:
clear negative scar

younger / post-ice-age cohorts:
initial negative earnings effect weakens / disappears
~~~

### United States

同一篇 Kahn 2010：

~~~text
national OLS  ≈ 13.54y
national IV   ≈ 10.83y
state IV      >15y
~~~

所以：

> **Scar half-life 不是一个国家常数，而是 sample × treatment × transition structure × identification 的结果。**

## 3. 第二条结果：Initial Damage 与 Persistence 必须分开

Canada 的 top group：

~~~text
initial earnings effect = -0.0147
half-life ≈ 3.30y
~~~

Bottom group：

~~~text
initial effect = -0.0277
half-life > 9.5y
~~~

这里 initial damage 与 persistence 同方向。

但 Netherlands 的 published summary 给出另一个组合：

~~~text
Academic:
larger initial wage loss
but fades ≈ 6y

Vocational:
smaller initial loss
but remains ≈1% at year 8
~~~

因此一般式必须拆成：

~~~text
Scar Severity
≠
Scar Persistence
~~~

一个 shock 可以：

- 打得重但恢复快；
- 打得轻但长期粘住。

## 4. 第三条结果：Canada 把 R3 的“re-entry”从国家变量变成了 worker-level mechanism

Canada Table 2 的 employer-quality gap：

### Full sample

~~~text
-0.0096
→ -0.0042
→ -0.0028
~~~

### Bottom skill quintile

~~~text
-0.0111
→ -0.0087
→ -0.0126
~~~

### Top skill quintile

~~~text
-0.0082
→ -0.0004
→ +0.0010
~~~

作者同时发现，初始 bad labor-market conditions 会把毕业生推向较低质量 employer，而前 3–5 年 employer quality 改善最快，这一时期 job mobility 也较高。

所以：

~~~text
Re-entry Flexibility
~~~

不能只理解成：

~~~text
这个国家允许不允许换工作
~~~

还必须包括：

~~~text
worker 是否拿得到新的 offer
是否有能力承担 mobility cost
是否能进入更好的 employer
是否在年龄 / tenure 增长前完成 re-match
~~~

## 5. 第四条结果：Measurement / Identification 本身就是 scar-duration 的一部分

Kahn 的 national / state、OLS / IV 差异，以及 Finland 不同 cohort window 的差异，都说明：

~~~text
Observed Half-life
=
Underlying Persistence
+
Exposure Definition
+
Sample Composition
+
Identification Variation
+
Outcome Definition
~~~

这里不是说 empirical result “只是 measurement artifact”。

而是说：

> **如果不把 estimand 保存下来，“half-life”这个数字本身没有可比意义。**

所以本项目以后不允许只写：

~~~text
half-life = 6 years
~~~

必须至少写：

~~~text
study
sample
outcome
exposure
specification
event-time basis
half-life
censoring
~~~

## 6. R3 的 Phase II working refinement

Canonical R3 不修改，仍然是：

~~~text
Persistent Scar
≈
Entry Shock Severity
× State Dependence
× Re-entry Friction
÷ Alternative Adjustment Routes
~~~

但 Project 01 当前的 working decomposition 更具体：

~~~text
Re-entry Friction
=
Institutional Gate
× Worker-specific Search Friction
× Mobility Cost
× Employer-access Friction
× Time / Age Dependence
~~~

因此：

~~~text
Country Institution
~~~

只是其中一层。

这不是新的第七条 regularity，而是对 R3 内部变量的 empirical decomposition。

## 7. Netherlands 为什么暂时不硬算 half-life

公开可核验的 published abstract 已经支持：

~~~text
academic initial wage loss ≈ 10%
fade ≈ 6 years

vocational initial ≈ 6%
≈1% remains at year 8
~~~

并明确指出：

~~~text
job / sector mobility
→ better-paying employers
~~~

是主要 catch-up mechanism。

但在没有取得可核验的逐年 table / figure 数字前，本项目不会根据图形目测或二手文本“补齐”一条 annual curve。

因此 Netherlands 当前状态保持：

~~~text
summary-verified
not curve-extracted
~~~

这也是 source discipline 的一部分。

## 8. 当前最重要的研究问题已经变化

Project 01 最初的问题：

> **为什么不同国家 scar duration 不一样？**

经过第一轮 extraction 后，更好的问题变成：

> **在同一个 macro shock 之后，谁能在 mobility cost 上升、career state 固化之前完成 re-matching？**

这把 R3 从：

~~~text
country-level institutional story
~~~

推进到：

~~~text
institution
× worker type
× initial match
× search / mobility
× time
~~~

的 transition problem。

## 9. 当前不允许得出的结论

不能从上表推出：

~~~text
Canada 比 Japan 更容易恢复
US 制度一定比 Finland 差
某国的真实 scar 就等于表中的 half-life
~~~

这些 half-life 来自不同：

~~~text
outcome
sample
exposure
specification
event-time grid
~~~

它们当前的用途是：

~~~text
发现 heterogeneity
检验 metric
寻找 mechanism
~~~

而不是排名。
