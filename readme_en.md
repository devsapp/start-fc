# Alibaba Cloud：FC Cases

![图片alt](https://serverless-article-picture.oss-cn-hangzhou.aliyuncs.com/1638188206727_20211129121647053051.png)

<p align="center"><b> <a href="./readme.md"> 中文 </a> | English </b></p>

## Local quick experience

With this application, you can easily and quickly create an FC case to Alibaba Cloud Function Compute.

- Download the command line tool: `npm install -g @serverless-devs/s`
- Initialize a template project: `s init start-fc-http-python3`
- Deploy the project after entering the project: `cd start-fc && s deploy`

## Included

- Event Function
  - [fc-event-node.js6](event-function/fc-event-node.js6/src):`s init start-fc-event-nodejs6`
  - [fc-event-node.js8](event-function/fc-event-node.js8/src):`s init start-fc-event-nodejs8`
  - [fc-event-node.js10](event-function/fc-event-node.js10/src):`s init start-fc-event-nodejs10`
  - [fc-event-node.js12](event-function/fc-event-node.js12/src):`s init start-fc-event-nodejs12`
  - [fc-event-php7.2](event-function/fc-event-php7.2/src):`s init start-fc-event-php7`
  - [fc-event-python2.7](event-function/fc-event-python2.7/src):`s init start-fc-event-python2`
  - [fc-event-python3.6](event-function/fc-event-python3.6/src):`s init start-fc-event-python3`
  - [fc-event-java8](event-function/fc-event-java8/src):`s init start-fc-event-java8`
  - [fc-event-golang1.x](event-function/fc-event-golang1.x/src):`s init start-fc-event-golang1.x`
- HTTP Function
  - [fc-http-node.js6](http-function/fc-http-node.js6/src):`s init start-fc-http-nodejs6`
  - [fc-http-node.js8](http-function/fc-http-node.js8/src):`s init start-fc-http-nodejs8`
  - [fc-http-node.js10](http-function/fc-http-node.js10/src):`s init start-fc-http-nodejs10`
  - [fc-http-node.js12](http-function/fc-http-node.js12/src):`s init start-fc-http-nodejs12`
  - [fc-http-php7.2](http-function/fc-http-php7.2/src):`s init start-fc-http-php7`
  - [fc-http-python2.7](http-function/fc-http-python2.7/src):`s init start-fc-http-python2`
  - [fc-http-python3.6](http-function/fc-http-python3.6/src):`s init start-fc-http-python3`
  - [fc-http-java8](http-function/fc-http-java8/src):`s init start-fc-http-java8`
  - [fc-http-golang1.x](http-function/fc-http-golang1.x/src):`s init start-fc-http-golang1.x`
- Custom Cases（Custom Runtime）
  - Golang 
    - Event Function [fc-custom-golang-event](custom-function/golang/fc-custom-golang-event/src):`s init fc-custom-golang-event`
    - Websocket [fc-custom-golang-websocket](custom-function/golang/fc-custom-golang-websocket/src):`s init fc-custom-golang-websocket`
  - Nodejs10 
    - Event Function [fc-custom-nodejs10-event](custom-function/nodejs10/fc-custom-nodejs10-event/src):`s init fc-custom-nodejs10-event`
    - Websocket [fc-custom-nodejs10-websocket](custom-function/nodejs10/fc-custom-nodejs10-websocket/src):`s init fc-custom-nodejs10-websocket`
    -  Grpc  [fc-custom-golang-grpc](custom-function/golang/fc-custom-golang-grpc/src):`s init fc-custom-golang-grpc`
  - Nodejs12 
    - Event Function [fc-custom-nodejs12-event](custom-function/nodejs12/fc-custom-nodejs12-event/src):`s init fc-custom-nodejs12-event`
    - Websocket [fc-custom-nodejs12-websocket](custom-function/nodejs12/fc-custom-nodejs12-websocket/src):`s init fc-custom-nodejs12-websocket`
  - PHP74-Swoole 
    - Event Function [fc-custom-php74-event](custom-function/php74/fc-custom-php74-event/src):`s init fc-custom-php74-event`
    - HTTP Function [fc-custom-php74-http](custom-function/php74/fc-custom-php74-http/src):`s init fc-custom-php74-http`
  - Python37 
    - Event Function [fc-custom-python37-event](custom-function/python37/fc-custom-python37-event/src):`s init fc-custom-python37-event`
    - HTTP Function  [fc-custom-python37-http](custom-function/python37/fc-custom-python37-http/src):`s init fc-custom-python37-http`
    - Webscoket  [fc-custom-python37-websocket](custom-function/python37/fc-custom-python37-websocket/src):`s init fc-custom-python37-websocket`
  - C++
    - Event Function [fc-custom-cpp-event](custom-function/cpp/fc-custom-cpp-event/src):`s init fc-custom-cpp-event`
    - HTTP Function  [fc-custom-cpp-http](custom-function/cpp/fc-custom-cpp-http/src):`s init fc-custom-cpp-http`
  - Java8-SpringBoot [fc-custom-java8-http](custom-function/java8/fc-custom-java8-http/src):`s init fc-custom-java8-http`
  - Ruby [fc-custom-ruby-event](custom-function/ruby/fc-custom-ruby-event/src):`s init fc-custom-ruby-event`
  - Powershell [fc-custom-powershell-event](custom-function/powershell/fc-custom-powershell-event/src):`s init fc-custom-powershell-event`
  - F# [fc-custom-fsharp-http](custom-function/f#/fc-custom-fsharp-http/src):`s init fc-custom-fsharp-http`
  - TypeScript [fc-custom-typescript-event](custom-function/typescript/fc-custom-typescript-event/src):`s init fc-custom-typescript-event`
  - Lua [fc-custom-lua-event](custom-function/lua/fc-custom-lua-event/src):`s init fc-custom-lua-event`
  - Dart [fc-custom-dart-event](custom-function/dart/fc-custom-dart-event/src):`s init fc-custom-dart-event`
  - Rust [fc-custom-rust-event](custom-function/rust/fc-custom-rust-event/src):`s init fc-custom-rust-event`
- Custom Container Cases（Custom Container Runtime）
  - Event Function
      - [fc-custom-container-event-cpp](custom-container-function/fc-custom-container-event-cpp/src):`s init start-fc-custom-container-event-cpp`
      - [fc-custom-container-event-nodejs14](custom-container-function/fc-custom-container-event-nodejs14/src):`s init start-fc-custom-container-event-nodejs14`
      - [fc-custom-container-event-python3.9](custom-container-function/fc-custom-container-event-python3.9/src):`s init start-fc-custom-container-event-python3.9`
  - HTTP Function
      - [fc-custom-container-http-cpp](custom-container-function/fc-custom-container-http-cpp/src):`s init start-fc-custom-container-http-cpp`
      - [fc-custom-container-http-springboot](custom-container-function/fc-custom-container-http-springboot/src):`s init start-fc-custom-container-http-springboot`
      - [fc-custom-container-http-aspdotnetcore](custom-container-function/fc-custom-container-http-aspdotnetcore/src):`s init start-fc-custom-container-http-aspdotnetcore`
  - Websocket Function
      - [fc-custom-container-websocket-golang](custom-container-function/fc-custom-container-websocket-golang/src):`s init start-fc-custom-container-websocket-golang`
      - [fc-custom-container-websocket-nodejs14](custom-container-function/fc-custom-container-websocket-nodejs14/src):`s init start-fc-custom-container-websocket-nodejs14`
      - [fc-custom-container-websocket-python3.9](custom-container-function/fc-custom-container-websocket-python3.9/src):`s init start-fc-custom-container-websocket-python3.9`
  - No Web Server Function
     -  [fc-custom-container-no-web-server-event-env](custom-container-function/fc-custom-container-no-web-server-event-env)
     -  [fc-custom-container-no-web-server-event-fibonacci](custom-container-function/fc-custom-container-no-web-server-event-fibonacci)
- Task
  - [Python3](async-task/python3/src):`s init start-async-task-python3`
  
---

> - Serverless Devs Repo：https://www.github.com/serverless-devs/serverless-devs
> - Serverless Devs Docs：https://docs.serverless-devs.com
> - Serverless Devs Dingtalk Group：33947367
