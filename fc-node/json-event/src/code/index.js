exports.handler = function (event, context, callback) {
  var eventObj = JSON.parse(event.toString());
  callback(null, eventObj['key']);
};