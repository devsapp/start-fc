<?php

define('FC_LOG_TAIL_START_PREFIX', 'FC Invoke Start RequestId: '); // Start of invoke log tail mark
define('FC_LOG_TAIL_END_PREFIX', 'FC Invoke End RequestId: '); // End of invoke log tail mark

define('FC_INIT_LOG_TAIL_START_PREFIX', 'FC Initialize Start RequestId: '); // Start of init log tail mark
define('FC_INIT_LOG_TAIL_END_PREFIX', 'FC Initialize End RequestId: '); // End of init log tail mark

$http = new swoole_http_server("0.0.0.0", 9000);

$options = [
    'worker_num' => 4,
];

$http->set($options);

$http->on("start", function ($server) {
    echo "FC customruntime Swoole http server is started at http://0.0.0.0:9000" . PHP_EOL;
});

$http->on('shutdown', function ($server) {
    echo "FC customrutime Swoole http server shutdown" . PHP_EOL;
});

function handler($request, $response)
{
    $rid = $request->header["x-fc-request-id"];
    echo FC_LOG_TAIL_START_PREFIX . $rid . PHP_EOL;

    # do your things
    var_dump($request->rawContent());

    $response->header("Content-Type", "application/octet-stream");
    $response->end($request->rawContent());
    echo FC_LOG_TAIL_END_PREFIX . $rid . PHP_EOL;
}

function init($request, $response)
{
    $rid = $request->header["x-fc-request-id"];
    echo FC_INIT_LOG_TAIL_START_PREFIX . $rid . PHP_EOL;

    # do your things
    echo "init" . PHP_EOL;
    var_dump($request->rawContent());

    $response->header("Content-Type", "application/octet-stream");
    $response->end($request->rawContent());
    echo FC_INIT_LOG_TAIL_END_PREFIX . $rid . PHP_EOL;
}

$http->on("request", function ($request, $response) {
    $path = $request->server['request_uri'];
    if ($path == "/initialize") {
        init($request, $response);
    }
    if ($path == "/invoke") {
        handler($request, $response);
    }
});

$http->start();
