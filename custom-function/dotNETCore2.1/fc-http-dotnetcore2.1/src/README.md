# start-fc-http-aspdotnetcore2.1帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc-http-aspdotnetcore2.1&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-fc-http-aspdotnetcore2.1" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc-http-aspdotnetcore2.1&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-fc-http-aspdotnetcore2.1" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc-http-aspdotnetcore2.1&type=packageDownload">
  </a>
</p>

<description>

快速部署一个基于 custom runtime 的 .NET Core 2.1 Web API 应用到阿里云函数计算，并为该函数配置 Initializer 回调函数。本案例代码示例基于 .NET Core 2.1 官方 Web API 模版，即 `dotnet new webapi`

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

- [ :smiley_cat:  源代码](https://github.com/penghuima/fc-http-dotnetcore2.1)

</codepre>

<deploy>

## 快速部署 & 体验

通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init start-fc-http-aspdotnetcore2.1 -d start-fc-http-aspdotnetcore2.1`   
  - 进入项目，并进行项目部署：`cd start-fc-http-aspdotnetcore2.1 && s deploy -y`
  - 部署成功之后，可以看到 `system_url`,执行 `curl ${system_url}/api/values` 可看到 `["value1","value2"]` 输出,如下图所示:

  ![img_helloword](https://img.alicdn.com/imgextra/i4/O1CN01yAlmFc1H5OOdRFOZv_!!6000000000706-2-tps-1136-546.png)
</deploy>

<appdetail id="flushContent">

# 应用详情
### 应用概览
本案例将创建以下 API:
```c#
public class ValuesController : ControllerBase
{
    // POST /initialize
    [Route("initialize")]
    [HttpPost]
    public void Initialize()
    {
        Console.WriteLine("Hello initialize!");
    }

    // GET api/values
    [Route("api/values")]
    [HttpGet]
    public ActionResult<IEnumerable<string>> HandleRequest()
    {
        return new string[] { "value1", "value2" };
    }

}
```
### 
### 编译部署
> 根据自定义运行时 custom runtime 要求，我们需要保证自己的服务监听端口与 custom runtime 运行时监听端口保持一致,在本案例中我们在 Program.cs 中将端口设置为 9000,代码修改如下所示

  ```c#
  public static IWebHostBuilder CreateWebHostBuilder(string[] args) =>
              WebHost.CreateDefaultBuilder(args)
                  .UseUrls("http://0.0.0.0:9000")  //修改监听端口为 9000
                  .UseStartup<Startup>();
  ```

下面详细展开介绍执行 `s deploy -y` 都发生了什么
1. 编译项目
  ```yaml
      pre-deploy:   # 在deploy之前运行
        - run: dotnet publish -c Release -o ./target  # 要执行的系统命令，类似于一种钩子的形式
          path: ./dotnetcore2webapi        # 执行系统命令/钩子的路径
  ```
- 我们在部署项目之前通过 `dotnet publish -c Release -o ./target` 命令发布应用并将其输出到 `./target`目录下，其中 path字段的值是`./dotnetcore2webapi  ` 表示执行命令所在的路径。当 pre-deploy 命令执行完毕后，你可以在代码目录结构 `./dotnetcore2webapi /target/` 看到编译之后的输出文件如 `dotnetcore2webapi .dll` 等

2. 项目部署
```yaml
      function:
        name: "{{ functionName }}"
        description: "hello world by serverless devs"
        runtime: custom
        codeUri: ./dotnetcore2webapi           # 代码位置，即 dotnetApp/*
        layers:        # 层
          - acs:fc:${vars.region}:1431999136518149:layers/Dotnetcore21/versions/1
        customRuntimeConfig:           # 自定义运行时启动配置
          command:                     # 启动指令，示例值: ["/code/myserver"]
            - dotnet
          args:                        # 启动参数，示例值: ["-arg1", "value1"]
            - ./target/dotnetcore2webapi.dll
        memorySize: 128
        timeout: 60
        initializationTimeout: 20
        initializer: "true"   #开启初始化回调
        environmentVariables:  #为dotnetcore2.1 运行时添加运行时环境
          PATH: /opt/dotnet2:/usr/local/bin/apache-maven/bin:/usr/local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/local/ruby/bin
```
- 当编译项目之后，可以在 function 字段下配置函数，`runtime: custom` 表示函数运行时被设置为自定义运行时 custom,`codeUri: ./dotnetcore2webapi `表示代码目录所在位置，即 dotnetcore2webapi /*,函数代码运行时和代码都指定后，我们还需要设置函数启动命令及参数，很显然我们的启动命令及参数为 `dotnet ./target/dotnetcore2webapi .dll`
- 字段 `layers: ` 表示我们为函数配置的层，这里是通过层的方式来为函数提供 .NET Core 2.1 运行时环境，所以我们还需要在字段 `environmentVariables:` 为其配置 `PATH` 路径.有关层的更多信息，请移步[这里](https://help.aliyun.com/document_detail/181602.html)
- Initializer 回调函数，在Custom Runtime里如果想实现生命周期Initializer回调函数，需要在代码里实现 POST /initialize 路由，更多信息可查看 [函数实例生命周期回调](https://help.aliyun.com/document_detail/425056.html)。在本示例中陆游代码实现如下:

  ```c#
  // POST /initialize
  [Route("initialize")]
  [HttpPost]
  public void Initialize()
  {
      Console.WriteLine("Hello initialize!");
  }
  ```
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
- 测试 GET 方法来查看所有事件项,请求路径为 /api/values
  测试结果如下：
  ![img_get](https://img.alicdn.com/imgextra/i3/O1CN01IwUdGg1cJEI94nRvd_!!6000000003579-2-tps-3480-1674.png)
  
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