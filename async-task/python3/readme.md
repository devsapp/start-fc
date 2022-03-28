# 阿里云函数计算 Python3.6 Async Task 函数案例

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

- [:octocat: 源代码](https://github.com/devsapp/start-fc/tree/master/async-task/python3/src)

## 通过应用中心部署

<appcenter>

您可以在阿里云 [:earth_asia: Serverless 应用中心](https://fcnext.console.aliyun.com/applications/create?template=start-async-task-python3) ，快速体验该应用：   

[![Deploy with Severless Devs](https://img.alicdn.com/imgextra/i1/O1CN01w5RFbX1v45s8TIXPz_!!6000000006118-55-tps-95-28.svg)](https://fcnext.console.aliyun.com/applications/create?template=start-async-task-python3) 

</appcenter>

## 通过命令行工具部署

> 在开始之前，需要先安装 Serverless Devs 开发者工具：`npm install @serverless-devs/s -g`，更多安装方法，可以参考[Serverless Devs 安装文档](https://www.serverless-devs.com/serverless-devs/install) ，针对阿里云还需要配置密钥信息，配置密钥信息的方法可以参考[阿里云密钥配置文档](https://www.serverless-devs.com/fc/config)

- 初始化项目：`s init start-async-task-python3 -d start-async-task-python3`    
    > 涉及到确定密钥的选择、服务名称的确定、函数名称的确定以及容器镜像的确定    
- 进入项目：`cd start-async-task-python3`
- 部署项目：`s deploy -y`
- 调用函数：
   - 1. `s async-task invoke -e {} --invocation-type async`,  成功调用一次 task 函数， 预计 30s 后， 函数执行成功， 会触发调用dest-succ 函数一次 
   - 2. `s async-task invoke -e {"mock_error":1} --invocation-type async`, 调用一次 task 函数, 预期让 task 函数执行失败一次，会触发调用 dest-fail 函数一次  
   - 3. `s async-task invoke -e {} --invocation-type async`,  成功调用一次 task 函数， 在函数执行过程中，在控制台取消这次任务函数的执行， 会触发调用 dest-fail 函数一次  


## 通过阿里云CloudShell部署

如果您不想在应用中心中快速体验，也不想下载命令行工具体验，您也可以在[ :rocket:  阿里云 CloudShell](https://api.aliyun.com/new#/tutorial?action=git_open&git_repo=https://github.com/devsapp/start-fc.git&tutorial=async-task/python3/cloudshell.md) 中快速体验。

# 应用详情

本应用仅作为学习和参考使用，您可以基于本项目进行二次开发和完善，实现自己的业务逻辑

# 关于我们

- Serverless Devs 工具：
    - 仓库：[https://www.github.com/serverless-devs/serverless-devs](https://www.github.com/serverless-devs/serverless-devs)    
      > 欢迎帮我们增加一个 :star2: 
    - 官网：[https://www.serverless-devs.com/](https://www.serverless-devs.com/)
- 阿里云函数计算组件：
    - 仓库：[https://github.com/devsapp/fc](https://github.com/devsapp/fc)
    - 帮助文档：[https://www.serverless-devs.com/fc/readme](https://www.serverless-devs.com/fc/readme)
- 钉钉交流群：33947367    