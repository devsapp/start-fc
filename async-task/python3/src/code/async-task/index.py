# -*- coding: utf-8 -*-
import logging
import time
import json

# To enable the initializer feature (https://help.aliyun.com/document_detail/158208.html)
# please implement the initializer function as below：
# def initializer(context):
#   logger = logging.getLogger()
#   logger.info('initializing')


def handler(event, context):
    logger = logging.getLogger()
    logger.info('async task begin with event: {}'.format(event))

    evt = json.loads(event)
    if evt.get('mock_error'):
        raise Exception("An error occurred while the function was executing")

    # do your task, It could be transcoding a video
    # use a sleep 30s mock a task
    time.sleep(30)

    ret = {}
    return ret
