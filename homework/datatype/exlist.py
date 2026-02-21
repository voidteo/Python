# ===========HOMETASK FROM LEARNING CENTRE=================

#task 1: Create a list of your 5 favorite fruits.
"""
l = ["banana", "apple", "orange", "pinapple", "grape"]
print(l)

"""
#task 2: Create a list of the numbers from 1 to 10.
"""
l = [1,2,3,4,5,6,7,8,9,10]
print(l)

"""
#task 3: Create an empty list called my_shopping_cart.
"""
my_shopping_cart = []
print(my_shopping_cart)
"""
#task 4: Access the third item in a given list.
"""
l = ["banana", "apple", "orange", "pinapple", "grape"]
print(l[2])
"""
#task 5: Print the last item of a list using a negative index.
"""
l = [1,2,3,4,5,6,7,8,9,10]
print(l[-1])
""" 
#task 6: Print the first three items of a list using slicing.
"""
l = [1,2,3,4,5,6,7,8,9,10]
print(l[:3])
"""
#task 7: Create a new list that contains a slice of the original list from the 4th item to the 8th.
"""
l = [1,2,3,4,5,6,7,8,9,10]
nl = l[3:8]
print(nl)
"""
#task 8: Check if a specific fruit is in your list of favorite fruits using an if statement.
"""
l = ["banana", "apple", "orange", "pinapple", "grape"]

if "banana" in l:
    print("banana exists in list")
else:
    print("the fruiet doest'n exist in list")
"""
#task 9: Add "grapes" to the end of your fruit list.
"""
l = ["banana", "apple", "orange", "pinapple"]

l.append("grape")
print(l)
"""
#task 10: Insert "mango" at the second position of your fruit list.
"""
l = ["banana", "apple", "orange", "pineapple"]

l.insert(1, "mango")
print(l)
"""
#task 11: Change the first item in your fruit list to "kiwi".
"""
l = ["banana", "apple", "orange", "pineapple"]

l[0] = "kiwi"
print(l)

""" 
#task 12: Remove the last item from your fruit list using .pop().
"""
l = ["banana", "kiwi", "apple", "orange", "pinapple"]

l.pop(-1)
print(l)
"""
#task 13: Remove "apple" from your fruit list using .remove().
"""
l = ["banana", "kiwi", "apple", "orange", "pinapple"]

l.remove("apple")
print(l)

""" 
#task 14: Empty the entire list of fruits.
"""
l = ["banana", "kiwi", "apple", "orange", "pinapple"]
l.clear()
print(l)
""" 
#task 15: Create a list of names and a list of ages. Extend the names list with the ages list.
"""
names = ["teo", "scott", "styles", "allison"]
ages = ["17", "17", "16", "18"]

names.extend(ages)

print(names)

""" 
#task 16: Create a copy of a list and modify the copy without affecting the original.
"""
names = ["scott", "styles", "allison"]
names2 = names.copy()

names2[0] = "teo"

print(names2)
print(names)

"""
#task 17: Use a for loop to print each fruit in your fruit list.
"""
fruit = ["kiwi", "banana", "apple", "orange", "pineapple"]

for i in fruit:
    print(i)
""" 
#task 18: Use a while loop to print each number from 1 to 5 from a list.
"""
num = [1,2,3,4,5]

item = 0
while item < len(num):
    print(num[item])
    item+=1
""" 
#task 19: Iterate through a list of strings and print only the ones that contain the letter 'a'.
"""
txt = ["Anas", "is", "learning", "programming", "never", "give up"]

for item in txt:
    if "a" in item.lower():
        print(item)
""" 
#task 20: Iterate through a list of numbers and print only the even numbers.
"""
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

for item in num:
    if item % 2 == 0:
        print(item)
""" 
#task 21: Find the sum of all numbers in a list using a loop.
"""
num = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
s = 0

for item in num:
    s+=item
print(s)

""" 
#task 22: Find the largest number in a list without using the built-in max() function.
"""
num = [1,2,3,4,5,6,20,8,9,10,11,12,13,14,15]
mx = num[0]

for item in num:
    if item > mx:
        mx = item
print(f"the largest number in list is: {mx}")

"""
#task 23: Count how many times "banana" appears in a list.
"""
fruit = ["banana", "orange", "apple", "banana", "kiwi", "banana"]

# print(fruit.count("banana")) # it is one method of solving to the given problem

cnt = 0
for item in fruit:
    if item == "banana":
        cnt+=1
print(f"there are {cnt} times in list")
"""
#task 24: Use a list comprehension to create a new list containing the squares of numbers from 1 to 10.
"""
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nl = [i**2 for i in l]

print(nl)

""" 
#task 25: 
"""
fruit = ["banana", "orange", "apple", "banana", "kiwi", "teo"]
upper_fruit = [fruit.upper() for fruit in fruit]
print(upper_fruit)

""" 
#task 26: Use a list comprehension to filter a list of words, keeping only those with more than 5 characters.
"""
fruit = ["banana", "orange", "apple", "banana", "kiwi", "teo"]

nfruit = [item for item in fruit if len(item)>5]

print(nfruit)

""" 
#task 27: Use a list comprehension to convert all strings in a list to uppercase.
"""
fruit = ["banana", "orange", "apple", "banana", "kiwi", "teo"]

upper_fruit = [item.upper() for item in fruit]

print(upper_fruit)

"""
#task 28: Create a list of sentences. Use a loop to print each sentence along with its length.
"""
txt = ["Dunya", "has", "fitna", "seek", "knowledge"]

for i in txt:
    print(i, ":",len(i))
""" 
#task 29: Create a list of mixed data types (e.g., strings, numbers, booleans).
"""
l = ["python", 1, True, False, 3.5]
print(l)

"""
#task 30: Reverse a list without using the built-in .reverse() method.
"""
l = ["python", 1, True, False, 3.5]
print(l[::-1])
"""
#task 31: Given two lists, create a third list containing only the items that are present in both.
"""
l = ["python", "teo", "learn"]
m = ["python", 22, "tree"]

lm = [item for item in l if item in m]

print(lm)

"""
#task 32: Remove all duplicate items from a list.
"""
l = ["python", "teo", "learn", "python", "teo", "learn"]

newls = []

for i in l:
    if i not in newls:
        newls.append(i)
print(newls)
""" 
#task 33 Sort a list of strings alphabetically.
"""
l = ["some", "people", "argue", "i", "am", "seeking"]
l.sort()
print(l)
"""
#task 34: Sort a list of numbers in descending order.
"""
l = [10,9,8,7,6,5,4,3,2,1]
l.sort()

print(l)
""" 
#task 35: Given a list of names, create a new list with a greeting for each name (e.g., "Hello, Alice!").
"""
names = ["allison", "scott", "styles", "lydia"]
greet = []

for i in names:
    greet.append(f"Hello, {i}")
print(greet)

"""
#task 36: Create a list of five user-entered names.
"""
names = []

for i in range(1, 6):
    n = input("enter name: ")
    names.append(n)
print(names)
""" 
"""
names = [input("enter name: ") for _ in range(5)]   # this is list comprehension method of code that was above this
print(names)

"""
#task 37: Ask the user for a number, then create a list containing that many zeros.
"""
num = int(input("enter number: "))
l = []
i = 0

while i < num:
    l.append(0)
    i+=1
print(l)

"""
"""
num = int(input("enter number: "))
l = []

for _ in range(num):
    l.append(0)
print(l)
"""
"""
num = int(input("enter number: "))
l = [0 for _ in range(num)]
print(l)

"""
#task 38: Split a string into a list of words.
"""
st = "i am learning python"

newlist = st.split()
print(newlist)

"""
#task 39: Join a list of words into a single string with spaces in between.
"""
l = ["I", "am", "learning", "python"]
res = " ".join(l)

print(res)
""" 

#task 40: Write a program that takes a list of grades and prints the average.
"""
l = []
avg = 0
s = 0

for _ in range(5):
    grade = int(input("enter grades: "))
    l.append(grade)
    s+=grade
avg = s / len(l)

print(avg)

"""
#task 41: Write a program that asks the user for numbers until they enter "done," then stores all numbers in a list and prints them.
"""
l = []

while True:
    num = input("enter number: ")

    if num == "done":
        break
    else:
        l.append(int(num))
print(l)

""" 
