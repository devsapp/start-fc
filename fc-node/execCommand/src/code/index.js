'use strict';

var exec = require('child_process').exec;
exports.handler = (event, context, callback) => {
  console.log('start to execute a command');
  exec("ls -l", function (error, stdout, stderr) {
    callback(null, stdout);
  });
}