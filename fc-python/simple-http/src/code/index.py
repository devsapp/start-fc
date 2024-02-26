# -*- coding: utf-8 -*-
import logging
import json
import base64

def handler(event, context):
    logger = logging.getLogger()
    logger.info("receive event: %s", event)

    try:
        event_json = json.loads(event)
    except:
        return "The request did not come from an HTTP Trigger because the event is not a json string, event: {}".format(event)
    
    if "body" not in event_json:
        return "The request did not come from an HTTP Trigger because the event does not include the 'body' field, event: {}".format(event)
    req_body = event_json['body']
    if 'isBase64Encoded' in event_json and event_json['isBase64Encoded']:
        req_body = base64.b64decode(event_json['body']).decode("utf-8")

    return {
        'statusCode': 200,
        'headers': {'Content-Type': 'text/plain'},
        'isBase64Encoded': False,
        'body': req_body
    }
