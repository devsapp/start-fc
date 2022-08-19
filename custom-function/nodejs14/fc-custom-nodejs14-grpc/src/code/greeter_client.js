/*
 *
 * Copyright 2015 gRPC authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */

var PROTO_PATH = '../proto/helloworld.proto';

var parseArgs = require('minimist');
var grpc = require('@grpc/grpc-js');
var protoLoader = require('@grpc/proto-loader');
const fs = require("fs");
var packageDefinition = protoLoader.loadSync(
    PROTO_PATH,
    {keepCase: true,
     longs: String,
     enums: String,
     defaults: true,
     oneofs: true
    });
var hello_proto = grpc.loadPackageDefinition(packageDefinition).helloworld;

function main() {
  var argv = parseArgs(process.argv.slice(2), {
    string: 'target'
  });
  var target;
  if (argv.target) {
    target = argv.target;
  } else {
    target = 'xiaoyu.functioncompute.com:8089';
  }
  var ssl_creds = grpc.credentials.createSsl(fs.readFileSync('../Digicert-OV-DV-root.cer'));
  var client = new hello_proto.Greeter(target,
                                       ssl_creds);
  var user;
  if (argv._.length > 0) {
    user = argv._[0]; 
  } else {
    user = 'world';
  }
  client.sayHello({name: user}, function(err, response) {
      if(err != null){
          console.log('err : '+err);
      }
      else{
          console.log('response : '+ response.message);
      }
  });
}

main();
