'use strict';

// Constants
const PORT = 9000;
const HOST = '0.0.0.0';
const REQUEST_ID_HEADER = 'x-fc-request-id'

const express = require('express');
const app = express();
app.use(express.raw());

app.post('/initialize', (req, res) => {
  // console.log(JSON.stringify(req.headers));
  var rid = req.headers[REQUEST_ID_HEADER]
  console.log(`FC Initialize Start RequestId: ${rid}`)
  // do your things
  res.send('Hello FunctionCompute, initialize \n');
  console.log(`FC Initialize End RequestId: ${rid}`)
});

// invocation
app.post('/invoke', (req, res) => {
  // console.log(JSON.stringify(req.headers));
  var rid = req.headers[REQUEST_ID_HEADER]
  console.log(`FC Invoke Start RequestId: ${rid}`)
  console.log("hello world!");
  res.send('hello world!');
  console.log(`FC Invoke End RequestId: ${rid}`)
});

var server = app.listen(PORT, HOST);
console.log(`Running on http://${HOST}:${PORT}`);

server.timeout = 0; // never timeout
server.keepAliveTimeout = 0; // keepalive, never timeout