const WebSocket = require('ws');

const WebSocketServer = WebSocket.Server;

const wss = new WebSocketServer({
  host: "0.0.0.0",
  port: 9000
});

wss.on('connection', function (ws, req) {
  console.log(`[SERVER] connection()`);
  ws.on('message', function (message) {
    ws.send(`${message}`, (err) => {
      if (err) {
        console.log(`[SERVER] error: ${err}`);
      }
    });
  })
});