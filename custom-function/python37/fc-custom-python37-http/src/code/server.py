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


@app.route('/', methods=['GET'])
def hello_world():
    rid = request.headers.get(REQUEST_ID_HEADER)
    print("FC Invoke Start RequestId: " + rid)
    # do your things
    print("FC Invoke End RequestId: " + rid)
    return 'Hello World!'


@app.route('/event', methods=['POST'])
def event():
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

# 没有使用自定义域名， 直接使用 fc system 生成的 http url 或者本地调试 s local start
# 访问函数的时候能正确访问到 path


class CustomProxyFix(object):
    def __init__(self, app):
        self.app = app

    def __call__(self, environ, start_response):
        host = environ.get('HTTP_HOST', '')
        region = environ.get('HTTP_X_FC_REGION', '')
        uid = environ.get('HTTP_X_FC_ACCOUNT_ID', '')
        serviceName = environ.get('HTTP_X_FC_SERVICE_NAME', '')
        functionName = environ.get('HTTP_X_FC_FUNCTION_NAME', '')
        if host == "{0}.{1}.fc.aliyuncs.com".format(uid, region) or \
                "localhost" in host or \
                "127.0.0.1" in host:
            environ['SCRIPT_NAME'] = "/2016-08-15/proxy/{0}/{1}".format(
                serviceName, functionName)
            environ['PATH_INFO'] = environ['PATH_INFO'].replace(
                environ['SCRIPT_NAME'], "")
            print(environ)
        return self.app(environ, start_response)


app.wsgi_app = CustomProxyFix(app.wsgi_app)
