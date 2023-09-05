package com.example.demo.controller;

import org.springframework.context.annotation.Configuration;
import java.util.Map;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestHeader;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.PostMapping;

@RestController
public class helloController {
    @RequestMapping("/")
    public String sayHello() {
        return "hello world!";
    }

    // FC Initializer: /initialize will be called when the FC functions are
    // initialized by
    // API calls, Function updates or FC internal system upgrades
    @PostMapping("/initialize")
    public String fcEventInitialize(@RequestHeader Map<String, String> headers) {
        String fcRequestID = headers.get("x-fc-request-id");
        System.out.println("Initialized, request ID: " + fcRequestID);
        return "Hello Spring Boot, from FC Event function initializer!\nPowered by FunctionCompute custom-container runtime\n"
                + "RequestID: " + fcRequestID + "\n";
    }

    // FC Event function:
    // Invoke handler: /invoke will be called when the FC function responds to an
    // event (e.g. API call or OSS PutObject)
    @PostMapping("/invoke")
    public String fcEventInvoke(@RequestHeader Map<String, String> headers, @RequestBody String event) {
        String fcRequestID = headers.get("x-fc-request-id");
        System.out.println("hello world!");
        System.out.println(event);
        System.out.println("Invoke finished, request ID: " + fcRequestID);
        return "hello world!";
    }

}
