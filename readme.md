# 阿里云函数计算：FC 案例

![图片alt](https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1638188206727_20211129121647053051.png)

<p align="center"><b> 中文 | <a href="./readme_en.md"> English </a>  </b></p>

## 本地快速体验

通过该应用，您可以简单快速的创建一个 FC 案例到阿里云函数计算服务。

- 下载命令行工具：`npm install -g @serverless-devs/s`
- 初始化一个模版项目：`s init start-fc-http-python3`
- 进入项目后部署项目：`cd start-fc && s deploy`

## 包含内容

- Event函数（事件函数）
  - [fc-event-node.js6](event-function/fc-event-node.js6/src):`s init start-fc-event-nodejs6`
  - [fc-event-node.js8](event-function/fc-event-node.js8/src):`s init start-fc-event-nodejs8`
  - [fc-event-node.js10](event-function/fc-event-node.js10/src):`s init start-fc-event-nodejs10`
  - [fc-event-node.js12](event-function/fc-event-node.js12/src):`s init start-fc-event-nodejs12`
  - [fc-event-php7.2](event-function/fc-event-php7.2/src):`s init start-fc-event-php7`
  - [fc-event-python2.7](event-function/fc-event-python2.7/src):`s init start-fc-event-python2`
  - [fc-event-python3.6](event-function/fc-event-python3.6/src):`s init start-fc-event-python3`
  - [fc-event-java8](event-function/fc-event-java8/src):`s init start-fc-event-java8`
  - [fc-event-golang1.x](event-function/fc-event-golang1.x/src):`s init start-fc-event-golang1.x`
- HTTP函数
  - [fc-http-node.js6](http-function/fc-http-node.js6/src):`s init start-fc-http-nodejs6`
  - [fc-http-node.js8](http-function/fc-http-node.js8/src):`s init start-fc-http-nodejs8`
  - [fc-http-node.js10](http-function/fc-http-node.js10/src):`s init start-fc-http-nodejs10`
  - [fc-http-node.js12](http-function/fc-http-node.js12/src):`s init start-fc-http-nodejs12`
  - [fc-http-php7.2](http-function/fc-http-php7.2/src):`s init start-fc-http-php7`
  - [fc-http-python2.7](http-function/fc-http-python2.7/src):`s init start-fc-http-python2`
  - [fc-http-python3.6](http-function/fc-http-python3.6/src):`s init start-fc-http-python3`
  - [fc-http-java8](http-function/fc-http-java8/src):`s init start-fc-http-java8`
  - [fc-http-golang1.x](http-function/fc-http-golang1.x/src):`s init start-fc-http-golang1.x`
- Custom案例（自定义运行时）
  - Golang 
    - Event函数（事件函数） [fc-custom-golang-event](custom-function/golang/fc-custom-golang-event/src):`s init fc-custom-golang-event`
    - Websocket案例 [fc-custom-golang-websocket](custom-function/golang/fc-custom-golang-websocket/src):`s init fc-custom-golang-websocket`
  - Nodejs10 
    - Event函数（事件函数） [fc-custom-nodejs10-event](custom-function/nodejs10/fc-custom-nodejs10-event/src):`s init fc-custom-nodejs10-event`
    - Websocket案例 [fc-custom-nodejs10-websocket](custom-function/nodejs10/fc-custom-nodejs10-websocket/src):`s init fc-custom-nodejs10-websocket`
  - Nodejs12 
    - Event函数（事件函数） [fc-custom-nodejs12-event](custom-function/nodejs12/fc-custom-nodejs12-event/src):`s init fc-custom-nodejs12-event`
    - Websocket案例 [fc-custom-nodejs12-websocket](custom-function/nodejs12/fc-custom-nodejs12-websocket/src):`s init fc-custom-nodejs12-websocket`
  - PHP74-Swoole 
    - Event函数（事件函数） [fc-custom-php74-event](custom-function/php74/fc-custom-php74-event/src):`s init fc-custom-php74-event`
    - HTTP函数 [fc-custom-php74-http](custom-function/php74/fc-custom-php74-http/src):`s init fc-custom-php74-http`
  - Python37 
    - Event函数（事件函数） [fc-custom-python37-event](custom-function/python37/fc-custom-python37-event/src):`s init fc-custom-python37-event`
    - HTTP函数  [fc-custom-python37-http](custom-function/python37/fc-custom-python37-http/src):`s init fc-custom-python37-http`
    - Webscoket案例  [fc-custom-python37-websocket](custom-function/python37/fc-custom-python37-websocket/src):`s init fc-custom-python37-websocket`
  - C++
    - Event函数（事件函数） [fc-custom-cpp-event](custom-function/cpp/fc-custom-cpp-event/src):`s init fc-custom-cpp-event`
    - HTTP函数  [fc-custom-cpp-http](custom-function/cpp/fc-custom-cpp-http/src):`s init fc-custom-cpp-http`
  - Java8-SpringBoot [fc-custom-java8-http](custom-function/java8/fc-custom-java8-http/src):`s init fc-custom-java8-http`
  - Ruby [fc-custom-ruby-event](custom-function/ruby/fc-custom-ruby-event/src):`s init fc-custom-ruby-event`
  - Powershell [fc-custom-powershell-event](custom-function/powershell/fc-custom-powershell-event/src):`s init fc-custom-powershell-event`
  - F# [fc-custom-fsharp-http](custom-function/f#/fc-custom-fsharp-http/src):`s init fc-custom-fsharp-http`
  - TypeScript [fc-custom-typescript-event](custom-function/typescript/fc-custom-typescript-event/src):`s init fc-custom-typescript-event`
  - Lua [fc-custom-lua-event](custom-function/lua/fc-custom-lua-event/src):`s init fc-custom-lua-event`
  - Dart [fc-custom-dart-event](custom-function/dart/fc-custom-dart-event/src):`s init fc-custom-dart-event`
  - Rust [fc-custom-rust-event](custom-function/rust/fc-custom-rust-event/src):`s init fc-custom-rust-event`
- Custom Container案例（自定义容器镜像运行时）
  - Event函数（事件函数）
      - [fc-custom-container-event-cpp](custom-container-function/fc-custom-container-event-cpp/src):`s init start-fc-custom-container-event-cpp`
      - [fc-custom-container-event-nodejs14](custom-container-function/fc-custom-container-event-nodejs14/src):`s init start-fc-custom-container-event-nodejs14`
      - [fc-custom-container-event-python3.9](custom-container-function/fc-custom-container-event-python3.9/src):`s init start-fc-custom-container-event-python3.9`
  - HTTP函数
      - [fc-custom-container-http-cpp](custom-container-function/fc-custom-container-http-cpp/src):`s init start-fc-custom-container-http-cpp`
      - [fc-custom-container-http-springboot](custom-container-function/fc-custom-container-http-springboot/src):`s init start-fc-custom-container-http-springboot`
      - [fc-custom-container-http-aspdotnetcore](custom-container-function/fc-custom-container-http-aspdotnetcore/src):`s init start-fc-custom-container-http-aspdotnetcore`
  - Websocket案例
      - [fc-custom-container-websocket-golang](custom-container-function/fc-custom-container-websocket-golang/src):`s init start-fc-custom-container-websocket-golang`
      - [fc-custom-container-websocket-nodejs14](custom-container-function/fc-custom-container-websocket-nodejs14/src):`s init start-fc-custom-container-websocket-nodejs14`
      - [fc-custom-container-websocket-python3.9](custom-container-function/fc-custom-container-websocket-python3.9/src):`s init start-fc-custom-container-websocket-python3.9`
- 任务
  - [Python3](async-task/python3/src):`s init start-async-task-python3`

---

> - Serverless Devs 项目：https://www.github.com/serverless-devs/serverless-devs
> - Serverless Devs 文档：https://www.github.com/serverless-devs/docs
> - Serverless Devs 钉钉交流群：33947367
