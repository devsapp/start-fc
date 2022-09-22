# start-fc-http-aspdotnetcore6 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc-http-aspdotnetcore6&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-fc-http-aspdotnetcore6" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc-http-aspdotnetcore6&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-fc-http-aspdotnetcore6" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc-http-aspdotnetcore6&type=packageDownload">
  </a>
</p>

<description>

快速部署一个基于 custom runtime 的 .NET6 Web API 应用到阿里云函数计算。本案例代码示例来源于 .NET6 官方 Web API 应用教程:[创建最小 Web API](https://docs.microsoft.com/zh-cn/aspnet/core/tutorials/min-web-api?view=aspnetcore-6.0&tabs=visual-studio#add-the-api-code)

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

- [ :smiley_cat:  源代码](https://github.com/penghuima/fc-http-aspdotnetcore6)

</codepre>

<deploy>

## 快速部署 & 体验

通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init start-fc-http-aspdotnetcore6 -d start-fc-http-aspdotnetcore6`   
  - 进入项目，并进行项目部署：`cd start-fc-http-aspdotnetcore6 && s deploy -y`
  - 部署成功之后，可以看到 `system_url`,执行 `curl ${system_url}` 可看到 `Hello World!` 输出
  ![img_helloword](https://img.alicdn.com/imgextra/i2/O1CN01zsjVIZ295NdP5Qk45_!!6000000008016-2-tps-761-234.png)
</deploy>

<appdetail id="flushContent">

# 应用详情
### 应用概览
本案例将创建以下 API:
![img_api](https://img.alicdn.com/imgextra/i4/O1CN01oCM0lE23UfoUOfO4J_!!6000000007259-2-tps-1744-642.png)
### 
### 编译部署
> 根据自定义运行时 custom runtime 要求，我们需要保证自己的服务监听端口与 custom runtime 运行时监听端口保持一致,在本案例中我们在 Program.cs 中将端口设置为 9000: `builder.WebHost.UseUrls("http://0.0.0.0:9000"); `

下面详细展开介绍执行 `s deploy -y` 都发生了什么
1. 编译项目
  ```yaml
      pre-deploy:   # 在deploy之前运行
        - run: dotnet publish -c Release -o ./target  # 要执行的系统命令，类似于一种钩子的形式
          path: ./TodoApi        # 执行系统命令/钩子的路径
        - plugin: layer-fc                # 与运行的插件 （可以通过s cli registry search --type Plugin 获取组件列表）
          args:                           # 插件的参数信息
            customRuntime: dotnet6
  ```
- 我们在部署项目之前通过 `dotnet publish -c Release -o ./target` 命令发布应用并将其输出到 `./target`目录下，其中 path字段的值是`./TodoApi ` 表示执行命令所在的路径。当 pre-deploy 命令执行完毕后，你可以在代码目录结构 `./TodoApi/target/` 看到编译之后的输出文件如 `TodoApi.dll` 等
- `layer-fc ` 是插件的一种，我们通过此插件可以使用 .NET6 运行时层，作为我们函数执行运行时。可以登陆函数计算控制台在函数配置中查看该层信息。
![img_layer](https://img.alicdn.com/imgextra/i4/O1CN01NwHOnN1wxLIRnEG40_!!6000000006374-2-tps-3514-366.png)

2. 项目部署
```yaml
      function:
        name: dotnet6api
        description: "hello world by serverless devs"
        runtime: custom
        codeUri: ./TodoApi           # 代码位置，即 TodoApi/*
        customRuntimeConfig:           # 自定义运行时启动配置
          command:                     # 启动指令，示例值: ["/code/myserver"]
            - dotnet
          args:                        # 启动参数，示例值: ["-arg1", "value1"]
            - ./target/TodoApi.dll
```
- 当编译项目之后，可以在 function 字段下配置函数，`runtime: custom` 表示函数运行时被设置为自定义运行时 custom,`codeUri: ./TodoApi`表示代码目录所在位置，即 TodoApi/*,函数代码运行时和代码都指定后，我们还需要设置函数启动命令及参数，很显然我们的启动命令及参数为 `dotnet ./target/TodoApi.dll`
3. 配置函数触发器
```yaml
      triggers:
        - name: httpTrigger
          type: http
          config:
            authType: anonymous
            methods:
              - GET
              - POST
              - PUT
              - DELETE
              - HEAD
```
通过以上字段配置就可以创建一个 HTTP 函数触发器。
### 代码测试
- 测试 POST 方法，请求路径为 /todoitems

  请求 Body 中输入待办事项的 JSON 格式内容
  ```JSON
  {
    "name":"walk dog",
    "isComplete":true
  }
  ```
  测试结果如下:
  ![img_post](https://img.alicdn.com/imgextra/i2/O1CN0103Ct2Z23tPCYWZ1SP_!!6000000007313-2-tps-3454-1972.png)
- 测试 PUT 方法，请求路径为 /todoitems/{id}
更新 ID 为 1 的待办事项并将其名称设置为 "feed fish":
  ```JSON
  {
    "id": 1,
    "name": "feed fish",
    "isComplete": false
  }
  ```
  成功响应返回 204 (无内容)
- 测试 GET 方法来查看所有事件项,请求路径为 /todoitems
  测试结果如下：
  ![img_get](https://img.alicdn.com/imgextra/i2/O1CN01W0zzWy1GEiqYvU9Ft_!!6000000000591-2-tps-3456-1578.png)
- 其它路由感兴趣小伙伴可以自己测试
  
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