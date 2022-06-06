from flask.logging import default_handler
import time
from flask import Flask
from flask import request
import json
import sys
import traceback
import logging


log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)


app = Flask(__name__)


REQUEST_ID_HEADER = 'x-fc-request-id'


@app.route('/initialize', methods=['POST'])
def init_invoke():
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Initialize Start RequestId: " + rid)
    # do your things

    print("FC Initialize End RequestId: " + rid)
    return "OK"


@app.route('/invoke', methods=['POST'])
def event_invoke():
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)

    data = request.stream.read()
    print(data)

    try:
        # do your things, for example:
        evt = json.loads(data)
        print(evt)
    except Exception as e:
        exc_info = sys.exc_info()
        trace = traceback.format_tb(exc_info[2])
        errRet = {
            "message": str(e),
            "stack": trace
        }
        print(errRet)
        print("FC Invoke End RequestId: " + rid +
              ", Error: Unhandled function error")
        return errRet, 404, [("x-fc-status", "404")]

    print("FC Invoke End RequestId: " + rid)

    return data


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=9000)
