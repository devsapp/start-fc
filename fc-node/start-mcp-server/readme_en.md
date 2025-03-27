# Application development instructions

<p align="center"><b> <a href="./readme.md"> 中文 </a> | English </b></p>

> The development of Serverless Devs applications must strictly conform to the [application model specification](../../spec/en/0.0.2/serverless_package_model/3.package_model.md#Application-model-specification) in [Serverless Package Model](../../spec/en/0.0.2/serverless_package_model/readme.md). In the [application model specification](../../spec/en/0.0.2/serverless_package_model/3.package_model.md#Application-model-specification), the instructions on [application model metadata](../../spec/en/0.0.2/serverless_package_model/3.package_model.md#Application-model-metadata) are described.

The component development cases of Serverless Devs are integrated into the Serverless Devs CLI tool. You can use the CLI tool to initialize an application project that is not developed. Developers only need to run the s init command, and the following command output is returned:

```shell script
🚀  More applications: https://registry.serverless-devs.com
? Hello Serverless for Cloud Vendors (Use arrow keys or type to search)
❯ Alibaba Cloud Serverless
  AWS Cloud Serverless
  Tencent Cloud Serverless
  Baidu Cloud Serverless
  Dev Template for Serverless Devs
```

At this point, select `Dev Template for Serverless Devs` and hit enter:

```shell script
$ s init
🚀  More applications: https://registry.serverless-devs.com
? Hello Serverless for Cloud Vendors Dev Template for Serverless Devs
? Which template do you like? (Use arrow keys or type to search)
❯ Application Scaffolding
  Component Scaffolding
  Plugin Scaffolding
```

Now, select `Application Scaffolding` and hit enter to complete the initialization of a full Serverless Devs Application project. You can view the file tree with the following command:

```shell script
$ find . -print | sed -e 's;[^/]*/;|____;g;s;____|; |;g'
.
|____readme.md
|____version.md
|____publish.yaml
|____readme_en.md
|____src
| |____s.yaml
| |____code
| | |____index.js
| |____readme.md
```

In which:
| Directory | Meaning |
| --- | --- |
| readme.md | Description of the component, or help documentation |
| version.md | Description of the version, such as the content of the current version update |  
| publish.yaml | Required file for the project, the identification document for Serverless Devs Package development |
| src | The application directory, which needs to include `s.yaml` and related application code, etc. |

At this point, developers can complete the application development in the src directory and write the `publish.yaml` file for the project. After completion, the project can be published through the following steps:

- Change the `Version` field in `publish.yaml`. Make sure the version number is one higher than the existing highest version number, for example: 1.0.0 -> 1.0.1.

  > You can use a fixed dev version for continuous deployment of test versions.

- For the first publication, you must log in to the Serverless Devs Registry with the [registry](https://docs.serverless-devs.com/serverless-devs/command/registry) command.

  ```shell script
  s registry login
  ```

  Afterward, a browser window will pop up for login, and you can follow the prompts to proceed.

- Subsequently, simply executing `s registry publish` will publish the project.

- Testing Applications

  If you have deployed your application using the dev version, assuming your application name is start-application-v3, then you can use the following for testing:

  - Execute in local terminal: `s init start-application-v3@dev`
  - Open in the browser: https://fcnext.console.aliyun.com/applications/create?template=start-application-v3@dev
