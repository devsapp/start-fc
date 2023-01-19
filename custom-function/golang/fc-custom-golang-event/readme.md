# fc-custom-golang-event 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-custom-golang-event&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc-custom-golang-event" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-custom-golang-event&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc-custom-golang-event" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-custom-golang-event&type=packageDownload">
  </a>
</p>

<description>

快速部署一个基于custom runtime 的 Golang Event 类型的 Hello World 到阿里云函数计算

</description>

<table>

## 前期准备
使用该项目，推荐您拥有以下的产品权限 / 策略：

| 服务/业务 | 函数计算 |     
| --- |  --- |   
| 权限/策略 | AliyunFCFullAccess |  

</table>

<codepre id="codepre">

# 代码 & 预览

- [ :smiley_cat:  源代码](https://github.com/devsapp/start-fc/blob/main/custom-function/golang/fc-custom-golang-event)

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

-  :fire:  通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=fc-custom-golang-event) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=fc-custom-golang-event)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init fc-custom-golang-event -d fc-custom-golang-event`   
    - 进入项目，并进行项目部署：`cd fc-custom-golang-event && s deploy -y`

> 注意: s deploy 之前的 actions 中 pre-deploy 中完成了编译， 如果编译过程中 go mod 下载很慢，可以考虑使用国内 go proxy 代理 [https://goproxy.cn/](https://goproxy.cn/)

</deploy>

<appdetail id="flushContent">

# 应用详情

本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑

## 如何本地调试
直接根据您的平台完成编译， 然后将目标二进制运行起来， 其实本质是启动了一个 http server，然后对这个  http server 发动 http 请求即可

**build**

```bash
$ cd code

# linux
$ GOOS=linux GOARCH=amd64 CGO_ENABLED=0 go build -o target/main main.go

# mac
$ GOOS=darwin GOARCH=amd64 CGO_ENABLED=0 go build -o target/main main.go

# windows
$ GOOS=windows GOARCH=amd64 CGO_ENABLED=0 go build -o target/main main.go
```

**debug**

``` bash
# 打开一个终端， 运行 target/main
# 然后打开另外一个终端，curl 发 http 请求
$ curl 127.0.0.1:9000/invoke -d "my event" -H "x-fc-request-id:rid123456"
```

![](https://img.alicdn.com/imgextra/i4/O1CN019fgqet1haF7QDSTT3_!!6000000004293-2-tps-2338-358.png)

</appdetail>

<devgroup>

## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
|--- | --- | --- |
| <center>微信公众号：`serverless`</center> | <center>微信小助手：`xiaojiangwh`</center> | <center>钉钉交流群：`33947367`</center> | 

</p>

</devgroup>