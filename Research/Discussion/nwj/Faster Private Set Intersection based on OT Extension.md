# Faster Private Set Intersection based on OT Extension
## Preliminaries
### Security parameters
对称安全参数为 $\kappa$，非对称安全参数为 $\rho$，统计安全参数为 $\lambda$

### The random oracle model
用于分析使用哈希函数的加密协议安全性的理论框架。在该模型中，哈希函数被视为一个理想化的“预言机”，它对任何查询都会回应一个从其输出空间中随机选择的输出。random oracle model 假设哈希函数是完全随机和无偏的，并且它产生的输出在其输出空间上是均匀分布的。random oracle model 经常用于加密协议的设计和分析，因为它允许更简单、更精确地分析它们的安全属性。特别是，它可以帮助识别协议中潜在的弱点，这些弱点可能在纯语法或语义分析中不明显。需要注意的是，random oracle model 是一个理想化的模型，实际的哈希函数并不完全像 random oracle model 那样运作。因此，random oracle model 提供的安全保证可能不一定适用于现实世界。
### Oblivious Transfer
- [Naor-Pinkas OT](https://blog.csdn.net/qq_34793644/article/details/113337973)：m 次 OT 的摊还时间复杂度为 3m 次公钥操作开销。
- OT extension：把 $OT_l^m$ 的公钥操作开销降到 $OT_\kappa^\kappa$ 的公钥操作开销（其中 $\kappa$ 是安全参数，和 OT 次数 m 无关，可以小到80或128），并使用更有效的对称加密操作来计算协议的其余部分，这比以前快了几个数量级。因此，执行 OT 的计算复杂度降低到一定程度，网络带宽成为主要瓶颈。
- random OT

### Circuit-Based PSI
- SOTA method： sortcompare-shuffle (SCS) circuit，$O(n\log n)$ *什么的size？*
- 使用 GMW 评估 SCS 电路的主要优化
- **使用通用协议的优点是可以很容易地扩展协议的功能，而不必更改协议或所生成协议的安全性**。

#### The GMW Protocol
[Goldreich-Micali-Wigderson (GMW) Protocol](https://zhuanlan.zhihu.com/p/237061306)：两个 party 能在互相不知晓对方数据的情况下计算某一能被逻辑电路表示的函数。
Evaluating AND gates using multiplication triples：讲一下原理
multiplication triples：讲一下如何生成的

#### Optimized Circuit-Based PSI
- 多路选择器
  输入 $\sigma-bit\ x,y$，选择信号 $1-bit\ s$.
  输出 $\sigma-bit\ z$.
  计算方式：$z[j] = s\wedge(x[j]\oplus y[j])\oplus x[j]$，for each $1 \le j \le \sigma $
- 处理 $\sigma-bit$ 的输入不采用 $1-bit$ 的简单叠加，而是使用 vector multiplication triple
- 效率：
  - 对于 $\sigma-bit$ 输入 $x,y$，$1-bit$ 的简单叠加通信开销为 4$\sigma\ bits$，使用 vector multiplication triple 降到 $2\sigma+2\ bits$（不含生成 multiplication triple 的通信开销）。**主要思想是在保证安全性的前提下适量减小随机性来换取效率**，在这个场景下具体体现为令 $\alpha_i[1],\alpha_i[2],...,\alpha_i[\sigma]$ 取相同的值。
  - $1-bit$ 的简单叠加需要 $OT_1^{2\sigma}$，使用 vector multiplication triple 需要 $OT_{\sigma}^2$
  - 把 SCS circuit 从 $2\sigma(2n\log 2n+n+1)$ 次 random OT 降低到 $2(2n\log 2n+n+1)$.
- 应用场景：两个 $\sigma-bit$ 的 $x,y$ 相乘，使用 vector multiplication triples 能把 random OT 次数从 $4\sigma^2-2\sigma$ 降到 $2\sigma^2$.
  
### Bloom Filter-Based PSI
#### The Bloom Filter
本质上是一个很长的二进制向量和一系列随机映射函数。Bloom Filter 可以用于检索一个元素是否在一个集合中。它的优点是空间效率和查询时间都远远超过一般的算法，缺点是。
#### Garbled Bloom Filter-Based PSI
- 对于基于 BF 的 PSI，不能简单地计算代表每个集合的 BF 的按位与，因为这会泄露信息。（C. Dong Et al. 2013）
- 改进：Garbled Bloom Filter (GBF)：仍然是 $\kappa$ 个哈希函数，但是 $G[i]$ 从单 bit 变成了一个长度为 $l$ 的 share。元素 $x$ 在集合中 $\iff \oplus_{j=1}^\kappa G[h_j(x)]=x$
- 使用一个 GBF 表示一个集合的流程：讲述
- 由于现有的 share 需要被重用，GBF 的生成不能完全并行化。
- GBF 应用于 PSI：讲述

#### Random GBF 
- 核心理念是让各方协作生成随机 GBF。原始协议中，GBF 必须具有特定的结构 ($\oplus_{j=1}^\kappa G[h_j(x)]=x$)。修改后的协议可以基于随机OT扩展。对于滤波器中的每个位置，如果其BF中对应的位为1，则每一方学习一个随机值。然后P1将每个输入对应的GBF值的异或发送给P2, P2将这些值与自己输入的GBF值的异或进行比较。
- oblivious pseudo-random generator (OPRG)
  - 从每个参与方 $P_i$ 接收输入 $b_i\in \{0,1\}$，生成一个 random string $s$，如果 $b_i=1$ 就把 $s$ 发给 $P_i$，否则什么都不发。**要求参与方不知道对方是否获得了 $s$**.
  - random OT extension：S 在第 i 个 OT 中没有输入，输出两个值 $(x^i_0, x^i_1)$，而 R 输入一个选择位向量 b，输出 $x^i_{b[i]}$。新的功能是通过让 S 忽略它接收到的 $x^i_0$ 输出，并且如果 $b_1 = 0$也忽略 $x^i_1$ 输出；类似地，如果 $b_2 = 0$, R 忽略它的输出。random OT extension 协议因此变得更高效，因为各方可以忽略部分计算。
  - **OPRG 本质上是个 GBF 的生成器**
- Bloom filter-based protocol：讲述

### Private Set Intersection via OT
一种新的私有集交集协议，该协议基于最高效的 OT 扩展技术，特别是random OT 和高效的 $1-out-of-n$ OT。随着集合大小的增加，这种 PSI 协议可以非常有效地扩展。
#### The Basic PEQT Protocol
- basic private equality test：讲述
- 改进：将输入使用 N 进制表示，只需要一次 $1-out-of-n$ OT。
  原理：$\sigma-bit$ 二进制最大 $2^\sigma$，N 进制下的位数：$t=\log_N2^\sigma=\sigma\log_N2$，论文中 $N=2^\eta$，故 $t=\frac{\sigma}{\eta}$.
  具体实现：讲述

#### Private Set Inclusion Protocol
- 为了并行地执行多个比较，需要在更长的字符串上计算OTs，本质上是(并行地)为集合 X 中的每个元素传输一个随机字符串。 
- 具体实现：讲述（和 BQET 一样）

#### The OT-Based PSI Protocol
$P_2$ 调用 Private Set Inclusion Protocol $n_2$ 次即可。

### Hashing Schemes and PSI
- 朴素想法：暴力枚举，调用 $n_1n_2$ 次 BQET。
- 改进：使用哈希方案来减少必须计算的比较次数。思想是让每一方使用公开的随机散列方案将其输入元素映射到一组 bins 中。如果输入元素在交集中，则双方将其映射到相同的 bin。因此，协议只要检查双方映射到同一个 bin 的项之间的交集。**Bucket sort Alg + Rabin Karp Alg的思想**。

隐私要求各方相互隐藏他们的输入中有多少被映射到每个bin中。因此，必须提前计算将映射到items最多的bin的items数量，然后将所有bin设置为该大小。(这可以通过将 dummy items 存储在未被完全占用的箱子中来实现。)这增加了协议的开销，因为每个容器的比较次数现在取决于填充最多的容器的大小，而不是容器中items的实际数量。然而，尽管各方需要在外部假装他们的所有items都是真实的，但他们不需要将所有内部计算应用于他们的 dummy items (因为他们知道这些items不在交集中)。通过精心设计，即使考虑计时攻击，也可以进一步优化底层协议的计算复杂性。

#### Hashing Schemes
- Simple Hashing
  - 只有一个哈希函数
  - 哈希函数选择和输入无关
  - 对于一个给定的元素，映射到的bin是唯一确定的
  - m个元素m个bins，一个bin的最大items数量：$\frac{\ln m}{\ln\ln m}(1+o(1))$，一个bin的平均items数量：1
  - **实际采用的方案**：当减少bins的个数，满足一定数学条件下，一个bin的平均items数量和一个bin的最大items数量能达到相同的阶：$O(\ln m)$。

- Balanced Allocations
  - 两个哈希函数
  - 通过检查两个bin $B_{h_1(e)}$ 和 $B_{h_2(e)}$ 中哪个较少被占用，并将元素映射到该bin，来映射元素e。
  - 通过检查 $B_{h_1(q)}$ 和 $B_{h_2(q)}$ 这两个bin来查找元素 $q$，并将这两个bin中的元素与 $q$ 进行比较。
  - m个元素m个bins，一个bin的最大items数量：$\frac{\ln\ln m}{\ln 2}(1+o(1))$

- Cuckoo Hashing
  - 两个哈希函数将m个元素映射到 $b = 2(1 +\varepsilon)m$ 个bin
  - 在发现冲突时重新定位元素来避免冲突：
    1. 将元素e插入bin $B_{h_1(e)}$。
    2. 将 $B_{h_1(e)}$ 的任何先前内容 $o$ 驱逐到新的bin  $B_{h_i(o)}$，使用 $h_i$ 确定新的bin位置，其中$h_i(o) \ne h_1(e), i\in\{1,2\}$。
    3. 重复这个过程，直到不再需要驱逐，或者直到执行了阈值次数的relocations。在后一种情况下，将最后一个元素放入一个特殊的存储库 $s$ 中。
  - 对于 $size(s)\le \ln m$的存储库，m个元素的插入失败概率为$m^{−s}$。
  - 查找非常有效：只要将$e$与 $B_{h_1(e)}$ 和 $B_{h_2(e)}$ 中的两个项以及存储库中的$s$个项进行比较。
  - 降低查找开销的代价是哈希表的大小增加到大约2m个bin。

#### Evaluation of Hashing-Based PSI


#### Maximum Bin Size and Overhead
bin的个数 $b$ 和对应的最大bin大小 $max_b$ 的设置是效率和安全性的 trade off：如果选择的 $max_b$ 太小，则一方无法执行映射的概率(记为 $P_{fail}$)会增加 (因为不是所有的 items 都可以映射到某个bin，**$max_b$ 的大小本质上代表对哈希冲突的容忍程度**)。因此，输出可能不准确，或者其中一方需要请求一个新的哈希函数(这种请求会泄露有关该方输入集的信息)；另一方面，执行的比较次数随着$b$和 $max_b$ 的增加而增加。。
> 当使用具有固定存储空间大小的散列方案时，映射到某个存储空间(例如通过P1)的项目数量可能大于该存储空间的容量。(此事件发生的概率为 $P_{fail}$ )在这种情况下，P1可能会请求使用新的哈希函数。这个请求揭示了关于P1输入的一些信息。此问题的最佳解决方案是确保这些事件发生的概率可以忽略不计，因此几乎可以肯定这些事件在实践中不会发生。这是我们在比较中采用的方法。(另一种方法是P1忽略遗漏的项，因此实际上是计算交集的近似值，同时分析这种计算的隐私泄漏影响，并决定是否容忍它们。结果可能是一个更自由的参数选择，这将导致原始协议的更有效实现。)
