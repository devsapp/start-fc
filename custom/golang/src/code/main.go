package main

import (
	"encoding/json"

	gr "github.com/awesome-fc/golang-runtime"
)

func initialize(ctx *gr.FCContext) error {
	ctx.GetLogger().Infoln("init golang!")
	return nil
}

func handler(ctx *gr.FCContext, event []byte) ([]byte, error) {
	fcLogger := ctx.GetLogger()
	_, err := json.Marshal(ctx)
	if err != nil {
		fcLogger.Error("error:", err)
	}
	fcLogger.Infof("hello golang!")
	fcLogger.Infof("hello golang2!")
	return event, nil
}

func main() {
	gr.Start(handler, initialize)
}
