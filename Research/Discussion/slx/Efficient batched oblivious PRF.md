# Efficient Batched Oblivious PRF
## INTRODUCTION
> IKNP：一个非常高效的 OT 协议，基于 Yao’s Garbled Circuit (GC) 实现。
> KK：是 IKNP 协议在处理短秘密上的一个改进。它将 1-out-of-n OT 的开销降到接近 1-out-of-2 OT 的开销 ($n\le 256$)。
### Oblivious Transfer

### Oblivious PRF
- pseudorandom function (PRF)：发送方选择一个随机种子 $s$，接收方输入一个 $r$，得到一个输出 $F(s,r)$. **本文中只考虑接收方只有一次输入机会（即只能选择一个 $r$ 作为输入）**。
- OT 可以看做 OPRF 的一个特例：对于 1-out-of-2 OT，发送者拥有 $m_0,m_1$，接收者选取 $r\in\{0,1\}$，得到输出 $F((m_0,m_1),r)=m_r$。1-out-of-n OT同理。

### Other applications of OPRF
- string-select OT (SOT)：发送方 S 有一个 keywords 到 secret values 的映射。接收方 R 接收与其选择的 keywords 对应的 secret。
- Oblivious PRFs 可用于 secure pattern matching，其中一方持有长文本 T，另一方持有短模式字符串 p。双方学习 p 在 T 中所有出现的位置。
## Contributions
- 对于任意大的 $n$，将 1-out-of-n OT 的开销降到和 1-out-of-2 IKNP OT 和 1-out-of-2 KK OT 相近的开销。**可以看成输入域不限的 OPRF**。 
- In this work, we take the coding-theoretic
perspective to the extreme. We observe that we never need
to decode codewords, and by using (pseudo-)random codes
we are able to achieve what amounts to a 1-out-of-poly OT
by consuming a single row of the OT matrix, which for the
same security guarantee is only about 3:5× longer than in
the original IKNP protocol.

- 使用 BaRK-OPRF，我们可以通过只使用OT扩展矩阵的一行来实现关键字搜索。

## TECHNICAL OVERVIEW OF OUR RESULTS
### IKNP
- 目标：使用 $k$ 次 1-out-of-2 OT 实现实际上 $m>>k$ 次 1-out-of-2 OT。
- Notation: $\boldsymbol{t_j}$ 表示矩阵 $T$ 的第 $j$ 行；$\boldsymbol{t^j}$ 表示矩阵 $T$ 的第 $j$ 列。$\boldsymbol{u_j}$ 和 $\boldsymbol{u^j}$ 同理。
- receiver：$r\in\{0,1\}^m, T\in\{0,1\}^{m\times k}, U\in\{0,1\}^{m\times k}, s.t.\  \boldsymbol{t_j}\oplus\boldsymbol{u_j}=r_j\cdot 1^k$
- sender：$ s\in \{0,1\}^k $ 
- 具体过程
  1. sender 和 receiver 角色互换进行 $k$ 次 1-out-of-2 OT：在每一次 OT 中，receiver 向 sender 发送 $\boldsymbol{t^i}$ 和 $\boldsymbol{u^i}$，sender 根据自己拥有的 $s_i$ 来决定接收 $\boldsymbol{t^i}$ 或 $\boldsymbol{u^i}$. $k$ 次 OT 后，sender 将选择的输出拼成矩阵 $Q\in \{0,1\}^{m\times k}$，并且可以证明： 
  $$ \boldsymbol{q_ {j}}  =  \boldsymbol{t_ {j}}  \oplus [r_ {j}\cdot s ] =  \begin{cases}\boldsymbol{t_ {j}} &if& r_{j}=0\\\boldsymbol{t_ {j}}\oplus s &if& r_j=1\end{cases} $$
     > 一个简要证明如下：由上述过程，结合 $\boldsymbol{t_j}\oplus\boldsymbol{u_j}=r_j\cdot 1^k$ 可以得知：
     $$ q_j^i = \begin{cases}t_j^i &if& s_{i}=0\\u_j^i=t_j^i\oplus r_j &if& s_i=1\end{cases} $$
     表达成行向量的形式，显然有 $\boldsymbol{q_ {j}}  =  \boldsymbol{t_ {j}}  \oplus [r_ {j}\cdot s ]$.
  2. 如上操作之后，sender 拥有 $m$ 个消息对：$(\boldsymbol{t_j},\boldsymbol{t_j}\oplus s)=(\boldsymbol{q_j},\boldsymbol{q_j}\oplus s), 1\le j\le m$，receiver 拥有 $\boldsymbol{t_j}$。这就通过 $k$ 次 OT 完成了实际上的 $m(>>k)$ 次 OT。
     > 由于 receiver 并不知道 $s$，所以 receiver 无法得知 $\boldsymbol{t_j}\oplus s$；由于 sender 不知道 $r$，而 $\boldsymbol{q_j}$ 和 $\boldsymbol{t_j}$、$\boldsymbol{t_j}\oplus s$ 二者中哪个相等完全由 $r$ 决定，因此 sender 不知道 receiver 拥有消息对中的哪一条消息。因此这是满足 OT 定义的。
- 存在的问题与改进
  1. 上述的消息对之间重复的使用了同一个比特串 $s$，这使得生成的消息之间存在相关性，所以必须解决这种相关性。IKNP 协议采用的方法是：使用一个 Random Oracle $H_i$ 来解决相关性, 即将消息对哈希, 成为 $(H_i(q_i), H_i(q_i \oplus s))$, $Bob$ 的消息为$H_i(t_i)$, 从而解决上述问题.
  2. 使用 $k$ 次 OT 实现实际上 $m>>k$ 次 OT 会使每次 OT 的消息变长。解决方法是：对消息对中两个长信息分别使用不同公钥加密，然后使用 OT 传对应的私钥。

### IKNP 推广
- 目标：实现 1-out-of-$2^l$ OT。
- 主要思想：将上述 1-out-of-2 IKNP OT 过程中的 choice bit $r_i$ 换成一个 $l-bit$ string. $C$ 是 $l$ 的 $k-bit$ 线性纠错码。
- 具体过程：receiver 生成的 $T\in\{0,1\}^{m\times k}, U\in\{0,1\}^{m\times k}$ 满足的约束条件变为 $\boldsymbol{t_j}\oplus\boldsymbol{u_j}=C(r_j)$. 在相同操作下，sender 得到的矩阵也相应变为 $\boldsymbol{q_ {j}}  =  \boldsymbol{t_ {j}}  \oplus [C(r_ {j})\cdot s ]$，其中 $\cdot$ 是按位与。sender 无法得知 $r_j$ 以及 $C(r_j)$，因此 sender 可以遍历 $r_j$ 的全部 $2^l$ 个可能取值，计算出 $2^l$ 个 $H(\boldsymbol{q_j}\oplus [C(r_j)\cdot s])$. receiver 只拥有其中一个，即 $H(\boldsymbol{t_j})$。
  > 由于 receiver 并不知道 $s$，所以 receiver 无法得知 $\boldsymbol{t_j}\oplus [C(r')\cdot s],r'\in\{0,1\}^l$；由于 sender 不知道 $r_j$，而 $\boldsymbol{q_j}$ 和 $\boldsymbol{t_j}\oplus [C(r')\cdot s],r'\in\{0,1\}^l$ 中哪个相等完全由 $r_j$ 决定，因此 sender 不知道 receiver 拥有消息对中的哪一条消息。因此这是满足 OT 定义的。
- 这完成了 random strings 的 OT。对于 chosen strings 的 OT，发送方只需要将 $2^l$ 个 chosen strings 分别使用 $2^l$ 个不同的 $H(\boldsymbol{q_j}\oplus [C(r')\cdot s]), r'\in\{0,1\}^l$ 作为对称密钥加密后发给 receiver 即可。
- 安全性保证：假设 receiver 拥有 $r_j$，还想知道 $2^l$ 个字符串中其他的字符串 $H(\boldsymbol{q_j}\oplus [C(\tilde{r})\cdot s])$，注意到：$\boldsymbol{q_j}\oplus[C(\widetilde{r})\cdot s]=\boldsymbol{t_j}\oplus[C(r_j)\cdot s]\oplus[C(\widetilde{r})\cdot s]=\boldsymbol{t_j}\oplus[(C(r_j)\oplus C(\widetilde{r}))\cdot s]$，显然只有 $s$ 是 receiver 未知的，因此如果 receiver 采用穷举攻击的方法，穷举空间大小取决于 $C(r_j)\oplus C(\widetilde{r})$ 的 Hamming weight (即1的个数)。

### Pseudorandom codes
对于上面用到的线性纠错码 $C$ 的讨论。
- $C$ 不需要具有纠错码的许多特性：
  - 不需要解码
  - 安全性由 $C(r_j)\oplus C(\widetilde{r})$ 的 Hamming weight 保证
- 因此，可以将对 $C$ 的要求从纠错码放宽到伪随机码（pseudorandom code，PRC），消除了对 receiver 选择字符串大小的限制。$C:\{0,1\}^*\to\{0,1\}^l$ 
