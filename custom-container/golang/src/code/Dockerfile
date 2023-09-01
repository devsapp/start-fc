FROM golang:1.17.11-stretch
RUN mkdir -p $GOPATH/src/golang.org/x/
RUN cd $GOPATH/src/golang.org/x/ && git clone https://github.com/golang/net.git
RUN cd $GOPATH/src/golang.org/x/ &&  git clone https://github.com/golang/sys.git
RUN GO111MODULE=auto go get github.com/awesome-fc/golang-runtime

WORKDIR /tmp
COPY . .

RUN go build -o bootstrap main.go
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN cp /tmp/bootstrap  ./bootstrap
ENTRYPOINT ["/usr/src/app/bootstrap"]