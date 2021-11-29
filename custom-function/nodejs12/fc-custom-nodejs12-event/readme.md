# 阿里云函数计算 Custom Node.js12 Event 函数案例

只需几步就可以快速在阿里云函数计算服务上体验一键部署一个 Node.js12 应用:

- 初始化项目：`s init fc-custom-nodejs12-event -d fc-custom-nodejs12-event`
- 进入项目：`cd fc-custom-nodejs12-event`
- 构建项目：`cd code && s build --use-docker && cd ..`
- 部署项目：`s deploy -y`
- 调用函数：`s invoke -e "hello"`

即可实现`Custom Node.js12` Event 函数案例的初始化、部署整个流程。

> 本应用仓库地址：https://github.com/devsapp/start-fc

------------------------------------
> # More
> 欢迎您使用阿里云函数计算 FC 组件进行项目开发   
> 组件仓库地址/帮助文档：https://github.com/devsapp/fc   
> Yaml参考文档：https://github.com/devsapp/fc/blob/main/docs/zh/yaml.md   
> 快速入门：
>   - 快速创建应用：https://github.com/devsapp/fc/blob/main/docs/zh/quick_start_application.md
>   - 快速使用命令：https://github.com/devsapp/fc/blob/main/docs/zh/quick_start_function.md
------------------------------------
