不经意传输 oblivious transfer (OT) 
1. OT协议可以让发送者在不知道接收者需要哪些信息的情况下，互相交换信息。一般来说，OT协议被用来在远程计算中共享私密数据，以确保这些数据只能被授权用户获得.
OT协议的主要思想是发送方能够向接收方发送多个消息，但仅有其中一条消息与接收方真正需要的消息有关。发送方无法确定实际的情况，因此不会泄露再多信息.
OT协议可以追溯到1981年Rabin提出的方案，其用途是在密钥交换中保护计算机所处网络的连续性。后来，OT协议被证明与多方计算，安全多方计算（SMPC）和私有信息检索（PIR）等密码学问题密切相关。更完善的不经意传输形式被称为"1–2 oblivious transfer"或 "1 out of 2 oblivious transfer"，即发送方向接收方发送两个消息，接收方只能选择其中一个消息，同时而言，发送方对于接收方到底选择了哪一个消息一无所知,由Shimon Even、Oded Goldreich和Abraham Lempel$^{[1]}$开发，以建立用于安全多方计算的协议。后续"1–n oblivious transfer"的具体方案也被提出.

2. 第一种OT由Rabin$^{[2]}$于1981年提出：
其假设$Alice$有秘密$S_A$,$Bob$有秘密$S_B$，并且秘密为单比特，$Alice$ 和 $Bob$ 想要交换秘密，要求两方都有可能得到秘密并且秘密拥有方不知道对方是否得到秘密：
   1. $Alice$随机选取两个大素数$p,q$。并计算得到$one-time-  key ~~ n_ {A} $ , 然后将 $ n_ {A} $ 发
送给$Bob$。
   2. $Bob$随机选取一个数x,要求$x <  n_ {A} $ ,计算$ c \equiv  x^ {2}  mod ~n_ {A} $ ,然后将 $c$ 和私钥加密的 $x$ 发送给$Alice$。
   3. $Alice$找到一个 $ x_ {1} $ 使得 $ x_ {1}^ {2}  \equiv cmod(  n_ {A} )$ ,发送 $ x_ {1} $ 给$Bob$。
   4. $Bob$计算 $ gcd(x-  x_ {1}  ,  n_ {A}  )=d $, 此时有 $P(d = q\ or\ d = q)=  \frac {1}{2} $ 。
   5. $Bob$根据计算  $ v_ {B} $ = $ \begin{cases}0,if(x-x_{1},n_{A})=p~or~q,\\1,otherwise.\end{cases} $ 
    接着计算 $ \varepsilon _ {B} $ = $ v_ {B} $ $ \oplus $ $ S_ {B} $ 然后将 $ \varepsilon _ {B} $ 发送给$Alice$.

    这是$Alice$获得$Bob$的秘密 $ S_ {B} $ 的过程,可以得出$Alice$得到 $ S_ {B} $ 的概率为 $ \frac {1}{2} $ 。$Bob$获得 $ S_ {A} $ 的过程依然是上述步骤, 只不过是将$Alice$和$Bob$角色互换。
1. OT based on DH $^{[5]}$
   有如下假设
    1. $Alice$拥有值 $ v_ {0} $ , $ v_ {1} $ 和密钥$s$, $ r_ {0} $ , $ r_ {1} $ 
    2. $Bob$拥有值 $i \in {0,1} $ 和密钥$k$。$Bob$想获得 $ v_ {i} $ 
    3. $Alice $和$Bob$ 事先统一$g  \in  Z_p$, 其中$g$是大整数, $p$是大素数
    
    具体过程为:     

    1. $Alice  \rightarrow  Bob:  g^ {s} $ .
    2. $Bob$ 基于 $i$ 生成 $L_i $ = $ \begin{cases} g^k ~~~~~~~~if~ i = 0 ,\\ g^{s-k} ~~~~if~i=1.\end{cases} $ 
    3. $Bob$ $ \rightarrow $ $Alice$: $ L_ {i} $ 
    4. $Alice$生成 $ C_ {0} $ , $ C_ {1} $
       - $ C_ {0}  =(g^{r_0} ,(L_i)^{r_0} \oplus   v_ {0} )$ 
       - $ C_ {1}  =(g^{r_1} ,(g^s / L_i)^{r_1} \oplus   v_ {1} )$ )

    5. $Alice$ $ \rightarrow $ Bob: $ C_0, C_1 $ 
    6. $Bob$解密 $ v_ {i} $ 
        1. $case ~i=0$
            1. $Bob$ 可以通过如下方式解密获得 $ v_ {0} $ :
               $ C_ {0} $ $ [0]^ {k} $ $ \oplus $ $ C_ {0} $ [1]= $ (g^ {r_ {0}})^ {k} $ $ \oplus $ $ (L_ {i})^ {r_ {0}} $ $ \oplus $ $ v_ {0} $ = $ (g^ {r_ {0}})^ {k} $ $ \oplus $ $ (g^ {k})^ {r_ {0}} $ $ \oplus $ $v_0=v_0$
            2. $Bob$无法获得 $ v_ {1} $ 因为 $ C_ {1}  [1]=  (g^ {s}/L_{i})^ {r_ {1}} $ $ \oplus $ $ v_ {1} $ = $ g^ {(s-k)r1} $ $ \oplus $ $ v_ {1} $ 而$Bob$不知道$s$, $ r_ {1} $ 
        2. $case~ i=1$
           1. 类似地, $Bob$ 通过如下方式解密获得 $ v_ {1} $ :
            $ C_ {1} $ $ [0]^ {k} $ $ \oplus $ $ C_ {1}  [1]=  (g^ {r1})^ {k} $ $ \oplus $ $ (g^ {s}/L_ {i})^ {r_ {1}} $ $ \oplus $ $ v_ {1} $ = $ (g^ {r_ {1}})^ {k} $ $ \oplus $ $ (g^ {k})^ {r_ {1}} $ $ \oplus $ $ v_ {1} $ = $ v_ {1} $ 
           2. $ Bob $ 无法获得 $ v_ {0} $ 因为 $ C_ {0}  [1]=  (L_ {i})^ {r0} $ $ \oplus $ $ v_ {0} $ = $ g^ {(s-k)r0} $ $ \oplus $ $ v_ {0} $ 而$Bob$不知道$s,r_0$
        3. 因此,$Bob$只能解密 $ v_ {i} $ 而不能解密 $ v_ {1-i} $ 

4. OT based on RSA $^{[6]}$
    Even、Goldreich 和 Lempel 的协议可以使用RSA加密方案来实现，如下:
    1. $Alice$拥有消息 $ m_ {0} $ , $ m_ {1} $ , 并其中一个发送给$Bob$。$Bob$不想让$Alice$知道他收到了哪一个.
    2. $Alice$ 生成一个 RSA 密钥对，包括模数N，公有指数e和私有指数d.
    3. $Alice$还生成了两个随机值$x_{0},x_{1}$并将它们与模数N和指数e一起发送给$Bob$
    4. $Bob$选择 $b\in \{0,1\}$并生成随机数 $k$ ; 随后计算$v = (x_b + k^e) mod~ N$,并将 $v$ 发送给$Alice$.
    5. $Alice$计算$k_0 = (v - x_0)^d ~mod~N $ 和 $k_1 = (v - x_1)^d ~mod~N $; 于是$k_0$ 和 $k_1$ 其中之一是$k$, 但$Alice$并不知道是哪一个.
    6. $Alice$计算$m_0' = m_0 + k_0$ 和$m_1' = m_1 + k_1$, 将其发送给$Bob$.
    7. $Bob$计算$m_b = m_b' - k$, 于是$Bob$获得了$Alice$发送的消息$m_b$.
5. IKNP[03] $^{[3]}$
    $Bob$ 随机构造长度为 $n$ 比特串 $r$ ​,然后将其看为一个 $n \times 1$ 的列向量; 然后构造两个 $n \times \lambda $ 的矩阵 $T$ 和 P, 满足 $T$ 的列向量$t^i$与 $P$ 的列向量 $p^i$ 满足 $t^i \oplus p^i = r$;
    接着 $Alice$ 也随机选取长度为 $n$ 比特串 $s$, 然后双方共同执行base-OT 其中 $Bob$ 为发送方，将两个秘密份额矩阵 $T$ 和 $P$ 的第 $i$ 列作为输入, $Alice$ 作为接收方，以$s_i$为输入来选择两个秘密份额矩阵第 $i$ 列的某一个来构成自己的矩阵 $Q$ 的第 $i$ 列, $Q$ 的第 $i$ 列$q^i = \begin{cases}t^i ~~~~~~~~~~~~~~~~~~~~~if~s_i =0\\t^i \oplus r = p^i ~~~~~if~ s_i =1\end{cases}$,
     此时从行的角度来观察, 则有Q的第 $i$ 行$q_i =\begin{cases}
        t_i ~~~~~~~~~~~~~if~r_i =0\\
        t_i \oplus s~~~~~~ if~r_i =1
    \end{cases} $, 其中$t_i$代表T的第i行; 
    然后$Alice$再计算$q_i \oplus s$, 则$Alice$至此得到了消息对$(q_i, q_i \oplus s)$, 不难看出
    $q_i \oplus s  =\begin{cases}
        t_i \oplus s~~~~~~if~r_i =0\\
        t_i ~~~~~~~~~~~~~ if~r_i =1
    \end{cases} $
    同时至此, $Bob$拥有比特选择位$r_i$和$Alice$消息对中的一个消息$t_i$.
    由于s为$Alice$私有,$Bob$不知道另一个消息$t_i \oplus s$, 同时$Alice$也不知道$Bob$的比特选择位$r_i$, 因此$Alice$和$Bob$都无法获得对方的秘密, 但是$Alice$和$Bob$都可以获得自己的秘密, 从而完成OT协议.
    但是仔细观察可以看到，上述的消息对之间重复的使用了同一个比特串 $s$，这使得生成的消息之间存在相关性，所以必须解决这种相关性。本协议采用的方法是：使用一个随机预言机(Random Oracle) $H_i$来解决相关性, 即将消息对哈希, 成为$(H_i(q_i), H_i(q_i \oplus s))$, $Bob$的消息为$H_i(t_i)$, 从而解决上述问题.
6. KK[13] $^{[4]}$
    在Kolesnikov, Kumaresan $^{[4]}$等人2013年发表的文章中, 对 IKNP[03]协议在GMW中长度扩展步骤的通信开销远高于核心归约步骤的通信开销问题进行了优化。Kolesnikov等人发现,IKNP[03]在base-OT阶段, 对$Bob$的选择比特串 $r$ 进行扩展的时, 使用的是重复编码扩展方法, 这是最简单的编码方法, 其编码效率仅为 $ \frac {1}{2} $ , $ \lambda $ 是扩展后的向量长度。因此Kolesnikov等人从此着手, 使用更加复杂的编码方式在优化IKNP[03]协议。
    用$C(  r_ {i}  )$表示对 $ r_ {i} $ ,使用某种编码方法,用编码的视角看待IKNP[03]协议,首先是$Bob$对选
    择向量 $r$ 扩展, 扩展后的矩阵如下:
    $$\begin{array}{c|c}
    r & \\
    \hline 1 & \cdots C(1) \cdots \\
    0 & \cdots C(0) \cdots \\
    0 & \cdots C(0) \cdots \\
    0 & \cdots C(0) \cdots \\
    \vdots & \vdots
    \end{array}$$
    然后再运用秘密分享得到: (其中 $ t_ {i} $ 表示其中一个份额矩阵的行向量):
    $$T = \begin{array}{c|c}
    r & \\
    \hline 1 & \cdots t_1 \cdots \\
    0 & \cdots t_2 \cdots \\
    0 & \cdots t_3 \cdots \\
    0 & \cdots t_4 \cdots \\
    \vdots & \vdots
    \end{array}\oplus\begin{array}{c|c}
    r & \\
    \hline 1 & \cdots t_1 \oplus C(1) \cdots \\
    0 & \cdots t_2 \oplus C(0) \cdots \\
    0 & \cdots t_3 \oplus C(0) \cdots \\
    0 & \cdots t_4 \oplus C(0) \cdots \\
    \vdots & \vdots
    \end{array}$$
    通过秘密分享矩阵得到$Alice$的向量组{ $ q_ {i} $ },然后每一个向量分别异或$C(0)  \wedge  s$ ,$C(1)  \wedge  s$,得到 $Q$

    $$Q=\begin{array}{c|c}
    q_1 \bigoplus(C(0) \bigwedge s) & q_1 \bigoplus(C(1) \bigwedge s) \\
    \hline q_2 \bigoplus(C(0) \bigwedge s) & q_2 \bigoplus(C(1) \bigwedge s) \\
    \hline q_3 \bigoplus(C(0) \bigwedge s) & q_3 \bigoplus(C(1) \bigwedge s) \\
    \hline \vdots & \vdots
    \end{array}$$

    使用 $ q_ {i} $ = $ t_ {i} $ $ \oplus $ (C( $ r_ {i} $ ) $ \wedge $ s),改写 $Q$ 矩阵为:
    
    $$\begin{array}{c|c}
    t_1 \bigoplus(C(1) \bigwedge s) \bigoplus(C(0) \bigwedge s) & t_1 \bigoplus(C(1) \bigwedge s) \bigoplus(C(1) \bigwedge s) \\
    \hline t_2 \bigoplus(C(0) \bigwedge s) \bigoplus(C(0) \bigwedge s) & t_2 \bigoplus(C(0) \bigwedge s) \bigoplus(C(1) \bigwedge s) \\
    \hline t_3 \bigoplus(C(0) \bigwedge s) \bigoplus(C(0) \bigwedge s) & t_3 \bigoplus(C(0) \bigwedge s)\bigoplus(C(1) \bigwedge s) \\
    \hline \vdots & \vdots
    \end{array}\\
    =\begin{array}{c|c}
    t_1 \bigoplus(C(1) \bigwedge s) & t_1\\
    \hline t_2 & t_2 \bigoplus(C(1) \bigwedge s) \\
    \hline t_3  & t_3 \bigoplus(C(1) \bigwedge s) \\
    \hline \vdots & \vdots
    \end{array}$$

    可以看到最后 $Alice$ 获得结果进一步变为: $t_i$, $ t_ {i}  \oplus  (C(1)  \wedge  s)$,然后再用随机预言机来破坏其关联性:$H_i(t_ {i})$,$H_i(  t_ {i}   \oplus  (C(1)  \wedge  s))$, $Bob$的值也就变为$H_1( t_ {1} )$,$H_2(  t_ {2}  )$, $ \cdots $ $ \cdots $ ,$H_n(  t_ {n}  )$。从编码的方式了解了IKNP[03]之后就可以使用其他的编码方式对其推广,按照这种方式推广的结果相比于IKNP[03]也就是 $Alice$ 获得的两个消息结果中的编码部分改变而已,例如用 $ \varepsilon $ 表示一个编码结果( $ \varepsilon _i$  表示编码结果的第 $i$ 位),则 $Alice$ 获得的两个消息变为$H_i(  t_ {i}  ),H_i(  t_ {i} \oplus  (C(  r_{i}  \oplus  \varepsilon _ {i}  )  \wedge s ))$。而 $Bob$ 的结果并不变。所以改进后协议的提升也都来自编码效率的改变。

[1]S. Even, O. Goldreich, and A. Lempel, "A Randomized Protocol for Signing Contracts", Communications of the ACM, Volume 28, Issue 6, pg. 637–647, 1985.
[2] Rabin M O . How to Exchange Secrets by Oblivious Transfer[J]. Technical Memo TR-81, 1981.
[3] Ishai Y , Kilian J , Nissim K , et al. Extending Oblivious Transfers Efficiently[C] 23rd Annual International Cryptology Conference. CiteSeer, 2003.
[4] Kolesnikov V , Kumaresan R . Improved OT Extension for Transferring Short Secrets[M]. Springer Berlin Heidelberg, 2013.
[5] Efficient oblivious transfer protocols. SODA 2001
[6] https://en.wikipedia.org/wiki/Oblivious_transfer#ref_Note6