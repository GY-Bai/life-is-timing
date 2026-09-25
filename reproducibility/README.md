# Reproducibility｜可复现层

Phase I 的最后阶段不再扩张理论，而是把核心 claim 变成：

```text
Claim ID
→ Source
→ Raw Input
→ Transformation
→ Check
```

## 当前可以直接验证的内容

### C009：中国住宅指数回撤

Raw / derived artifact：

```text
data/derived/china_house_price_drawdown.csv
```

运行：

```bash
python3 scripts/verify_derived_claims.py
```

脚本会：

1. 读取 C009 两个 raw observations；
2. 重新计算 drawdown；
3. 与 CSV 中保存的 derived value 比较；
4. 如果误差超过 tolerance，则退出非零状态。

## Metadata audit

运行：

```bash
python3 scripts/audit_claim_registry.py
```

检查：

- claim_id 是否重复；
- verification level 是否属于允许集合；
- URL 是否缺失；
- derived artifact 是否指向已登记路径格式。

## 当前目标

Phase I 不试图完整 replication 所有论文。

目标更窄：

> **README 和 cases 中出现的关键数字，至少可以被追踪、重算或定位到原始来源。**
