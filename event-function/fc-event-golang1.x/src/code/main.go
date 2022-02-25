package main

import (
	"fmt"

	"github.com/aliyun/fc-runtime-go-sdk/fc"
)

func main() {
	fc.Start(HandleRequest)
}

/*
event:
{
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
*/
func HandleRequest(event map[string]interface{}) (string, error) {
	fmt.Printf("event: %v\n", event)
	fmt.Println("hello world! 你好，世界!")
	return "hello world! 你好，世界!", nil
}
