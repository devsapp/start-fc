# fc-custom-python-grpc 帮助文档

<p align="center" class="flex justify-center">
    <a href="https://www.serverless-devs.com" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-custom-golang-event&type=packageType">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc-custom-python-grpc" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-custom-golang-event&type=packageVersion">
  </a>
  <a href="http://www.devsapp.cn/details.html?name=fc-custom-python-grpc" class="ml-1">
    <img src="http://editor.devsapp.cn/icon?package=fc-custom-golang-event&type=packageDownload">
  </a>
</p>

<description>

快速部署一个基于custom runtime 的 python grpc demo

</description>

<table>

## 前期准备
使用该项目，推荐您拥有以下的产品权限 / 策略：

| 服务/业务 | 函数计算 |     
| --- |  --- |   
| 权限/策略 | AliyunFCFullAccess |
|产品/服务| 自定义域名、ssl证书|

</table>

<codepre id="codepre">

# 代码 & 预览

- [ :smiley_cat:  源代码](../fc-custom-python37-grpc)

</codepre>

<deploy>



## 部署 & 体验

<appcenter>

-  :fire:  通过 [Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=fc-custom-python-grpc) ，
   [![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=fc-custom-python-grpc)  该应用。

</appcenter>

- 通过 [Serverless Devs Cli](https://www.serverless-devs.com/serverless-devs/install) 进行部署：
    - [安装 Serverless Devs Cli 开发者工具](https://www.serverless-devs.com/serverless-devs/install) ，并进行[授权信息配置](https://www.serverless-devs.com/fc/config) ；
    - 获取项目并且填入相关信息：`s init fc-custom-python-grpc -d fc-custom-python-grpc`,自定义域名需要绑定账号对应region的fc endpoint
    - 进入项目`cd fc-custom-python-grpc`，将您的server端证书，server端私钥，ca根证书复制到当前目录，修改s.yaml中的server端证书`certificate: .\xxxxxx.pem`server端私钥`privateKey: .\xxxxxxkey.pem`
    - 进行项目部署：`cd  fc-custom-python-grpc && s build --use-docker `安装函数运行所需要的依赖，完成之后`s deploy`直接部署到fc
    - `cd code`进入代码目录，修改client端代码填入ca根证书的路径`ca_cert = open("../xxxxxxxx-root.cer", 'rb').read()`
    - 调用client端，向server端发起请求并且获得相应结果：`python greeter_client.py -addr {你的自定义域名}`
    - 若要试用grpc的其他模式，在client文档中修改注释即可
    - 若要修改配置，参考用户文档
      </deploy>

<appdetail id="flushContent">


# 应用详情



本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑



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