## install nsq
[docs and file](https://nsq.io/deployment/installing.html)

## nsq running
`nsq`安装后，配置环境变量或`cd`到`nsq`目录下， 在三个窗口分别执行以下命令：
```shell
nsqlookupd
```
```shell
nsqd
```
```shell
nsqadmin -nsqd-http-address 127.0.0.1:4151
# ui http://127.0.0.1:4171/nodes
```

## turing-ws running
添加配置文件`local_config.json`
```shell
go run *.go
```

## server

`websocket`需解析域名，在执行脚本的机器中配置
```shell
vi /etc/hosts
# add
127.0.0.1 dev.turing-ws.com
```

指定接受/发送`nsq`消息的`topic`
```shell
python app_read_msg.py
python send_app_user.py
```

### test
单队列测试
```shell
python run.py
```
并发测试
```shell
# 需手动修改具体并发数
python ws_stress.py
```