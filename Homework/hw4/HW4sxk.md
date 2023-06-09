# T3
a.攻击步骤：
- 在输入中输入abcdefghiabcdefghi\n
- 则由于使用gets，会覆盖str1中的内容，使得str1中的内容和str2中的内容相同，这样就算不知道密码也可以登录。
![](attack.png)

b.为了防止攻击者通过这种方式进行攻击，可以将gets改为fgets指定可以读取的位数，这样就可以避免上述安全问题。

# T4
首先设置ecx=0x5000，edx=0x899c将程序执行一遍，再将ecx改为ecx=0x6000将程序跑一遍。内存的值分别为：
```
0x9000=0x4000
0x9004=0x3333
0x9008=0x4000
0x900c=0x6666
```
这样就可以将0x3333写入0x6666。

# T5
```
uint32_t nlen, vlen; 
char buf[8264];

```
这里将nlen，vlen定义为unsigned int类型。
```
nlen = 8192;
if ( hdr->nlen <= 8192 ){
 nlen = hdr->nlen; 
}
memcpy(buf, hdr->ndata, nlen); 
buf[nlen] = ':';

```
这段代码检测```hdr->nlen```是否超过8192，若未超过则将其赋值给```nlen```并将```buf```中的```nlen```区域大小的位置分配给```hdr->ndata```。
```
vlen = hdr->vlen;
if (8192 - (nlen+1) <= vlen ){ /* DANGER */
 vlen = 8192 - (nlen+1);
}
memcpy(&buf[nlen+1], hdr->vdata, vlen);
buf[nlen + vlen + 1] = 0;
```
这段代码检测剩余的空间大小是否小于```vlen```，若小于则将```vlen```变为剩余空间的大小```8192 - (nlen+1)```并将```hdr->vdata```拷贝到这块空间中。
- 若此时nlen=8192，则vlen会等于-1，由于其为unsigned类型，则其值会变成0xffffffff。同时由于使用了memset，这将会导致缓冲区的溢出。
- 由于攻击者可以控制```hdr```，则只需将```hdr->nlen```设置为8192，且将```hdr->vlen```设置为大于0的值，即会导致缓冲区溢出。