#==============TASKS THAT RELATED TO FUNCTIONS===========

#task 1: Simple Greeting: Write a function greet() that prints "Hello, world!" when called.
"""
def greet()->None:
    print("hello world!")
    return None

greet()

""" 
#task 2: Return vs Print: Write two functions: one prints the sum of two numbers, the other returns the sum. Show the difference when you use them in another expression.
"""
def add(a: int, b: int)-> int:
    return a + b

res = add(4, 4)

print(res+10) # we can easily use it later if we need

def add1(a: int, b: int)->None:
    print(a+b)
    

add1(7, 7)

""" 
#task 3: Personal Greeting: Define a function greet_user(name) that returns "Hello, <name>!".
"""
def greet(name: str)->str:
    return f"Hello, {name}"

res = greet("Rura")
print(res)

user_name = input("enter your name: ") # function ichida bolmaydi chunki , function bu hisob , tekshiruv va return qiladi , ichida input bolsa buzib qoyadi!
res = greet(user_name)
print(res)

""" 
#task 4: Odd or Even: Create a function is_even(n) that returns True if a number is even, else False.
"""
def state_ch(n: int)->bool:
    if n % 2 == 0:
        return f"is_even {True}"
    else:
        return f"is_even {False}"
    
res = state_ch(9)
print(res)

""" 
#task 5: Square Function: Write a function square(x) that returns the square of the number. Print the result of squaring numbers from 1 to 5 using a loop.
"""
def square(a: int)->int:
    return a*2

for i in range(1, 11):
    print(square(i))
""" 
#task 6: Maximum of Two: Write a function max_of_two(a, b) that returns the larger of two numbers using an if statement.
"""
def max_of_two(a: int, b: int)->int:
    if a > b:
        return a
    elif a == b:
        return f"{a} and {b} are equal"
    else:
        return b
    
res = max_of_two(6, 5)

print(res)

""" 
#task 7: Multiple Calls: Define a function repeat_message(msg, n) that prints the message n times using a loop.
"""
def repeat_message(msg: str, n: int):
    for i in range(n):
        print(msg)
        
msg = "rura is rura"
n = 3

repeat_message(msg, n)
""" 
#task 8: String Length: Write a function string_length(s) that returns the length of a string. Use it in a loop to print lengths of each word in a list.
"""
def string_length(s: str)->int:
    return len(s)

n = ["rura", "is", "python", "learn"]

for i in n:
    print(string_length(i))
""" 
#task 9: Sum of List: Define a function sum_list(numbers) that returns the sum of all numbers in a list.
"""
def sum_list(n: list)-> int:
    s = 0
    for i in n:
        s+=i
    return s

n = [1,2,3,4,5,6,7,8,9,10]

res = sum_list(n)
print(res)

""" 
#task 10: Greeting All: Write a function greet_all(names) that takes a list of names and prints a greeting for each.
"""
def greet_all(names: list):
    for i in names:
        print(f"hello, {i}")

names = ["rura", "teo", "eshmat", "ahmad"]
greet_all(names)

""" 
#task 11: Minimum of Three: Write a function min_of_three(a, b, c) that returns the smallest number.
"""
def min_of_three(a: int, b: int, c: int)-> int:
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < b and c < a:
        return c
    else:
        return a, b, c
    
    
res = min_of_three(5,5,5)
print(res)

""" 
#task 12: Check Membership: Write a function contains(item, collection) that returns True if item is found in the list, set, or tuple.
"""
from typing import Iterable, Any

def check_member(item: any, l: Iterable)->bool:
    return item in l
    
names = ["rura", "perror", "iterbek", "genbek"]
res = check_member("ruraw", names)
print(res)

""" 
#task 13: Count Vowels: Write a function count_vowels(word) that returns the number of vowels in the given word.
"""
def count_v(word: str)->int:
    c = 0
    vovel = "aeoui"
    for ch in word.lower():
        if ch in vovel:
            c+=1
    return c

word = "HellO world"
res = count_v(word)

print(res)

""" 
#task 14: Word Reverser: Write a function reverse_word(word) that returns the reversed version of the string.
"""
def reverser(w: str)->str:
    return "".join(reversed(w))

w = "Iman"
res = reverser(w)
print(res)

#=======TWO WAYS FOR SOLUTION======

def rev(w):
    return w[::-1]

w = "Itarator"
res = rev(w)
print(res)

""" 

#task 15: Grade Calculator: Define a function get_grade(score) that returns "A", "B", "C", etc., based on numeric score using if-elif-else.
"""
def grade_score(a: int)->str:
    if a >= 90 :
        return "A"
    elif a >= 70:
        return "B"
    elif a >= 50:
        return "C"
    else:
        return "F"
    
user = int(input("enter score: "))

res = grade_score(user)
print(res)

"""
#task 16: Power Function: Write a function power(base, exp=2) that returns base ** exp. Demonstrate both default and explicit argument usage.
"""
def power(b: int, exp = 2)-> int:
    return b**exp


res = power(5,3)
print(res)
""" 
#task 17: Temperature Converter: Create a function to_celsius(kelvin) and kelvin(celsius) using appropriate formulas. 
# Celsius to Kelvin: K = C + 273.15 Kelvin to Celsius = C = K - 273.15
"""
def convert_temp(val: float, to: str)->float:
    if to == "C":
        return val - 273.15
    elif to == "K":
        return val + 273.15
    else:
        raise ValueError("to must be C or K")
    
    
print(convert_temp(300, "C"))
print(convert_temp(300, "K"))

""" 
#task 18: Unique Elements: Write a function unique_elements(lst) that returns a set of unique values from a list.
"""
def unique_element(l: list)-> list:
    return list(set(l))

l = [1,1,1,2,2,2,3,3,4,4,5,5,6]
res = unique_element(l)
print(res)

""" 
#task 19: Factorial Calculation: Define a function factorial(n) that returns the factorial of a positive integer using a loop.
"""
def factorial(n: int)-> int:
    s = 1
    for i in range(1, n + 1):
        s = s * i
    return s


n = 5
res = factorial(n)
print(res)

""" 
#task 20: Filter Positives: Write a function filter_positive(nums) that returns a list of only positive numbers.
"""
def filter_positive(l: list)-> list:
    res = [i for i in l if i > 0]
    return res

l = [-1, -2, -3, 1,2,3]
res = filter_positive(l)
print(res)

""" 
#task 21: Sum of All: Define sum_all(*args) that returns the sum of all arguments passed.
"""
def find_sum(*args)-> int:
    return sum(args)

l = [1,2,3,4,5,6,7,8,9]
res = find_sum(*l)
print(res)

def find_s(*args: int)-> int:
    return sum(args)

res = find_s(1,2,3,4,5,6,7,8,9,10)
print(res)

""" 
#task 22: Multiply All: Write a function multiply_all(*args) that multiplies all numbers passed.
"""
def multiply_all(*args: int)-> int:
    total = 1
    for i in args:
        total*=i
    return total

res = multiply_all(1,2,3,4,5,6,7,8,9)
r = [1,2,3,4,5,6,7,8,9]
x = multiply_all(*r) # it is unpacking datas from r: list

print(res)
print(x)

""" 
#task 23: Student Info: Define a function student_info(name, age, **details) that prints student information. Example call:
"""
def show(**kwargs):
    print(kwargs)
    
show(**{"name": "teo", "city": "termez", "age": 22}) # name=key qilib bermoqchi bolmasak , shunaqa beramiz bu argumentni dict qilib yig'ib beradi
""" 
"""
def student_info(name: str, age: int, **details: dict):
    print(name,age,details)
    
student_info("teo", 22, phone="937026403")
""" 
#task 24: Keyword Override: Write a function describe_pet(animal, name="Unknown"). Call it using both positional and keyword arguments.
"""
def describe_pet(animal: str, name="whisky")->dict:
    info ={"animal": animal, "name": name}
    return info
    
print(describe_pet("lion"))

""" 
#task 25: Flexible Average: Define a function average(*numbers) that returns the average of any count of numbers.
"""
def average(*args):
    return sum(args)

res = average(1,2,3,4,5,6,7,8,9,10)
print(res)

n = [10,20,30,40,50,60,70,80,90,100]
res1 = average(*n)
print(res1)

""" 
#task 26: Dictionary Printer: Write a function print_dict(**kwargs) that prints key-value pairs.
"""
def person(**kwargs: dict)-> dict:
    print(kwargs)
    
person(
    name= "Teo",
    age= 22,
    city= "USA",
    skill= "backendDev"
)

""" 
#task 27: Args & Kwargs Combo: Create a function show_data(*args, **kwargs) that prints args and kwargs separately.
"""
def show_date(*args, **kwargs):
    print(args)
    print(kwargs)
    
show_date("teo", 22, skill="programming", hobby="building")

""" 
#task 28: Sum or Multiply: Write a function calculate(*args, operation="sum") that performs either sum or multiplication depending on the keyword argument.
"""
def calculate(*args , operation="sum"):
    if operation == "multiply":
        s = 1
        for i in args:
            s*=i
        return s
    elif operation == "sum":
        return sum(args)
    else:
        print("you can only enter multiply! and enter nothing to sum")
    
print(calculate(1,2,3,4))

print(calculate(1,2,3,4,5,6,7, operation= "multiply"))

""" 
#task 29: Configurable Greeting: Define a function custom_greet(name, **options) that can change greeting style:
"""
def custom_greet(name: str, **options):
    styles = options.get("style", "normal")
    emoji = options.get("emoji", False)
    
    if styles == "formal":
        greeting = f"Good day, {name}"
    elif styles == "friendly":
        greeting= f"hey {name}"
    else:
        greeting = f"hello, {name}"
        
    if  emoji:
        greeting 
    return greeting

print(custom_greet("teo", options="friendly"))

""" 
#task 30: Build Sentence: Write a function build_sentence(*words, sep=" ") that joins words with the given separator and returns the sentence.
"""
def build_sentence(*args, sep=" "):
    return sep.join(args)

res = build_sentence("rura", "is", "learning", "programming", sep="-")
print(res)
""" 
#task 31: List Squarer: Write square_all(nums) that returns a new list containing the squares of all numbers.
"""
def square_all(num: list)-> list:
    res = [i**2 for i in num]
    return res

n = [1,2,3,4,5,6,7,8,9]
res = square_all(n)
print(res)

""" 
#task 32: Dict Inverter: Define invert_dict(d) that returns a new dict where keys and values are swapped.
"""
def invert_d(d: dict)->dict:
    res = {k: v for v, k in d.items()}
    return res


d = {"name": "teo", "age": 22, "skill": "backend"}
res = invert_d(d)
print(res)
""" 
#task 33: Set Intersection: Write a function common_elements(set1, set2) that returns their intersection.
"""
def common_elements(set1: set, set2: set)-> set:
    res = set1.intersection(set2)
    return res

myset = {1,2,3}
myset1 = (2, 3, 4)

res = common_elements(myset, myset1)
print(res)
""" 
#task 34: Tuple Converter: Define a function list_to_tuple(lst) that converts a list into a tuple.
"""
def list_to_tuple(l: list)-> tuple:
    return tuple(l)

l = [1,2,3,4,5]
print(list_to_tuple(l))
""" 
#task 35: Dict Search: Write find_key(d, value) that returns the key matching the given value in a dictionary.
"""
def find_key(d: dict, val):
    for k, v in d.items():
        if val == v:
            return k
    return None
d = {"name": "teo", "age": 22, "skill": "backend"}
res = find_key(d, 22)
print(res)

""" 
#task 36: List Filter Function: Define filter_even(numbers) that returns a list of even numbers only.
"""
def even_n(num: list)->list:
    res = [i for i in num if i % 2 == 0]
    return res

n = [1,2,3,4,5,6,7,8,9,10]
res = even_n(n)
print(res)

""" 
#task 37: Longest String: Write a function longest_word(words) that returns the word with the maximum length.
"""
def longest_word(words: str):
    mx_word = None
    for i in words.split():
        if mx_word is None or len(mx_word) < len(i):
            mx_word = i
    return f"{mx_word}: {len(mx_word)}"

print(longest_word("the longest word should be concentration"))

""" 
#task 38: Merge Dictionaries: Define a function merge_dicts(d1, d2) that combines both into one dictionary.
"""
def merge_dicts(d1: dict, d2: dict)-> dict:
    return d1 | d2 # it combines two dicts and same with update method , like  ==d1.update(d2)==

d1 = {"name": "teo"}
d2 = {"age": 22, "skill": "python"}
print(merge_dicts(d1, d2))

""" 
#task 39: Unique Count: Write unique_count(lst) that returns how many unique elements are in the list.
"""
def unique_count(l: list):
    res = []
    for i in l:
        if i not in res:
            res.append(i)
    return len(res) and res

l = ["rura","rura", "teo", 1, 2, 2, "r", "t", "t"]
print(unique_count(l))

"""
#task 40: List to Set Converter: Define list_to_set(lst) that removes duplicates and returns a set.
"""
def list_to_set(l: list)->set:
    return set(l)

l = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,7,7,8]
print(list_to_set(l))
""" 
#task 41: Prime Checker: Write a function is_prime(n) that returns True if n is a prime number.
"""
def is_prime(n: int)->bool:
    if n % 2 == 0:
        return False
    if n < 2:
        return False
    if n == 2:
        return True
    
    limit = int(n** 0.5)+1
    
    for i in range(3, limit, 2):
        if i % 2 == 0:
            return True
    return False

print(is_prime())

""" 
#task 42: Palindrome Checker: Define is_palindrome(s) that returns True if the string reads the same backward.
"""
def is_palindrome(s: str)-> bool:
    if s == s[::-1]:
        return True
    else:
        return False
    
s = "termat"
print(is_palindrome(s))
""" 
#task 43: Word Frequency: Write a function word_count(sentence) that returns a dictionary with word frequencies.
"""
def word_count(sentence: str)-> dict:
    freq = {}
    for i in sentence.split():
        if i not in freq:
            freq[i] = 1
        else:
            freq[i]+=1
    return freq

s = "i am learning python and he is learning python and i and he are learning C++"
print(word_count(s))

""" 
#task 44: Character Counter: Define char_frequency(s) that returns how many times each character appears in a string.
"""
def char_counter(s: str):
    freq = {}
    for ch in s:
        if ch == " ":
            continue
        else:
            if ch not in freq:
                freq[ch] = 1
            else:
                freq[ch]+=1
    return freq

s = "Dunyo ushalmagan armonlarga ushalmagan armonlar dunyo"
print(char_counter(s))

""" 
#task 45: Sort by Length: Write a function sort_by_length(words) that returns a list sorted by word length.
"""
def sorted_l(words: list)->list:
    res = sorted(words, key=len )
    return res

l = ["python", "dura", "concentration", "is", "isa", "s"]
print(sorted_l(l))

""" 
#task 46: Find Max Value in Dict: Define max_value(d) that returns the key with the highest value.
"""
def max_val(d: dict)-> dict:
    max_value = None
    max_key = None
    for k, v in d.items():
        if max_value is None or max_value < v:
            max_value = v
            max_key = k
    return max_key, max_value

d = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6, "g": 7}
res = max_val(d)
print(res)
""" 
"""
def mx_val(d: dict):
    return max(d, key=d.get)
print(mx_val({'a': 1, 'b': 2, 'c': 3}))
""" 
#task 47: Email Validator (Simple): Write is_valid_email(email) that checks if an email contains '@' and '.'.
"""
def is_valid_email(email: str)->bool:
    if "@" in email and "." in email:
        return True
    else:
        return False

s = "rura@gmail.com"
print(is_valid_email(s))

""" 
#task 48: Nested Function: Define outer_function(x) that contains an inner_function(y) returning x + y. Return the result of calling inner_function.
"""
def outer_func(x: int):
    def inner(y):
        return x + y
    return  inner(5)
    
print(outer_func(5))

""" 
#task 49: Custom Filter: Write a function custom_filter(numbers, condition) where condition is another function (e.g., is_even). Return numbers that satisfy the condition.
"""
def is_even(n):
    return n % 2 == 0

def custom_filter(num, con):
    res = []
    
    for i in num:
        if con(i):
            res.append(i)
    return res

print(custom_filter([1,2,3,4,5,6,7,8,9,10], is_even))

""" 
#task 50: Student Grades Average: Write a function average_grades(grades_dict) that takes a dictionary like:

st = {
    "teo": [70, 80, 60],
    "rura": [72, 75, 80],
    "eshmat": [50, 55, 60],
    "styles": [75, 80, 85]
}

def average_grade(d: dict):
    res = {}
    for student, subj in d.items():
        avg = sum(subj)/ len(subj)
        res[student] = round(avg, 2)
    return res

res = average_grade(st)
print(res)