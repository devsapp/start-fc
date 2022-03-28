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
      1. [actions] are declared in s.yaml, execute before deployment
         If you don't need to build the project every time, or you don't need to build before deployment, or you have built it manually, you can comment out this part
         > PS: When deploying, you also need to modify the image field in s.yaml to configure the address for your own acr
      2. The Serverless Devs version required by the current project is at least v2.0.103. You can view the current version through [s -v] and upgrade the version through [npm install -g @serverless-devs/s].
    * After the project is initialized, you can directly enter the project directory and use s deploy to deploy the project
    \n`)
}

module.exports = {
    postInit,
    preInit
}
