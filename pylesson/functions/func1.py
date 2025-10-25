# task 1: 
"""
def greeting():
    print("hello world")
greeting()

"""
#task 2: Return vs Print: Write two functions: one prints the sum of two numbers, the other returns the sum. Show the difference when you use them in another #expression.
"""
def sum_find(a:int, b:int) -> int:
    return a + b
res = sum_find(5, 5)
print(res)

""" 
"""
def sum_f(a:int, b:int) -> int:
    print(a + b)
sum_f(5, 5)

""" 
#task 3: Personal Greeting: Define a function greet_user(name) that returns "Hello, <name>!".

def greet_user(name: str) -> str:
    return "Hello" "Mr" + name 

greet_user("Teo")