# Alibaba Cloud Function Computing Custom Container C++ HTTP function

You can quickly experience one-click deployment of a C++ application on Alibaba Cloud Function Computing Service in just a few steps:

- Initialize the project: `s init start-fc-custom-container-http-cpp -d start-cc-http-cpp`
- Enter the project: `cd start-cc-http-cpp`
- Modify Image in s.yaml to be your own ACR mirror address
- Deployment project: `s deploy -y`
- Invoke function: Directly use POST or GET method curl to the custom domain name that is generated when deploying the project

# Secondary development

Modify the two function logic in code/sample/src/handlers/echo_handler.cpp:

-EchoHttpHandler::OnInvoke
-EchoHttpHandler::OnInitialize

> This application warehouse address: https://github.com/devsapp/start-fc

------------------------------------
> # More
> Welcome to use Alibaba Cloud Function Compute FC component for project development
> 
> Component warehouse address/help document: https://github.com/devsapp/fc
> 
> Yaml reference documentation: https://github.com/devsapp/fc/blob/main/docs/zh/yaml.md
> 
> Quick start:
>   - Quickly create an application: https://github.com/devsapp/fc/blob/main/docs/zh/quick_start_application.md
>   - Quick use of commands: https://github.com/devsapp/fc/blob/main/docs/zh/quick_start_function.md
------------------------------------