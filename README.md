# website_docs

标准产品APIServer相关文档

- api_tests API自动化测试脚本 [api test](https://docs.turingvideo.cn/best_practices/restful-api-test/)
- design API设计文档
- references API规范 (使用openAPI)


## 运行API自动化测试(python>3.6.0)

#### 1. 安装测试环境

```shell
pip install -r api_tests/requirements.txt
```

#### 2. 设置环境变量

```shell
export API_TEST_SERVER='http://local.turingvideo.cn:8000/api/v1/'
export API_TEST_USER='dev@turingvideo.net'
export API_TEST_PASS='find it yourself'
```

#### 3. 执行脚本

```shell
./run_api_test.py
```
