# task 14: Word Reverser: Write a function reverse_word(word) that returns the reversed version of the string.
""""
def reverse(string)->str:
    return string[::-1]

print(reverse("Eshmat"))
"""

#task 1: Simple Greeting: Write a function greet() that prints "Hello, world!" when called.
"""
def greeting()->str :
    print("hello world")
    return None
greeting()

"""
#task 2: Return vs Print: Write two functions: one prints the sum of two numbers, the other returns the sum. Show the difference when you use them in another expression.
"""
def sm()->int:
    print(5+5)
    return None
sm()
""" 

def sm(x:int, y: int)->int:
    return x+y
a, b = map(int, input("Enter two numbers: ")).split()
res = sm(a, b)