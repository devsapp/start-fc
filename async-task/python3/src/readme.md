# 阿里云函数计算 Python 3.6 async task 案例

只需几步就可以快速在阿里云函数计算服务上体验 Python 3.6 的 async task：

- 初始化项目：`s init start-async-task-python3`
- 进入项目：`cd start-async-task-python3`
- 部署项目：`s deploy`
- 触发项目
  - 1. `s async-task invoke -e {} --invocation-type async`,  成功调用一次 task 函数， 预计 30s 后， 函数执行成功， 会触发调用dest-succ 函数一次 
  - 2. `s async-task invoke -e {"mock_error":1} --invocation-type async`, 调用一次 task 函数, 预期让 task 函数执行失败一次，会触发调用 dest-fail 函数一次  
  - 3. `s async-task invoke -e {} --invocation-type async`,  成功调用一次 task 函数， 在函数执行过程中，在控制台取消这次任务函数的执行， 会触发调用 dest-fail 函数一次  

即可实现`Python 3.6` async task 案例的初始化、部署整个流程。

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