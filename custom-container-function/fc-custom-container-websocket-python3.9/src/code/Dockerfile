FROM python:3.9.0-slim

WORKDIR /usr/src
RUN pip install flask -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip install websockets -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY . .

CMD [ "python", "-u", "/usr/src/app.py" ]
