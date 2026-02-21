# ==============EXERCISES FOR TUPLE===================

#task 1: Create a tuple of the 7 days of the week.
"""
week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",)
print(week)
"""
#task 2: Create a tuple with a single item, "Python".
"""
single = (1,)
print(type(single))
"""
# task 3: Access the first item of a given tuple.
"""
tup = ("teo", "is", "learning", "python", 1,)

print(tup[0])

"""
#task 4: Access the last three items of a tuple using slicing.
"""
tup = ("teo", "is", "learning", "python", 1, 2, 3, 4, 5,)
print(tup[-3:])

"""
#task 5: Unpack the following tuple into three separate variables: my_tuple = ("red", "green", "blue").
"""
my_tup = ("red", "green", "blue")

x, y, z = my_tup
print(x, y, z)

""" 
#task 6: Attempt to change the second item of a tuple and observe the TypeError.
"""
tupl = ("teo", "is", "learning", "python", 1,)
l = list(tupl)
l[1] = "reo"
tupl = l
print(tupl)  # i have done task and this is other thing

"""
#task 7: Check if "Tuesday" is in your days of the week tuple.
"""
week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",)

if "tuesday" in week:
    print("yes, tuesday is in week")
else:
    print("tuesday is not in week")
"""
#task 8: Count how many times "a" appears in the following tuple: ('a', 'b', 'c', 'a', 'd').
"""
mytup = ('a', 'b', 'c', 'a', 'd')
print(mytup.count('a'))
"""
# task 9: Find the index of "red" in a tuple of colors.
"""
colors = ("blue", "orange", "black", "red", "white")
print(colors.index("red"))
"""
#task 10: Convert your days of the week tuple into a list.
"""
week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",)

lweek = list(week)
print(lweek)

"""
#task 11: Add a new day, "Funday", to the list you created, then convert it back to a tuple.
"""
week = ("monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday",)
lweek = list(week)
lweek.append("funday")
week = tuple(lweek)

print(week)

"""
#task 12: Convert a string like "hello" into a tuple of its characters.
"""
st = "Hello"
tup = tuple(st)

print(tup)

"""
#task 13: Given two tuples, t1 = (1, 2) and t2 = (3, 4), concatenate them to create a new tuple t3 = (1, 2, 3, 4).
"""
t1 = (1, 2,)
t2 = (3, 4,)
t3 = t1 + t2

print(t3)
"""
#task 14: Repeat a tuple three times to create a new tuple.
"""
t1 = ('a', 'b')
t2 = t1 * 3
print(t2)
"""
#task 15: Use a for loop to print each item in a tuple.
"""
tup = ("python", "is", "ok", "me", 1, 2,)

for i in tup:
    print(i)
"""
#task 16: Use a while loop to print each character of a tuple of characters.
"""
i = 0
tup = ("python", "is", "ok", "me", 1, 2,)

while i < len(tup):
    print(tup[i])
    i+=1
"""
#task 17: Iterate through a tuple of numbers and print only the odd ones.
"""
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for i in tup:
    if i % 2 == 1:
        print(i)
""" 
#task 18: Find the sum of all numbers in a tuple.
"""
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
s = 0
for i in tup:
    s+=i
print(s)

"""
#task 19: Find the length of each string in a tuple of strings.
"""
tup = ("python", "learning", "ego", "path")

for i in tup:
    print(len(i))
"""
#task 20: Given a tuple of tuples (e.g., ((1, 2), (3, 4))), print each inner tuple.

#tup = ((1,2), (3, 4))
"""
for i in tup:
    for j in i:
        print(j)
"""
"""
for a, b in tup:
    print(a, b)
"""
#task 21: Create a function that returns a tuple containing the minimum and maximum numbers from a list.
"""
def come_back(l: list)->tuple:
    res = tuple(l)
    return max(res), min(res)

res = come_back(l = [1,2,3,4,5,6])
print(type(res))
print(res)
""" 
#task 22: Create a tuple to represent the latitude and longitude of your city.
"""
coords = (41.2995, 69.2401)
print(coords)
""" 
#task 23: Create a tuple of strings that can be used as keys in a dictionary.
"""
keys = ("name", "age", "country")
person = dict.fromkeys(keys)
print(person)

""" 
#task 24: Create a list of tuples, where each tuple contains a student's name and grade.
"""
l = [("teo", 70), ("scott", 77), ("reo", 88)]
print(l)
""" 
#task 25: Iterate through the list of student tuples and print the name and grade for each.
"""
l = [("teo", 70), ("scott", 77), ("reo", 88)]
for item in l:
    name, grade = (item)
    print(name, grade)
""" 
#task 26: Sort the list of student tuples by grade.
"""
l = [("teo", 88), ("scott", 50), ("reo", 49)]
l.sort()
print(l)

""" 
#task 27: Create a function that takes a list of numbers and returns a tuple with the count of positive and negative numbers.
"""
def func(l: list)-> tuple:
    cnt_n , cnt_p = 0, 0
    for i in l:
        if i > 0:
            cnt_p+=1
        else:
            cnt_n-=1
    return cnt_p, cnt_n
res = func(l = [1,-1,2,-2,3,-3,4,-4])
print(res)
print(type(res))
""" 
#task 28: Given a string "Hello World", use a tuple to count the occurrences of vowels (a, e, i, o, u) and print the results.
"""
st = "Hello World"
vovels = ("a", "e", "i", "o", "u",)
cnt = 0

for i in st.lower():
    if i in vovels:
        cnt+=1
print("vovels in string: ", cnt)
""" 
#task 29: Create a tuple representing a user's profile: (username, email, registration_date).
"""
user_profile = (
    "teo7",
    "teostark@gmail.com",
    "2025-12-11"
)
print(user_profile)
""" 
#task 30: Given a tuple of integers, use a loop to check if all numbers are positive.
"""
nums = (1, 2, 3, 4, 5, 6, 1,)
all_nums = True

for i in nums:
    if i < 0:
        all_nums = False
        break
print(all_nums)
""" 
#task 31: Use a for loop to print the index and item of a tuple using enumerate().
"""
things = ("reo", "apple", "python", 1, 2, 4)

for i , item in enumerate(things, start=1):
    print(i, item)
""" 
#task 32: Create a tuple of fruits. Write a loop to print the fruit and "is a fruit" for each.
"""
fruit = ("apple", "banana", "grape", "orange", "kiwi")
i = 0

while i < len(fruit):
    print(f"{fruit[i]} is a fruit")
    i+=1
""" 
#task 33: Given a tuple of names, find the longest name.
"""
names = ("teo", "teo", "tony", "steve", "eve")
mx = names[0]
i = 0
while i < len(names):
    if len(names[i]) > len(mx):
        mx = names[i]
    i+=1
print(f"the longest name is {mx}")

""" 
"""
names = ("teo", "teo", "tony", "steve", "eve")

mx = max(names, key=len)
print(mx, "is the longest name")
""" 
"""
names = ("teo", "teo", "tony", "steve", "eve")
mx = sorted(names, key=len)[-1]
print(mx, "is the longest name")
""" 
#task 34: Given a nested tuple ( (1,2,3), (4,5,6) ), flatten it into a single tuple (1,2,3,4,5,6).
"""
num = ( (1,2,3), (4,5,6) )

a, b = ((1,2,3), (4,5,6))
tup = (*a, *b)

print(tup)
""" 
#task 35: Check if an item exists in a tuple without using a loop or if/in. (Hint: Use .index() and handle the ValueError).
"""
names = ("teo", "teo", "tony", "steve", "eve")

try:
   idx = names.index("teo")
   print("index of item is : ", idx)
except ValueError:
    print("thing you try to find is not here")
""" 
#task 36: Create a tuple of numbers. Find the average of all numbers.
"""
nums = (1,2,3,4,5,6,7,8,9,10)
avg = 0
avg = sum(nums) / len(nums)

print(f"average of nums is: {avg}")

""" 
#task 37: Create a function that takes a string and returns a tuple of the first character, the last character, and the length of the string.
"""
def taker(s: str)-> tuple:
    return s[0], s[-1], len(s)

print(taker(s = "i am learning python"))
""" 
#task 38: Write a program that asks a user for a name, email, and age, and stores this information as a single tuple.
"""
name = input("enter your name: ")
email = input("enter your email: ")
age = int(input("enter your age: "))

info = name, email, age
print(info)

""" 
#task 39: Explain the difference between (1, 2, 3) and [1, 2, 3] in terms of mutability and memory.

t = (1,2,3,) # omce we create this , it wont change again , we can't change it later in memory unchangebale
l = [1,2,3] # this is list after creating , we can easyly change , remove and modify this datatype it is changeable in memory
