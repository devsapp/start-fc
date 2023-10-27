var OSSClient = require('ali-oss');

exports.handler = function (event, context, callback) {
  console.log(event.toString());

  var ossClient = new OSSClient({
    accessKeyId: context.credentials.accessKeyId,
    accessKeySecret: context.credentials.accessKeySecret,
    stsToken: context.credentials.securityToken,
    region: `oss-${context.region}`,
    bucket: process.env.BUCKET_NAME,
  });

  ossClient.put('myObj', Buffer.from('hello, fc', "utf-8")).then(function (res) {
    callback(null, 'put object');
  }).catch(function (err) {
    callback(err);
  });
};