async function preInit(inputObj) {
    console.log(`\n     ____  _     _ ___  _ _     _        _____ ____ 
    /  _ \\/ \\   / \\\\  \\/// \\ /\\/ \\  /|  /    //   _\\
    | / \\|| |   | | \\  / | | ||| |\\ ||  |  __\\|  /  
    | |-||| |_/\\| | / /  | \\_/|| | \\||  | |   |  \\__
    \\_/ \\|\\____/\\_//_/   \\____/\\_/  \\|  \\_/   \\____/
    `)
}

async function postInit(inputObj) {
    console.log(`\nThis application requires to open these services: 
         FC : https://fc.console.aliyun.com/
     
    * Additional note: 
      1. The Serverless Devs version required by the current project is at least v2.0.103. You can view the current version through [s -v] and upgrade the version through [npm install -g @serverless-devs/s].
    * After the project is initialized, you can directly enter the project directory and use s deploy to deploy the project
    \n`)
}

module.exports = {
    postInit,
    preInit
}
