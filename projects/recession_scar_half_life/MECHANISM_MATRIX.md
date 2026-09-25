# Mechanism Matrix｜R3 Entry–Re-entry Hysteresis

> 目标：把“scar 持续多久”进一步拆成“为什么会持续 / 为什么会恢复”。

| Study | Initial damage | Re-matching / recovery channel | Persistence evidence | 主要边界 |
|---|---|---|---|---|
| Japan — Kondo | entry unemployment → employment / earnings scar in older cohorts | regular-track re-entry / labor-market transition | older cohorts persistent；younger cohorts scar weakens / disappears | same-country regime changed |
| US — Kahn | bad graduation unemployment → wage / occupation penalty | no single direct re-match channel isolated | national estimates show long right tail；specification highly sensitive | national/state + OLS/IV identify different variation |
| Canada — OVH | lower earnings + lower-quality initial employer | job mobility + employer upgrading + within-firm recovery | full sample halves ≈4.39y；bottom skill >9.5y | worker type strongly changes access to recovery |
| Netherlands — van den Berge | wage loss + mismatch | job / sector mobility to better-paying employers | academic fades ≈6y；vocational still ≈1% at 8y | exact annual curve not publicly extracted |
| Finland — Päällysaho | earnings / unemployment scar | mechanism less directly isolated | all-cohort half-life 9y；1996–2004 ≈3.26y | cohort window changes identifying variation |

## 1. 当前最强的 R3 mechanism evidence 来自哪里

目前最干净的不是跨国差异，而是 **Canada 的 within-study heterogeneity**。

同一篇论文、同一种 regional unemployment exposure：

~~~text
Top skill:
earnings half-life ≈ 3.30y

Middle:
≈ 4.97y

Bottom:
> 9.5y
~~~

同时 employer-quality path：

~~~text
Top:
-0.0082 → -0.0004 → +0.0010

Bottom:
-0.0111 → -0.0087 → -0.0126
~~~

所以：

> **R3 的关键不是抽象的“能不能换工作”，而是 shock 后还能不能获得更好的 match。**

---

## 2. Re-entry 应该拆成五个可观察组件

Project 01 暂时把：

~~~text
Re-entry Capacity
~~~

拆成：

~~~text
1. Entry Gate
2. Offer Arrival / Employer Access
3. Search & Mobility Cost
4. Skill / Credential Portability
5. Time Dependence
~~~

### Entry Gate

第一次进入 core track 的门有多窄。

Japan 是典型候选。

### Offer Arrival / Employer Access

worker 之后能否获得更好 employer 的 offer。

Canada 的 skill heterogeneity 最接近这一层。

### Search & Mobility Cost

搬家、换行业、换雇主的成本是否随：

~~~text
age
tenure
family formation
specific human capital
~~~

上升。

### Skill / Credential Portability

同样的 worker quality 能不能被下一个 employer 看见和定价。

### Time Dependence

如果 re-match 机会随着年龄下降：

~~~text
delay itself
~~~

会把 temporary shock 变成 state dependence。

---

## 3. 当前 working equation

Canonical R3 仍然不改。

Project 01 的 operational version：

~~~text
Scar Persistence
=
f(
Initial Shock,
Initial Match Quality,
Offer Arrival,
Mobility Cost,
Skill Portability,
State Dependence,
Time to Re-match
)
~~~

Institution 进入每一项，而不是单独作为：

~~~text
Country Dummy
~~~

存在。

---

## 4. 当前最重要的 falsifier

如果后续数据发现：

~~~text
better employer access / higher mobility
~~~

并没有对应：

~~~text
faster earnings / match recovery
~~~

那么 Canada-based re-matching interpretation 就需要收缩。

同样，如果 Japan 后续 cohort 的 scar 消失主要来自：

~~~text
measurement / composition
~~~

而不是 transition structure 变化，

也不能用它支持：

~~~text
institution evolved
~~~

的故事。

---

## 5. 当前 Phase II 判断

第一轮 evidence 更支持：

~~~text
Bad Entry
× Unequal Re-matching Access
→ Heterogeneous Persistence
~~~

而不是：

~~~text
Bad Country
→ Long Scar
~~~

这使 R3 从国家标签向 transition mechanism 前进了一步。
