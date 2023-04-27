# Circuit-PSI with Linear Complexity via Relaxed Batch OPPRF

### 1. OPPRF
Alice：想要根据自己拥有的x查询y；
Bob：拥有所有的(x,y)对应关系。
Alice能告诉Bob自己有的x，Bob不能告诉Alice数据集X。
结果：如果x=$x_i$，Alice得到$y_i$，否则Alice得到一个随机数。
过程：有一个由k定义的函数$F_k(x)$,Bob知道这个函数。
1.Alice将自己的x输入OPPRF协议获得F(x)。
2.Bob将原来的(x,y)点对替换为(x,y$\oplus$F(x)),根据自己有的这些点对通过拉格朗日插值法建立多项式P(x)。将P(x)发送给Alice。
3.Alice根据自己的x计算P(x)。
4.Alice输出P(x)$\oplus$F(x),即$y\oplus$F(x)$\oplus$F(x),可以看出如果满足Bob所拥有的(x,y)点对，则Alice会得到对应的y。
这个多项式P(x)即为hint。

### 2.Batch OPPRF
由于通常有多个数据集，每个数据集都生成一个多项式会造成查询代价的升高，所以提出了Batch OPPRF，将所有的数据集放在一起建立一个统一的多项式来验证。


## 贡献
提出了计算复杂度和通信复杂度为线性的Circuit PSI。
B-OPPRF能使Circuit PSI协议的通信复杂度达到线性，但是时间复杂度仍然是非线性的，因为计算hint需要使用拉格朗日插值法，本文作者提出了RB-OPPRF，使算法时间复杂度也达到了线性，提高了性能。同时，其也建立了新的和更有效地PSM协议。
主要想法：对两方的数据集P0和P1使用布谷鸟哈希将原本的PSI问题转换为多个数据集规模为O(logn)的PSM问题（PSM：A有数据a，B有数据集X，希望知道a是否属于X），然后通过RB-OPPRF的方法来减少最终需要比较的次数来减小复杂度，达到线性复杂度。