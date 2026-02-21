#=========THIS IS HOMETASK FOR SET FROM OFFLINE LESSON===============

#task 1: Create a set of your favorite colors.
"""
myset = {"blue", "green", "gold", "black"}
print(myset)
""" 
#task 2: Create a set from the following list, observing how duplicates are removed: [1, 2, 3, 4, 2, 3].
"""
myset = {1, 2, 3, 4, 3}
print(myset)

""" 
#task 3: Create an empty set.
"""
empty = set()
print(type(empty), empty)

""" 
#task 4: Add a new color to your set of favorite colors.
"""
myset = {"blue", "green", "gold", "black"}
myset.add("red")
print(myset)

""" 
#task 5: Remove a specific color from your set.
"""
myset = {"blue", "green", "gold", "black"}
myset.remove("black")
print(myset)

""" 
#task 6: Remove a random item from a set using .pop().
"""
myset = {"blue", "green", "gold", "black"}
myset.pop()
print(myset)
""" 
#task 7: Check if "red" is in your set of favorite colors.
"""
myset = {"blue", "green", "gold", "black"}
print("red" in myset)

""" 
#task 8: Iterate through a set and print each item.
"""
myset = {"blue", "green", "gold", "black"}
for i in myset:
    print(i)
""" 
#task 9: Given two sets, set1 = {1, 2, 3} and set2 = {3, 4, 5}, find their union.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.union(set2)

print(set3)

""" 
#task 10: Find the intersection of set1 and set2.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.intersection(set2)
print(set3)

""" 
#task 11: Find the difference of set1 and set2 (set1 - set2).
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.difference(set2)
print(set3)

""" 
#task 12: Find the symmetric difference of set1 and set2.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1.symmetric_difference(set2)
print(set3)

""" 
#task 13: Check if set1 is a subset of a larger set.
"""
set1 = {1, 2, 3}
set2 = {3, 4, 5}

set3 = set1 | set2

print(set1.issubset(set3))

""" 
#task 14: Check if a set of all vowels ({'a', 'e', 'i', 'o', 'u'}) is a subset of a string converted to a set.
"""
vovel = {'a', 'e', 'i', 'o', 'u'}
st = "education"

stset = set(st)

print(vovel.issubset(stset))
""" 
#task 15: Check if one set is a superset of another.
"""
vovel = {'a', 'e', 'i', 'o', 'u'}
st = "education"

stset = set(st)

print(stset.issuperset(vovel))

""" 
#task 16: Find all the unique words in a given string sentence.
"""
st = "people should not fear from future or upsets from past live moment"

words = st.split()

unique_words = set(words)

print(unique_words)

""" 

#task 17: Given a list of numbers with duplicates, use a set to find the number of unique items.
"""
num = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8]

res = set(num)
print(len(res))
""" 
#task 18: Find all the common characters between two strings using sets.
"""
word1 = "python is interpretted language"
word2 = "python has byte-code somehow own compiler"

res1 = set(word1)
res2 = set(word2)

res3 = res1.intersection(res2)

print(res3)

""" 
#task 19: Given two lists of student IDs, find the students who are in both classes using sets.
"""
klas = ["reo123", "teo345", "lisa79", "anna1717"]
klas1 = ["natawa12", "teo345", "anna111", "reo123"]

sklas = set(klas)
sklas1 = set(klas1)

res = sklas.intersection(sklas1)
print(res)

""" 
#task 20: Use a for loop to iterate through a list of numbers and add all the unique numbers to a set.
"""
num = [1,1,2,3,3,4,5,5,6,6,7,7,6,6,8,8,9,9,10]

res = set()

for i in num:
    res.add(i)
print(res)

""" 
#task 21: Find the number of unique vowels in a given string.
"""
words = "the worst thing is that you know what is the consequences but u can't take action"
vovel = "aeoiu"

res = set()

for ch in words:
    if ch in vovel:
        res.add(ch)
print(len(res))

""" 
#task 22: Given a list of student names, find all names that appear more than once.
"""
names = ["ali", "teo", "teo", "ali", "reo", "eshmat", "lisa", "lisa", "anna", "anna", "scott", "lydia"]

duplicate = set()

for item in names:
    if names.count(item) > 1:
        duplicate.add(item)
print(f"names that appears more than one are: {duplicate}")

""" 
#task 23: Create a function that takes a list of integers and returns a set of all even numbers.
"""
def func(l: list)-> set:
    res = set()
    for i in l:
        if i % 2 == 0:
            res.add(i)
    return res

print(func(l = [1,2,3,4,5,6,7,8,9,10]))

""" 
#task 24: Given a list of emails, find and print the number of unique domains (e.g., gmail.com, yahoo.com).
"""
email = ["eshmat@gmail.com", "reo@yahoo.com", "toshmat@gmail.com", "gishmat@yahoo.com", "scott@gmail.com", "lisa@yahoo.com"]
res = set()

for i in email:
    domain = i.split("@")[1]
    res.add(domain)

print(res)
print(len(res))

""" 
#task 25: Use a set to count the number of unique words in a text file.
"""
word = "one way is to study word lists. I very much associate this method one way study word lists very associate method"

res = set()

for w in word.lower().split():
    res.add(w.strip(",."))
print(res, len(res))

""" 
#task 26: Given a list of numbers, use a set to find which numbers are missing from the range 1-10.
"""
nums = [2,4,6,8,10]

full = set(range(1, 11))

present = set(nums)

missing = full - present

print(missing)

""" 
#task 27: Create a set of favorite genres. Ask the user for their favorite genre and add it to the set if it's not already there.
"""
genre = {"horror", "love", "comedy"}

user = input("enter your favorite genre: ")

if user not in genre:
    genre.add(user)
print(genre)

""" 
#task 28: Given a list of numbers, find the sum of all the unique numbers.

nums = [1,1,2,2,3,4,4,5,3,6,6,5,7,7,8,9,10]

res = set()
"""
for i in nums:
    res.add(i)
print(sum(res))

""" 
"""
s = 0
for i in nums:
    res.add(i)

for j in res:
    s+=j
print(s)
""" 
#task 29: Use a set to remove all duplicate characters from a string.
"""
word = "you should know how to do where to do when to do what to do listen"
res = set()
result = []

for ch in word:
    if ch not in res:
        res.add(ch)
        result.append(ch)

print("-".join(result))

""" 
#task 30: Given two lists, find all items that are unique to the first list or the second, but not in both.
"""
l1 = ["reo", "teo", 1, 2]
l2 = ["reo", 3, 4, 1, 5, "rura"]

res1 = set(l1 )
res2 = set(l2)
res3 = res1.symmetric_difference(res2)

res = list(res3)
print(res)

""" 
#task 31: Create a frozenset and demonstrate that you cannot add or remove items from it.
"""
num = frozenset({1,2, "teo", 3})
num.add1(2)
print(num)

""" 
#task 32: Explain why a list cannot be an item in a set.
"""
myset = {[1,"teo"], (1,), {1,2}} # value inside set must be immutable , list can't be value coz we can change list 
print(myset)

""" 
#task 33: Given a dictionary, create a set of all the keys.
"""
mydict = {1: "apple", 2: "orange", 3: "banana"}

key_set = set(mydict.keys())
print(key_set)

""" 
#task 34: Given a dictionary, create a set of all the values.
"""
mydict = {1: "apple", 2: "orange", 3: "banana"}
values_set = set(mydict.values())
print(values_set)

""" 
#task 35: Create a set of numbers. Use a for loop to print each number along with whether it is even or odd.
"""
nums = {1,2,3,4,5,6,7,8,9,10}

for i in nums:
    if i % 2 == 0:
        print(f"{i}: is even")
    else:
        print(f"{i}: is odd")
""" 
#task 36: Given two sentences, find all the words that are in the first sentence but not in the second.
"""
sent1 = "i started learning python"
sent2 = "before that i was learning C"

res1 = set(sent1.split())
res2 = set(sent2.split())

res = res1.difference(res2)
print(res)

""" 
#task 37: Write a program that takes two comma-separated lists of numbers from the user and prints their intersection.
"""
user1 = input("enter numbers: ")
user2 = input("enter numbers: ")

list1 = user1.split(",")
list2 = user2.split(",")

set1 = {int(i) for i in list1}
set2 = {int(j) for j in list2}

res = set1.intersection(set2)

print(res)

""" 
#task 38: Create a set of banned usernames. Ask a user for a username and check if it's in the banned set.
"""
banned_users = {"teo", "reo", "scott"}

user = input("enter name: ")

if user in banned_users:
    print("Sorry you can't access coz you were banned!")
else:
    print("welcome you have access")
""" 
#task 39: Given a list of numbers, use a set to efficiently check for the presence of a specific number.
"""
nums = [1,2,3,4,5,6,7,8,9,10]

check = set(nums)

print(1 in check)

""" 
#task 40: Use a set and a loop to find the first non-repeated character in a string.

word = "usually people do not understand me why i dont know"

seen = set()
repeated = set()

for ch in word:
    if ch not in seen:
        seen.add(ch)
    else:
        repeated.add(ch)

for ch in word:
    if ch not in repeated:
        print(ch)
        break