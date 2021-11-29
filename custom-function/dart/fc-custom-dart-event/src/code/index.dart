import 'dart:io';
import 'dart:convert' show utf8;

final String REQUEST_ID_HEADER = 'x-fc-request-id';

Future handler(HttpRequest request) async {
  var rid = request.headers.value(REQUEST_ID_HEADER);
  print("FC Invoke Start RequestId: $rid");
  // do your things
  String content = await utf8.decodeStream(request);
  print(content);
  request.response.write("OK");

  await request.response.close();
  print("FC Invoke End RequestId: $rid");
}

Future init(HttpRequest request) async {
  var rid = request.headers.value(REQUEST_ID_HEADER);
  print("FC Initialize Start RequestId: $rid");
  // do your things
  print("init");
  request.response.write("init OK");

  await request.response.close();
  print("FC Initialize End RequestId: $rid");
}

Future main() async {
  var server = await HttpServer.bind(
    InternetAddress.anyIPv4,
    9000,
  );
  // #enddocregion bind
  print('FunctionCompute dart2.8 runtime inited!');
  print('Listening on *:${server.port}');

  // #docregion listen
  await for (HttpRequest request in server) {
    if (request.uri.path == "/initialize") {
      await init(request);
    }
    if (request.uri.path == "/invoke") {
      await handler(request);
    }
  }
}
