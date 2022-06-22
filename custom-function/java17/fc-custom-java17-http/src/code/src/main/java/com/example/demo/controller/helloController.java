package com.example.demo.controller;

import org.springframework.context.annotation.Configuration;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class helloController {
  @RequestMapping("/")
  public String sayHello() {
      return "Hello, World!";
  }
}
