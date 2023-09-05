build:
ifeq ($(shell uname), Linux)
	apt-get update && apt install -y cmake && ./build.sh
else
	docker run --rm -it -v $$(pwd):/tmp aliyunfc/runtime-custom:build bash -c "cd /tmp && ./build.sh"
endif

deploy: build
	s deploy -y
