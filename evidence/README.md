# Evidence｜证据与核验

这个目录回答的不是“我们的框架是什么”，而是：

> **哪些命题已经被核验？哪些只是 synthesis？哪些反例会迫使我们收缩理论？**

当前文件：

1. [Claims Ledger](CLAIMS_LEDGER.md)  
   核心命题的 claim-level 台账，使用稳定 ID（C001–）。

2. [Evidence Ledger](EVIDENCE_LEDGER.md)  
   按主题记录支持证据、状态与主要边界。

3. [Counterevidence Ledger](COUNTEREVIDENCE_LEDGER.md)  
   专门记录 null result、sign reversal、measurement dispute 与制度反例。

4. [Source Verification Protocol](SOURCE_VERIFICATION_PROTOCOL.md)  
   规定数字、因果措辞、版本与 derived value 的核验标准。

5. [P0 Verified Claims](P0_VERIFIED_CLAIMS.md)  
   第一批定量 / 强断言的逐条核验记录。

## 核心原则

```text
Document
→ Claim
→ Source
→ Exact location
→ Transformation
→ Counterevidence
```

任何核心数字都应最终能沿这条链条回到原始证据。
