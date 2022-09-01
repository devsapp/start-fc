# start-fc-custom-container-http-dotnet6 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc-custom-container-http-dotnet6&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-fc-custom-container-http-dotnet6" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc-custom-container-http-dotnet6&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-fc-custom-container-http-dotnet6" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc-custom-container-http-dotnet6&type=packageDownload">
  </a>
</p>

<description>

快速部署一个基于custom container runtime 的 .NET 6 HTTP 类型的 Hello World 到阿里云函数计算

</description>

<table>

## 前期准备
使用该项目，推荐您拥有以下的产品权限 / 策略：

| 服务/业务 | 函数计算 |     
| --- |  --- |   
| 权限/策略 | AliyunFCFullAccess<br/>AliyunContainerRegistryFullAccess |  

</table>

<codepre id="codepre">

# 代码 & 预览

- [ :smiley_cat:  源代码](https://github.com/devsapp/start-fc/blob/main/custom-container-function/fc-custom-container-http-dotnet6)

</codepre>

<deploy>

## 部署 & 体验

<!-- 
<appcenter>

-  :fire:  通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-fc-custom-container-http-dotnet6) ，
[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-fc-custom-container-http-dotnet6)  该应用。 

</appcenter>
-->

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 初始化项目：`s init start-fc-custom-container-http-dotnet6 -d start-fc-custom-container-http-dotnet6`   
    - 进入项目，并进行项目部署：`cd start-fc-custom-container-http-dotnet6 && s deploy -y`

</deploy>

<appdetail id="flushContent">

# 应用详情
本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑


## 应用概览
本案例使用 .NET 6 Runtime，通过命令 `dotnet new web` 创建一个空的web项目进行修改。

## 代码说明
代码详见 `./code/dotnet6-web-demo/Program.cs` 文件。

**注意**：在代码中设置了 web server的监听地址 `http://0.0.0.0:9000`, 
- 监听IP必须设为`0.0.0.0` 或 `*`
- 监听端口必须与函数配置中的端口保持一致，函数配置中端口默认为`9000`。

## 编译部署
通过执行 `s deploy -y` 命令进行编译和部署，会执行以下流程
1. 执行 `pre-deploy` 回调
该命令基于 `./code/Dockerfile` 制作运行镜像
```yaml
      pre-deploy:  # 在deploy之前运行
        - component: fc build --use-docker --dockerfile ./code/Dockerfile
```
2. 执行部署流程
该流程会首先将创建好的镜像推送到远端仓库中（在s.yaml中配置的镜像仓库地址），然后创建函数。
创建成功后，会生成自定义域名信息 `custom_domain`, 可以通过该域名进行测试。
![](https://img.alicdn.com/imgextra/i3/O1CN01l465Gh28x8Vcy9U6P_!!6000000007998-2-tps-1754-178.png)

## 测试
使用前面的域名进行测试，注意要访问 9000 端口.
```bash
# curl http://xxx:9000/
Hello World!
# curl http://xxx:9000/test
this is a test function.
```


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