<?php
use RingCentral\Psr7\Response;

/*
To enable the initializer feature (https://help.aliyun.com/document_detail/89029.html)
please implement the initializer function as below：
function initializer($context) {
    echo 'initializing' . PHP_EOL;
}
*/

function handler($request, $context): Response{
    /*
    $body       = $request->getBody()->getContents();
    $queries    = $request->getQueryParams();
    $method     = $request->getMethod();
    $headers    = $request->getHeaders();
    $path       = $request->getAttribute('path');
    $requestURI = $request->getAttribute('requestURI');
    $clientIP   = $request->getAttribute('clientIP');
    */

    return new Response(
        200,
        array(
            'custom_header1' => 'v1',
            'custom_header2' => ['v2', 'v3'],
        ),
        'hello world'
    );
}