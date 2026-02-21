#===========THESE TASKS RELATED TO OFFLINE COURSE FROM GITHUB============

#task 1: Create a tuple numbers containing the integers 1, 2, 3, 4, 5.
"""
num = (1,2,3,4,5,)
print(num)
""" 
#task 2: Access and print the third element of the numbers tuple.
"""
num = (1,2,3,4,5,)
print(num[2])

""" 
#task 3: Find the length of the numbers tuple.
"""
num = (1,2,3,4,5,)
print(len(num))
""" 
#task 4: Try to change the first element of numbers to 10. What happens?
"""
num = (1,2,3,4,5,6,7,8,9,10,)
num[0] = 2
print(num) # TypeError , since that we can't modify tuple's value once it is created

""" 
#task 5: Create a tuple fruits with the elements 'apple', 'banana', 'cherry'.
"""
fruit = ("apple", "banana", "cherry",)
print(fruit)

""" 
#task 6: Check if 'banana' exists in the fruits tuple using an if statement.
"""
fruit = ("apple", "banana", "cherry",)

if "banana" in fruit:
    print("True: banana exists in this tuple")
else:
    print("False: banana doesn't exist in this tuple")

""" 
#task 7: Use a for loop to print each fruit in the fruits tuple.
"""
fruit = ("apple", "banana", "cherry",)
for item in fruit:
    print(item)
""" 
#task 8: Create a new tuple combined by joining numbers and fruits.
"""
nfruit = ("banana", "apple", 1, 3, 5, "orange")
print(nfruit)
""" 
#task 9: Count how many times the number 3 appears in a tuple like (1, 2, 3, 3, 4).
"""
num = (1,2,3,3,4,)
print(num.count(3))

""" 
#task 10: Unpack the tuple ('red', 'green', 'blue') into three separate variables.
"""
color = ('red', 'green', 'blue')

x, y, z = color
print(x,y,z)

""" 
#task 11: Create a tuple colors with three colors. Use a for loop to print each color along with its index.
"""
color = ('red', 'green', 'blue')
for item in color:
    print(item)
""" 
#task 12: Create a tuple with a single element, ('single',).
"""
single = (1,)
print(type(single))

""" 
#task 13: Write a program to find the maximum value in a tuple of numbers (10, 5, 20, 15).
"""
num = (10, 5, 20, 15,)
"""
""""""
"""mx = num[0]
for i in num:
    if i > mx:
        mx = i
print("max num: ", mx)"""
""" 
print(max(num))

"""
#task 14: Use a while loop to print the elements of the tuple ('a', 'b', 'c').
"""
alpha = ("a", "b", "c")
i = 0

while i < len(alpha):
    print(alpha[i])
    i+=1
""" 
#task 15: Create a nested tuple my_data = (('John', 25), ('Jane', 30)).
"""
my_data = (("john",25), ("jane", 30))
print(my_data)
""" 
#task 16: Access and print the age of 'John' from my_data.
"""
my_data = (("john",25), ("jane", 30))
print(my_data[0][1])

""" 
#task 17: Convert the list ['milk', 'bread', 'eggs'] into a tuple.
"""
items = ["milk", "bread", "eggs"]

mytup = tuple(items)
print(mytup)
""" 
#task 18: Check if a tuple is empty using an if statement.
"""
num = tuple()

if len(num) == 0:
    print("empty")
else:
    print("full")
""" 
#task 19: Write a program that takes a number and checks if it is present in the tuple (2, 4, 6, 8, 10).
"""
num = (2,4,6,8,10,)

user = int(input("enter the number: "))
if user in num:
    print(f"{user} is in tuple")
else:
    print(f"{user} is not in tuple")
""" 
#task 20: Create a tuple of squares for numbers from 1 to 5 without using a comprehension.
"""
num = (1,2,3,4,5,)

ls = []

for i in num:
    ls.append(i**2)
res = tuple(ls)

print(res, type(res))
""" 

#==========SET EXERCISES==================

#task 1: Create a set unique_numbers with the elements 1, 2, 3, 4, 2. Print the set.
"""
nums = {1,2,3,4,2}
print(nums)
""" 
#task 2: Add the number 5 to the unique_numbers set.
"""
nums = {1,2,3,4,2}
nums.add(5)
print(nums)
""" 
#task 3: Add multiple numbers, 6 and 7, to the set.
"""
nums = {1,2,3,4,5}
num = {6,7}

nums.update(num)
print(nums)
""" 
#task 4: Remove the number 3 from the set.
"""
nums = {1,2,3,4,5}
nums.discard(3)
print(nums)

""" 
#task 5: Try to remove a number that doesn't exist, like 10, using the discard() method.
"""
nums = {1,2,3,4,5}
nums.discard(10)
print(nums)

""" 
#task 6: Use an if statement to check if the number 4 is in the set.
"""
nums = {1,2,3,4,5}
if 4 in nums:
    print("4 is in set")
else:
    print("4 is not in set")
""" 
#task 7: Create two sets: set1 = {1, 2, 3, 4} and set2 = {3, 4, 5, 6}.
"""
set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1, set2)

""" 
#task 8: Find and print the union of set1 and set2.
"""
set1 = {1,2,3,4}
set2 = {3,4,5,6}

print(set1.union(set2))

""" 
#task 9: Find and print the intersection of set1 and set2.
"""
set1 = {1,2,3,4}
set2 = {3,4,5,6}

res = set1.intersection(set2)
print(res)

""" 
#task 10: Find and print the difference between set1 and set2.
"""
set1 = {1,2,3,4}
set2 = {3,4,5,6}

res = set1.difference(set2)
print(res)

"""
#task 11: Convert the list [1, 1, 2, 3, 3, 4] into a set to find all the unique numbers.
"""
num = [1,1,2,3,3,4]

res = set(num)
print(res)

""" 
#task 12: Use a for loop to iterate through a set and print each element.
"""
myset = {"reo", 1,2,3,4, "teo", False, 3.3}

for item in myset:
    print(item)
""" 
#task 13: Write a program that uses if-else to determine if a number is present in a set.
"""
num = {1,2,3,4,5,6,7,8,9,False}

if 0 in num:
    print(" 0 is in set")
else:
    print("0 is not in set")
""" 
#task 14: Check if set1 is a subset of a new set set3 = {1, 2, 3, 4, 5}.
"""
set1 = {1,2,3,4}
set2 = {1,2,3,4,5}

res = set1.issubset(set2)
print(res)
""" 
#task 15: Check if set3 is a superset of set1.
"""
set2 = {1,2,3,4,5}
set3 = {1,2,3,4,5,6,7}

print(set3.issuperset(set2))

""" 
#task 16: Write a program to find the unique elements in a list ['a', 'b', 'a', 'c', 'b'] using a set.
"""
l = ['a', 'b', 'a', 'c', 'b']

res = set(l)

print(res)
""" 
#task 17: Clear all elements from a set.
"""
set3 = {1,2,3,4,5,6,7}
set3.clear()

print(set3)
""" 
#task 18: Ask a user for three of their favorite colors and store them in a set.
"""
empty = set()

for _ in range(3):
    user = input("enter favorite colors(3): ")
    empty.add(user)
print(empty)

""" 
#task 19: Find the symmetric difference between set1 and set2.
"""
set1 = {1,2,3,4}
set2 = {2, 5, 3, 6}

res = set1.symmetric_difference(set2)
print(res)

""" 
#task 20: Create a set of even numbers from 1 to 10.
"""
myset = {i for i in range(1,11) if i % 2 == 0}
print(myset)
""" 
