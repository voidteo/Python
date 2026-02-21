#task 1: Define a function add(a, b) that returns the sum of two numbers. Assign this function to a new variable called plus. Call plus(5, 3) and print the result.
from typing import Callable

"""
def add(a: int, b: int)-> int:
    return a + b

plus = add
print(plus(7, 8))

""" 
#task 2: Create a list called operations containing the built-in functions min, max, and sum.
# Iterate through the list and apply each function to a list of numbers [10, 20, 30] and print the results.
"""
oper = [min, max, sum]
num = [10,20,30]

#for i in oper:
#    print(i([10,20,30]))

for i in oper:
    res = i(num)
    print(res)
""" 
#task 3: Write a function apply_operation(x, y, operation) that takes two numbers and a function as arguments. 
#Inside, return the result of applying the operation function to x and y. Use it with your add function from Exercise 1.
"""
from typing import Callable

def add(a: int, b: int)->int:
    return a + b

def apply_operation(x: int, y: int, operation: Callable):
    return operation(x, y)

print(apply_operation(7, 3, add))

""" 
#task 4: Write a function process_string(s, func) that takes a string and a function. 
# Use the function to process the string (e.g., str.upper or str.lower) and return the result.
"""
def upword(s: str)-> str:
    return s.upper()

def process_string(s, func: callable):
    return func(s)

print(process_string("hello", upword))

""" 
#task 5: Create a function execute_twice(func) that calls the passed function func two times. Pass a simple function that prints "Hello!" to execute_twice.
"""
def greet():
    print("hello")
    
def execute_twice(func: Callable):
    func()
    func()

execute_twice(greet)

""" 
#task 6: Define a function safe_divide(a, b) and a function error_handler().
# Write a function run_if_safe(func, handler, a, b) that calls func(a, b) only if b ≠ 0 ; otherwise, it calls handler().
"""
def safe_divide(a,b)-> float:
    return a / b

def error_handler():
    return "0 ga bo'lish mumkun emas"

def run_if_safe(func, handler, a, b):
    if b != 0:
       return func(a, b)
    else:
        return handler()
    
print(run_if_safe(safe_divide, error_handler, 14, 0))

""" 
#task 7: Define an outer function create_multiplier(n) 
# that takes one number n and returns an inner function. The inner function should take one argument x and return x × n .
"""
def create_multiplier(n: int):
    def inner(x: int):
        return x * n
    return inner

res = create_multiplier(7)
print(res(4), res(7), res(10))

""" 
#task 8: Use the create_multiplier(n) function from Exercise 7 to create two new functions:
# double = create_multiplier(2) and triple = create_multiplier(3). Test them by calculating double(5) and triple(5).
"""
def c_multiply(n: int):
    def inner(x):
        return x* n
    return inner

double = c_multiply(2)
triple = c_multiply(3)

print(double(2))
print(triple(3))

""" 
#task 9: Create a dictionary called command_map where keys are strings ('up', 'down') and values are functions 
# (e.g., functions that print "Moving Up" or "Moving Down"). Get a command from a variable and execute the corresponding function.
"""
def up():
    print("moving up....")

def down():
    print("moving down.....")
    
command_map = {
    "a": up,
    "b": down
}

command_map["a"]()  # funksiyani dict ni valuesiga uzatyapmiz
command_map["b"]()

""" 
#task 10: Write a function filter_list(data_list, criterion_func) that takes a list and a function that returns True or False. 
# Return a new list containing only the elements for which criterion_func returned True. Use a function that checks if a number is even as the criterion.
"""
def filter_list(data_list: list, criterion: Callable):
    return [i for i in data_list if criterion(i)]

def is_even(n: int):
    return n % 2 == 0

l = [2,4,6,8,10]

res = filter_list(l, is_even)
print(res)

""" 
#task 11: Write a lambda function that takes two arguments, a and b , and returns their sum. 
# Assign it to a variable called quick_add. Call it with ( 10 , 7 ) and print the result.
"""
quick_add = lambda a, b: a/b
print(round(quick_add(10, 7),2 ))

""" 
#task 12: Write a lambda function that takes one argument x and returns x 2 . Call it with 9 and print the result.
"""
print((lambda x: x**2)(9))

skr = lambda i: i**2
print(skr(9))

""" 
#task 13: Write a lambda function that takes one argument x . If x > 10 , return "Large"; otherwise, return "Small". Test it with 15 and 5 .
"""
a = lambda x: "large" if x > 10 else "small"
print(a(5)) 
print(a(15))

""" 
#task 14: Write a lambda function that takes one string argument s and returns the length of the string. Assign it to get_length.
"""
get_length = lambda s: len(s)

print(get_length("result"))

""" 
#task 15: Create a list of names: ["Alice", "Bob", "Charlie"]. Use a lambda function and a for loop to print each name prefixed with "Hello, ".
"""
names = ["Alice", "Bob", "Charlie"]

f = lambda n: "Hello "+ n

for i in names:
    print(f(i))
    
""" 
#task 16:Use the built-in filter() function and a lambda function to filter the list [1, 5, 8, 12, 17, 20] 
# to include only numbers greater than 10 . Print the resulting list.
"""
l = [1, 5, 8, 12, 17, 20]

res = filter(lambda x: x > 10, l)
print(list(res))

""" 
#task 17: Use the built-in map() function and a lambda function to convert every number in the list [1, 2, 3, 4]
# to its string representation (e.g., "1", "2"). Print the resulting list.
"""
l = [1,2,3,4]

res = map(lambda x: str(x), l)
print(list(res))

""" 
#task 18: Import the reduce function from functools. Use reduce() and a lambda function to multiply all numbers in the list [2, 3, 4] together.
"""
from functools import reduce

l = [2,3,4]
res = reduce(lambda a, b: a * b, l)
print(res)

""" 
#task 19: Write a lambda function that takes three arguments x , y , z and returns ( x + y ) / z . Call it with ( 10 , 2 , 4 ) .
"""
res = lambda x, y, z: (x+y)/z
result = res(10,2, 4)
print(result)
""" 
#task 20: Write a lambda function that simply returns its single argument. Use it to demonstrate that it can be used in place of a named function.
"""
lm = lambda a: a
print(lm(5), lm("hello python"))

""" 
#task 21: sorting according to the key= 
"""
data = [("apple", 5), ("banana", 2), ("cherry", 8)]

res = sorted(data, key=lambda x: x[1]) # sorted(iterable, key=lambda x: x[])
print(res)

""" 
#task 22: sorting dict
"""
users = [{"name": "Jane", "age": 30}, {"name": "John", "age": 25}]

res = sorted(users, key=lambda x: x["age"])
print(res)

""" 
#task 23: Use filter() with a lambda to keep only odd numbers from [1, 2, 3, 4, 5, 6]. 
# Then use map() with a separate lambda to cube ( power of  3 ) the remaining numbers.
"""
l = [1,2,3,4,5,6]
res = filter(lambda x: x % 2 == 1 , l)

cube = map(lambda x: x**3, res)
print(list(cube))
print(list(res)) # bosh list chiqadi chunki res bu iterator va res ni map ishlatib qoydi 

""" 
#task 24: Sort a list of strings names = ['Zoe', 'Adam', 'Alex', 'Ben'] first by length (shortest first),
# and then alphabetically (A-Z) using the key argument in the sorted() function with a tuple-returning lambda.
"""
names = ["Zoe", "Alex", "Ben"]

res = sorted(names, key=lambda x: (len(x), x))
print(res)

""" 
#task 25: Create a list of lambda functions: one for adding 5 , one for subtracting 2 , and one for multiplying by 10 .
# Iterate through a number, say 10 , and apply all the functions sequentially, printing the result of each step.
"""
l = [lambda x: x+5, lambda x: x - 2, lambda x: x * 10]
n = 10
for i in l:
    print(i(n))
""" 
#task 26: Use the apply_operation function from Exercise 3. Pass a lambda function to it that calculates the remainder (modulo) of two numbers.
"""
def add(a: int, b: int)->int:
    return a + b

def apply_operation(x: int, y: int, operation: Callable):
    return operation(x, y)

#print(apply_operation(7, 3, add))

res = apply_operation(7, 3, lambda a, b: a % b)
print(res)

""" 
#task 27: 
"""
l = [1,2,3,4,5,6,7,8,9]

res = [i for i in l if (lambda x: x % 2 == 0)(i)]
print(res)

is_even = lambda x: x % 2 == 0
result = [i for i in l if is_even(i)]

""" 
#task 28: Define a lambda function that takes a and returns another lambda function that takes b and returns a + b . 
# Call the outer lambda with 10 to get a new function, and then call the new function with 5 .
"""
r_out = lambda a: lambda b: a + b

res = r_out(10)
result = res(5)
print(result)

""" 

