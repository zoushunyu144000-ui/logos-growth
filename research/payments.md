# 跨境收款方案研究（中国护照 · 槟城 · 个人网页设计接单）

> 检索日期：2026-10-20。费率经常变动，下文每个数字都附来源；标"未核实"的表示没找到官方页面确认，或来源互相矛盾。**付款前请再看一次官方页面和你账户里显示的费用。** 本文不构成法律或税务意见。

## 0. 先确认一件事：你的 PayPal 注册在哪个国家？

- 判断方法：登录 PayPal → 设置/账户 → 查看"国家/地区"；或看你账户里的费用链接是 `paypal.com/c2`/`/cn`（中国）还是 `/my`（马来西亚）。国家在注册时就定下，一般不能直接改，要换只能关掉旧账户另开新账户（未核实，请问客服）。
- 你用中国身份证件完成了验证，所以**大概率是中国账户**。下面两种情况都写了，但推荐方案按中国账户来设计。

## 1. PayPal

| 项目 | 中国账户 | 马来西亚账户 |
|---|---|---|
| 能否收境外商业款 | 能。中国站费用页专门有一张"接收国际交易"的费率表 [1] | 能。马来西亚费用页同样列出国际收款费率 [3] |
| 收款费率 | **4.40% + 固定费**，收美元时固定费是 **0.30 USD** [1] | **4.40% + 固定费**（"all other markets"那一档）[3]；收美元的固定费是多少，搜索结果里没显示（**未核实**）|
| 货币转换 | 汇率里包含加价，官方页没给出具体百分比；第三方说约 3%–4% [2][4]（**未核实**）| 官方页写 **2.5%** [3]；但 WorldFirst 说 3.5% 起 [5]，两者矛盾 |
| 提现 | 电汇到大陆银行卡，**每笔 35 USD**，只能提美元，3–7 个工作日到账 [2]；中转行可能再扣 5–25 USD（来自论坛，**未核实**）[6] | 提到马来西亚银行账户（MYR）：满 RM400 免费，不满收 RM3，此外还有 2.5% 的转换费（来自 Wise 2026 年的文章，非官方）[7]。**问题是你没有马来西亚银行账户**，TNG 和 Merchantrade 都不能作为 PayPal 的提现账户（**未核实**）|
| 第三方提现 | 连连支付：最低 150 USD，收 1.2%，按当天汇率换成人民币打到你的卡，要求中国身份证与 PayPal 账户信息一致（来自个人博客，**未核实**）[4][8] | 不适用 |

- **一定要用商业付款（Goods & Services），不要用亲友付款（F&F）**：PayPal 官方说明，个人付款不享受买家保护 [9]；美国已经不允许向商家账户发起亲友付款 [10]。用 F&F 收生意款等于违反用户协议，还容易触发风控。直接发 PayPal 的 **Invoice（账单）或付款链接**，这样自动走商业费率，还会留下完整记录。
- **服务类交易的卖家保护很弱**：卖家保护主要针对实物商品。无形商品只有在 PayPal 把交易标记为符合条件，或书面通知你时，才能获得未授权交易方面的保护 [11]。也就是说，客户发起"未收到/与描述不符"或信用卡拒付时，你基本只能靠自己的证据（合同、验收邮件、交付记录）。
- **冻结/限额风险**：新账户突然收到大额款项，容易被暂扣或限制。"新卖家资金暂扣 21 天"这个说法我没找到官方依据（**未核实**）[11]。降低风险的做法：先收几笔小额定金；账单里写清服务内容；按时回应 PayPal 的资料要求。

## 2. Wise 个人账户

- **居住地验证（你卡住的就是这一步）**：如果你验证身份用的证件不是居住国签发的，Wise 会核查你在该国居住的权利。Wise 帮助中心明确写着**不接受短期、旅游和过境签证**，签证必须是 90 天以上的长期签证；不能提供合格文件的，账户功能会被限制 [12][13]。所以持短期多次入境签证，**很难通过 Wise 马来西亚的居住验证**。
- **个人账户不能做生意**：英国金融申诉专员（FOS）的裁决援引了 Wise 的 Acceptable Use Policy："个人账户不应用于商业目的"。裁决认定，自由职业者收客户款就算没有注册公司，也属于商业用途，并支持了 Wise 关户 [14][15]。Wise 的商业条款把 sole trader 和 freelancer 归为商业客户 [16]。**结论：不要用 Wise 个人账户收设计费。**
- **Wise Business**：你需要一个商业主体，而外国人通常没法在马来西亚 SSM 注册独资企业（一般只有公民或永久居民可以）[17]。所以目前大概率开不了（**未核实**）。
- **收款账户与费用（仅供参考）**：Wise 马来西亚页面列出可用的账户信息包括 AUD/CAD/EUR/GBP/HUF/MYR/NZD/PHP/SGD/USD [18]，但 2024 年论坛有人说美元账户信息需要有美国住址（**未核实**）[19]。美元 ACH 收款免费；美元电汇和 SWIFT 收款每笔 **6.11 USD** [20]。马来西亚地址的个人账户余额上限约 **20,000 MYR 等值** [18]。货币转换费率按线路不同，请用 Wise 的计算器查（**未核实**）[21]。
- **从 Wise 汇到中国**：可以汇到银联卡或支付宝。银联只能付给个人收款人，每个收款人每年最多 5 万美元，每天最多 5 笔，每月最多 20 笔；支付宝要求收款人是持中国身份证的大陆公民，并且有按用途划分的额度 [22][23]。

## 3. SWIFT 电汇直接到招商银行

- **招行收费**：招行官网写着"不收取任何入账手续费（国外中间行的扣费除外），部分分行会收取无兑换手续费"，入账后按原币种进入现汇账户 [24]。汇款人那边的银行手续费、中转行费用（常见 10–30 USD 左右，**未核实**）要在汇款时约定由谁承担。建议让客户选 **OUR**（全部费用由汇款人承担），或者把这部分成本算进报价。
- **收款信息**：问招行（95555 或 App 里"境外汇款汇入"）拿到 SWIFT 代码和英文户名、地址格式。**拼音户名必须和账户完全一致。**
- **申报**：2022 年的外汇局细则规定，居民个人单笔等值 1 万美元以下（含 1 万）的涉外收付款可以免申报 [25]；更早的版本门槛是 5,000 美元 [26]。超过门槛时，银行会通知你填写涉外收入申报单，交易性质选"服务贸易"之类的项目（具体编码请问银行）。
- **结汇额度**：个人结汇每人每年有等值 **5 万美元**的"年度便利化额度"，按自然年计算，年底清零 [27][28]。额度内凭身份证就能办；超过额度时，经常项目下要提供**真实性证明材料**（比如服务合同、发票、往来邮件）[29][30]。2020 年版的《经常项目业务指引》把 5 万美元定位为"便利化额度"，不是硬上限 [31]。**建议每个项目都保存合同、发票、交付确认邮件，单独建一个文件夹。**
- **不结汇也可以**：美元可以先留在现汇账户里，需要人民币时再分批结汇。

## 4. 其他渠道的可行性

| 渠道 | 结论 | 依据 |
|---|---|---|
| Payoneer | 你注册失败的常见原因：地址证明的姓名、地址、日期和注册时填的不一致（账单/银行流水限 6 个月内，税务文件限 12 个月内），以及"一人一户"限制。马来西亚短签没有当地地址证明，确实很难通过。可以试着用**中国地址**加中国的银行流水重新注册（**未核实**）| [32][33] |
| Airwallex | 马来西亚站只面向**在马来西亚注册的企业**（独资企业需要 SSM）→ 你不符合条件。中国站也是面向企业的，没找到个人开户的说明（**未核实**）| [34][35] |
| Revolut | 马来西亚居民目前不能开户，开户需要支持国家的住址 → 不可用 | [36] |
| Stripe 马来西亚 | 协议写明只限"位于马来西亚"的企业，含独资企业，注册时要提供营业或税务编号 → 你目前大概率开不了（**未核实**，请问 Stripe）| [37][17] |
| Lemon Squeezy / Paddle | **两家都不能用于服务收款**：Lemon Squeezy 明确禁止设计、网站开发和咨询服务；Paddle 说以人工服务为主的业务"不适合" | [38][39] |
| 连连 / PingPong / XTransfer | 主要面向电商和外贸企业。连连可以用来从**中国 PayPal 提现**（见第 1 节）；PingPong 对个人做服务收款的门槛说法不一，有论坛说需要企业资质和年费（**未核实**）；XTransfer 定位 B2B 企业，没找到个人开户信息 | [40][41][42] |
| Upwork / Contra | 托管付款（escrow）相当于平台替你担保。Upwork 提现到本地银行每笔 0.99 USD [43]；平台服务费 2025 年起改为浮动，具体数字以你账户页面显示为准（**未核实**）[44]。适合当获客渠道，但平台抽成高，而且要求后续交易继续在平台内完成 | [43][44] |

## 5. 签证 / 税务（只说大方向，务必咨询专业人士）

- **短期签证能不能远程为海外客户工作**：我没找到马来西亚移民局对"持社会访问准证（social visit pass）为境外客户远程工作"的明确官方说法 [45]，**未核实**。正规的路子是 **DE Rantau Nomad Pass**。
- **DE Rantau**（MDEC 官方 FAQ v10.0，2026-08-28）：科技/数字类人才年收入至少 **24,000 USD**，非科技类至少 60,000 USD。UX/UI 属于数字领域 [46]。除以色列公民外，所有国籍都可以申请；如果在马来西亚境内申请，获批后要先出境，再入境办签注 [46]。申请费各方说法不一（RM1,000 / RM1,080 等，**未核实**）[47]。第三方资料说要求有 3 个月以上的有效客户合同，不能接马来西亚本地客户 [47][45]。**注意：这个准证本身不是免税签证** [47]。
- **中国税务**：《个人所得税法实施条例》把"住所"定义为因户籍、家庭、经济利益关系而在中国境内习惯性居住 [48]。中国公民在国内有户籍的，通常仍被认定为居民个人，境外所得也要申报。居民个人取得境外所得，应在**次年 3 月 1 日至 6 月 30 日**申报，在境外缴的税可以在限额内抵免 [49]。具体按什么所得项目计税、能否抵免，请咨询税务师。

## 6. 推荐方案

### 排序
1. **主力：PayPal（中国账户）+ 发账单**。适合 AU/UK/US 客户，他们最习惯用卡或 PayPal 付款。余额留成美元，**攒到一定金额再一次性电汇到招行**，把每笔 35 USD 的固定费摊薄。
2. **主力（大单、企业客户）：SWIFT 美元直接汇到招行**，费用条款写 OUR。项目金额在 2,000 USD 以上时，按比例算明显比 PayPal 便宜。
3. **备用**：连连从 PayPal 提现（**未核实**，先小额测试）；Upwork/Contra 作为获客和托管渠道。
4. **不要用于收生意款**：Wise 个人账户（第 2 节）、PayPal F&F、Merchantrade、Touch 'n Go。
5. **之后再考虑**：拿到 DE Rantau 后，再重新评估马来西亚银行账户、Wise Business 和 Stripe 的可行性。

### 1,500 USD 项目费用估算（定金 50% + 尾款 50% = 两笔 750 USD）
| 路径 | 计算 | 到手约 |
|---|---|---|
| PayPal 中国 → 电汇招行 | 每笔 750×4.4%+0.30 = 33.30 USD，两笔共 66.60 → 余额 1,433.40；电汇扣 35 → **1,398.40 USD**，中转行可能再扣（**未核实**） | 约 93.2%（成本 ≈ 6.8%）|
| 同上，攒到 5,000 USD 再提现 | 35 USD 平摊到多个项目，单个项目实际分摊不到 10 USD | 约 95%（成本 ≈ 5%）|
| PayPal 中国 → 连连提现 | 1,433.40×1.2% ≈ 17.20 → ≈ 1,416 USD 等值的人民币（**未核实**） | 约 94.4% |
| SWIFT 直汇招行（OUR） | 招行不收入账费 [24]；客户那边的汇出费由客户承担 | 接近 100%，SHA 方式下中转行可能扣 10–30 USD（**未核实**）|
| （参考）PayPal 马来西亚 | 每笔 4.4%+固定费，再加 2.5% 转换成 MYR [3]，而且你没有马来西亚银行账户可以提现 | 不推荐 |

### 完整流程
1. **报价单/合同**写明：币种 **USD**；"Bank transfer (SWIFT, all fees paid by sender – OUR) or PayPal invoice"；"Payments via PayPal include a 4.5% processing adjustment"。直接加手续费附加费是否符合 PayPal 当地规定，我没查到（**未核实**），**更稳妥的做法是直接把 4–5% 的缓冲算进报价，不单独列出来**。另外写明：定金不退（工作开始后）；交付以书面验收为准。
2. **定金**：发 PayPal Invoice（或 SWIFT 账单），**收到款再开工**。在 Invoice 里写清项目名称、阶段（Deposit 50%）、交付物。
3. **尾款**：先给客户看预览链接或演示站，**收到尾款后再移交域名、代码和账号权限**。这是对付服务类拒付风险最有效的办法。
4. **月度维护（100–250 USD/月）**：小额付款按比例被固定费吃掉的更多，建议**按季度或按年预付**（例如年付打 9 折）。也可以每月发一张 PayPal 账单（PayPal 有没有自动循环账单要在你的账户里确认，**未核实**）。
5. **资金归集**：PayPal 美元余额 → 每月或攒到一定金额，电汇到招行美元现汇账户 → 留美元，或在 5 万美元额度内分批结汇。每笔都保存好合同、发票和交付邮件，以备银行做真实性审核和报税。
6. **在马来西亚日常花钱**：用招行或工行卡消费，或者先从国内把钱转进 TNG/Merchantrade 再用。不要拿这些钱包来收客户的款。

### 收款方式对选市场的影响
- **AU / UK / US**：客户习惯用卡付款、用 PayPal Invoice，接受度高 → 你的收款方式最顺，可以作为主攻市场。
- **SG**：客户偏好 PayNow 或本地转账，但你没有新加坡银行账户，用不了 PayNow → 只能请客户走 SWIFT 或 PayPal，成交阻力稍大，报价时要提前说明。
- **定价**：如果主要靠 PayPal 收款，整体价格加 **4–5% 缓冲**；如果收 SWIFT 且费用条款写 OUR，可以给"银行转账价"小幅优惠，引导大单走电汇。

## 来源
[1] https://www.paypal.com/cn/webapps/mpp/merchant-fees ；https://www.paypal.com/c2/webapps/mpp/merchant-fees
[2] https://www.paypal.com/c2/digital-wallet/paypal-consumer-fees?locale.x=en_C2 ；https://www.paypal.com/c2/webapps/mpp/using-paypal?locale.x=en_C2
[3] https://www.paypal.com/my/business/paypal-business-fees
[4] https://www.webnots.com/a-beginners-guide-to-paypal-china/
[5] https://www.worldfirst.com/my/blog/business-bank-insights/paypal-malaysia-review/
[6] https://www.extrabux.com/chs/guide/6318624
[7] https://wise.com/my/blog/paypal-fees
[8] https://en.xiaoz.org/post/6642
[9] https://www.paypal.com/bt/cshelp/article/whats-the-difference-between-friends-and-family-or-goods-and-services-payments-help277
[10] https://tomsguide.com/how-to/paypal-friends-and-family-how-does-it-work
[11] https://www.paypal.com/gt/webapps/mpp/security/seller-protection
[12] https://wise.com/help/articles/3xConsbhr7buWkQuqDEQ5V/how-do-i-verify-my-country-of-residence
[13] https://wise.com/help/articles/3W3Vq0ASUBh9AFII3rXsFX/getting-verified-in-thailand
[14] https://www.financial-ombudsman.org.uk/decision/DRN-5998464.pdf
[15] https://wise.com/acceptable-use-policy
[16] https://wise.com/gb/legal/terms-of-use-business
[17] https://www.dhl.com/discover/en-my/small-business-advice/starting-a-business/start-a-business-in-malaysia-foreigner ；https://landco.my/sole-proprietorship/
[18] https://wise.com/my/pricing/receive ；https://wise.com/help/articles/5sL5X2V2PbxUBIsQ1Fyfn4/holding-limits-if-you-live-in-malaysia
[19] https://forum.lowyat.net/topic/4953197/+2580
[20] https://www.wise.com/help/articles/2827506/how-do-i-receive-money-with-my-usd-account-details
[21] https://remitanalyst.com/send-money-to-china-from-usa/remit-profiles/transferwise/
[22] https://wise.com/help/articles/5rpQjZ2pueSOeIh5s2mh7w/how-to-send-and-receive-cny-via-unionpay
[23] https://www.wise.com/help/articles/2kTApouGnjRj6JM1yduMIL/how-to-send-and-receive-cny-via-alipay
[24] https://www.cmbchina.com/personal/saving/savingInfo?guid=86652863-3ab6-4061-bf13-1ea4673d5dd0
[25] https://www.safe.gov.cn:443/safe/file/file/20220323/66cc920601ae4e93b380763585a0a65d.pdf
[26] https://www.safe.gov.cn/safe/file/file/20200927/3575602a7b9a4760899064bd2e621bb7.pdf
[27] https://www.safe.gov.cn/neimenggu/file/file/20170728/b94fb1d6db30472584863040ecb838f3.pdf
[28] https://www.safe.gov.cn/xiamen/file/file/20211022/f4794075e84e40dd9394be523a52731b.pdf
[29] https://www.safe.gov.cn:443/safe/file/file/20240301/67efecf61b05467399e235bb9f5794d9.pdf
[30] https://www.hsbc.com.cn/content/dam/hsbc/cn/docs/foreign-exchange/personal-foreign-exchange-business-handling-guide.pdf
[31] https://www.allbrightlaw.com/CN/10475/d554e7b18efeb185.aspx
[32] https://payoneer.custhelp.com/app/answers/detail/a_id/34658
[33] https://vocal.media/01/how-to-open-a-payoneer-account-from-a-non-supported-country
[34] https://www.airwallex.com/en-my/blog/how-to-open-business-bank-account-malaysia
[35] https://www.airwallex.com/cn/business-account/global-accounts/hkd-account
[36] https://wise.com/my/blog/revolut-malaysia
[37] https://stripe.com/en-my/legal/ssa/my
[38] https://docs.lemonsqueezy.com/help/getting-started/prohibited-products
[39] https://paddle.com/support/what-products-am-i-not-allowed-to-sell-on-paddle
[40] https://www.amz123.com/ask/7IX9PDSJ
[41] https://community.shopify.com/t/pingpongpay-lianlianpay/90266
[42] https://www.xtransfer.com/zh/compare/xtransfer-vs-traditional-bank
[43] https://support.upwork.com/hc/en-us/articles/211063888
[44] https://www.skydo.com/blog/upwork-fees-freelancers
[45] https://emerhub.com/malaysia/digital-nomad-visa-malaysia
[46] https://www.mdec.my/api/media/file/DE-Rantau_Pass_FAQ_v10.pdf
[47] https://altery.com/guides/personal/malaysia-digital-nomad-visa ；https://malaysia4u.com/de-rantau-pass-guide ；https://www.countrytaxcalc.com/tax-guides/malaysia-digital-nomad-visa-2026/
[48] https://zh.wikisource.org/wiki/%E4%B8%AD%E5%8D%8E%E4%BA%BA%E6%B0%91%E5%85%B1%E5%92%8C%E5%9B%BD%E5%9B%BD%E5%8A%A1%E9%99%A2%E4%BB%A4%E7%AC%AC142%E5%8F%B7 （条例第二条，现行文本以国务院令第707号修订版为准）
[49] https://kpmg.com/cn/zh/home/insights/2020/02/china-tax-alert-07.html
