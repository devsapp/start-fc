# 阿里云函数计算：FC 3.0 案例

![图片alt](https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1638188206727_20211129121647053051.png)

> 注意，如果您使用函数计算2.0，请切换到 V2 分支

## 本地快速体验

通过该应用，您可以简单快速的创建一个 FC 案例到阿里云函数计算服务。

- 下载命令行工具：`npm install -g @serverless-devs/s`
- 初始化一个模版项目：`s init start-fc3-python -d start-fc3-python`
- 进入项目后部署项目：`cd start-fc3-python && s deploy`

## 包含内容

### 标准 Runtime

#### nodejs

- [start-fc3-nodejs-es](./fc-node/hello-world-es/src) (ES Module)

- [start-fc3-nodejs](./fc-node/hello-world/src) (CommonJS Module)

- [start-fc3-nodejs-json](./fc-node/json-event/src)

- [start-fc3-nodejs-oss](./fc-node/oss-event/src)

- [start-fc3-nodejs-exec](./fc-node/exec-command/src)

- [start-fc3-nodejs-http](./fc-node/simple-http/src)

#### 其他

- [start-fc3-python](./fc-python/src)

- [start-fc3-java](./fc-java/src)

- [start-fc3-golang](./fc-golang/src)

- [start-fc3-dotnetcore](./fc-dotnetcore/src)

### Custom Runtime

- [start-fc3-custom-nodejs](./custom/nodejs/src)

- [start-fc3-custom-python](./custom/python/src)

- [start-fc3-custom-golang](./custom/golang/src)

- [start-fc3-custom-java](./custom/java/src)

### Custom Container

- [start-fc3-custom-container-nodejs](./custom-container/nodejs/src)

- [start-fc3-custom-container-python](./custom-container/python/src)

- [start-fc3-custom-container-golang](./custom-container/golang/src)

- [start-fc3-custom-container-java](./custom-container/java/src)

## Custom Domain

- [fc-custom-domain](./fc-custom-domain/src)


---
> - Serverless Devs 项目：https://www.github.com/serverless-devs/serverless-devs
> - Serverless Devs 钉钉交流群：33947367