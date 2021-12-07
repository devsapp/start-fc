# 阿里云函数计算 Custom Container C++ Event 函数案例

只需几步就可以快速在阿里云函数计算服务上体验 C++:

- 初始化项目：`s init start-fc-custom-container-event-cpp -d start-cc-event-cpp`
- 进入项目：`cd start-cc-event-cpp`
- 修改 s.yaml 中 Image 为自己的 ACR 镜像地址
- 部署项目：`s deploy -y`
- 调用函数：`s invoke -e "{\"key\":\"val\"}"`

即可实现`Custom Container C++` Event 函数案例的初始化、部署整个流程。

# 二次开发

修改 code/sample/src/handlers/echo_handler.cpp 中的两个函数逻辑即可：

- EchoHandler::OnInvoke
- EchoHandler::OnInitialize

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
