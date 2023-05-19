# Practical Private Set Intersection Protocols with Linear Complexity

## Concepts

### PSI
PSI consists of two algorithms: {Setup, Interaction}
- **Setup**: a process wherein all global/public parameters are selected.
- **Interaction**: a protocol between client and server that results in the client obtaining the intersection of two sets.

### APSI
APSI is a tuple of three algorithms: {Setup, Authorize, Interaction}. 
- **Setup**: a process wherein all global/public parameters are selected.
- **Authorize** : a protocol between client and CA resulting in client committing to its input set and CA issuing authorizations (signatures), one for each element of the set.
- **Interaction**: a protocol between client and server that results in the client obtaining the intersection of two sets.

### Security Properties
- **Correctness**: A PSI scheme is correct if, at the end of Interaction, client outputs the exact (possibly empty) intersection of the two respective sets.
- **Server Privacy**: Informally, a PSI scheme is server-private if the client learns no information (except the upper bound on size) about the subset of elements on the server that are NOT in the intersection of their respective sets.
- **Client Privacy**: Informally, client privacy (in either PSI or APSI) means that no information is leaked about client’s set elements to a malicious server, except the upper bound on the client’s set size.
- **Client Unlinkability** (optional): Informally, client unlinkability means that a malicious server cannot tell if any two instances of Interaction are related, i.e., executed on the same inputs by the client.
- **Server Unlinkability** (optional): Informally, server unlinkability means that a malicious client cannot tell if any two instances of Interaction are related, i.e., executed on the same inputs by the server.
- **Correctness** (APSI): An APSI scheme is correct if, at the end of Interaction, client outputs the exact (possibly empty) intersection of the two respective sets and each element in that intersection has been previously authorized by CA via Authorize.
- **Server Privacy** (APSI): Informally, an APSI scheme is server-private if the client learns no information (except the upper bound on size) about the subset of elements on the server that are NOT in the intersection of their respective sets (where client’s set contains only authorizations obtained via Authorize).

## Notation

![[Pasted image 20230516205712.png]]

## Methods

### Baseline: APSI from RSA-PPIT
大致过程：
1. 对于Client端的每个元素，Client计算一个$\mu$，发送给Server
2. Server对于每个$\mu$和Server的每个元素，计算一个t；另外，Server还生成一个数Z，这个数与用于计算t的随机数有关。最后把Z和t都发给Client
3. Client利用Z，对自己的每一个元素计算$t^\prime$，比较$t^\prime$和t的交集

具体过程：
![[Pasted image 20230516210722.png]]

### APSI with Linear Costs
This protocol incurs **linear** computation (for both parties) and communication complexity.

具体过程：
![[Pasted image 20230516211241.png]]

### Deriving Efficient PSI
从上一个方法获得对应的PSI版本

具体过程：
![[Pasted image 20230516211357.png]]

### 最终结果：More Efficient PSI
引入预处理操作，减轻计算负担

具体过程：
![[Pasted image 20230516211539.png]]

#### 缺点：
1. Although very efficient, this PSI protocol has some issues. First, it is unclear how to convert it into an APSI version.
2. If precomputation is somehow impossible, its performance becomes worse than that of the PSI protocol