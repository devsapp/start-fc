'use strict';
exports.handler = (event, context, callback) => {
  const eventObj = JSON.parse(event);
  console.log(`receive event: ${JSON.stringify(eventObj)}`);

  let body = 'Hello World!';
  // get http request body
  if ("body" in eventObj) {
    body = eventObj.body;
    if (eventObj.isBase64Encoded) {
      body = Buffer.from(body, 'base64').toString('utf-8');
    }
  }
  console.log(`receive http body: ${body}`);

  callback(null, {
    'statusCode': 200,
    'body': body
  });
}