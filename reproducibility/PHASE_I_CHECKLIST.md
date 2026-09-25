# Phase I Closure Checklist

> Phase I 的目标不是“研究完成”，而是让 framework 从可读笔记变成可审计研究仓库。

## A. Theory Freeze

- [x] Canonical Model V2
- [x] 六条 Candidate Regularities V2
- [x] Counterexample Audit
- [x] False Friends
- [x] 不再因“案例有趣”自动新增 core regularity

## B. Foundations

- [x] Life Course Theory
- [x] Experience Effects
- [x] APC identification
- [x] Real Options
- [x] Hysteresis / Path Dependence
- [x] Foundations 第一阶段冻结

## C. Evidence Engineering

- [x] Evidence Ledger
- [x] Counterevidence Ledger
- [x] C001–C050 Claims Ledger
- [x] Source Verification Protocol
- [x] Verification Levels
- [x] P0 registry machine-readable
- [x] P0 first-pass source verification
- [x] C014 design-level verification
- [x] C020 design-level verification
- [x] C025 design-level verification

## D. Negative Cases

- [x] recession scars fade
- [x] slow stock can be bypassed
- [x] leverage amplification weak / delayed under protected contracts
- [x] optionality with high exercise cost

## E. Reproducibility

- [x] data/ layer
- [x] C009 raw + derived values
- [x] C009 verification script
- [x] P0 registry audit script
- [ ] convert more numeric claims to data artifacts where licensing permits
- [ ] optional CI job after local scripts stabilize

## F. Documentation

- [x] README slimmed
- [x] canonical reading path
- [x] Phase I Freeze documented
- [x] foundations / methods / evidence / synthesis / negative-cases indexes

## Phase I Exit Condition

Phase I 可以正式封板，当且仅当：

```text
1. ~~三个 P0 causal / empirical claims 达到 L2~~ ✅
2. ~~两个待补 negative cases 完成~~ ✅
3. 所有 repository reproducibility checks 在 CI 中通过；
4. README 与 Canonical Model 不再存在 V1/V2 术语冲突。
```

之后进入 Phase II：

```text
Empirical Projects
```

而不是继续扩展世界观。
