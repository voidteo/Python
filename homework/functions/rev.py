#============GENERATED EXERCISES FOR EXTRA IMPROVEMENT=================
from typing import Callable
#task 1: Create a function that prints “Hello”. Assign it to another variable and call it from there.
"""
def greet():
    print("hello")
    
a = greet
a()

""" 
#task 2: Store two different functions inside a list and call both using a loop.
"""
l = [min, max]

print(l[0](4,7,3))
print(l[1](5,3,7))

""" 
#task 3: Write a function and store it in a dictionary as a value. Call it using the key.
"""
def func1(a: int, b: int)->int:
    return a + b

def func2(a: int, b: int)-> int:
    return a - b

cal = {
    "add": func1,
    "substract": func2,
}
print(cal["add"](7, 3))
print(cal["substract"](9, 4))

""" 
#task 4: Pass a function as an argument to another function and call it inside.
"""
def is_even(n: list)-> bool:
    res = []
    for i in n:
        if i % 2 == 0:
            res.append(i)
    return res
        
    

def add(l: list, func: Callable):
    return func(l)

l = [1,2,3,4,5,6,7,8,9,10]
res = add(l, is_even)
print(res)
""" 
#task 5: Return a function from another function and call the returned function.
"""
def outer(n: int):
    def inner(a: int):
        return n + a
    return inner

res = outer(6)
print(res(3))

""" 
#task 6: Assign the same function to three different variables and call each.
"""
def say():
    print("hello python")
    
res = say
result = say
rep = say

res(), result(), rep()

""" 
#task 7: Write a function that returns another function based on a condition.
"""
def maker(func1: Callable, func2:  Callable, cond: bool)-> Callable:
    if cond:
        return func1
    return func2

def add(a: int, b: int):
    return a + b

def mul(a: int, b: int)-> int:
    return a * b

res = maker(add, mul, False)
print(res(4, 4))
""" 
#task 8: Replace a function name with another variable pointing to the same function. Test both.
"""
def greet():
    print("hello")
    
res = greet
print(res.__name__)
print(greet.__name__)   
""" 
#task 9: Delete the original function name and call it using the variable.
"""
def greet():
    print("hello worl")
    
res = greet

del greet

print(res())

""" 
#task 10: Put functions inside a tuple and call them one by one.
"""
def add(a: int, b: int):
    return a + b

def div(a: int, b: int):
    return a / b

def sub(a: int, b: int):
    return a - b

def mul(a: int, b: int):
    return a * b

rest = (add, sub, mul, div,)

for i in rest:
    print(i(7, 3))
    
""" 
#task 11: Compare two variables that point to the same function using == and is.
"""
def greet():
    print("Python")

a = greet
b = greet

a()
b()

print(a is b)

""" 
#task 12: Create a function that prints its own name using __name__.
"""
def greet():
    print(greet.__name__)
    
greet()

""" 
#task 13: Pass a function into a list, then call it from inside the list.
"""
def even(n: int):
    if isinstance(n, int):
        if n % 2 == 0:
            return f"{n} is even"
        else:
            return f"{n} is not even"
    else:
        return f"ERROR you can only enter int"
l = [1, "a", "py", even]

print(l[3]("r"))

""" 
#task 14: Write a function that accepts another function and prints its name.
"""
def aksl(func: Callable):
    return func.__name__

def adder(a: int):
    return a + a

res = aksl(adder)
print(res)

""" 
#task 15: Pass a function into a list, then loop through and call each.
"""
def add(a: int, b: int)-> int:
    return a + b

def bigfind(a: int, b: int)->int:
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return f"{a, b} is equal"
    

def sub(a: int, b: int)-> int:
    return a - b

def mul(a: int, b: int):
    return a * b

def div(a: int, b: int):
    if a == 0:
        return f"ZeroDivisionError"
    return a / b

l = [add, bigfind, sub, mul, div]

for i in l:
    print(i(8, 4))
    
""" 
#========================HIGHER ORDER FUNCTION=================================

#task 16: Write a function that applies a given function to a number.
"""
def apply_n(func: Callable, num):
    return func(num)

def cube(a: int):
    return a ** 3

print(apply_n(cube , 4))

""" 
#task 17: Make a function that takes two functions and calls one based on a condition.
"""
def taker(func1: Callable, func2: Callable, cond: bool):
    if cond:
        return func1
    return func2

def minimum(a: int, b: int):
    if a < b:
        return a
    return b

def maximum(a: int, b: int)->int:
    if a > b:
        return a
    return b

res = taker(minimum, maximum, False)
print(res(2, 6))

""" 
#task 18: Build a function that returns a function which multiplies numbers by N.
"""
def mult(a: int):
    def inner(n: int): 
        return a * n
    return inner

res = mult(4)
print(res(3))

""" 
#task 19: Create a function that applies a function to each element of a list.
"""
def apply_all(func: Callable, l: list):
    res = []
    for i in l:
        res.append(func(i))
    return res


def length(l: list):
    for i in l:
        print(len(i))
        
l = ["is", "ruas", "python", "batman"]

res = apply_all(length, l)
print(res)

""" 
#task 20: Implement your own map() using a higher-order function.
"""
def cube(a: int):
    return a **3

l = [1,2,3,4]

res = list(map(cube, l))   # need to check this
print(res)

""" 
#task 21: Implement your own filter() using a higher-order function.
"""
def even(a: int):
    return a % 2 == 0

l = [1,2,3,4,5,6,7,8,9]

res = list(filter(even, l)) #need to check this
print(res)

""" 
#task 22: Implement your own reduce() using a higher-order function.
"""
def implement(func: Callable, val: list):
    it = iter(val)
    result = next(it)
    
    for i in it:
        result = func(result, i)
    return result

def add(a: int, b: int):
    return a + b

res = implement(add, [1,2,3,4,5,6,7,8,9,10])

print(res)

""" 
#task 23: Write a function that times the execution of another function.

import time

def timer(func: Callable, val):
    start = time.time()
    func(val)
    end = time.time()
    res = start - end
    
    
def count(n: int):
    for i in range(1, n+1):
        print(i)
        
timer(lambda: count(100))