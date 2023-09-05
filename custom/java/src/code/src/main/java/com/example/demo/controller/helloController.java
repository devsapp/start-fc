package com.example.demo.controller;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class helloController {
  @RequestMapping("/invoke")
  public String sayHello() {
    System.out.println("hello world!");
    return "hello world!";
  }
}
