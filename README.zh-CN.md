# 你好，我是杨孟川 Harvey 👋

[English](README.md) · **中文**

衍生品交易员出身，后来做加密交易所的产品经理。职业生涯一直在跟复杂衍生品和交易打交道——互换、票据、期权、结构化产品的定价与交易，覆盖股票、利率与外汇；之后转到加密行业，做结构化产品、组合保证金、永续合约风控、预测市场，以及美股永续与 RWA 合约。

现在我在用 AI 把自己的交易想法做成真正能跑的工具。我不是科班工程师，写不了生产代码，靠指挥 coding agent 落地，下面这些项目都是这样做出来的。

🔗 [LinkedIn](https://www.linkedin.com/in/mengchuan-yang-43068768/) · 🐦 [X](https://x.com/imajuana) · 📕 [小红书](https://www.xiaohongshu.com/user/profile/64995a930000000011002c99) · ✉️ [ymcharvey@gmail.com](mailto:ymcharvey@gmail.com)

> 📈 **正在 Arcus 上实盘运行**
>
> [**arcus-v2-farmer**](https://github.com/realnaka/arcus-v2-farmer) —— 一条美元中性的记忆体篮子价差，赚的是**持仓时间（OI-time）**而不是成交量；配杠杆排班、止损阶梯、ADL 复位，以及支撑这套形状的研究和估分模型。
>
> **想照着跑？从这里开始 → [app.arcus.xyz/ref/SKHYGO](https://app.arcus.xyz/ref/SKHYGO)**（邀请链接，不影响你的费率）

---

## ⭐ 精选项目

用得最多的几个。

⚖️ [**onchain-arbitrage**](https://github.com/realnaka/onchain-arbitrage) - 我自己实盘在用的那套引擎：链上股票代币 × 永续合约，两腿都按真实成交均价定价，坏报价一律拒绝成交

📈 [**arcus-v2-farmer**](https://github.com/realnaka/arcus-v2-farmer) - 在 Arcus 上跑真钱的那个：赚**持仓时间**而不是成交量的美元中性篮子，含风控护栏、研究与估分模型

🌀 [**alphaloop**](https://github.com/realnaka/alphaloop)（<!--stars:alphaloop-->20<!--/stars--> stars）- 人机投研闭环：人出方向，agent 负责找证据、筛标的、记账本，最后拍板的仍然是人

📚 [**OpenOrder**](https://github.com/realnaka/OpenOrder) - 把每一次 agent 对话变成永久沉淀、跨 session 复利的投研 Wiki，灵感来自 Karpathy 的 LLM Wiki

🔌 [**trading-agent-mcp**](https://github.com/realnaka/trading-agent-mcp) - 多市场金融研究的 MCP Server：在 IDE 里跑多空辩论，零 LLM 调用成本

✅ [**claim-verification**](https://github.com/realnaka/claim-verification) - 把推文、新闻、研报、其他 AI 的结论拆成原子声明，逐条回到一手源验证，再打标签

🌐 [**stock-data-fetch**](https://github.com/realnaka/stock-data-fetch) - 多市场行情 skill，美股 / A 股 / 港股 / 加密 / 商品全覆盖，多数据源自动切换

📡 [**crypto-social-radar**](https://github.com/realnaka/crypto-social-radar) - 任意代币的三轨热度雷达（X + 新闻 + 币安期货），每天自动推送到飞书

---

## 🧠 投研与交易 Agent

用机器做投研，而不是守在机器前面。

🌀 [**alphaloop**](https://github.com/realnaka/alphaloop) - 方向由人给，查证 / 选股 / 记账交给 agent，决策权始终在人这边

📚 [**OpenOrder**](https://github.com/realnaka/OpenOrder) - 一个任何 agent 都能读写的投研 Wiki，让结论和踩过的坑跨 session 累积，而不是每次从零开始

✅ [**claim-verification**](https://github.com/realnaka/claim-verification) - 把推文、新闻、研报、其他 AI 的结论拆成原子声明，逐条回到一手源验证，再打标签

🌐 [**stock-data-fetch**](https://github.com/realnaka/stock-data-fetch) - 一套接口打通所有市场，多源兜底，在受限网络里也能稳定取数

🔌 [**trading-agent-mcp**](https://github.com/realnaka/trading-agent-mcp) - 多市场金融研究的 MCP Server：在 IDE 里跑多空辩论，零 LLM 调用成本

📡 [**crypto-research-radar**](https://github.com/realnaka/crypto-research-radar) - 加密行业日报调研：Perp DEX、交易所、预测市场、AI × Crypto、DeFi

🧊 [**trading-discipline-coach**](https://github.com/realnaka/trading-discipline-coach) - 一个会拒绝你的 AI 交易教练，给 Cursor 用的交易纪律 skill

---

## 📡 监控与自动化

所有会自己醒来、自己汇报的东西。

📡 [**crypto-social-radar**](https://github.com/realnaka/crypto-social-radar) - 代币三轨热度雷达：X + 新闻 + 币安期货，每天推飞书

🛰️ [**hk-ipo-radar**](https://github.com/realnaka/hk-ipo-radar) - 港股 IPO 自动扫描 + 8 维 AI 深度分析，推送到飞书群并附云文档链接

🛡️ [**edgex-risk-monitor**](https://github.com/realnaka/edgex-risk-monitor) - EdgeX 永续合约行情监控，异常经飞书 webhook 告警

🐋 [**edgex-flow-monitor**](https://github.com/realnaka/edgex-flow-monitor) - 链上资金流监控：L2 鲸鱼成交与 L1 提现

💧 [**edge-lp-monitor**](https://github.com/realnaka/edge-lp-monitor) - Uniswap V3（Arbitrum）与 PancakeSwap V4（BSC）的 LP 仓位监控，每 8 小时告警

📊 [**liquidity-depth-comparison**](https://github.com/realnaka/liquidity-depth-comparison) - 跨交易所合约深度对标看板：10+ 交易所实时盘口深度，快照同步到飞书多维表格

📝 [**captain-trading-booking**](https://github.com/realnaka/captain-trading-booking) - 把交易截图或粘贴文字变成飞书多维表格 / Excel 里的结构化记录

🎯 [**okr-agent-skill**](https://github.com/realnaka/okr-agent-skill) - 把季度目标拆成 agent 能直接执行的任务

---

## 🛠️ 交易所工具链

在 EdgeX 期间做的工具，现在以开源方式维护。

🖥️ [**edgex-cli**](https://github.com/realnaka/edgex-cli) - EdgeX 永续与美股合约的 CLI，为 agent 消费而设计

🔌 [**edgex-mcp**](https://github.com/realnaka/edgex-mcp) - EdgeX 合约交易的 MCP Server：行情、账户、下单都变成 agent 工具

---

## 🎬 内容与效率

把长内容和想法变成真正用得上、发得出去的形态。

🎬 [**md-to-bilibili**](https://github.com/realnaka/md-to-bilibili) - Markdown 进去，B 站视频出来：AI 配音、AI 配图、中文字幕，并自动投稿

📖 [**youtube-to-markdown**](https://github.com/realnaka/youtube-to-markdown) - 把 YouTube 视频变成通顺、带翻译的 Markdown 文稿，人工字幕、自动字幕或 Whisper 都能处理

🎨 [**frontend-slides-to-pdf**](https://github.com/realnaka/frontend-slides-to-pdf)（fork）- 把前端原生 HTML 幻灯片转成稳定的高分辨率 PDF 与长图
