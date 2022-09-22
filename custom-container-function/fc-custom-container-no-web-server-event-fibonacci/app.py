import os
import numpy as np

def PrintFibonacci(first, second, length):
    if(length == 0):
        return
    print(first + second, end=" ")
    PrintFibonacci(second, first+second, length-1)

if __name__ == '__main__':
    print("Calculate Fibonacci numbers using FC Custom Container")
    print("Fibonacci numbers of length 10 is: ")
    print(0, 1, end=" ")
    PrintFibonacci(0, 1, 8)
