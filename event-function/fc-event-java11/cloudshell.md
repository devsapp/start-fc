# 快速体验 Java11 Event 函数案例

欢迎您使用 Serverless Devs 开发者工具进行项目开发，本实验是基于 Serverless Devs 部署 Java11 Event 案例到阿里云函数计算。

整个实验过程包括：

- [下载工具](#下载工具)
- [配置密钥](#配置密钥)
- [初始化项目](#初始化项目)
- [部署项目](#部署项目)
- [更多信息](#更多信息)

> - [:octocat: 源代码](https://github.com/devsapp/start-fc/tree/main/event-function/fc-event-java11/src)

## 下载工具

> 由于本系统已经默认集成了 Serverless Devs，所以该步骤在本次试验中可以跳过

通过`npm`安装 Serverless Devs 开发者工具：

```
npm install -g @serverless-devs/s
```

除了上述的安装方法之外，您还可以参考[Serverless Devs Cli 安装文档](https://www.serverless-devs.com/serverless-devs/install) 查看更多安装方法。

## 配置密钥

> 由于本系统已经配置了密钥信息，所以该步骤在本次试验中可以跳过

配置阿里云账号的 AccessKeyID, AccessKeySecret 以及密钥别名。

配置方法可以通过`s config add`指令，选择`Alibaba Cloud`并根据提示进行配置。

除了上述的配置方法之外，您还可以参考[Serverless Devs 配置阿里云密钥信息](https://www.serverless-devs.com/fc/config) 查看更多密钥配置方法。

## 初始化项目

进行项目初始化：

```
s init start-fc-event-java11 -d start-fc-event-java11
```

在初始化的过程中，可能涉及到部分服务的开通、参数的获取以及参数的定义，请根据命令行的提醒进行具体的操作。

## 部署项目

- 进入项目：`cd start-fc-event-java11`
- 进行项目的部署：`s deploy`

稍等片刻，即可完成项目的部署。

## 更多信息

- 组件仓库地址：https://github.com/devsapp/fc
- 组件帮助文档：https://www.serverless-devs.com/fc/readme
- Yaml 参考文档：https://www.serverless-devs.com/fc/yaml/readme
- 关于：
  - Serverless Devs 和 FC 组件的关系、如何声明/部署多个函数、超过 50M 的代码包如何部署
  - 关于.fcignore 使用方法、工具中.s 目录是做什么、函数进行 build 操作之后如何处理 build 的产物  
    等问题，可以参考文档：https://www.serverless-devs.com/fc/tips
- 关于如何做 CICD 等问题，可以参考：https://www.serverless-devs.com/serverless-devs/cicd
- 关于如何进行环境划分等问题，可以参考：https://www.serverless-devs.com/serverless-devs/extend

更多函数计算案例，可参考：https://github.com/devsapp/awesome/

> 有问题快来钉钉群问一下吧：33947367
