#==============INTRODUCTION TO THE DECORATORS  exercises from GPT.............
from typing import Callable

#task 1: Write a decorator that prints "start" before a function runs
"""
def starter(func):
    def wrapper(*args, **kwargs):
        print("start.....")
        res = func(*args, **kwargs)
        return res
    return wrapper

@starter
def greet(s):
    return s

print(greet("hello wrapper"))

""" 
#task 2: Write a decorator that prints "end" after a function runs
"""
def ender(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        print("end.....")
        return res
    return wrapper

@ender
def say_hello():
    print("say hello")

say_hello()

""" 
#task 3: Write a decorator that prints both before and after
"""
def befter(func):
    def wrapper(*args, **kwargs):
        print("starting....")
        res = func(*args, **kwargs)
        print("ending....")
        return res
    return wrapper

@befter
def add(a, b):
    return a + b

print(add(5, 5))

""" 
#task 4: Apply a decorator without using @ syntax
"""
def befter(func):
    def wrapper(*args, **kwargs):
        print("starting....")
        res = func(*args, **kwargs)
        print("ending....")
        return res
    return wrapper

@befter
def taker(s):
    return s



print(taker("rura"))

""" 
#task 5: Print func.__name__ inside a decorator and observe what happens
"""
def namer(func: Callable):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        res = func(*args, **kwargs)
        print("this is function name")
        return res
    return wrapper

@namer
def say_hello(s):
    return

say_hello()

""" 
#task 9: Apply the same decorator to two different functions
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        print("starting.....")
        res = func(*args, **kwargs)
        print("ending.....")
        return res
    return wrapper

@decorator
def greeting():
    print("Hello World")
    
@decorator
def add(a, b):
    return a + b

greeting()
print(add(5, 9))

""" 
#task 10: Prove that each decorated function has its own wrapper
