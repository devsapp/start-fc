# Alibaba Cloud Function Computing Custom Container Node.JS 14 Event function

You can quickly experience one-click deployment of a Node.JS 14 application on Alibaba Cloud Function Computing Service in just a few steps:

- Initialize the project: `s init start-fc-custom-container-event-nodejs14 -d start-cc-nodejs14`
- Enter the project: `cd start-cc-nodejs14`
- Modify Image in s.yaml to be your own ACR mirror address
- Deployment project: `s deploy -y`
- Invoke function: `s invoke -e "{\"key\":\"val\"}"`

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