# Re-matching Capacity｜Operationalization Spec

> 状态：**Phase II-2 working specification**  
> 目的：把 R3 中抽象的 `Re-entry Flexibility` 拆成可以被论文直接观察、反驳和比较的变量。  
> 这不是新的 regularity，也不构造一个主观“国家灵活度分数”。

## 1. 为什么现在必须 operationalize

第一轮 extraction 已经表明：

~~~text
Country
≠
Scar Parameter
~~~

Canada 同一制度、同一数据和相近 treatment 下：

~~~text
Top skill earnings half-life     ≈ 3.30y
Middle                           ≈ 4.97y
Bottom                           > 9.5y
~~~

Japan 同一国家中：

~~~text
older cohorts:
entry-unemployment scar persistent

younger cohorts:
entry-unemployment effect weakens / disappears
~~~

因此下一步不能继续把：

~~~text
Re-entry Flexibility
~~~

写成一个国家标签。

我们真正要观察的是：

> **坏的 initial match 之后，一个 worker 通过什么 transition 回到更好的 career state，以及这个 transition 的 hazard 是否随时间快速下降。**

---

## 2. State-space representation

先定义简化 career states：

~~~text
S0 = not employed / unstable entry
S1 = low-quality / nonregular / low-paying match
S2 = regular or medium-quality match
S3 = high-quality / higher-paying match
~~~

R3 关心的不是单纯：

~~~text
P(employed)
~~~

而是：

~~~text
P(S1 → S2 or S3 | t)
~~~

以及：

~~~text
E[time to better match | bad entry]
~~~

如果：

~~~text
P(upgrade | bad entry, t)
~~~

随 tenure / age 快速下降，

temporary entry shock 就可能变成 persistent state dependence。

---

## 3. 五个 operational components

### C1｜Entry Gate

定义：

~~~text
第一次进入 core / regular / career-track job 的窗口有多集中。
~~~

可观察 proxy：

- first-job regular status；
- school-to-work immediate transition rate；
- new-graduate-only vacancy share；
- employer preference for fresh graduates；
- missed-new-grad-window penalty。

R3 作用：

~~~text
Entry Gate Rigidity ↑
→ bad initial state probability ↑
→ initial state 更重要
~~~

Japan 的 first-job state-dependence literature 直接对应这一层。

---

### C2｜Offer Arrival / Employer Access

定义：

~~~text
已经处于较差 match 的 worker，
之后获得更好 employer offer 的机会。
~~~

可观察 proxy：

- employer-quality upgrading；
- movement to higher-paying firms；
- job-to-job transition；
- transition into regular employment；
- sector / occupation upgrading。

R3 作用：

~~~text
Better-offer arrival ↑
→ time to re-match ↓
→ scar decay faster
~~~

Canada 当前最直接。

---

### C3｜Search & Mobility Cost

定义：

~~~text
worker 即使看到更好的 match，
能否承担寻找和转换的成本。
~~~

可观察 proxy：

- job mobility rate；
- geographic mobility；
- employer switching；
- sector switching；
- unemployment spell required for switching；
- mobility differences by family / tenure / age。

注意：

~~~text
Observed low mobility
≠ automatically high mobility cost
~~~

因为低 mobility 也可能意味着：

~~~text
没有 better offer
或
当前 match 已经很好
~~~

所以 C3 必须和 C2 联合解释。

---

### C4｜Skill / Credential Portability

定义：

~~~text
worker 的已有能力能否被下一个 employer 识别并重新定价。
~~~

可观察 proxy：

- education track；
- occupation transferability；
- field-specific mismatch；
- credential recognition；
- employer-quality transition by predicted skill；
- sector switching without wage penalty。

R3 作用：

~~~text
Portability ↑
→ bad first match 更容易被下一次匹配纠正
~~~

Canada skill quintiles 和 Netherlands academic / vocational split 都是候选证据。

---

### C5｜Time Dependence / Window Decay

定义：

~~~text
re-match opportunity 是否随着离开 graduation window 的时间而下降。
~~~

可观察 proxy：

- transition hazard by years since graduation；
- regular-employment entry by experience；
- employer upgrading concentrated in first 3–5 years；
- eligibility for second-new-graduate hiring；
- age / tenure interaction。

这是 R3 最关键但目前最缺数据的一层。

如果：

~~~text
upgrade hazard(t)
↓ rapidly with t
~~~

那么：

~~~text
delay
→ lower future exit probability
→ hysteresis
~~~

---

## 4. 不建立主观 composite score

当前禁止构造：

~~~text
Japan re-entry score = 2/10
Canada = 8/10
~~~

因为五个 component：

~~~text
不是同一个量纲
不是同一个 estimand
也未必同方向共变
~~~

本项目使用：

~~~text
mechanism vector
~~~

而不是 score：

~~~text
R = [
Entry Gate,
Offer Access,
Mobility,
Portability,
Time Dependence
]
~~~

每个 cell 只允许：

~~~text
direct evidence
proxy evidence
not observed
contradictory
~~~

---

## 5. Canada：目前最接近 observable re-matching

Oreopoulos–von Wachter–Heisz Table 2 已经给出：

### Earnings

~~~text
Top:
-0.0147 → -0.0042 → -0.0024

Middle:
-0.0232 → -0.0124 → -0.0039

Bottom:
-0.0277 → -0.0167 → -0.0161
~~~

### Employer quality

~~~text
Top:
-0.0082 → -0.0004 → +0.0010

Middle:
-0.0128 → -0.0050 → -0.0043

Bottom:
-0.0111 → -0.0087 → -0.0126
~~~

这允许一个非常具体的 working test：

~~~text
Employer-quality recovery speed
↔
Earnings recovery speed
~~~

排序在当前三个 skill groups 中是一致的：

~~~text
Top    fastest
Middle intermediate
Bottom slowest / no clear employer-quality recovery
~~~

这不是 causal mediation estimate。

但它是：

~~~text
within-study mechanism alignment
~~~

比跨国相关性更强。

---

## 6. Japan：为什么 younger cohort 不是简单的“制度突然变好了”

Kondo 2024 对 weakening scars 提出若干可能机制，其中最接近 R3 的是：

~~~text
job mobility increased
+
lifetime-employment structure eroded
+
some employers allowed graduates 1–3 years out
to apply to new-graduate openings
~~~

这意味着：

~~~text
Entry Gate
可能变宽

+
Time Window
可能延长

+
Mobility
可能增加
~~~

三个 component 同时变化。

但 Kondo 明确指出这些只是 potential factors，不能把 weakening scar 单独因果归于 mobility。

另外：

~~~text
post-ice-age cohort aggregate outcomes
并没有明显恢复到 bubble cohorts
~~~

所以：

> **Scar coefficient weakening ≠ younger cohort 整体 career outcome 恢复。**

可能同时存在：

~~~text
cyclical entry sensitivity ↓
but
structural youth-labor-market level ↓
~~~

这是 Project 01 必须保留的重要 distinction。

---

## 7. Canada × Japan：第一轮可检验映射

| Component | Canada | Japan | 当前证据状态 |
|---|---|---|---|
| Entry Gate | 非核心识别对象 | fresh-graduate market / first regular job 很重要 | Japan direct/proxy |
| Offer Access | employer upgrading 可直接观察 | second-new-graduate opening 是候选机制 | Canada direct；Japan proxy |
| Mobility | early-career job mobility 与 upgrading 同期 | younger cohorts quitting / mobility 上升 | 两国均有 evidence，但非完整 mediation |
| Portability | skill quintile recovery 差异很大 | education-group differences 存在 | proxy |
| Time Dependence | upgrading 集中在早期 | graduation window / 1–3 year extension | mechanism evidence |
| Earnings decay | skill-specific 可量化 | older vs younger cohort effect 改变 | direct |
| Employer-quality decay | 可量化 | 当前主表未直接给出同构 outcome | asymmetric evidence |

这张表的作用不是说：

~~~text
Canada flexible
Japan rigid
~~~

而是明确：

~~~text
哪一个 mechanism 在哪一篇论文里真的被观察到了。
~~~

---

## 8. Phase II-2 hypotheses

### H2a｜Employer-upgrading alignment

~~~text
Employer-quality recovery faster
→ Earnings recovery faster
~~~

当前 Canada evidence：

~~~text
consistent
~~~

但尚未构成 mediation proof。

### H2b｜Window extension

~~~text
Fresh-graduate eligibility window ↑
→ initial-state dependence ↓
~~~

Japan 的 second-new-graduate practice 是候选 evidence。

需要后续寻找：

~~~text
policy / employer practice timing
+
transition outcome
~~~

来验证。

### H2c｜Mobility without better matches is insufficient

~~~text
Job switching ↑
but employer quality does not improve
→ scar need not decay
~~~

因此未来不能把：

~~~text
switching rate
~~~

单独当作 re-matching capacity。

### H2d｜Re-matching is worker-specific

~~~text
same institution
+
same macro treatment
+
different worker type
→ different offer / upgrade path
→ different persistence
~~~

Canada 当前最支持这一点。

---

## 9. Falsifiers

R3 的 re-matching interpretation 会被削弱，如果：

1. Canada employer-quality recovery 与 earnings recovery 在更细 event-time 数据中并不同步；
2. skill groups 的 persistence 差异主要由不同 initial shock exposure，而非后续 transition 解释；
3. Japan mobility 增加发生在 scar weakening 之后，时间顺序不支持 mechanism；
4. second-new-graduate access 扩大但 regular-employment state dependence 没有变化；
5. Netherlands 的 mobility mechanism 在 full text 中无法支持 published summary 的解释。

---

## 10. 下一步数据结构

新增一个独立 mechanism dataset，而不是污染 effect curve：

~~~text
mechanism_observations.csv
~~~

每行记录：

~~~text
study_id
country
sample_group
mechanism_component
proxy_name
event_time
estimate
unit
direction
evidence_type
source
verification
notes
~~~

只有论文直接给出 quantitative observation 时才填 estimate。

定性机制只记录：

~~~text
evidence_type = qualitative_author_interpretation
~~~

不伪造数字。

---

## 11. 当前结论

Project 01 现在从：

~~~text
How long is the scar?
~~~

进入：

~~~text
What transition makes the scar decay?
~~~

而 R3 最有希望被真正 operationalize 的对象不是：

~~~text
country flexibility
~~~

而是：

> **从 bad initial state 到 better match 的 transition process。**
