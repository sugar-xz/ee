# OpenApi

OpenApi线上部署相关

- 使用`nodejs`部署（之前使用`docker`）
- 使用`pm2`管理`node`(本地运行可不使用pm2)
- 基于`swagger-ui`下`dist`进行修改

## 运行

#### 1. 安装测试环境

```shell
sudo apt install nodejs
sudo apt install npm
sudo npm i pm2 -g
```

#### 2. 搭建node环境

```shell
mkdir openapi
cd openapi/
npm init
npm install express
touch index.js
```

```js
# index.js
var express = require('express');
var app = express();
app.use('/openapi', express.static('dist'));
app.get('/', function (req, res) {
  res.send('Hello World!');
});
app.listen(3000, function () {
  console.log('Example app listening on port 3000!');
});
```

#### 3. swagger-ui
`swagger-ui`自行在`GitHub`下载

修改`dist`目录下下`index.html`，如下
```html
<script>
    window.onload = function() {
		var promise = new Promise(function(resolve, reject){
			var url = "openapi/urls.json"
			var request = new XMLHttpRequest();
			request.open("get", url);
			request.send(null);
			request.onload = function(){
				if (request.status ==200){
					var json = JSON.parse(request.responseText);
					console.log(json);
					resolve(json);
				}
			}
		});
		
		promise.then(function(json){
			// Begin Swagger UI call region
		  const ui = SwaggerUIBundle({
			urls: json,
			dom_id: '#swagger-ui',
			deepLinking: true,
			presets: [
			  SwaggerUIBundle.presets.apis,
			  SwaggerUIStandalonePreset
			],
			plugins: [
			  SwaggerUIBundle.plugins.DownloadUrl
			],
			layout: "StandaloneLayout"
		  })
		  // End Swagger UI call region

		})
		
		
      
      window.ui = ui
    }
	function changeJsonSrc() {
		var urlBox = document.getElementsByClassName('download-url-input')[0];
		var btn = document.getElementsByClassName('download-url-button')[0];
		urlBox.value = child.options[child.selectedIndex].value;
		window.ui.specActions.updateUrl(urlBox.value); //添加这里可以
		btn.click();
	}

  </script>
```
把`dist`目录拷贝到第二步`node`创建的`openapi`目录下！！！

### 启动
首先，拉取最新的`website_docs`代码，把`references/openapi`拷贝到第二步的`openapi/dist`目录下。

```shell script
cd openapi
# 直接启动
node index.js
# pm2管理启动
pm2 start index.js
```