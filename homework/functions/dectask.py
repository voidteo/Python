#=============OFFLINE HOMEWORK FROM OFFLINE COURCE UIC================

#task 1: Write a decorator that prints "Starting..." before and "Done." after a function runs.
"""
from typing import Callable
import time

def decorator(func: Callable):
    def wrapper(*args, **kwargs):
        print("Starting.....(3 sec)")
        time.sleep(3)
        func()
        print("Done......(2 sec)")
        time.sleep(2)

    return wrapper

@decorator
def greet():
    time.sleep(1)
    print("Hello Eshmat")
    
greet()

""" 
#task 2: Create a decorator that measures how many times a function was called and prints the count each time.
"""
def counter(func: callable):
    cnt = 0
    def wrapper(*args, **kwargs):
        nonlocal cnt
        cnt+=1
        print("function was called: ", cnt)
        return func(*args, **kwargs)
    return wrapper

@counter
def say_learn():
    print("Always learn")

say_learn()
say_learn()
say_learn()

""" 
#task 3: Write a decorator that prints the name of the function being called.
"""
def tell_name(func: callable):
    def wrapper(*args, **kwargs):
        print("function name:", func.__name__)
        return func(*args, **kwargs)
    
    return wrapper

@tell_name
def sayma():
    print("hello")

sayma()

""" 
#task 4: Write a decorator that converts a function’s string return value to uppercase.
"""
def converter(func: callable):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res.upper()
    return wrapper

@converter
def greet():
    return "decorator works with return"

print(greet())

"""
#task 5: Write a decorator that checks if a string argument is empty before calling the function.
"""
def checker(func: callable):
    def wrapper(*args, **kwargs):
        ret = args[0]
        if ret == "":
            print("ValueError string should not be empty")
        return func(*args, **kwargs)    
    return wrapper

@checker
def star(s: str):
    return s

print(star("dddixox"))

""" 
#task 6: Write a decorator that prevents execution if a number argument is negative.
"""
def preventer(func: callable):
    def wrapper(*args, **kwargs):
        if not args:
            print("you should enter argument!")
            return 
        
        n = args[0]
        if not isinstance(n, int):
            print("you should enter int!")
            return
        
        if n < 0:
            print("number should not be negative!")
            return
        return func(*args, **kwargs)
    return wrapper

@preventer
def safer(n: int):
    return n

print(safer(1))

""" 
#task 7: Create a decorator that prints "Executing <function name>" and the arguments it was called with.
"""
def excall(func):
    def wrapper(*args, **kwargs):
        print("function name:", func.__name__)
        res = func(*args, **kwargs)
        return res
    
    return wrapper

@excall
def add(a, b):
    return a + b

print(add(7, 4))

""" 
#task 8: Make a decorator that prints the type of each argument passed to the function.
"""
def tayper(func):
    def wrapper(*args, **kwargs):
        for arg in args:
            print(f"value: {arg}, type: {type(arg)}")
        
        res = func(*args, **kwargs)
        
        for key, val in kwargs.items():
            print(f"{key} = {val}, type: {type(kwargs)}")
            
        return res
    return wrapper

@tayper
def info(*args, **kwargs):
    return *args, *kwargs

print(info("teo", age=22))

""" 
#task 9: Write a decorator that repeats the function’s output 3 times.
"""
def repeater(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            print(func(*args, **kwargs))
        
    return wrapper

@repeater
def add(*args, **kwargs):
    return args, kwargs

add("teo", age=22)

""" 
#task 10: Write a decorator that replaces None return values with "No result".
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if res is None:
            return "No Result" 
        return res       
    return wrapper

@decorator
def greet():
    print("blabla")
    
print(greet())

""" 
#task 11: Create a decorator that only allows even numbers to be passed to the function.
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        if not args:
            return "You should enter numbers!"
        
        n = args[0]
        if not isinstance(n, int):
            return "Input should be integer"
        
        if n % 2 != 0:
            return "odd numbers are not allowed"
        return func(*args, **kwargs)
    return wrapper

@decorator
def even(n: int):
    return n
        
print(even(3))

""" 
#task 12: Write a decorator that filters out duplicate elements from a list argument before calling the function.
"""
def filter_num(func):
    def wrapper(lista: list):
        res = []
        for i in lista:
            if i % 2 == 0:
                res.append(i)
        return func(res)
    return wrapper

@filter_num
def nums(l: list):
    return l

print(nums([1,2,3,4,5,6,7,8,9,10]))

""" 
#task 13: Write a decorator that converts all string arguments to lowercase before calling the function.
"""
def converter(func):
    def wrapper(*args, **kwargs):
        new_arg = []
        for i in args:
            if isinstance(i, str):
                new_arg.append(i.lower())
            else:
                new_arg.append(i)
                
        new_kwarg = {}
        for key, val in kwargs.items():
            if isinstance(val, str):
                new_kwarg[key] = val.lower()
            else:
                new_kwarg[key] = val
            
        return func(*new_arg, **new_kwarg)
    return wrapper
                

@converter
def text(a, b=""):
    return a, b

print(text("APENDIC", "RUZVELT"))

""" 
#task 14: Write a decorator that sorts any list or tuple argument before passing it to the function.
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        new_arg = []
        for i in args:
            if isinstance(i, (list, tuple)):
                new_arg.append(sorted(i))
            else:
                new_arg.append(i)
        return func(*new_arg, **kwargs)
    return wrapper

@decorator
def numba(l):
    return l

print(numba((9,8,7,6,5,)))

""" 
#task 15: Create a decorator that checks if all numeric arguments are positive; if not, print a warning and skip execution.
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        for i in args:
            if isinstance(i, (list, tuple)):
                for n in i:
                    if not isinstance(n, (int, float)):
                        continue
                    if n <=0:
                        print("warning numbers should be positive!")
                        return
                    
            else:
                if isinstance(i, (int, float)) and i <= 0:
                    print("waring numbers should be positive")
                    return 
                
        return func(*args, **kwargs)
    return wrapper

@decorator
def cheker(l):
    return l 

print(cheker([1,2,3]))

""" 
#task 16: Write a decorator that limits how many times a function can be called (e.g., max 5 times).
"""
def limiter(func):
    max_limit = 5
    cnt = 0

    def wrapper(*args, **kwargs):
        nonlocal cnt
        
        if cnt >=  max_limit:
            return "Limitda oshib ketdi !"
        
        cnt+=1
        return func(*args, **kwargs)
    return wrapper
    
@limiter
def greet():
    return"msg: Hello coding"
    
print(greet())
print(greet())
print(greet())
print(greet())
print(greet())
print(greet())

""" 
#task 17: Create a decorator that counts how many elements in a list argument satisfy a certain condition (e.g., even numbers).
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        n = args[0]
        c_e = 0
        for i in n:
            if i % 2 == 0:
                c_e+=1
        print(f"there are {c_e} even numbers in list")
        return func(*args, **kwargs)
    return wrapper

@decorator
def con(n: list):
    return n

print(con([1,2,3,4,5,6,7,8,9,10]))

""" 
#task 18: Write a decorator that skips calling the function if the first argument is an empty list or string.
"""
def skipper(func):
    def wrapper(*args, **kwargs):
        first = args[0]
        
        if isinstance(first, (str, list)) and not first:
            
            return("Function skipped an empty input!")
        return func(*args, **kwargs)
    return wrapper

@skipper
def myfunc(*args):
    return args
res = myfunc("s", 1,2,3,4)
print(res)

""" 
#task 19: Write a decorator that removes None values from list arguments before calling the function.
"""
def remover(func):
    def wrapper(*args, **kwargs):
        l = args[0]
        
        clean_list = [i for i in l if i is not None]
        return func(clean_list, *args[1:], **kwargs)
    return wrapper
@remover
def myfunc(n):
    return n

print(myfunc([None, 1, None, 2, 3, None]))

""" 
#task 20: Write a decorator that reverses all string arguments passed to the function.
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        new_args = tuple(arg[::-1] if isinstance(arg, str) else arg for arg in args)
        new_kwargs = {k: v[::-1] if isinstance(v, str) else v for k, v in kwargs.items()}
        return func(*new_args, **new_kwargs)
    return wrapper
@decorator
def myfunc(a):
    return a

print(myfunc("rura"))

""" 
#task 21: Create a decorator that multiplies a numeric return value by 10.
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, (int, float)):
            return res * 10
        return res
    return wrapper

@decorator
def piton(n):
    return n
#print(piton(2, 3, "python is begining", "always seek"))

print(piton(4))

""" 
#task 22: Write a decorator that wraps a function’s string result in parentheses.
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            return f"({res})"
        return res
    return wrapper

@decorator  # task is asking to play with return value not argument value it may be tricky at first, but reading in clear way , you see what task wants
def sark(s):
    return s

print(sark("rura"))

""" 
#task 23: Write a decorator that converts a function’s return type: if list -> tuple, if tuple -> list
"""
def converter(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, list):
            return tuple(res)
        
        if isinstance(res, tuple):
            return list(res)
        
        return res
    return wrapper

@converter
def giver(r):
    return r

print(giver((1,2,3,)))

""" 
#task 24: Create a decorator that joins the characters of a string return value with -.
"""
def joiner(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            return  "-".join(res)
        return res
    return wrapper

@joiner
def say_hi(s):
    return s

print(say_hi("i wanna say hi"))

""" 
#task 25: Write a decorator that returns a sorted version of any iterable returned by the function.
"""
def changer(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return sorted(res)
    return wrapper

@changer
def myfunc(s):
    return s

print(myfunc("wasabi"))

""" #task 26: Write a decorator that applies a given lambda to every element of a list returned by the function.
"""
def decorator(lambda_func):
    def real_decorator(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            new_res = [lambda_func(x) for x in res]
            return new_res
        return wrapper
    return real_decorator

@decorator(lambda x: x ** 2)
def square_all(l: list):
    return l

print(square_all([1,2,3,4,5,6,7,8,9]))

""" 
#task 27: Write a decorator that adds "Hello, " before and "!" after a string return value.
"""
def adder(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, str):
            return f"Hello, {res}!"
        return res # if it is not str it return value , it means beside str there will be no None return in output
    return wrapper

@adder
def greet(n):
    return n

print(greet("reo"))

"""
#task 28: Write a decorator that doubles each element in a list returned by the function.
"""
def decorator(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        if isinstance(res, list):
            new_res = []
            for i in res:
                new_res.append(i * 2)
            return new_res
        return res
    return wrapper

@decorator
def trano(m):
    return m

print(trano([1,2,3,4]))

""" 
#task 29: Write a decorator that converts a dictionary’s values to uppercase if they are strings.
"""
def converter(func):
    def wrapper(*args, **kwargs):
        new_kwargs = {}
        for k, v in kwargs.items():
            if isinstance(v, str):
                new_kwargs[k] = v.upper()
            else:
                new_kwargs[k] = v
        return func(*args, **new_kwargs)
    return wrapper

@converter
def taker(**a):
    return a

print(taker(name="teo", city="tashkent"))

""" 
#task 30: Create a decorator that, when the function returns a list of numbers, filters out the odd ones.
"""
def filter_odd(func):
    def wrapper(*args, **kwargs):
        new_res = []
        res = func(*args, **kwargs)
        if isinstance(res, list):
            for i in res:
                if i % 2 == 0:
                    new_res.append(i)
        return new_res
    return wrapper

@filter_odd
def rembo(l):
    return l

print(rembo([1,2,3,4,5,6,7,8,9,10]))

""" 
