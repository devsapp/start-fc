# Alibaba Cloud Function Compute Java8 HTTP function case

<toc>

<p align="center"><b> <a href="./readme.md"> 中文 </a> | English </b></p>

- [Quick start](#Quick-start)
    - [Deploy via command line tool](#Deploy-via-command-line-tools)
- [Application details](#Application-details)
- [About Us](#About-Us)

</toc>

# Quick start

- [:octocat: source](https://github.com/devsapp/start-fc/tree/main/custom-function/java8/fc-custom-java8-http/src)

## Deploy via command line tools

> Before starting, you need to install the Serverless Devs developer tools: `npm install @serverless-devs/s -g`, for more installation methods, please refer to [Serverless Devs Installation Documentation](https://www.serverless-devs.com/serverless-devs/install) , you also need to configure key information for Alibaba Cloud. For the method of configuring key information, please refer to [Alibaba Cloud Key Configuration Document](https://www.serverless-devs.com/fc/config)

- Initialize the project: `s init fc-custom-java8-http -d fc-custom-java8-http`
    > It involves determining the selection of the key, the determination of the service name, the determination of the function name, and the determination of the container image
- Enter the project: `cd fc-custom-java8-http`
- Deploy the project: `s deploy -y`
- Invoke function: Directly use POST or GET method curl to the custom domain name that is generated when deploying the project

# Application details

This application is only used for learning and reference. You can carry out secondary development and improvement based on this project to realize your own business logic.

# About Us

- Serverless Devs Tools:
    - Repository: [https://www.github.com/serverless-devs/serverless-devs](https://www.github.com/serverless-devs/serverless-devs)
      > Welcome to add a :star2:
    - Official website: [https://www.serverless-devs.com/](https://www.serverless-devs.com/)
- Alibaba Cloud Function Compute components:
    - Repository: [https://github.com/devsapp/fc](https://github.com/devsapp/fc)
    - Help document: [https://www.serverless-devs.com/fc/readme](https://www.serverless-devs.com/fc/readme)
- Dingding communication group: 33947367