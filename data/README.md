# Data｜可复现数据层

这个目录只保存：

- 可以合法再分发的小型 raw inputs；
- 我们自己从公开数据推导出的 derived values；
- 对应 claim ID；
- 必要的 provenance。

不把第三方大型数据库整份复制进仓库。

## 当前内容

- [derived/china_house_price_drawdown.csv](derived/china_house_price_drawdown.csv)  
  C009 的两端 raw values 与 derived drawdown。

后续优先把：

```text
claim ID
source series
raw observation
formula
result
```

连接起来。

目标不是堆数据，而是让 README / cases 里的关键数字可以重新生成。


## Phase II project data

### Recession Scar Half-life

```text
data/projects/recession_scar_half_life/study_registry.csv
data/projects/recession_scar_half_life/effect_curve_template.csv
```

其中 registry 保存 source / sample / treatment / access regime；
effect curve 文件目前只是 extraction schema，不包含伪造或插值出来的论文系数。
