import logging
import sys
import traceback
from flask import Flask, request
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)


@app.route('/initialize', methods=['POST'])
def initialize():
    # See FC docs for all the HTTP headers: https://www.alibabacloud.com/help/doc-detail/132044.htm#common-headers
    request_id = request.headers.get("x-fc-request-id", "")
    print("FC Initialize Start RequestId: " + request_id)

    # do your things
    # Use the following code to get temporary credentials
    # access_key_id = request.headers['x-fc-access-key-id']
    # access_key_secret = request.headers['x-fc-access-key-secret']
    # access_security_token = request.headers['x-fc-security-token']

    print("FC Initialize End RequestId: " + request_id)
    return "Function is initialized, request_id: " + request_id + "\n"


@app.route('/invoke', methods=['POST'])
def invoke():
    # See FC docs for all the HTTP headers: https://www.alibabacloud.com/help/doc-detail/132044.htm#common-headers
    request_id = request.headers.get("x-fc-request-id", "")
    print("FC Invoke Start RequestId: " + request_id)

    # Get function input, data type is bytes, convert as needed
    event = request.get_data()
    event_str = event.decode("utf-8")

    # Use the following code to get temporary STS credentials to access Alibaba Cloud services
    # access_key_id = request.headers['x-fc-access-key-id']
    # access_key_secret = request.headers['x-fc-access-key-secret']
    # access_security_token = request.headers['x-fc-security-token']

    try:
        # do your things
        print(event_str)
    except Exception as e:
        exc_info = sys.exc_info()
        trace = traceback.format_tb(exc_info[2])
        errRet = {
            "message": str(e),
            "stack": trace
        }
        print(errRet)
        print("FC Invoke End RequestId: " + request_id)
        return errRet, 404, [("x-fc-status", "404")]

    print("FC Invoke End RequestId: " + request_id)
    return "Hello from FC event function, your input: " + event_str + ", request_id: " + request_id + "\n"


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=9000)
