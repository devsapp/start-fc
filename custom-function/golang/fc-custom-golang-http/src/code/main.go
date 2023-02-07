package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
)

const (
	fcRequestID          = "x-fc-request-id"
	fcLogTailStartPrefix = "FC Invoke Start RequestId: %s" // Start of log tail mark
	fcLogTailEndPrefix   = "FC Invoke End RequestId: %s"   // End of log tail mark
)

func aHandler(w http.ResponseWriter, req *http.Request) {
	requestID := req.Header.Get(fcRequestID)
	fmt.Println(fmt.Sprintf(fcLogTailStartPrefix, requestID))

	defer func() {
		fmt.Println(fmt.Sprintf(fcLogTailEndPrefix, requestID))
	}()

	// your logic
	w.Write([]byte(fmt.Sprintf("Hello, golang  http invoke!")))
}

func bHandler(w http.ResponseWriter, req *http.Request) {
	requestID := req.Header.Get(fcRequestID)
	fmt.Println(fmt.Sprintf(fcLogTailStartPrefix, requestID))

	defer func() {
		fmt.Println(fmt.Sprintf(fcLogTailEndPrefix, requestID))
	}()

	// your logic
	b, err := ioutil.ReadAll(req.Body)
	if err != nil {
		panic(err)
	}
	info := fmt.Sprintf("method =  %+v;\nheaders = %+v;\nbody = %+v", req.Method, req.Header, string(b))
	w.Write([]byte(fmt.Sprintf("Hello, golang  http invoke! detail:\n %s", info)))
}

func main() {
	fmt.Println("FunctionCompute custom go runtime inited.")
	http.HandleFunc("/a", aHandler)
	http.HandleFunc("/b", bHandler)
	http.ListenAndServe(":9000", nil)
}
