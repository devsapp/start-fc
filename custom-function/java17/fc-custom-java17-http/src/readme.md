# fc-custom-java17-http 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-custom-java17-http&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc-custom-java17-http" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-custom-java17-http&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc-custom-java17-http" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-custom-java17-http&type=packageDownload">
  </a>
</p>

<description>

快速部署一个基于custom runtime 的 Java17 HTTP 类型的 Hello World 到阿里云函数计算

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

- [ :smiley_cat:  源代码](https://github.com/devsapp/start-fc/blob/main/custom-function/java8/fc-custom-java17-http)

</codepre>

<deploy>

## 部署 & 体验

<appcenter>

-  :fire:  通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=fc-custom-java17-http) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=fc-custom-java17-http)  该应用。 

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init fc-custom-java17-http -d fc-custom-java17-http`   
    - 进入项目，并进行项目部署：`cd fc-custom-java17-http && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情
[Custom Runtime](https://help.aliyun.com/document_detail/194660.html) 内置的是 Java8 和 Java11，可以通过 Layer 扩展 Runtime 到 

[Layer插件](https://github.com/devsapp/layer-fc)
```yaml
actions:
  pre-deploy:  # 在deploy之前运行
    - run: mvn package
      path: ./code
    - plugin: layer-fc
      args:
        customRuntime: java17
```
## 查看效果
1. 控制台上测试函数
  ![alt](https://img.alicdn.com/imgextra/i3/O1CN0143x0R91xDN9Gcb7yQ_!!6000000006409-2-tps-3304-1164.png)
2. 登录实例
   ![alt](https://img.alicdn.com/imgextra/i3/O1CN01tx8PZi1aD9nblsJwf_!!6000000003295-0-tps-3590-588.jpg)
3. 输入Java -version查看JDK版本
   ![alt](https://img.alicdn.com/imgextra/i1/O1CN01tDd7OR1ccvJTeAHY4_!!6000000003622-0-tps-2006-450.jpg)


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