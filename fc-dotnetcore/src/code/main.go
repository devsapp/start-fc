package main

import (
	"fmt"

	"github.com/aliyun/fc-runtime-go-sdk/fc"
)

func main() {
	fc.Start(HandleRequest)
}

func HandleRequest(event []byte) (string, error) {
	fmt.Printf("event: %s\n", string(event))
	fmt.Println("hello world! 你好，世界!")
	return "hello world! 你好，世界!", nil
}
