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
"""
def greet_user(name: str) -> str:
    return "Hello" "Mr" + name 

greet_user("Teo")

""" 
#task 4:  Create a function is_even(n) that returns True if a number is even, else False.
"""
def num_check(a: int)-> int:
    if a % 2 == 0:
        return True 
    else:
        return False 
    
res = num_check(3)
print(res)

""" 
#task 5: Write a function square(x) that returns the square of the number. Print the result of squaring numbers from 1 to 5 using a loop.
"""
def square(x: int)-> int:
    return x**2
for i in range(1,5):
    res = square(i)
    print(res)
""" 
#task 6: Write a function max_of_two(a, b) that returns the larger of two numbers using an if statement.
"""
def max_of_two(a: int, b: int)-> int:
    if a > b:
        return a
    elif b > a:
        return b
    else:
        return a, b
    
res = max_of_two(5, 6)
print(res)

""" 
#task 7: Define a function repeat_message(msg, n) that prints the message n times using a loop.
"""
def repeat_message(msg: str, n: int):
    for i in range(n):
        print( msg)
    
repeat_message("Hello Teo", 5)

""" 
#task 8: Write a function string_length(s) that returns the length of a string. Use it in a loop to print lengths of each word in a list.
"""
def find_l(s: str)-> int:
    cnt = 0
    for i in s:
        cnt+=1
    return cnt

word = ["Teo", "you", "have", "aim"]
for w in word:
    print(w, "->", find_l(w))
""" 
#task 9: Define a function sum_list(numbers) that returns the sum of all numbers in a list.
"""
def sum_list(nums: list) -> int:
    s= 0
    for i in nums:
        s+=i
    return s
res = sum_list([1,2,3,4,5,6,7])
print(res)

""" 
#task 10: Write a function greet_all(names) that takes a list of names and prints a greeting for each.
"""
def greet(name: list[str])-> str:
    for n in name:
        print(f"hello Mr {n}")
greet(["Ali", "Teo", "Timba"])

""" 
#task 11: Write a function min_of_three(a, b, c) that returns the smallest number.
"""
def small_num(a: int, b: int, c:int)->int:
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < b and c < a:
        return c
    else:
        return a, b, c

res = small_num(10, 11, 13)
print(res)

"""
#task 12: Check Membership: Write a function contains(item, collection) that returns True if item is found in the list, set, or tuple.
"""
from typing import Any

def contain(item: Any, collection: Any)-> bool:
    return item in collection

print(contain("apple", ["banana", "orange", "pineapple", "Ttrue"]))

""" 
#task 13: Count Vowels: Write a function count_vowels(word) that returns the number of vowels in the given word.
"""
def count_v(word: str)->int:
    vovels = "aeiou"
    cnt = 0
    for w in word.lower():
        if w in vovels:
            cnt+=1
    return cnt       
 
res = count_v("Eshmat")
print(res)

""" 
#task 14: Word Reverser: Write a function reverse_word(word) that returns the reversed version of the string.
"""
def reverser(word: str)-> str:
    return  word[:: -1]

n = input("Enter word you wanna reverse: ")
print(reverser(n))

""" 
#task 15: Grade Calculator: Define a function get_grade(score) that returns "A", "B", "C", etc., based on numeric score using if-elif-else
"""
def grade_calculate(a: int)-> str:
    if a  > 100:
        return "You must enter between 1 and 100"
    if a > 90 and a <= 100 :
        return 'A'
    elif a < 90 and a >= 80:
        return 'B'
    elif a < 80 and a >= 60:
        return 'C'
    else:
        return 'D'
    
print(f"your grade is {grade_calculate(101)}")

""" 
#task 16: Power Function: Write a function power(base, exp=2) that returns base ** exp. Demonstrate both default and explicit argument usage.
"""
def power(base: int, exp: int = 2)-> int:
    return base**exp
res = power(2,3)
print(res)

""" 
# task 17: Temperature Converter: Create a function to_celsius(kelvin) and kelvin(celsius) using appropriate formulas. Celsius to Kelvin: K = C + 273.15 Kelvin #to Celsius = C = K - 273.15
"""
def temp_convert()-> float:
    print("=" * 40)
    print(" TEMPERATURE CONVERTER ")
    print("=" * 40)
    print("1 CELSIUS -> KELVIN")
    print("2 KLEVIN -> SELSIUS")
    print("-" * 40)
    
    choice = int(input("enter your choice(1, 2): "))
    temp = float(input("enter temperature: "))
    
    print("-" * 40)
    
    if choice == 1:
        kelvin = temp + 273.15
        print(f"{temp} C = {kelvin:.2f} K")
        return kelvin
    elif choice == 2:
        celsius = temp - 273.15
        print(f"{temp} K = {celsius:.2f} C")
        return celsius
    else:
        print("wrong choice !")
        return None
    
res = temp_convert()

""" 
#task 18: Unique Elements: Write a function unique_elements(lst) that returns a set of unique values from a list.
"""
def unique_elements(lst: list[int])-> set[int]:
    return set(lst)

res = unique_elements([1,2,1,1,1,2,2,3,4,4,4,5,5])
print(res)
""" 
#task 19: Factorial Calculation: Define a function factorial(n) that returns the factorial of a positive integer using a loop.
"""
def faktorial(n: int)-> int:
    if n < 0:
        return "ERROR YOU SHOULD ENTER BIGGER THAN ZERO"
    else:
        res = 1
        for i in range(1, n + 1):
            res*=i
    return res
    
res = faktorial(5)
print(res)
""" 
#task 20: Filter Positives: Write a function filter_positive(nums) that returns a list of only positive numbers.
"""
def filter_positive(n: list[int])->list[int]:
    positive = []
    for i in n:
        if i > 0:
            positive.append(i)
    return positive
        
res = filter_positive([-1,-2,-3,1,2,3])
print(res)

""" 
