build: 
	docker run --rm -it -v $$(pwd):/tmp aliyunfc/runtime-custom:build bash -c "cd /tmp && ./build.sh"

deploy: build
	s deploy -y