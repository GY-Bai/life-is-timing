# Life Is Timing

> **当你没见到“Matrix”的全貌时，你会以为“Matrix”不存在；当你被周期拷打过时，你就会敬畏周期的力量。**

这个仓库研究一个简单但经常被忽略的问题：

> **同一个人生选择，发生在不同的历史位置，就不再是同一个选择。**

22 岁毕业遇到扩张期，与 22 岁毕业遇到就业冰河期，不是同一种“22 岁”。

28 岁第一次买房发生在低估值、信用扩张和城市化早期，与发生在高估值、高杠杆和信用收缩的转折附近，也不是同一种“28 岁”。

因此这里的 **timing** 不是精准抄底逃顶，而是：

```text
Life Stage
× Historical Regime
× Irreversibility
× Optionality
```

---

## Matrix 是什么

这里的 **Matrix** 只是一个比喻。

它不是指隐藏组织，也不是指有人在后台操纵人生。

它指的是：

> **个人看到的世界，通常只是自己出生年份、家庭、城市、行业和过去几十年经历形成的一条局部 sample path。**

问题在于，人很容易把：

```text
“I experienced X”
```

压缩成：

```text
“The world works like X”
```

所以这个项目既研究现实中的周期，也研究：

```text
Experience
→ Belief
→ Decision
```

为什么会把上一代的成功经验、自己的创伤经验或某一轮资产周期错误外推成普遍规律。

---

## Canonical Model V2

第一阶段的 canonical model 已冻结在：

[CANONICAL_MODEL.md](CANONICAL_MODEL.md)

当前统一分解为：

```text
Shock
  ↓
Available Adjustment Margin
  ↓
Binding Non-substitutable Stock
  ↓
Timing / Life-stage Exposure
  ↓
State-Contingent Amplification
  ↓
Exercisable Optionality
  ↓
Long-run Path
```

它不是一个命运公式，也不是一个可以直接估计的统一结构方程。

它是一个 **constraint map**，用来问：

```text
什么东西最先能动？
什么东西真正绑定而且最难重建？
谁恰好在那个窗口暴露？
杠杆或合同怎样放大 shock？
shock 后还剩多少真正能执行的选择？
过去经验是否已经不适用于当前 regime？
```

---

## 六条 Candidate Regularities V2

目前 14 个历史与现实 case 横向比较后，保留六条条件规律：

```text
R1  Available-Margin Principle
R2  Binding-Stock Principle
R3  Entry–Re-entry Hysteresis
R4  State-Contingent Leverage Amplification
R5  Exercisable Optionality
R6  Locally Adaptive, Globally Incomplete Experience
```

它们不是自然科学“定律”。

详细版本：

- [Cross-Case Mechanism Matrix](synthesis/01_cross_case_mechanism_matrix.md)
- [Candidate Regularities V2](synthesis/06_candidate_regularities_v2.md)
- [Counterexample Audit](synthesis/05_counterexample_audit.md)
- [Testable Predictions](synthesis/04_testable_predictions.md)
- [False Friends](synthesis/03_false_friends.md)

最重要的方法变化是：

```text
从：
“这个案例能不能被我们的框架解释？”

转向：
“什么数据最容易让这个框架失败？”
```

---

## 三个最初的问题

这个 repo 最早来自三条主线。

### 1. 就业冰河期

为什么：

```text
Bad Graduation Timing
```

可能通过：

```text
First Job
→ OJT
→ Employer Signal
→ Re-entry Friction
```

留下多年 scar？

但又为什么日本、美国、荷兰、芬兰的 persistence 并不一样？

见：

[就业冰河期](docs/01_employment_ice_age.md)

### 2. 危机以后为什么不是一起恢复

为什么常见：

```text
financial conditions / prices
→ profits / flows
→ hiring
→ wages
→ household balance sheets
→ cohort paths
```

存在明显 Jet Lag？

而为什么这条顺序又不是每次 crisis 都机械相同？

见：

[Jet Lag 与多层次复苏](docs/02_crisis_recovery_jet_lag.md)

### 3. 年轻人怎样降低 bad timing 的长期伤害

不是预测顶部底部，而是：

```text
Avoid Catastrophic Timing
+
Preserve Exercisable Optionality
```

见：

[年轻人的破局框架](docs/03_youth_breakout_playbook.md)

---

## 从哪里开始读

如果第一次进入这个 repo，推荐顺序：

```text
1. CANONICAL_MODEL.md
2. foundations/
3. synthesis/06_candidate_regularities_v2.md
4. cases/README.md
5. evidence/README.md
6. methods/
```

其中：

- [Foundations](foundations/README.md)：学术母体；
- [Cases](cases/README.md)：14 个文献化案例；
- [Synthesis](synthesis/README.md)：跨案例比较与反例审计；
- [Evidence](evidence/README.md)：claim、证据、反证和 source verification；
- [Methods](methods/README.md)：identification 与 red-team 规则；
- [Negative Cases](negative_cases/README.md)：专门寻找 timing 作用弱、scar 衰减或 slow stock 被绕过的案例；
- [Research Status](RESEARCH_STATUS.md)：哪些是 evidence、synthesis、hypothesis。

---

## 研究纪律

这个仓库不试图证明：

```text
出生年份决定命运
周期可以稳定预测
年轻人应该永远等待
高杠杆一定失败
underinvestment 一定制造牛市
AI 一定摧毁 junior pipeline
```

相反，每条重要命题都要求区分：

```text
Observation
Association
Causal Evidence
Model Result
Synthesis
Hypothesis
Boundary
Counterevidence
```

现在已经建立：

- [Claims Ledger](evidence/CLAIMS_LEDGER.md)：C001–C050 claim-level 台账；
- [Evidence Ledger](evidence/EVIDENCE_LEDGER.md)；
- [Counterevidence Ledger](evidence/COUNTEREVIDENCE_LEDGER.md)；
- [Source Verification Protocol](evidence/SOURCE_VERIFICATION_PROTOCOL.md)；
- [P0 Verified Claims](evidence/P0_VERIFIED_CLAIMS.md)；
- [Identification Guide](methods/IDENTIFICATION_GUIDE.md)；
- [Red Team Protocol](methods/RED_TEAM_PROTOCOL.md)。

原则只有一句：

> **先找 identification，再找故事；先找反例，再扩大理论。**

---

## Phase I Complete

第一阶段已于 **2026-09-25** 完成封板。核心理论不再继续无限扩张。

除非新材料能够：

```text
推翻
收缩
显著强化
或识别 R1–R6 的边界
```

否则不再增加新的核心 regularity。

新增案例也不以“数量更多”为目标。

下一阶段重点是：

```text
Claim Audit
→ Source Verification
→ Negative Cases
→ Reproducibility
```

其中前三步已经开始执行：

- 已建立 C001–C050 [Claims Ledger](evidence/CLAIMS_LEDGER.md)；
- 第一批 P0 定量与强断言已完成 [source verification](evidence/P0_VERIFIED_CLAIMS.md)；
- 已建立 [Negative Cases](negative_cases/README.md)，主动寻找 timing 作用弱或机制被绕过的情形。

第一批 P0 定量 claim 已完成核验，其中 C014、C020、C025 已推进到 design-level；C025 还在审计中发现并修复了 working-paper → QJE final version 的数字漂移。

可复现层已经建立：

- [data/](data/README.md)
- [reproducibility/](reproducibility/README.md)
- [Phase I Closure Checklist](reproducibility/PHASE_I_CHECKLIST.md)

仓库也加入最小 CI 检查，用于验证 derived claim、P0 registry 与 canonical terminology。

---

## Phase II：Empirical Projects

下一阶段路线已经固定在：

[PHASE_II_ROADMAP.md](PHASE_II_ROADMAP.md)

项目入口：

[projects/README.md](projects/README.md)

Phase I 完成报告：

[reproducibility/PHASE_I_REPORT.md](reproducibility/PHASE_I_REPORT.md)

Phase II 的目标不再是“找到更多能解释的故事”，而是：

```text
Measure
Identify
Falsify
Revise
```

---

## 核心命题

> **人生有自己的时钟，经济也有自己的时钟。真正危险的不是无法预测周期，而是误以为这两只钟彼此无关。**

> **同一个人生选择，发生在不同的历史位置，就不再是同一个选择。**

> **不要把自己的出生年份，误认为经济规律。**

**Life is timing.**

不是因为 timing 能让人预测未来。

而是因为人生从来不是发生在历史之外。
