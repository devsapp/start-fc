FROM python:stretch

RUN apt-get update && apt-get install -y gcc g++ openssl tar wget libopencv-dev

RUN pip install --upgrade cmake  -i https://pypi.tuna.tsinghua.edu.cn/simple

RUN mkdir /tmp/bin
WORKDIR /tmp
COPY . .

RUN bash ./build.sh


## prod image on FC
FROM debian:stretch-slim
COPY --from=0 /tmp/bin/libcppruntime.so /usr/lib/libcppruntime.so
ENV LD_LIBRARY_PATH=/usr/lib
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY --from=0 /tmp/bin/bootstrap  ./bootstrap
COPY ./dog.jpg ./dog.jpg

RUN apt-get update && apt-get install -y libopencv-dev

ENTRYPOINT ["/usr/src/app/bootstrap"]