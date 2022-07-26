build-img:
	docker build -t fc-go-runtime  -f build-image/Dockerfile build-image

build: build-img
	docker run --rm -it -v "$$(pwd)":/go/src/tmp fc-go-runtime bash -c "GOARCH=amd64 go build -o /go/src/tmp/code//bootstrap /go/src/tmp/code/main.go"
	chmod +x code/bootstrap

deploy: build
	s deploy -y
