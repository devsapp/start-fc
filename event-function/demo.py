dirList = [
    {
        "{{titleName}}": "Node.js14 Event",
        "{{appDir}}": "fc-custom-container-event-nodejs14",
        "{{appName}}": "start-fc-custom-container-event-nodejs14",
        "{{appTempDir}}": "start-cc-nodejs14",
        "{{details_en}}": "This application is only used for learning and reference. You can carry out secondary development and improvement based on this project to realize your own business logic.",
        "{{details_zh}}": "本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑",
        "{{invoke_zh}}": "s invoke -e '{\"key\":\"val\"}'",
        "{{invoke_en}}": "s invoke -e '{\"key\":\"val\"}'"
    },
{
        "{{titleName}}": "Python3.9 Event",
        "{{appDir}}": "fc-custom-container-event-python3.9",
        "{{appName}}": "start-fc-custom-container-event-python3.9",
        "{{appTempDir}}": "start-cc-python39-event",
        "{{details_en}}": "This application is only used for learning and reference. You can carry out secondary development and improvement based on this project to realize your own business logic.",
        "{{details_zh}}": "本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑",
        "{{invoke_zh}}": "s invoke -e '{\"key\":\"val\"}'",
        "{{invoke_en}}": "s invoke -e '{\"key\":\"val\"}'"
    },
{
        "{{titleName}}": "ASP.NET Core HTTP",
        "{{appDir}}": "fc-custom-container-http-aspdotnetcore",
        "{{appName}}": "start-fc-custom-container-http-aspdotnetcore",
        "{{appTempDir}}": "start-cc-aspdotnetcore-http",
        "{{details_en}}": "This application is only used for learning and reference. You can carry out secondary development and improvement based on this project to realize your own business logic.",
        "{{details_zh}}": "本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑",
        "{{invoke_zh}}": "直接使用 POST 或者 GET 方法 curl 部署项目时候生成自定义域名",
        "{{invoke_en}}": "Directly use POST or GET method curl to the custom domain name that is generated when deploying the project"
    },
{
        "{{titleName}}": "C++ HTTP",
        "{{appDir}}": "fc-custom-container-http-cpp",
        "{{appName}}": "start-fc-custom-container-http-cpp",
        "{{appTempDir}}": "start-cc-cpp-http",
        "{{details_en}}": """This application is a case of Alibaba Cloud Function Computing Custom Container C++ Event function. If you want to improve based on this application, you can modify the two function logics in `code/sample/src/handlers/echo_handler.cpp`:

- EchoHandler::OnInvoke
- EchoHandler::OnInitialize""",
        "{{details_zh}}": """该应用是阿里云函数计算 Custom Container C++ Event 函数案例，如果想要基于该应用进行完善，可以修改`code/sample/src/handlers/echo_handler.cpp`中的两个函数逻辑即可：

- EchoHandler::OnInvoke
- EchoHandler::OnInitialize""",
        "{{invoke_zh}}": "直接使用 POST 或者 GET 方法 curl 部署项目时候生成自定义域名",
        "{{invoke_en}}": "Directly use POST or GET method curl to the custom domain name that is generated when deploying the project"
    },
{
        "{{titleName}}": "Springboot",
        "{{appDir}}": "fc-custom-container-http-springboot",
        "{{appName}}": "start-fc-custom-container-http-springboot",
        "{{appTempDir}}": "start-cc-springboot",
        "{{details_en}}": "This application is only used for learning and reference. You can carry out secondary development and improvement based on this project to realize your own business logic.",
        "{{details_zh}}": "本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑",
        "{{invoke_zh}}": "直接使用 POST 或者 GET 方法 curl 部署项目时候生成自定义域名",
        "{{invoke_en}}": "Directly use POST or GET method curl to the custom domain name that is generated when deploying the project"
    },
{
        "{{titleName}}": "Golang Websocket",
        "{{appDir}}": "fc-custom-container-websocket-golang",
        "{{appName}}": "start-fc-custom-container-websocket-golang",
        "{{appTempDir}}": "start-cc-golang-websocket",
        "{{details_en}}": "This application is only used for learning and reference. You can carry out secondary development and improvement based on this project to realize your own business logic.",
        "{{details_zh}}": "本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑",
        "{{invoke_zh}}": "使用浏览器或者 Postman 进行调用",
        "{{invoke_en}}": "Invoke by browser or postman"
    },
{
        "{{titleName}}": "Python3.9 Websocket",
        "{{appDir}}": "fc-custom-container-websocket-python3.9",
        "{{appName}}": "start-fc-custom-container-websocket-python3.9",
        "{{appTempDir}}": "start-cc-python39-websocket",
        "{{details_en}}": "This application is only used for learning and reference. You can carry out secondary development and improvement based on this project to realize your own business logic.",
        "{{details_zh}}": "本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑",
        "{{invoke_zh}}": "使用浏览器或者 Postman 进行调用",
        "{{invoke_en}}": "Invoke by browser or postman"
    },
{
        "{{titleName}}": "Node.js14 Websocket",
        "{{appDir}}": "fc-custom-container-websocket-nodejs14",
        "{{appName}}": "start-fc-custom-container-websocket-nodejs14",
        "{{appTempDir}}": "start-cc-nodejs14-websocket",
        "{{details_en}}": "This application is only used for learning and reference. You can carry out secondary development and improvement based on this project to realize your own business logic.",
        "{{details_zh}}": "本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑",
        "{{invoke_zh}}": "使用浏览器或者 Postman 进行调用",
        "{{invoke_en}}": "Invoke by browser or postman"
    }
]

cloudshell = '''# 快速体验 Custom Container {{titleName}} 函数案例

欢迎您使用Serverless Devs开发者工具进行项目开发，本实验是基于Serverless Devs部署 Custom Container {{titleName}} 案例到阿里云函数计算。

整个实验过程包括：
- [下载工具](#下载工具)
- [配置密钥](#配置密钥)
- [初始化项目](#初始化项目)
- [部署项目](#部署项目)
- [更多信息](#更多信息)

> - [:octocat: 源代码](https://github.com/devsapp/start-fc/tree/master/custom-container-function/{{appDir}}/src)

## 下载工具

> 由于本系统已经默认集成了Serverless Devs，所以该步骤在本次试验中可以跳过

通过`npm`安装Serverless Devs开发者工具：

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
s init {{appName}} -d {{appTempDir}}
```

在初始化的过程中，可能涉及到部分服务的开通、参数的获取以及参数的定义，请根据命令行的提醒进行具体的操作。

## 部署项目

- 进入项目：`cd {{appTempDir}}`
- 进行项目的部署：`s deploy`

稍等片刻，即可完成项目的部署。

## 更多信息

- 组件仓库地址：https://github.com/devsapp/fc
- 组件帮助文档：https://www.serverless-devs.com/fc/readme
- Yaml参考文档：https://www.serverless-devs.com/fc/yaml/readme
- 关于：
    - Serverless Devs和FC组件的关系、如何声明/部署多个函数、超过50M的代码包如何部署
    - 关于.fcignore使用方法、工具中.s目录是做什么、函数进行build操作之后如何处理build的产物    
  等问题，可以参考文档：https://www.serverless-devs.com/fc/tips
- 关于如何做CICD等问题，可以参考：https://www.serverless-devs.com/serverless-devs/cicd
- 关于如何进行环境划分等问题，可以参考：https://www.serverless-devs.com/serverless-devs/extend

更多函数计算案例，可参考：https://github.com/devsapp/awesome/

> 有问题快来钉钉群问一下吧：33947367'''

readme_en = '''# Alibaba Cloud Function Compute Custom Container {{titleName}} function case

<toc>

<p align="center"><b> <a href="./readme.md"> 中文 </a> | English </b></p>

- [Quick start](#Quick-start)
    - [Deploy via command line tool](#Deploy-via-command-line-tools)
- [Application details](#Application-details)
- [About Us](#About-Us)

</toc>

# Quick start

- [:octocat: source](https://github.com/devsapp/start-fc/tree/master/custom-container-function/{{appDir}}/src)

## Deploy via command line tools

> Before starting, you need to install the Serverless Devs developer tools: `npm install @serverless-devs/s -g`, for more installation methods, please refer to [Serverless Devs Installation Documentation](https://www.serverless-devs.com/serverless-devs/install) , you also need to configure key information for Alibaba Cloud. For the method of configuring key information, please refer to [Alibaba Cloud Key Configuration Document](https://www.serverless-devs.com/fc/config)

- Initialize the project: `s init {{appName}} -d {{appTempDir}}`
    > It involves determining the selection of the key, the determination of the service name, the determination of the function name, and the determination of the container image
- Enter the project: `cd {{appTempDir}}`
- Deploy the project: `s deploy -y`
- Invoke function: {{invoke_en}}

# Application details

{{details_en}}

# About Us

- Serverless Devs Tools:
    - Repository: [https://www.github.com/serverless-devs/serverless-devs](https://www.github.com/serverless-devs/serverless-devs)
      > Welcome to add a :star2:
    - Official website: [https://www.serverless-devs.com/](https://www.serverless-devs.com/)
- Alibaba Cloud Function Compute components:
    - Repository: [https://github.com/devsapp/fc](https://github.com/devsapp/fc)
    - Help document: [https://www.serverless-devs.com/fc/readme](https://www.serverless-devs.com/fc/readme)
- Dingding communication group: 33947367'''

readme_zh = '''# 阿里云函数计算 Custom Container {{titleName}} 函数案例

<toc>

<p align="center"><b> 中文 | <a href="./readme_en.md"> English </a>  </b></p>

- [快速开始](#快速开始)
    - [通过应用中心部署](#通过应用中心部署)
    - [通过命令行工具部署](#通过命令行工具部署)
    - [通过阿里云CloudShell部署](#通过阿里云CloudShell部署)
- [应用详情](#应用详情)
- [关于我们](#关于我们)

</toc>

# 快速开始

- [:octocat: 源代码](https://github.com/devsapp/start-fc/tree/master/custom-container-function/{{appDir}}/src)

## 通过应用中心部署

<appcenter>

您可以在阿里云 [:earth_asia: Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template={{appName}}) ，快速体验该应用：   

[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template={{appName}}) 

</appcenter>

## 通过命令行工具部署

> 在开始之前，需要先安装 Serverless Devs 开发者工具：`npm install @serverless-devs/s -g`，更多安装方法，可以参考[Serverless Devs 安装文档](https://www.serverless-devs.com/serverless-devs/install) ，针对阿里云还需要配置密钥信息，配置密钥信息的方法可以参考[阿里云密钥配置文档](https://www.serverless-devs.com/fc/config)

- 初始化项目：`s init {{appName}} -d {{appTempDir}}`    
    > 涉及到确定密钥的选择、服务名称的确定、函数名称的确定以及容器镜像的确定    
- 进入项目：`cd {{appTempDir}}`
- 部署项目：`s deploy -y`
- 调用函数：{{invoke_zh}}

## 通过阿里云CloudShell部署

如果您不想在应用中心中快速体验，也不想下载命令行工具体验，您也可以在[ :rocket:  阿里云 CloudShell](https://api.aliyun.com/new#/tutorial?action=git_open&git_repo=https://github.com/devsapp/start-fc.git&tutorial=custom-container-function/{{appDir}}/cloudshell.md) 中快速体验。

# 应用详情

{{details_zh}}

# 关于我们

- Serverless Devs 工具：
    - 仓库：[https://www.github.com/serverless-devs/serverless-devs](https://www.github.com/serverless-devs/serverless-devs)    
      > 欢迎帮我们增加一个 :star2: 
    - 官网：[https://www.serverless-devs.com/](https://www.serverless-devs.com/)
- 阿里云函数计算组件：
    - 仓库：[https://github.com/devsapp/fc](https://github.com/devsapp/fc)
    - 帮助文档：[https://www.serverless-devs.com/fc/readme](https://www.serverless-devs.com/fc/readme)
- 钉钉交流群：33947367    '''


def doContent(content, source):
    for eveKey, eveValue in source.items():
        content = content.replace(eveKey, eveValue)
    return content


for eve in dirList:
    with open(eve["{{appDir}}"] + "/cloudshell.md", 'w') as f:
        f.write(doContent(cloudshell, eve))
    with open(eve["{{appDir}}"] + "/readme.md", 'w') as f:
        f.write(doContent(readme_zh, eve))
    with open(eve["{{appDir}}"] + "/readme_en.md", 'w') as f:
        f.write(doContent(readme_en, eve))
    with open(eve["{{appDir}}"] + "/src/readme.md", 'w') as f:
        f.write(doContent(readme_zh, eve))
    with open(eve["{{appDir}}"] + "/src/readme_en.md", 'w') as f:
        f.write(doContent(readme_en, eve))
