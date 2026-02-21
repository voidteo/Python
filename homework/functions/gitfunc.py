#=========== EXERCISES FROM GITHUB , HOMETASK FROM OFFLINE COURSE===============
from typing import Callable

#task 1: Write a function greet() that prints "Hello". Assign it to another variable and call it using that variable.
"""
def greet():
    print("hello")
    
res = greet
res()
""" 
#task 2: Store two functions (add(), subtract()) inside a list and call them in a loop with arguments.
"""
def add(a: int, b: int)-> int:
    return a + b

def substract(a: int, b: int):
    return a - b

l = [add, substract]

print(l[0](7, 4))
print(l[1](3, 7))

""" 
#task 3: Store three different arithmetic functions in a dictionary with keys "add", "sub", "mul". Call them using user input.
"""
def add(a: int, b: int)-> int:
    return a + b

def substract(a: int, b: int)-> int:
    return a - b

def multiply(a: int, b: int)-> int:
    return a * b

d = {
    "add": add,
    "sub": substract,
    "mul": multiply 
}

print(d.get("add")(7, 7))

for k, v in d.items():
    res = d[k](7, 9)
    print(res)
    
""" 
#task 4: Create a list of lambdas that each multiply a number by 1, 2, 3, 4, 5. Call each lambda with the number 10.
"""
l = [lambda a: a * 1, lambda a: a * 2, lambda a: a * 3, lambda a: a * 4, lambda a: a * 5]

n = 10
for i in l:
   res = i(n)
   print(res)
""" 
#task 5: Write a function apply(func, value) that applies a given function to a value. Test with both a regular function and a lambda.
"""
def apply(func: Callable, val):
    return func(val)

def square(a: int)-> int:
    return a*a

res = apply(square, 7)
print(res)

print(apply(lambda x: x * x, 5))

""" 
#task 6: Write a function that takes another function and two numbers and returns the result of applying that function to both.
"""
def apply(func: Callable, a: int, b: int):
    return func(a, b)

def mul(a: int, b: int):
    return a * b

res = apply(mul, 7, 7)
print(res)

""" 
#task 7: Define a list of numbers. Define a lambda that squares a number. Use a for-loop to print the result of applying the lambda to each number.
"""
l = [1,2,3,4,5,6,7,8,9]

res = map(lambda a: a**2, l)
print(list(res))

for i in l:
    res = lambda a: a**2
    print(res(i))
""" 
#task 8: Store three lambdas performing different string operations (uppercase, lowercase, title). Apply each to "python".
"""
s: str = "python"

up = lambda s: s.upper()
lo = lambda s: s.lower()
ti = lambda s: s.title()

print(up(s), lo(s), ti(s))

""" 
#task 9: Create a tuple of functions that add 5, 10, and 15 to a number. Use a for-loop to apply all to the number 20.
"""
def add1(a: int):
    return a + 5

def add2(a: int):
    return a + 10

def add3(a: int):
    return a + 15

mytup = (add1, add2, add3,)
n = 20

for i in mytup:
    r = i(n)
    print(r)
""" 
#task 10: Define a function choose(condition) that returns one of two lambdas — one that adds 10 if condition is True, else subtracts 10. Test both cases.
'''
l1 = lambda a: a + 10
l2 = lambda a: a - 10

def con(func: Callable, func1: Callable, a: int):
    if a > 10:
        return func(a)
    else:
        return func1(a)
    
res = con(l1, l2, 7)
print(res)

'''
#task 11: Write operate(a, b, op) where op is a function (like add, sub, etc.). Pass lambdas directly as op.
"""
def operate(a: int, b: int, op: Callable):
    return op(a, b)

def add(a: int, b: int):
    return a + b

res = operate(7, 7, lambda a, b: a * b)
print(res)

""" 
#task 12: Write a function make_multiplier(n) that returns a lambda which multiplies its argument by n. Test with 2, 3, 5
"""
def make_multiplier(n):
    return lambda x: x * n

res1 = make_multiplier(10)
print(res1(2), res1(3), res1(5))

""" 
#task 13: Write a function select_function(name) that returns a lambda for "square", "cube", or "double".
"""
def select_func(name: str):
    if name == "square":
        return lambda x: x**2
    elif name == "cube":
        return lambda x: x**3
    elif name == "double":
        return lambda x: x + x
    else:
        raise ValueError("unknown function name! ")
    
    
f1 = select_func("square")
print(f1(2))
f2 = select_func("cube")
print(f2(7))
f3 = select_func("double")
print(f3(7))

""" 
#task 14: Create a function filter_even(func, numbers) that filters numbers based on a condition given by func.
"""
def filter_even(func: Callable, num: list):
    res = []
    for i in num:
        if func(i):
            res.append(i)
    return res

def num_even(n: int)-> bool:
    return n % 2 == 0

l = [1,2,3,4,5,6,7,8,9,10]
r = filter_even(num_even, l)

print(r)

""" 
#task 15: Write a function that returns different lambdas depending on whether a string starts with a vowel or not.
"""
def filter_s(s: str):
    vowel = "aioue"
    if s[0].lower() in vowel:
        return lambda : f"{s} starts with vowel char"
    else:
        return lambda : f"{s} does not start with vowel"
    
r = filter_s("avvalin")
print(r())

""" 
#task 16: Define a list of names. Write a function that takes a function transformer and applies it to every name in the list.
"""
def get_len(names: list, func: Callable):
    return {i: func(i) for i in names}


def len_word(s: str):
    return len(s)

names = ["rura", "alex", "scott", "eshmat", "toshmat"]
r = get_len(names, len_word)
print(r)

""" 
#task 17: Write a function conditional_apply(numbers, func_true, func_false) that applies func_true if number is even, else func_false.
"""
def conditional_app(num: int, func_true: Callable, func_false: Callable):
    if num % 2 == 0:
        return func_true(num)
    else:
        return func_false(num)
    
    
def square(n: int)-> int:
    return n**2

def cube(n: int)-> int:
    return n**3

r = conditional_app(4, square, cube)
print(r)

""" 
#task 18: Write a function that takes another function and prints its name and result (use func.__name__ and func() call).
"""
def show_func(func: Callable):
    print(f"Function name: {func.__name__}")
    print(f"result: {func()}")
    
def message():
    return f"this message is for person who is reading this text! "
    
show_func(message)
"""
#task 19: Make a higher-order function repeater(func, n) that returns a new function calling func n times.
"""
def repeater(func: Callable, n: int):
    for i in range(1, n+1):
        print(func())
        
def greet():
   return "Hello python"
    
repeater(greet, 5)
""" 
"""
def repeat(func: Callable, n: int):
    def inner():
        for _ in range(n):
            print(func())
    return inner
    
def message():
    return "never fear, don't give up"

r = repeat(message, 5)
r()

""" 
#task 20: Create a choose_operator(symbol) that returns a lambda performing that arithmetic operation (+, -, *, /).
"""
def choose_operator(symbol: str):
    if symbol ==  "+":
        return lambda a, b: a + b
    elif symbol == "-":
        return lambda a, b: a - b
    elif symbol == "*":
        return lambda a, b: a * b
    elif symbol == "/":
        return lambda a, b: a / b
    else:
        raise ValueError("unknown operator you have to use(+,-,*,/)")
    
r = choose_operator("+")
print(r(4, 4))
a = choose_operator("-")
print(a(7, 3))
b = choose_operator("*")
print(b(21, 3))
c = choose_operator("**")
print(c(63,7))

""" 
#task 21: Sort a list of strings by their length using a lambda as key.
"""
l = ["python", "s", "stamina", "learning", "journey"]

l.sort(key=lambda x: len(x))
print(l)

""" 
#task 22: Given a list of tuples (name, age), sort by age using a lambda.
"""
info = [("alex", 25), ("scott", 22), ("rura", 18), ("lisa", 16)]
info.sort(key=lambda x: x[1])

print(info)

""" 
#task 23: Use a lambda to extract all first elements of a list of tuples.
"""
info = [("alex", 25), ("scott", 22), ("rura", 18), ("lisa", 16)]

res = map(lambda x: x[0], info)
print(list(res))

""" 
#task 24: Map a lambda that reverses strings over a list of words.
"""
s = ["python", "is", "code"]
res = map(lambda x: x[::-1], s)

print(list(res))

""" 
#task 25: Use a lambda inside filter() to extract numbers divisible by 3 or 5 from a list.
"""
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]

res = list(filter(lambda x: x % 3 == 0 or x % 5 == 0, num))
print(res)

""" 
#task 26: Given a dictionary of products and prices, use a lambda to print only those above a certain price.
"""
products = {"milk": 1.2, "cola": 1.5, "chocolate": 3, "pista": 4, "cookie": 3.5}

res = dict(filter(lambda i: i[1] >= 2, products.items()))
print(res)

""" 
#task 27: Convert a list of strings to uppercase using a lambda and map().
"""
l = ["python", "is", "language", "execute"]

res = list(map(lambda x: x.upper(), l))
print(res)

""" 
#task 28: Given a list of numbers, use a lambda inside map() to replace negative numbers with 0.
"""
num = [-1, -2, -3, 4, 5, 3, 7, 9, -7]

res = list(map(lambda x: 0 if x < 0 else x, num))

print(res)

""" 
#task 29: Sort a list of tuples (city, population) by population in descending order using a lambda.
"""
population = [("tashkent", 3), ("samarqand", 4), ("termez", 5), ("kamilot", 6), ("vise city", 7)]

res = sorted(population, key= lambda x: x[1], reverse=True)

print(res)

""" 
#task 30: Write a function apply_all(funcs, value) that applies all functions in a list to the value and returns a list of results.
"""
def apply_all(funcs: Callable, val):
    res = []
    for i in funcs:
        res.append(i(val))
    return res

def double(a: int):
    return a + a

def triple(a: int):
    return a * 3

def square(a: int):
    return a ** 2

def cube(a: int):
    return a ** 3

my_func = [double, triple, square, cube]
res = apply_all(my_func, 7)
print(res)
""" 
#task 31: Write a lambda that returns "Even" if a number is even, else "Odd".
"""
res = lambda a: "even" if a % 2 == 0 else "odd"
print(res(9))
print(res(8))

""" 
#task 32: Use a list comprehension with a lambda inside to convert a list of numbers into "Even"/"Odd" labels.
"""
l = [1,2,3,4,5,6,7,8,9,10]

res = [(lambda i: "even" if i % 2 == 0 else "odd")(i) for i in l]
print(res)

""" 
#task 33: Define a list of strings. Use a lambda and filter() to extract those starting with a vowel.
"""
l = ["rura", "aron", "eagle", "surat", "satr", "oman"]

res = list(filter(lambda x: x[0].lower() in "aioue", l))
print(res)

""" 
#task 34: Create a function that accepts a list of numbers and a lambda condition. It prints numbers satisfying the condition.
"""
def accept(num: list, cond: Callable):
    for i in num:
        if cond(i):
            print(i)
            
number = [1,2,3,4,5,6,7,8,9,10]

accept(number, lambda x: x > 5)

""" 
#task 35: Write a function that counts how many elements in a list satisfy a condition (passed as lambda).
"""
def counter(num: list, condi: Callable):
    cnt = 0
    for i in num:
        if condi(i):
            cnt+=1   
    return cnt
            
num = [1,2,3,4,5,6,7,8,9,10]

res = counter(num, lambda x: x > 5)
print(res)

""" 
#task 36: Use lambdas to generate a list of factorials for numbers 1–5 (hint: use for loop and reduce-like logic).
"""
fact = 1 
for i in range(1, 5+1): 
    fact*=i
print(fact)

fakt = lambda n: (1 if n == 0 else (lambda r=1: ([(r:= r *i) for i in range(1, n+1)], r)[1])())

faktorials = [fakt(i) for i in range(1, 5+1)]
print(faktorials)

""" 
#task 37: Use a lambda to decide whether a string is a palindrome (ignore case).
"""
pal = lambda s: True if s.lower() == s.lower()[::-1] else None

print(pal("kiyik"))

""" 
#task 38: Create a switch_case lambda that converts a string to lowercase if it’s uppercase, and vice versa.
"""
switch_c = lambda s: s.lower() if s.isupper() else s.upper()

print(switch_c("KIYIK"))

""" 
#task 39: Given a list of integers, use a lambda inside a for-loop to print "Fizz" if divisible by 3, "Buzz" if divisible by 5, "FizzBuzz" if both.
"""
l = [1,2,3,4,5,6,7,8,9,10]

r = lambda i: (
    "FizzBuzz" if i % 3 == 0 and i % 5 == 0 else
    "fizz" if i % 3 == 0 else
    "Buzz" if i % 5 == 0 else i
)

for i in l:
    print(r(i))
""" 
#task 40: Write a lambda that checks if a number is prime (basic implementation with loop).
"""
def primeCheck(n: int):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return f"{n} is prime number"


res = primeCheck(5)
print(res)

""" 
#task 41: Write make_power(n) that returns a lambda to raise numbers to power n.
"""
def make_power(n: int):
    return lambda x: x ** n

square = make_power(2)
print(square(5))

def makePower(n: int):
    def inner(i: int):
        res = n ** i
        return res
    return inner

res = make_power(3)
print(res(3))

""" 
#task 42: Write a function that takes a list of functions and applies them one after another to a value (function composition).
"""
def apply_all(funcs: Callable, val):
    res = []
    for f in funcs:
       res.append(f(val))
    return res

def square(a:int):
    return a ** 2

def cube(a: int):
    return a ** 3

def double(a: int):
    return a + a

r = [double, square, cube]

res = apply_all(r, 5)

print(res)

""" 
#task 43: Write a function chain(func1, func2) that returns a new function applying both in sequence.
"""
def chain(func1: Callable, func2: Callable):
    def newfunc(n: int):
        f1 = func1(n)
        f2 = func2(f1)
        return f2
    return newfunc

def add(a: int):
    return a + 1

def times(a: int):
    return a * 2

r = chain(add, times)
print(r(3))

""" 
#task 44: Write make_counter() that returns a lambda remembering how many times it was called (use closure).
"""
def make_counter(func: Callable):
    count = 0
    def inner(n):
        nonlocal count
        count+=1
        return count
    return inner

def add(*args):
    return sum(args)

"""
#task 45: Create a function string_repeater(s) returning a lambda that repeats s a given number of times.
"""
def string_repeater(s: str)->Callable:
    return lambda x: x * s

res = string_repeater("rura")
print(res(5))

def st_r(s):
    res = lambda x: x * s
    return res

print(st_r("ru")(4))

r = st_r("bug")
print(r(5))

""" 
#task 46: Write a function choose_lambda(flag) that returns a lambda doing addition if flag=True, else subtraction.
"""
def choose_lambda(flag: bool):
    if flag:
        return lambda x: x + 7
    return lambda x: x - 7

res = choose_lambda(True)
print(res(4))

r = choose_lambda(False)(31)
print(r)

""" 
#task 47: Build a list of lambdas that return the square of 0 to 4 — fix the late-binding issue properly.
"""
num = [0,1,2,3,4]

res = lambda x: x ** 2
l = []
for i in num:
    l.append(res(i))
print(l)

""" 
#task 48: Write a function that takes a function f and returns a new function that adds 1 to its result.
"""
def maker(func: Callable):
    def newfunc(*args):
        return func(*args)+1
    return newfunc

def add(a: int, b: int)-> int:
    return a + b

res = maker(add)
print(res(4, 4))

""" 
    #task 49: Write a lambda that accepts another lambda and applies it twice to a number.
"""
apply_twice = lambda func: (lambda x: func(func(x)))

f = lambda x: x **2
res = apply_twice(f)
print(res(2))

""" 
#task 50: Build a simple calculator using a dictionary of lambdas for +, -, *, /, and let user choose operation.
"""
calculate = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "*": lambda x, y: x * y,
    "/": lambda x, y: None if x <= 0 else x / y
}

print(calculate["+"](4, 4))

""" 

#task 51: 