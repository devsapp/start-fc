async function preInit(inputObj) {
    console.log(`
  Serverless Devs Application Case
    
    Cloud services required：
    - FC : https://fc.console.aliyun.com/
    - ACR: https://cr.console.aliyun.com/
    
    Tips：
    - FC Component: https://www.serverless-devs.com/fc/readme`)

    try {
        var process = require('child_process')
        const version = (await process.execSync('s -v')).toString()
        const versionNumber = version.match(/s: 2\.0\.(.*?),/)[1]
        if (Number(versionNumber) < 103) {
            console.log('\x1B[31m%s\x1B[0m', '    * The application requires that the version of Serverless Devs is at least 2.0.103')
            console.log('\x1B[31m%s\x1B[0m', '    * Plaese upgraded through [npm install -g @serverless-devs/s]\n\n')
        }
    } catch (e) {
        console.log(e)
        console.log(`    - Serverless Devs Version >= v2.0.103
        `)
    }
}

async function postInit(inputObj) {
    console.log(`
    * Before using, please check whether the actions command in Yaml file is available
    * Carefully reading the notes in s.yaml is helpful for the use of the tool
    * If need help in the use process, please apply to join the Dingtalk Group: 33947367
    `)
}

module.exports = {
    postInit,
    preInit
}
