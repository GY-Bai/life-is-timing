# Case 03｜中国住房 Cohort：1970 vs 1993，不是同一个“28 岁买房”

> 研究状态：**B（跨数据整合）+ C（待做 cohort-level 因果验证）**

这个案例不是要证明：

```text
1970 cohort 一定赢
1993 cohort 一定输
```

而是用两个出生 cohort 展示：

> **同一个人生动作，发生在不同房地产与信用 regime 中，经济含义完全不同。**

---

## 1. 两个 cohort 的时间坐标

### 1970 cohort

25–28 岁：

```text
1995–1998
```

### 1993 cohort

25–28 岁：

```text
2018–2021
```

表面动作一样：

```text
工作
→ 结婚
→ 买第一套房
```

但 Historical Clock 完全不同。

---

## 2. 1970 cohort：住房制度 regime change

1998 年国务院发布国发〔1998〕23号，明确提出：

```text
停止住房实物分配
→ 逐步实行住房分配货币化
→ 发展住房金融
→ 培育住房交易市场
```

并规定：

```text
1998 年下半年开始停止住房实物分配
```

所以 1970 cohort 的 28 岁左右，恰好落在：

```text
福利住房 / 单位分配
→ 商品住房 / 按揭金融
```

的制度交界。

这本身就是巨大的 regime shift。

---

## 3. 当时价格处于什么位置

国家统计局历史数据：

```text
1995 全国住宅平均销售价格：1509 元/㎡
1998 全国住宅平均销售价格：1854 元/㎡
```

这些数据不是 repeat-sales index，也不能拿来直接算某个家庭的投资收益。

它们的意义是：

> 说明这一 cohort 的首次置业窗口，处于中国住房商品化扩张的早期阶段。

---

## 4. 1993 cohort：进入的是成熟高价阶段

1993 cohort 在 25–28 岁时对应：

```text
2018–2021
```

2021 年全国住宅：

```text
销售面积：156,532 万㎡
销售额：162,730 亿元
```

按成交额 / 面积粗算，全国成交均价约：

```text
10,396 元/㎡
```

必须强调：

```text
10,396 vs 1,854
```

不能直接解释成同一套住房涨了 5.6 倍。

原因包括：

- 城市化；
- 样本结构；
- 新房品质；
- 地区权重；
- 商品房覆盖；
- 名义价格；
- 统计口径变化。

它只能用来说明：

```text
首次置业面对的名义资产价格环境
```

已经完全不同。

---

## 5. 2021 之后发生了什么

BIS / FRED 中国住宅价格指数显示：

```text
2018Q1：125.8764
2021Q3：145.9129
2026Q1：113.9785
```

从 2021Q3 高点到 2026Q1：

```text
名义指数约 -21.9%
```

实际住宅价格指数同期从：

```text
112.9908
→ 85.1336
```

约为：

```text
-24.7%
```

需要注意一个口径边界：

BIS 该名义序列说明：

```text
2007Q1–2015Q4：70 城新建住房
2016Q1 起：70 城 existing buildings
```

因此不能把 2005–2026 全序列当成完全一致口径的 repeat-sales history。

但 2018–2026 段内部可以用于观察本轮 turning point。

---

## 6. 为什么住房 timing 对中国家庭尤其重要

研究显示，中国住房在家庭财富中占据极高比重。

Rogoff 与 Yang 2026 年的研究总结称：

```text
housing ≈ nearly 70% of household wealth
```

这意味着：

```text
Housing Timing
```

不只是一个消费选择。

它同时决定：

- household leverage；
- wealth concentration；
- collateral；
- consumption capacity；
- geographic lock-in；
- future optionality。

---

## 7. 但“1993 cohort 大概率负资产”不能直接推出

这是这个案例最重要的纪律之一。

即使全国住宅指数从高点下跌约 22%，也不能直接说：

```text
1993 cohort 多数家庭 equity < 0
```

因为还需要知道：

- 首付比例；
- 城市实际跌幅；
- mortgage vintage；
- 已偿还本金；
- 是否有第二套房；
- 其他金融资产；
- 家庭支持；
- 是否早于 2021 买入。

Fang 等对 2003–2013 mortgage borrowers 的研究发现，很多购房者的首付比例高，常见超过 35%。

所以：

```text
House-price Drawdown
≠ Automatically Negative Equity
```

真正要研究的是：

```text
Purchase Vintage
× City
× LTV
× Income Path
× Price Drawdown
```

---

## 8. 杠杆为什么把 timing 放大

假设：

```text
房价 = 100
首付 = 20
贷款 = 80
```

如果房价跌 22%，暂时忽略本金偿还：

```text
房价 = 78
净值 = -2
```

如果首付 30：

```text
贷款 = 70
房价 = 78
净值 = 8
```

虽然房价只跌 22%，但原本 30 的 equity 只剩 8。

所以 housing timing 的非线性来自：

```text
Leverage
```

---

## 9. 两个 cohort 的 regime 对照

### 1970 cohort

```text
Age 25–28
→ Housing Commercialization Begins
→ Low Nominal Entry Price
→ Urbanization
→ Credit Expansion
→ Long Compounding Window
```

### 1993 cohort

```text
Age 25–28
→ Mature Housing Boom
→ High Nominal Entry Price
→ Mortgage Expansion
→ 2021 Turning Point
→ Deleveraging / Price Correction
```

所以：

```text
“28 岁买第一套房”
```

根本不是一个稳定策略变量。

真正的变量是：

```text
Buy House @ Regime_t
```

---

## 10. 目前还缺什么证据

要把这个 thought experiment 升级为强实证，需要：

1. 按出生 cohort 的购房年龄分布；
2. mortgage origination vintage；
3. 城市级 price path；
4. initial LTV；
5. 提前还贷；
6. household income growth；
7. housing equity；
8. financial assets；
9. parental transfer；
10. household net worth。

最理想的研究是：

```text
同年龄
不同购房年份
不同城市 shock
→ 追踪十年以上 household balance sheet
```

---

## 11. 证据与来源

1. 国务院，**关于进一步深化城镇住房制度改革加快住房建设的通知（国发〔1998〕23号）**。  
   https://www.beijing.gov.cn/zhengce/zhengcefagui/qtwj/201309/t20130924_776668.html

2. 国家统计局，历史住宅平均销售价格：1995 年 1509 元/㎡，1998 年 1854 元/㎡。  
   https://www.stats.gov.cn/sj/ndsj/2005/html/F0638C.HTM

3. 国家统计局，**2021年全国房地产开发投资增长4.4%**，含住宅销售面积与销售额。  
   https://www.stats.gov.cn/sj/zxfb/202302/t20230203_1901340.html

4. BIS / FRED, **Residential Property Prices for China**。  
   https://fred.stlouisfed.org/series/QCNN628BIS

5. BIS / FRED, **Real Residential Property Prices for China**。  
   https://fred.stlouisfed.org/series/QCNR628BIS

6. Fang, Gu, Xiong & Zhou, **Demystifying the Chinese Housing Boom**, NBER / NBER Macroeconomics Annual.  
   https://www.nber.org/papers/w21112

7. Rogoff & Yang, **A Tale of Two Countries – The Real Estate Crises in 1990s Japan and Contemporary China**, NBER, 2026.  
   https://www.nber.org/papers/w35054

8. Chen, Wang, Xu & Zha, **Aggregate and Distributional Impacts of LTV Policy in China**, NBER.  
   https://www.nber.org/papers/w28092

9. Piketty, Yang & Zucman, **Capital Accumulation, Private Property and Rising Inequality in China, 1978–2015**, NBER.  
   https://www.nber.org/papers/w23368
