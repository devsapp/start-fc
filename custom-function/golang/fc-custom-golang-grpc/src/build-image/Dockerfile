FROM golang:1.17.11-stretch
RUN go env -w GO111MODULE=auto
RUN go env -w GOPROXY=https://goproxy.cn,direct
RUN mkdir -p $GOPATH/src/golang.org/x/
RUN cd $GOPATH/src/golang.org/x/ && git clone https://github.com/golang/net.git
RUN cd $GOPATH/src/golang.org/x/ &&  git clone https://github.com/golang/sys.git
RUN go get github.com/awesome-fc/golang-runtime
RUN go get github.com/golang/protobuf/proto
RUN go get google.golang.org/grpc