# PSI



## 问题定义
私有集合交集(PSI)协议允许拥有集合S和s0的双方计算交集I = S∩s0，而不向另一方透露任何关于各自集合的额外信息(除了它们的大小)。任何一方或双方都可以根据应用程序学习交集。
两方各自拥有集合 $S=\{s_1,s_2,...,s_n\}$ 和 $S'=\{s_1',s_2',...,s_n'\}$，其中 $s_i,s_i'\in\{0,1\}^\sigma$ 并且假设 $S,S'$ 中各自都没有重复的元素。目标：各方计算 $I=S\cap S'$，不泄露除了 $I$ 之外的任何信息。

## Survey
[Private Set Intersection: Past, Present and Future](https://www.scitepress.org/Papers/2021/105258/105258.pdf)

## SOTA Methods
### Naive PSI


### Public-key Cryptography-based PSI
#### Diffie Helman
[A more efficient cryptographic matchmaking protocol for use in the absence of a continuously available third party](https://ieeexplore.ieee.org/document/6234849)1986



#### RSA
[Practical private set intersection protocols with linear complexity](https://eprint.iacr.org/2009/491.pdf)2010
安全性基于 one-morediscrete-logarithm or one-more-RSA assumptions in
the random oracle model.
由于 RSA 计算复杂度较高，协议中 RSA 的计算次数会随着数据量的增大呈线性增长，使得基于 RSA 的求交方法，在数据量较大时会产生性能问题。
由于 RSA 盲签名算法在运行时只对一端的数据进行 RSA 加密，使得在求交数据量级差距较大时，可以把数据量较小的一端作为 Client 端，这样可以获得非常大的性能优势。另外，RSA 算法的流程适合并行处理，方便利用并行计算来提升性能。
RSA 盲签名协议能够在恶意对手模型下，为隐私集合求交提供安全保障，但由于非对称加密的次数随比对的数量量的增加呈线性增长，所以无法处理海量数据的隐私集合求交场景。


### Generic Secure Computation-based PSI(semi-honest)
[Private set intersection: Are garbled circuits better than custom protocols?](https://www.cs.umd.edu/~jkatz/papers/psi.pdf)
- 通用安全计算协议：允许双方安全地计算任何可以表示为布尔电路的函数。
- Yao’s garbled circuits protocol：通用安全计算协议的一种
- 贡献
  - 设计了三种针对不同集合大小和领域的PSI协议，都基于 Yao’s garbled circuits 
  - main idea：每个集合在本地排序，然后隐式地合并为单个排序列表。然后比较每一对相邻的元素，如果元素相等，则保留其中一个元素，如果元素不相等，则用一个随机值替换这对元素。为了不泄露任何信息，必须对结果列表进行洗牌。
  - 结论：基于通用安全计算的协议可以提供与最快的自定义协议竞争的性能。
  - 通用协议可以直接用于执行更复杂的安全计算。
  - 通用的乱码电路方法在许多情况下可以优于De Cristofaro-Tsudik协议

认为解决PSI的通用技术效率低下可能源于以下几个因素:一般认为通用协议本身很慢，并且乱码电路无法扩展，或者可能认为计算大小为n的两个集合的交集需要Θ(n2)大小的电路，因为必须比较所有对元素。最近姚的(通用)乱码电路技术的实现表明，第一个假设是无效的;第二种说法完全不正确

使用通用技术生成隐私保护协议有几个优点:通过依赖现有的软件包来构建乱码电路协议[17,32,33,36]，人们只需要为要计算的功能编写一个电路，而不必从头开始设计和实现一个新的协议。通用协议本身也比定制协议更加模块化。

三个协议：
Bitwise-AND (BWA)
使用基于各方集合的 bit-vector 表示的电路
在小集合上能获得最佳性能

Pairwise-Compare (PWC)
使用电路对双方集合中的元素进行成对比较。对于计算两个大小为n的集合的交集，该协议的最坏情况复杂度为Θ(n2)，即使全集很大，只要交集很小就行通时提出了一种优化方法，可以在不牺牲任何隐私的情况下提高交集很大时的性能

Sort-Compare-Shuffle 
协议的复杂度为Θ(nlogn)
主要思想是让每一方在本地对他们的集合进行排序，然后将他们的排序集合合并到一个排序列表中(privately)。然后比较每个相邻的元素对(obliviously)，如果元素对中的元素相等，则保留值，否则替换成 dummy value。最后，在显示整个列表之前，匹配/虚拟元素的结果列表被明显地洗牌。这个洗牌步骤是必要的，否则匹配元素的位置信息会泄露双方集合中不匹配元素的信息。
洗牌方法
(1)使用乱码电路方法(SCS-SORT)对整个匹配/虚拟元素列表进行无关洗牌;(2)使用基于同态加密的协议(SCS-HE)对匹配/虚拟元素列表进行随机洗牌;(3)与之前一样对列表进行随机洗牌，但使用应用于Waksman无关交换网络(SCS-WN)的乱码电路。

### Homomorphic Encryption-based PSI

[Fast Private Set Intersection from Homomorphic Encryption](https://eprint.iacr.org/2017/299.pdf)2017
基于全同态加密（FHE）的隐私集合求交方法 [5]。基于同态加密的隐私集合求交方法主要是对数据进行同态加密，并使用加密后的数据和原始数据构建多项式并计算多项式的值。

同态加密算法目前是一种低效的加密算法，全同态加密的密文长度通常非常大，使得目前基于同态加密的隐私集合求交方案在性能上不占据优势。
特别地，Chen 的基于全同态加密的隐私集合求交方案，只对接受者一侧执行同态加密，这使得算法适合运行在求交的集合差异较大的场景。

### Oblivious Transfer-based PSI
[Faster private set intersection based on OT extension](https://eprint.iacr.org/2014/447.pdf)2014
基于 OT 扩展协议的高效隐私集合求交方案 [8]，该方案使用 OT 扩展，传输数据使得通信双发获得一个伪随机函数，并使用此伪随机函数对双方持有的数据进行加密比对。方案主要分为三个阶段来执行，哈希阶段，隐秘传输阶段和求交阶段。在哈希阶段，通信 Alice 和 Bob 把各自持有的数据通过哈希运算均匀分布在一个给定大小的地址空间内，并使用随机数填充空余的哈希位置。在隐秘传输阶段，Bob 根据自己持有数据的比特信息作为选择位，使用 OT 扩展安全地获取 Alice 持有同样比特位置上的伪随机生成数据。最后在求交阶段，Bob 解密伪随机数据，并和自己持有的而数据进行比较。
[Efficient batched oblivious PRF with applications to private set intersection](https://eprint.iacr.org/2016/799.pdf)2016
使用批量 OT 扩展传输和布谷鸟哈希实现了更高效的隐私集合求交方案，基于 OT 的隐私集合求交成为性能上最接近朴素哈希求交技术的隐私集合求交方案。

[SpOT-Light: Lightweight Private Set Intersection from Sparse OT Extension](https://eprint.iacr.org/2019/634.pdf)2019
基于稀疏扩展的隐私集合求交方案，方案首先把秘密信息分成三份，这样在未获取到要求交的数据之前，可以提前随机生成两份秘密信息，以便在离线阶段进行 OT 扩展传输，提前获取伪随机生成函数。在在线阶段，为了避免传输大量的秘密信息，方案使用了多项式技术，把要传输的数据融入多项式，仅传递多项式的参数来代替传输大量数据。根据该方案的测试结果，在要对比的数据量庞大，或者带宽受限制场景下，此方案相较于目前最优的基于 OT 的隐私集合求交方案，提供了更好的性能优势。


## Future Trends
### Improvement Approaches
- [Practical multi-party private set intersection from symmetric-key techniques](https://eprint.iacr.org/2017/799.pdf) 2017


- [PSI from PaXoS:Fast, Malicious Private Set Intersection](https://eprint.iacr.org/2020/193.pdf) 2020
  - 提出一种两方 PSI 的新协议，半诚实版本和恶意版本之间的唯一区别是线性纠错码具有不同参数的实例化。
  - 通过一种新的数据结构：probe-and-XOR of strings 把 cuckoo hashing 应用于 malicious 场景下的 PSI。
  - PaXoS 数据结构原理：将n个二进制字符串映射到m个二进制字符串，其中n个原始字符串中的每一个都可以通过对m个字符串的特定子集进行异或来检索。
  - 在传统 Cuckoo hashing 基础上的改进：不是将 item 存储在哈希函数确定的两个位置中的一个，而是将这两个位置的异或值作为存储的值。**消除了在 malicious PSI 中使用 cuckoo hashing 的不足：因为各参与方不需要在两个存储 item 的位置中选择一个，因此不会通过 Cuckoo hashing 泄露任何信息**。

- [VOLE-PSI: Fast OPRF and Circuit-PSI from Vector-OLE](https://eprint.iacr.org/2021/266.pdf) 2021
  - 使用Schoppmann et al.改进版本的 Vector-OLE，并对 PaXoS 进行了自定义的修改，提出了一种 batched OPRF 新结构，通信和计算开销为 $O(n)$。
  - 证明了与半诚实的变体相比，提出的协议可以在没有额外开销的情况下实现 malicious security。
  - 提出基于 VOLE 的一个扩展，使 PSI 的输出可以在双方之间秘密共享(Circuit-PSI)。
  - 提出将 PaXoS 求解器与任何 OPRF 协议一起使用能够生成 Oblivious Programmable PRF (OPPRF) 协议。

- [Circuit-PSI with Linear Complexity via Relaxed Batch OPPRF](https://eprint.iacr.org/2021/034.pdf) 2021
  - 在 B-OPPRF 的基础上提出 RB-OPPRF，利用 Cuckoo hashing 代替了多项式插值，将 Circuit PSI 协议的计算复杂度和通信复杂度同时降为 $O(n)$。
  - 结合提出的 RB-OPPRF 建立了更高效的 PSM 协议（PSM：A 有数据 $a$，B 有数据集 $X$，希望知道 $a$ 是否属于 $X$）。
  - 主要想法：对两方的数据集 $P_0$ 和 $P_1$，先用 Cuckoo hashing 将原本的 PSI 问题转换为多个数据集规模为 $O(\log n)$ 的 PSM 问题，然后通过 RB-OPPRF 的方法来减少最终需要比较的次数来减小复杂度，达到线性复杂度。
- [Oblivious key-value stores and amplification for private set intersection](https://eprint.iacr.org/2021/883.pdf) 2021
  - 基于*将 PSI 协议输入集编码为多项式* 这一基本想法，提出了更一般的概念 **Oblivious key-value stores (OKVS)**，将希望存储的映射关系隐藏在多项式中。
  - 不足：目前的分析技术不足以找到具体的参数来保证 OKVS 结构的小失效概率。文章中的补救办法是通过把一个失效概率为 $p$ 的 OKVS 放大到具有相似开销且失效概率为 $p^c$ 的 OKVS，通过做 $O(\frac{1}{p})$ 次的实验来间接验证放大后的 OKVS。


- [Blazing Fast PSI from Improved OKVS and Subfield VOLE](https://eprint.iacr.org/2022/320.pdf) 2022
  - 对 Rindal et al. 的协议进行优化，利用 sub-field 向量不经意线性求值，把通信复杂度降到 $O(n\lambda + n \log n)$，并且通信开销不随 $\lambda n$ 扩展。
  - 对 Garimella et al. 提出的 OKVS 数据结构进行改进，基于 Cuckoo hashing 提出了一个理论框架，具体求解失败概率更 tight 的上界，提高了计算和通信效率。
  - 采用改进的 OKVS，提出了迄今为止最高效的 PSI 协议。
### Other Approaches
- Bilinear Maps Approach
- Secret Sharing Approach
- Modular Inverse Approach
- Symmetric Encryption Approach
  

