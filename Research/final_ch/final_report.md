## introduction
隐私集合求交（PSI）是一种密码学技术，它可以让两个或多个参与方在不泄露各自集合中其他元素的情况下，找出他们的集合中共有的元素。PSI有许多应用场景，例如，两个医院可以使用隐私集合求交来确定他们的病人数据库中有哪些人患有相同的疾病，而不暴露其他病人的信息。隐私集合求交的主要挑战是如何在保证安全性和效率的同时，最小化通信开销和计算复杂度。APSI是一种隐私集合求交的变体，它要求参与方的集合中的元素必须由一个可信的第三方（如证书颁发机构）进行授权。APSI可以保证只有授权的元素才能参与交集计算，而未授权的元素不会泄露给对方。Emiliano De Cristofaro等人在Practical Private Set Intersection Protocols with Linear Complexity一文中对以往的APSI协议进行改进，提出了高效的PSI协议。我们编写代码实现了他们的协议。

但是，Emiliano De Cristofaro等人在论文中提及，他们设计的PSI协议的其中一个缺点是不知如何转为对应的APSI协议。为此，在Emiliano De Cristofaro等人的基础上，进行一系列数学推导，我们设计了基于第三方证书的APSI协议，并给出了我们的编程实现，并进行了一系列测试。结果表明，我们的协议能够完成APSI的功能。

## Experiment & Results

我们编程实现了Emiliano De Cristofaro等人的高效PSI协议，并在此基础上进行改进，编写了基于证书的APSI协议的代码。代码仓库位于https://github.com/Layotiver/apsi

我们基于了pycryptodome包的哈希，取大质数，取随机数等功能，编程实现了扩展欧几里得算法，求乘法逆元，RSA公私钥生成，RSA加密等算法。这部分代码位于myutils.py。

本次实验中，隐私集合的元素是英语单词，隐私集合求交即求出双方共有的单词。客户端和服务器端的单词分别保存在client_set.txt和server_set.txt中。其中客户端的单词为{text, corpus, from, language, approach, resource}，服务器端的单词为{This, is, quite, a, departure, from, the, earlier, approach, in, NLP, applications}。其中from和approach是双方共有的单词。隐私集合求交的结果会输出这两个单词在client集合里的下标，即2和4。对于哈希，我们使用sha256函数，并通过设置不同的salt值来产生不同的哈希函数。

### PSI协议
我们在psi包里实现了Emiliano De Cristofaro等人的PSI协议。其中Client类和Server类对于算法中的Client和Server。两个类都有off_line和on_line函数，对应协议中的离线和在线处理的部分。

运行main_psi_server.py后，服务端程序启动。服务端会先进行off_line操作，然后监听本地的12121端口，接收来自客户端的PSI请求。接着运行main_psi_client.py，客户端先进行off_line操作，然后将协议中的需要传输的数据发送到本地的12121端口。服务器收到数据后进行一系列处理，即协议中的on_line部分，再发回处理过的数据给客户端。客户端收到数据后也进行on_line部分的操作，最后算出双方共有的集合元素。

运行main_psi_client.py后，控制台打印出\[2,4\]，代表计算出隐私集合里第2个和第4个元素为共有的元素，结果正确。

![](img/0.png)

### APSI协议
Emiliano De Cristofaro等人的PSI协议无法验证客户端的隐私集合的真实性。比如，客户端可以谎称自己的集合里有单词departure（实际上并没有），经过上述PSI协议，最后客户端能够知道服务器端是否有departure这个单词。因此我们需要授权的隐私集合求交（APSI）。我们实现了一种基于可信第三方证书的APSI，它同样有着较高的效率，并且客户端的每个元素都带有CA的证书。

#### 正常集合求交过程
我们在apsi包里实现了基于证书的PSI协议，这包里同样有Client和Server类。另外，apsi包里还有一个CertificateAuthority类，用于给客户端的元素颁发证书。

同样的，运行main_apsi_server.py后，服务端程序启动。服务端会先进行off_line操作，然后监听本地的12122端口，接收来自客户端的APSI请求。接着运行main_apsi_client.py，客户端先进行off_line操作，这里客户端的offline操作需要传入一个CA实例用于颁发证书。之后客户端按照协议将需要传输的数据发送到本地的12122端口。服务器收到数据后先进行证书验证。证书验证无误后，服务器端便按照协议进行数据处理，最后将处理过的数据返回给客户端。客户端收到数据后也进行on_line部分的操作，最后算出双方共有的集合元素。若证书验证错误，则客户端会受到服务器端的报错信息。

运行main_apsi_client.py后，控制台打印出\[2,4\]，代表计算出隐私集合里第2个和第4个元素为共有的元素，结果正确。

![](img/1.png)

#### 客户端证书无效的情况
我们设计了客户端带上伪造证书的情况，测试服务器能否检测到证书造假。

运行main_apsi_client_mal.py，此时客户端的off_line操作传入的CA实例为None，客户端会生成一份全为0的假证书。同样将这些信息发送给服务器，并打印服务器的返回信息。控制台输出-1，即设定了服务器报错信息，测试成功。

![](img/2.png)