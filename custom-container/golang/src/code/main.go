package main

import (
	"io/ioutil"

	"github.com/gin-gonic/gin"
)

func main() {
	r := gin.Default()
	r.POST("/invoke", func(c *gin.Context) {
		bodyBytes, err := ioutil.ReadAll(c.Request.Body)
		if err != nil {
			panic(err)
		}
		c.JSON(200, gin.H{
			"message": "hello " + string(bodyBytes),
		})
	})

	r.POST("/initialize", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "initialize ok",
		})
	})

	r.GET("/", func(c *gin.Context) {
		c.JSON(200, gin.H{
			"message": "hello world",
		})
	})
	// listen and serve on 0.0.0.0:8080 (for windows "localhost:8080")
	r.Run()
}
