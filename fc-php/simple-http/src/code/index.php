<?php

function handler($event, $context) {
  $logger = $GLOBALS['fcLogger'];
  $logger->info('hello world');
  $logger->info('receive event: ' . $event);
  
  try {
    $evt = json_decode($event, true);
    if (is_null($evt['body'])) {
      return "The request did not come from an HTTP Trigger, event: " . $event;
    }
    $body = $evt['body'];
    if ($evt['isBase64Encoded']) {
      $body = base64_decode($evt['body']);
    }
    return array(
      "statusCode" => 200,
      'headers' => array("Content-Type" => "text/plain"),
      'isBase64Encoded' => false,
      "body" => $body
    );
  } catch (Exception $e) {
      $logger->error("Caught exception: " . $e->getMessage());
      return "The request did not come from an HTTP Trigger, event: " . $event;
  }
}