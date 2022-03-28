# Alibaba Cloud Function Compute Custom Container C++ Event function case

<toc>

<p align="center"><b> <a href="./readme.md"> 中文 </a> | English </b></p>

- [Quick start](#Quick-start)
    - [Deploy via command line tool](#Deploy-via-command-line-tools)
- [Application details](#Application-details)
- [About Us](#About-Us)

</toc>

# Quick start

- [:octocat: source](https://github.com/devsapp/start-fc/tree/master/custom-function/cpp/fc-custom-cpp-event/src)

## Deploy via command line tools

> Before starting, you need to install the Serverless Devs developer tools: `npm install @serverless-devs/s -g`, for more installation methods, please refer to [Serverless Devs Installation Documentation](https://www.serverless-devs.com/serverless-devs/install) , you also need to configure key information for Alibaba Cloud. For the method of configuring key information, please refer to [Alibaba Cloud Key Configuration Document](https://www.serverless-devs.com/fc/config)

- Initialize the project: `s init start-fc-custom-container-event-cpp -d start-cc-event-cpp`
    > It involves determining the selection of the key, the determination of the service name, the determination of the function name, and the determination of the container image
- Enter the project: `cd start-cc-event-cpp`
- Deploy the project: `s deploy -y`
- Invoke function: `s invoke -e "{\"key\":\"val\"}"`

# Application details

This application is a case of Alibaba Cloud Function Computing Custom Container C++ Event function. If you want to improve based on this application, you can modify the two function logics in `code/sample/src/handlers/echo_handler.cpp`:

- EchoHandler::OnInvoke
- EchoHandler::OnInitialize

# About Us

- Serverless Devs Tools:
    - Repository: [https://www.github.com/serverless-devs/serverless-devs](https://www.github.com/serverless-devs/serverless-devs)
      > Welcome to add a :star2:
    - Official website: [https://www.serverless-devs.com/](https://www.serverless-devs.com/)
- Alibaba Cloud Function Compute components:
    - Repository: [https://github.com/devsapp/fc](https://github.com/devsapp/fc)
    - Help document: [https://www.serverless-devs.com/fc/readme](https://www.serverless-devs.com/fc/readme)
- Dingding communication group: 33947367