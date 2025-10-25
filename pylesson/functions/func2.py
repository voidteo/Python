# task 19:
"""
from typing import Callable

def repeater(func: Callable, n: int)-> Callable:
    def inner():
        for _ in range(n):
            func()
        return "Success"
    return inner

print(repeater(lambda : print("hello"), 10))

""" 
#tas 21: 