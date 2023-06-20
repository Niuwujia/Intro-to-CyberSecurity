# Traveling the Silk Road: A measurement analysis of a large anonymous online marketplace


## background
本文中，作者对丝绸之路（一个国际化匿名在线市场）进行了一系列数据分析。匿名化的网上市场使得执法部门很难辨别买家和卖家，因此常被用来进行非法交易。作者通过对丝绸之路的数据分析，来提供其各种特征。

### 丝绸之路运作方式
丝绸之路是一个在线匿名市场，其特点是尽可能保证买家和卖家的匿名性。
- 访问丝绸之路：由于丝绸之路没有将DNS映射到已知的IP地址，而是使用.onion的顶级域后缀，因此为了进入丝绸之路市场，Bob需要在电脑上安装Tor客户端。当Bob的客户端想要联系丝绸之路服务器时，Tor节点在Tor网络内部建立一个回合点使得双方可以在通信的同时保证自己的IP不被观察者和彼此知道。
- 购买商品：丝绸之路为了保持匿名性，只支持比特币交易。在支付时，Bob不直接将比特币支付给卖家，而是交由丝绸之路托管。
- 寄送商品：为了保证匿名性，丝绸之路建议使用与买家住所不同的送货地址。一旦卖家发货，买家的收货地址就会从记录中删除。

### 数据收集方法
主要通过对网站进行爬虫来获得数据。
作者注意到，用于身份验证的cookie可以重复使用长达一周，因此通过每周至少进行一次手动cookie刷新，可以绕过CAPTCHA机制进行爬虫，来获取网站的内容。
- 由于网站的运营者可能注意到爬虫行为，因此作者定期丢弃和建立新的Tor电路进行爬虫，并且进行爬虫的时间总是随机的。


### 市场特征
- 通过调查发现，市场上售卖的大多是毒品。
- 大部分商品在被列出后三周消失，超过25%的商品在被列出后三天就会消失。
- 卖家的数量呈线性增长，每个月大约新增50个活跃卖家，同时也有许多卖家离开。大多数卖家在网上停留大约100天。
- 大多数商品来自美国，远远多于排在第二位的英国。
- 少数卖家收到了绝大多数的反馈，约有100位卖家收到了60%的反馈。
- 虽然在丝绸之路网站上由于需要保证匿名性，没有针对骗子的法律追索权，但是高达96.5%的买家表示满意。


### 经济指标
- 丝绸之路使用比特币交易，而比特币一直是一种不稳定货币。
- 商品的价格随着比特币对现实货币汇率的变化而变化，比特币升值，商品价格就下降，反之亦然。
- 通过统计过去29天内一个商品获得的反馈数量，乘以该商品过去29天内的平均价格再除以29用来估算商品的平均销量。
- 通过数据观察到总销量增长相当显著，最后稳定的销售量大约是7665比特币每日。
- 丝绸之路的运营商会从所有销售中取得佣金，经过调查发现平均佣金为产品价格的7.4%。
- 在作者进行测量的29天内，丝绸之路上大约交换了1335580个比特币，而同期比特币市场所交易的比特币约为29553384，通过比较发现丝绸之路的交易占交易所发生的所有交易的4.5%。

### 讨论
- 由于买家每个订单通常只会留下一个反馈，而有一些订单会包含多种货物，因此作者低估了销售总量。
- 四种可能干预丝绸之路运行的策略：
  - 破坏Tor网络。没有Tor，丝绸之路就无法运作。但是丝绸之路等暗网仅仅是Tor的一小部分，其还是有非常多有益的用途，破坏Tor不是一个明智的做法。
  - 攻击经济设施。攻击者可以试图通过过操作比特币的汇率的快速波动来阻碍交易。由于比特币将公钥与实际身份绑定在一起，而网络分析可以将公钥映射到单个用户和事务，因此比特币的匿名性比大多数人像的要弱，对于丝绸之路中一次性提取大量比特币的卖家，有被识破的风险。然而丝绸之路对比特币的汇率波动已经有了良好的抵御措施，者仍是一种比较困难的方法。
  - 攻击交付模型。加强对邮政和海关的管制，防止非法物品送到目的地。
  - 减少消费者需求。通过预防毒品的运动，来减少对毒品的需求，进而干预丝绸之路。


### review
本文主要介绍了对于丝绸之路的分析，主要使用的方法是网络爬虫。通过数据分析揭示了该匿名市场的多种特点，并经过总结得出可以干预其运行的多种方法。破坏Tor网络，攻击经济设施以及攻击交付模型都是比较困难的干预方法，因此想要干预丝绸之路这样大型的非法网站，最好的方法还是减少消费者的需求，防止毒品以及各种管制药品的滥用。