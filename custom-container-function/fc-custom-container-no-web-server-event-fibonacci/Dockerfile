FROM python:3.9.0-slim

RUN pip install numpy

WORKDIR /usr/src/app
COPY . .

CMD [ "python", "./app.py" ]
