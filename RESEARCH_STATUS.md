# Research Status｜研究状态与证据分层

这个仓库同时包含三种不同性质的内容：

```text
A. 已有成熟文献支持的机制
B. 跨文献整合后的框架
C. 仍待验证的原创假设 / 类比
```

为避免把“合理解释”写成“已经证明”，后续文档统一按这个标准处理。

## A｜已有成熟文献传统支撑

目前优先归入这一层的主题包括：

- Life Course Theory；
- Age–Period–Cohort；
- recession scarring；
- experience effects；
- insider–outsider / labor-market segmentation；
- employer re-matching；
- real options；
- market liquidity / funding liquidity；
- household balance-sheet repair；
- private credit / illiquidity transmission；
- human capital accumulation。

这类内容后续目标是：

```text
补原始论文
→ 补数据
→ 标清国家 / 样本 / 年代
→ 区分 correlation 与 causality
```

## B｜跨领域整合后的框架

这些概念通常不是单篇论文直接提出，而是本仓库把多个成熟研究传统拼在一起：

- Jet Lag；
- Life Clock × Historical Clock；
- Historical Optionality；
- Adjustment Margin；
- Career as Asset；
- Human Capital Portfolio；
- Customer Beta；
- Slow Stock / Fast Variable；
- Cohort × Life Stage × Regime。

这类内容应明确标注为：

```text
Synthesis / Framework
```

而不是伪装成“学界已有统一理论”。

## C｜待验证假设

目前需要特别谨慎的内容：

- Human-capital Cannibalization；
- AI 导致 junior-to-senior pipeline 断裂；
- Intergenerational Timing Sandwich；
- Revenge of Underinvestment 向人力资本的映射；
- 某些行业是否会因长期 junior hiring 不足出现未来 scarcity rent；
- local business 的 customer beta 是否能稳定估计；
- cohort scar 是否系统性转化为 housing / wealth scar。

这些概念可以保留，因为它们具有解释力和可检验性。

但必须写成：

```text
Hypothesis
Research Question
Mechanism Candidate
```

不能写成已被证明的事实。

## D｜候选跨领域规律

在当前 14 个案例的横向比较中，六条机制被暂时提升为 candidate regularities：

- Fastest Adjustable Margin；
- Slow Stock Persistence；
- Entry × Re-entry；
- Leverage Nonlinearity；
- Optionality Buffers Scarring；
- Experience ≠ Historical Distribution。

它们仍然属于：

```text
Cross-case Synthesis
```

而不是“已经存在统一因果识别的自然定律”。

升级标准是：

```text
跨案例重复出现
+
有直接机制证据
+
有明确反例
+
能提出 falsifiable prediction
```

详见 [synthesis/](synthesis/)。

反例审计后，推荐使用 V2 表述：

```text
R1 Available-Margin
R2 Binding Non-substitutable Stock
R3 Entry–Re-entry Hysteresis
R4 State-Contingent Leverage
R5 Exercisable Optionality
R6 Locally Adaptive, Globally Incomplete Experience
```

原 V1 保留用于记录理论演化，不删除历史版本。

反例与失效边界统一记录在：

- [Counterexample Audit](synthesis/05_counterexample_audit.md)
- [Counterevidence Ledger](evidence/COUNTEREVIDENCE_LEDGER.md)
- [Red Team Protocol](methods/RED_TEAM_PROTOCOL.md)

## 未来每篇文档的建议模板

### 1. 命题

我们要解释什么？

### 2. 机制

为什么可能发生？

### 3. 已有证据

哪些论文 / 数据直接支持？

### 4. 反例

哪些国家、时期或群体不成立？

### 5. 边界条件

在什么条件下机制会失效？

### 6. 待验证

还缺什么数据？

### 7. 与 Life Is Timing 的关系

这个案例如何进入：

```text
Shock
→ Adjustment Margin
→ Stock
→ Life Stage
→ Optionality
```

## 核心纪律

> **先区分“我们看到了什么”“论文证明了什么”“我们推断了什么”。**

这个仓库的目标不是制造一个万能故事。

而是不断尝试：

```text
提出机制
→ 找反例
→ 找边界
→ 找数据
→ 修正模型
```

如果一个概念无法被反驳，它就不是一个有用的研究框架。


## Phase I Complete

第一阶段已于 **2026-09-25** 完成并封板。理论扩张保持冻结。

Canonical version：

- [CANONICAL_MODEL.md](CANONICAL_MODEL.md)
- [Candidate Regularities V2](synthesis/06_candidate_regularities_v2.md)

当前优先级不再是增加案例数量，而是：

```text
Claim-level audit
→ Primary-source verification
→ Negative-case search
→ Reproducibility
```

已建立：

- [Claims Ledger](evidence/CLAIMS_LEDGER.md)
- [Source Verification Protocol](evidence/SOURCE_VERIFICATION_PROTOCOL.md)
- [P0 Verified Claims](evidence/P0_VERIFIED_CLAIMS.md)
- [Counterevidence Ledger](evidence/COUNTEREVIDENCE_LEDGER.md)
- [Negative Cases](negative_cases/README.md)
- [Data layer](data/README.md)

### Freeze Rule

除非新材料能够：

```text
推翻
收缩
显著强化
或识别 R1–R6 的边界
```

否则不再进入核心 framework。

这意味着：

```text
more examples
```

本身不再构成新增核心 case 的理由。


## Phase II

Phase II 不再以：

```text
增加概念 / 增加案例数量
```

作为产出。

进入：

```text
Empirical Projects
```

当前路线：

[PHASE_II_ROADMAP.md](PHASE_II_ROADMAP.md)

核心问题从：

```text
framework 能解释什么？
```

变成：

```text
哪些机制能被识别？
哪些会失败？
scar half-life 到底由什么决定？
```
