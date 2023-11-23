
> 注：当前项目为 Serverless Devs 应用，由于应用中会存在需要初始化才可运行的变量（例如应用部署地区、函数名等等），所以**不推荐**直接 Clone 本仓库到本地进行部署或直接复制 s.yaml 使用，**强烈推荐**通过 `s init ${模版名称}` 的方法或应用中心进行初始化，详情可参考[部署 & 体验](#部署--体验) 。

# start-fc3-nodejs-json 帮助文档
<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc3-nodejs-json&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-fc3-nodejs-json" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc3-nodejs-json&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=start-fc3-nodejs-json" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=start-fc3-nodejs-json&type=packageDownload">
  </a>
</p>

<description>

快速部署一个 Node.JS 的解析JSON格式参数的函数到阿里云函数计算。

</description>

<codeUrl>

- [:smiley_cat: 代码](https://github.com/devsapp/start-fc/tree/V3/fc-node/helloworld/src)

</codeUrl>
<preview>



</preview>


## 前期准备

使用该项目，您需要有开通以下服务并拥有对应权限：

<service>



| 服务/业务 |  权限  |
| --- |  --- |
| 函数计算 |  AliyunFCFullAccess |

</service>

<remark>



</remark>

<disclaimers>



</disclaimers>

## 部署 & 体验

<appcenter>
   
- :fire: 通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-fc3-nodejs-json) ，
  [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-fc3-nodejs-json) 该应用。
   
</appcenter>
<deploy>
    
- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
  - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://docs.serverless-devs.com/fc/config) ；
  - 初始化项目：`s init start-fc3-nodejs-json -d start-fc3-nodejs-json`
  - 进入项目，并进行项目部署：`cd start-fc3-nodejs-json && s deploy -y`
   
</deploy>

## 应用详情

<appdetail id="flushContent">

当您传入JSON格式参数时，函数计算会透传参数内容,   函数代码自行解析， 该示例JSON格式事件的示例代码如下：

```nodejs
exports.handler = function(event, context, callback) {
  var eventObj = JSON.parse(event.toString());
  callback(null, eventObj['key']);
};
```

当您调用函数透传：

```json
{
  "key": "value"
}
```

函数执行成功后返回的结果为 value

</appdetail>

## 使用文档

<usedetail id="flushContent">
</usedetail>


<devgroup>


## 开发者社区

您如果有关于错误的反馈或者未来的期待，您可以在 [Serverless Devs repo Issues](https://github.com/serverless-devs/serverless-devs/issues) 中进行反馈和交流。如果您想要加入我们的讨论组或者了解 FC 组件的最新动态，您可以通过以下渠道进行：

<p align="center">  

| <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407298906_20211028074819117230.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407044136_20211028074404326599.png" width="130px" > | <img src="https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1635407252200_20211028074732517533.png" width="130px" > |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------- |
| <center>微信公众号：`serverless`</center>                                                                                         | <center>微信小助手：`xiaojiangwh`</center>                                                                                        | <center>钉钉交流群：`33947367`</center>                                                                                           |
</p>
</devgroup>

<testEvent>



| key |  value  |
| --- |  --- |

| key |  value |


</testEvent>
