FROM golang:1.20-bullseye


RUN mkdir -p /usr/src/app
WORKDIR /usr/src
COPY . .

RUN go env -w GO111MODULE=on
RUN go env -w GOPROXY=https://goproxy.cn,direct
RUN go mod tidy
RUN go build -o bootstrap main.go
RUN cp bootstrap  /usr/src/app/bootstrap
ENTRYPOINT ["/usr/src/app/bootstrap"]