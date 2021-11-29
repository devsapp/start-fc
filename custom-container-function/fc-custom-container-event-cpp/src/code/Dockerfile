FROM python:stretch
RUN sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list
RUN sed -i "s@http://security.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list && rm -rf /var/lib/apt/lists/* && apt-get update

RUN apt-get install -y gcc g++ openssl tar wget
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
ENTRYPOINT ["/usr/src/app/bootstrap"]