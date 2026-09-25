# Data Access Audit｜Recession Scar Half-life

> 核验日期：2026-09-25

这个项目的最大现实约束不是 estimator，而是：

```text
四国原始 microdata 的 access regime 完全不同
```

因此 Phase II-1 采用：

```text
Literature Effect Extraction
→ US Open-data Replication
→ Restricted-data Extensions
```

而不是假装现在就能做一份统一四国 raw-data panel。

---

## United States｜最适合先做 open-data replication

Census Bureau 公开提供 CPS ASEC 年度 microdata；2026 页面直接提供：

- ASCII；
- CSV；
- SAS；
- data dictionary；
- replicate weights。

官方 CPS ASEC time-series 页面当前覆盖 1998–2026 下载页；Census microdata API 页面提供 1992–2026 ASEC API vintages。

因此 US pilot 可以优先做：

```text
public CPS / ASEC
+
public unemployment data
```

但必须注意：

> CPS 并不天然给出“实际大学毕业年月”，需要采用文献中的 potential-entry / education-based construction 或限定样本。

官方入口：

https://www.census.gov/data/datasets/time-series/demo/cps/cps-asec.html

API：

https://www.census.gov/data/developers/data-sets/census-microdata-api/cps-asec.html

---

## Japan｜有匿名 Labour Force Survey，但需要申请

日本统计局截至 2026-06-12 的匿名数据目录明确列出：

```text
Labour Force Survey
1989-01 through 2023-12
```

可以提供匿名数据，但需要满足法定利用条件并支付一定费用。

官方页面：

https://www.stat.go.jp/info/tokumei/index.html

Kondo 2024 同时使用：

- Labour Force Survey；
- Basic Survey of Wage Structure。

厚生劳动省也提供 custom tabulation / anonymized-data 制度；BSWS 的可用年次需要按实际申请目录进一步确认，不能假设历史全期都可匿名获取。

官方：

https://www.mhlw.go.jp/toukei/itaku/

因此 Japan replication 状态：

```text
technically feasible
but application-gated
```

---

## Netherlands｜CBS microdata restricted environment

Statistics Netherlands 明确要求：

```text
institution authorization
+
project application
+
CBS microdata environment
```

microdata 可链接到 individual / business / address，但只能在严格条件下研究。

官方：

https://www.cbs.nl/en-gb/our-services/customised-services-microdata/microdata-conducting-your-own-research/applying-for-access-to-microdata

所以 van den Berge 2018 的 matched administrative design：

```text
cannot be treated as an immediately downloadable replication dataset
```

Phase II-1 先做 paper-level extraction。

---

## Finland｜Statistics Finland FIONA

Statistics Finland 的 research microdata 多数通过：

```text
FIONA remote access
```

使用。

需要：

- user licence；
- project agreement；
- remote-access commitment；
- fee；
- disclosure / output checking。

官方：

https://stat.fi/en/services/services-for-researchers/research-datasets

https://stat.fi/en/services/services-for-researchers/instructions-for-researchers/using-the-datasets/fiona-remote-access-system

所以 Finland 同样先做：

```text
published-effect extraction
```

而不是 raw replication。

---

# Access tier

| Country | Immediate public microdata | Restricted research microdata | Phase II-1 role |
|---|---:|---:|---|
| US | Yes | Some linked admin data restricted | open-data replication candidate |
| Japan | Limited / application-based anonymized | Yes | literature extraction → application |
| Netherlands | No for target admin design | Yes, CBS environment | literature extraction |
| Finland | No for target admin design | Yes, FIONA | literature extraction |

---

# Consequence for interpretation

第一版跨国结果必须叫：

```text
harmonized literature synthesis
```

而不是：

```text
four-country replication study
```

只有当 treatment、sample、outcome 与 estimator 被真正重跑并尽可能统一之后，才可以升级措辞。
