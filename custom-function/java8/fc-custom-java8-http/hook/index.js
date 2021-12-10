async function preInit(inputObj) {
    console.log(`\n     ____  _     _ ___  _ _     _        _____ ____ 
    /  _ \\/ \\   / \\\\  \\/// \\ /\\/ \\  /|  /    //   _\\
    | / \\|| |   | | \\  / | | ||| |\\ ||  |  __\\|  /  
    | |-||| |_/\\| | / /  | \\_/|| | \\||  | |   |  \\__
    \\_/ \\|\\____/\\_//_/   \\____/\\_/  \\|  \\_/   \\____/`)
}

async function postInit(inputObj) {
    console.log(`\n    Welcome to the Aliyun FC start application
     This application requires to open these services: 
         FC : https://fc.console.aliyun.com/
     
     * 额外说明：s.yaml中声明了actions：
        部署前执行：mvn package
       如果不需要每次都构建项目，或者部署前不需要构建，或者已经手动构建了，可以注释掉这部分内容
     * 项目初始化完成，您可以直接进入项目目录下，并使用 s deploy 进行项目部署
     \n`)
}