
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# start-mcp-server-python 帮助文档

<description>

基于 Python 的FC MCP SSE Server案例

</description>

<codeUrl>



</codeUrl>
<preview>



</preview>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>



| 服务/业务 |  权限  | 相关文档 |
| --- |  --- | --- |
| 函数计算 |  AliyunFCFullAccess | [帮助文档](https://help.aliyun.com/product/2508973.html) [计费文档](https://help.aliyun.com/document_detail/2512928.html) |

</service>

<remark>



</remark>

<disclaimers>



</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-mcp-server-python) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-mcp-server-python) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://docs.serverless-devs.com/user-guide/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://docs.serverless-devs.com/user-guide/install) ，并进行[授权信息配置]( https://docs.serverless-devs.com/user-guide/config) ；
  - 初始化项目：`s init start-mcp-server-python -d start-mcp-server-python`
  - 进入项目，并进行项目部署：`cd start-mcp-server-python && s deploy -y`
   
</deploy>

## 案例介绍

<appdetail id="flushContent">

基于 FastMCP 和 Starlette 构建的 Serverless 服务端事件(SSE)应用

## 功能特性

- 使用 FastMCP 框架实现 SSE 协议支持
- 集成 Starlette 高性能 ASGI 服务器
- 提供示例工具端点 `hello` 返回 "Hello World!"
- 支持阿里云函数计算部署

</appdetail>

## 使用流程

<usedetail id="flushContent">

### 环境要求

- Python ≥3.10
- pip 包管理工具

### 安装依赖

```bash
pip install -r requirements.txt
```

### 本地运行

```bash
uvicorn main:app --host 0.0.0.0 --port 9000
```

</usedetail>

## 注意事项

<matters id="flushContent">
</matters>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://img.alicdn.com/imgextra/i2/O1CN010Sk7sv1Xl6WuOb6uU_!!6000000002963-0-tps-666-662.jpg" width="130px" > | <img src="https://img.alicdn.com/imgextra/i4/O1CN010Vt5aw27VN5rJIguB_!!6000000007802-0-tps-668-630.jpg" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>
