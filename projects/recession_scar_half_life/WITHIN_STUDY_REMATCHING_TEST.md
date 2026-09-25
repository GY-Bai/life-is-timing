# Within-study Re-matching Test｜Canada × Japan

> 状态：**Phase II-2 first mechanism test**  
> 目的：不再把 country 当解释变量，先测试同一研究内部的 transition evidence 是否与 scar decay 对齐。

## 1. Canada：earnings decay 与 employer-quality recovery 是否同向？

Oreopoulos–von Wachter–Heisz 2012 Table 2 同时报告：

~~~text
annual earnings
firm median log earnings
~~~

并按 predicted-earnings skill group 分组。

这给了一个罕见的 within-study test：

> **如果 employer upgrading 是 recovery channel，那么 employer-quality gap 缩得更快的组，earnings scar 是否也缩得更快？**

---

## 2. Full sample

### Earnings

~~~text
0–1    -0.0183
4–5    -0.0089
9–10   -0.0042
~~~

descriptive half-life：

~~~text
≈ 4.39y
~~~

### Employer quality

~~~text
0–1    -0.0096
4–5    -0.0042
9–10   -0.0028
~~~

descriptive half-life：

~~~text
≈ 4.06y
~~~

两条 path 的 first-half crossing 很接近。

这与：

~~~text
employer upgrading
是 earnings catch-up 的一个重要 channel
~~~

相容。

但不能写成：

~~~text
employer upgrading causally explains all wage recovery
~~~

因为同一论文还存在 within-firm recovery 等其他 adjustment margins。

---

## 3. Skill groups：更强的排序检验

### Top group

Earnings：

~~~text
-0.0147
→ -0.0042
→ -0.0024
~~~

Employer quality：

~~~text
-0.0082
→ -0.0004
→ +0.0010
~~~

表现：

~~~text
fast employer-quality closure
+
fast earnings decay
~~~

### Middle group

Earnings：

~~~text
-0.0232
→ -0.0124
→ -0.0039
~~~

Employer quality：

~~~text
-0.0128
→ -0.0050
→ -0.0043
~~~

表现：

~~~text
intermediate recovery
~~~

### Bottom group

Earnings：

~~~text
-0.0277
→ -0.0167
→ -0.0161
~~~

Employer quality：

~~~text
-0.0111
→ -0.0087
→ -0.0126
~~~

表现：

~~~text
persistent earnings scar
+
no monotone employer-quality recovery
~~~

因此三个组的 ordinal pattern 是：

~~~text
Top
> Middle
> Bottom
~~~

这里的 “>” 表示：

~~~text
faster / stronger re-matching recovery
~~~

不是能力价值判断。

---

## 4. 这比 cross-country comparison 强在哪里

如果比较：

~~~text
Canada vs Japan
~~~

同时改变：

~~~text
institution
sample
treatment
data
outcome
period
~~~

而 Canada skill groups 至少共同拥有：

~~~text
same administrative data system
same broad institution
same regional-unemployment treatment construction
same outcome definitions
same paper specification family
~~~

所以它更接近我们真正要找的：

~~~text
conditional recovery heterogeneity
~~~

虽然仍不是随机分配的 re-matching capacity。

---

## 5. Japan：一个不同类型的 within-country regime test

Kondo 2024 给出的关键事实不是：

~~~text
younger cohorts outcomes fully recovered
~~~

而是：

~~~text
entry unemployment coefficient
stops being statistically important
for younger cohorts
~~~

同时作者讨论：

~~~text
job mobility increased
lifetime employment eroded
second-new-graduate eligibility expanded
~~~

这些变化都可能降低：

~~~text
initial state dependence
~~~

但 aggregate cohort profiles 又显示：

~~~text
post-ice-age employment / income
did not clearly return to bubble-cohort level
~~~

于是出现一个非常重要的分解：

~~~text
Cyclical Entry Scar ↓
does not imply
Structural Youth Outcome Level ↑
~~~

---

## 6. 一个新的识别框架：Sensitivity vs Level

Japan 提醒我们必须把两个问题分开：

### Sensitivity

~~~text
β_entry
=
outcome 对 graduation labor-market condition 的敏感度
~~~

### Level

~~~text
E[Y | cohort, experience]
=
这一代年轻人的总体 employment / earnings level
~~~

可能发生：

~~~text
β_entry ↓
but
outcome level remains weak
~~~

如果长期结构变化让所有年轻人都面对更差的 labor-market environment：

~~~text
good-entry cohort
和
bad-entry cohort
之间差距会缩小
~~~

但这并不代表：

~~~text
所有人都恢复得更好
~~~

这可能是 Japan younger cohort 最重要的 interpretation boundary。

---

## 7. 对 R3 的修正不是“推翻”，而是限定作用域

R3 原本描述：

~~~text
Bad Entry
→ State Dependence
→ Persistent Scar
~~~

Phase II-2 后更准确的作用域是：

~~~text
R3 explains
cross-entry-condition persistence

not necessarily
the secular level of youth labor-market outcomes
~~~

也就是说：

~~~text
scar mechanism
~~~

与：

~~~text
structural cohort deterioration
~~~

可以同时存在，也可以一个减弱、另一个恶化。

---

## 8. 当前 working result

Canada 给出：

> **better-match access 与 earnings recovery 在 worker groups 中呈一致排序。**

Japan 给出：

> **更流动的 transition structure 可能削弱 entry-condition state dependence，但这不等于年轻 cohort 的总体结果恢复。**

合起来，R3 更像：

~~~text
Entry Shock
× Transition Matrix
→ Relative Scar

Structural Regime
→ Cohort Outcome Level
~~~

二者不能混成一个变量。

---

## 9. 下一步 falsification target

下一轮不需要立刻找更多国家。

优先找能够区分：

~~~text
mobility quantity
vs
mobility quality
~~~

的证据。

真正关键的变量不是：

~~~text
Did the worker switch?
~~~

而是：

~~~text
Did the switch move the worker to a better state?
~~~

这也是 Canada bottom group 最值得继续追的地方。
