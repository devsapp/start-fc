package main

import (
	"encoding/base64"
	"encoding/json"
	"fmt"
	"net/http"

	"github.com/aliyun/fc-runtime-go-sdk/fc"
)

// HTTPTriggerEvent HTTP Trigger Request Event
type HTTPTriggerEvent struct {
	Version         *string           `json:"version"`
	RawPath         *string           `json:"rawPath"`
	Headers         map[string]string `json:"headers"`
	QueryParameters map[string]string `json:"queryParameters"`
	Body            *string           `json:"body"`
	IsBase64Encoded *bool             `json:"isBase64Encoded"`
	RequestContext  *struct {
		AccountId    string `json:"accountId"`
		DomainName   string `json:"domainName"`
		DomainPrefix string `json:"domainPrefix"`
		RequestId    string `json:"requestId"`
		Time         string `json:"time"`
		TimeEpoch    string `json:"timeEpoch"`
		Http         struct {
			Method    string `json:"method"`
			Path      string `json:"path"`
			Protocol  string `json:"protocol"`
			SourceIp  string `json:"sourceIp"`
			UserAgent string `json:"userAgent"`
		} `json:"http"`
	} `json:"requestContext"`
}

func (h HTTPTriggerEvent) String() string {
	jsonBytes, err := json.MarshalIndent(h, "", "  ")
	if err != nil {
		return ""
	}
	return string(jsonBytes)
}

// HTTPTriggerResponse HTTP Trigger Response struct
type HTTPTriggerResponse struct {
	StatusCode      int               `json:"statusCode"`
	Headers         map[string]string `json:"headers,omitempty"`
	IsBase64Encoded bool              `json:"isBase64Encoded,omitempty"`
	Body            string            `json:"body"`
}

func NewHTTPTriggerResponse(statusCode int) *HTTPTriggerResponse {
	return &HTTPTriggerResponse{StatusCode: statusCode}
}

func (h *HTTPTriggerResponse) String() string {
	jsonBytes, err := json.MarshalIndent(h, "", "  ")
	if err != nil {
		return ""
	}
	return string(jsonBytes)
}

func (h *HTTPTriggerResponse) WithStatusCode(statusCode int) *HTTPTriggerResponse {
	h.StatusCode = statusCode
	return h
}

func (h *HTTPTriggerResponse) WithHeaders(headers map[string]string) *HTTPTriggerResponse {
	h.Headers = headers
	return h
}

func (h *HTTPTriggerResponse) WithIsBase64Encoded(isBase64Encoded bool) *HTTPTriggerResponse {
	h.IsBase64Encoded = isBase64Encoded
	return h
}

func (h *HTTPTriggerResponse) WithBody(body string) *HTTPTriggerResponse {
	h.Body = body
	return h
}

func HandleRequest(event HTTPTriggerEvent) (*HTTPTriggerResponse, error) {
	fmt.Printf("event: %v\n", event)
	if event.Body == nil {
		return NewHTTPTriggerResponse(http.StatusBadRequest).
			WithBody(fmt.Sprintf("the request did not come from an HTTP Trigger, event: %v", event)), nil
	}

	reqBody := *event.Body
	if event.IsBase64Encoded != nil && *event.IsBase64Encoded {
		decodedByte, err := base64.StdEncoding.DecodeString(*event.Body)
		if err != nil {
			return NewHTTPTriggerResponse(http.StatusBadRequest).
				WithBody(fmt.Sprintf("HTTP Trigger body is not base64 encoded, err: %v", err)), nil
		}
		reqBody = string(decodedByte)
	}
	return NewHTTPTriggerResponse(http.StatusOK).WithBody(reqBody), nil
}

/*
// GetRawRequestEvent: obtain the raw request event
func GetRawRequestEvent(event []byte) (*HTTPTriggerResponse, error) {
	fmt.Printf("raw event: %s\n", string(event))
	return NewHTTPTriggerResponse(http.StatusOK).WithBody(string(event)), nil
}
*/

func main() {
	fc.Start(HandleRequest)
}
