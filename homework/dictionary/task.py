#==========THESE TASKS ARE RELATED TO DICT=====================

#task 1: Create a dictionary person with keys 'name', 'age', and 'city'.
"""
person = {
    "name": "Jordan",
    "age": 22,
    "city": "Washington"
}
print(person)

""" 
#task 2: Access and print the value associated with the key 'name'.
"""
person = {
    "name": "Jordan",
    "age": 22,
    "city": "Washington"
}
print(person.get("name"))

""" 
#task 3: Add a new key-value pair, 'occupation', to the person dictionary.
"""
person = {
    "name": "Jordan",
    "age": 22,
    "city": "Washington"
}

person["occupation"] = "Backend Dev"
print(person)
""" 
#task 4: Change the value of the 'age' key to a new number.
"""
person = {
    "name": "Jordan",
    "age": 22,
    "city": "Washington"
}
print(person)
person["age"] = 23
print(person)
""" 
#task 5: Remove the 'city' key-value pair from the dictionary.
"""
person = {
    "name": "Jordan",
    "age": 22,
    "city": "Washington"
}

deleted = person.pop("city")
print(person)
print(deleted)

""" 
#task 6: Check if the key 'name' exists in the dictionary.
"""
person = {
    "name": "Jordan",
    "age": 22,
    "city": "Washington"
}

print("name" in person)
""" 
#task 7: Get a list of all keys from the dictionary.
"""
person = {
    "name": "Jordan",
    "age": 22,
    "city": "Washington"
}

print(person.keys())

""" 
#task 8: Get a list of all values from the dictionary.
"""
person = {
    "name": "Jordan",
    "age": 22,
    "city": "Washington"
}

print(person.values())
""" 
#task 9: Get a list of all key-value pairs (items) from the dictionary.
"""
person = {
    "name": "Jordan",
    "age": 22,
    "city": "Washington"
}
print(person.items())
""" 
#task 10: Create an empty dictionary and add three key-value pairs to it.
"""
empty = {}

data = [("name", "rura"), ("age", 22), ("city", "termez")]

for key, val in data:
    empty[key] = val
print(empty.keys())
print(empty.values())

""" 
#task 11: Iterate through the dictionary and print each key.
"""
person = {
    "name": "rura",
    "age": 22,
    "job": "backend dev",
    "city": "baconhills"
}

for key in person.keys():
    print(key)
""" 

#task 12: Iterate through the dictionary and print each value.
"""
person = {
    "name": "rura",
    "age": 22,
    "job": "backend dev",
    "city": "baconhills"
}

for val in person.values():
    print(val)
""" 
#task 13: Iterate through the dictionary and print each key and its corresponding value.
"""
person = {
    "name": "rura",
    "age": 22,
    "job": "backend dev",
    "city": "baconhills"
}

for key, val in person.items():
    print(key, ":", val)

"""
#task 14: Use a dictionary comprehension to create a dictionary with numbers as keys (1 to 5) and their squares as values.
"""
num = {i: i**2 for i in range(1,5)}
print(num)

""" 
#task 15: Use a dictionary comprehension to create a dictionary from a list of words, where the keys are the words and the values are the lengths of the words.
"""
l = ["apple", "banana", "orange", "kiwi", "watermelon"]

fruit = {word: len(word) for word in l}

print(fruit)

""" 
#task 16: Create a dictionary from two lists, one for keys and one for values.
"""
names = ["ildar", "samandar", "aziz", "javohir"]
age = [21, 22, 20, 19]

people = {k: v for k, v in zip(names, age)}

print(people)
""" 
"""
names = ["ildar", "samandar", "aziz", "javohir"]
age = [21, 22, 20, 19]
people ={}

for key, val in zip(names, age):
    people[key]= val
print(people)

""" 
#task 17: Merge two dictionaries into one.
"""
person = {
    "name": "rura",
    "age": 18,
    "gender": "female"
}

p1 = {
    "city": "marsland",
    "skill": "coding",
    "hobby": "horse-riding"
}

person.update(p1)
print(person.items())
""" 
#task 18: Create a dictionary students where each key is a student's name and the value is another dictionary containing their 'math' and 'science' scores.
"""
students = {
    "scott": {
        "math-score": 60,
        "science": 61
    },
    "styles": {
        "math-score": 88,
        "science": 77,
    },
    "allison": {
        "math-score": 90,
        "science": 91
    }
}

print(students["scott"]["math-score"])
""" 
#task 19: Access and print the science score of a specific student.
"""
students = {
    "scott": {
        "math-score": 60,
        "science": 61
    },
    "styles": {
        "math-score": 88,
        "science": 77,
    },
    "allison": {
        "math-score": 90,
        "science": 91
    }
}

print(students.get("allison").get("science"))
""" 

#task 20: Add a new subject, 'history', and its score for one of the students.
"""
students = {
    "scott": {
        "math-score": 60,
        "science": 61
    },
    "styles": {
        "math-score": 88,
        "science": 77,
    },
    "allison": {
        "math-score": 90,
        "science": 91
    }
}

students["allison"]["history"] = 88
print(students)

""" 
#task 21: Iterate through the students dictionary and print each student's name and their average score.
"""
students = {
    "scott": {
        "math-score": 60,
        "science": 61
    },
    "styles": {
        "math-score": 88,
        "science": 77,
    },
    "allison": {
        "math-score": 90,
        "science": 91
    }
}

for student , scores in students.items():
    print(f"Student: {student}")
    for subject, score in scores.items():
        print(f"{subject}: {score}")
    
    print()
""" 
#task 22: Get the number of key-value pairs in the dictionary.
"""
students = {
    "scott": {
        "math-score": 60,
        "science": 61
    },
    "styles": {
        "math-score": 88,
        "science": 77,
    },
    "allison": {
        "math-score": 90,
        "science": 91
    }
}

for key, val in students.items():
    print(f"{key} has {len(val)} key-value pairs")
""" 
#task 23: Create a copy of a dictionary.
"""
car = {
    "brand": "BMW",
    "model": "m5f90",
    "year": 2022,
    "color": "dark-blue"
}

car1 = car.copy()
print(car1)

""" 
#task 24: Use the get() method to access a key, providing a default value if the key doesn't exist.
"""
car = {
    "brand": "BMW",
    "model": "m5f90",
    "year": 2022,
    "color": "dark-blue"
}

print(car.get("owner", "owner yoq"))

""" 
#task 25: Use the setdefault() method to add a new key only if it doesn't already exist.
"""
car = {
    "brand": "BMW",
    "model": "m5f90",
    "year": 2022,
    "color": "dark-blue"
}

car.setdefault("speed")
print(car)
""" 
#task 26: Count the frequency of characters in a string and store them in a dictionary.
"""
word = "if will is weak what will happen ?"

freq = {}

for ch in word:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch] = 1
print(freq)

""" 
#task 27: Count the frequency of words in a sentence and store them in a dictionary.
"""
words = "willpower is willpower is to get get you you are is me"

freq = {}

for word in words.split():
    if word in freq:
        freq[word]+=1
    else:
        freq[word] = 1

print(freq)

""" 
#task 28: Invert a dictionary, so that the values become keys and the keys become values (handle duplicate values by storing them in a list).
"""
car = {
    "brand": "BMW",
    "model": "m5f90",
    "year": 2022,
    "color": "dark-blue"
}

inverted = {}

for k, v in car.items():
    inverted.setdefault(v, [].append(k))
print(inverted)

""" 
#task 29: Sort a dictionary by its keys and print the sorted dictionary.
"""
car = {
    "brand": "BMW",
    "model": "m5f90",
    "year": 2022,
    "color": "dark-blue"
}

for key, val in sorted(car):
    print(key)
""" 

#task 30: Sort a dictionary by its values and print the sorted dictionary.
"""
data = {
    "rura": "good",
    "life": "testable",
    "health": "must-have fit",
    "advantage": "as possible should do"
}

sorted_data = dict(sorted(data.items(), key=lambda x: x[1]))  

print(sorted_data)

""" 
#task 31: Write a function that takes a dictionary and returns True if all values are unique, otherwise returns False.
"""
def myfunc(d: dict)->bool:
    freq = {}
    for val in d.values():
        if val in freq:
            return False
        else:
            freq[val]=1
    return True

person = {
        "teo": 23,
        "reo": 22,
        "car": "m5f90",
    }
res = myfunc(person)

print(res)

""" 
#task 32: Find the key with the maximum value in a dictionary.
"""
car = {
    "brand": "BMW",
    "model": "m5f90",
    "year": '2022',
    "colour": "dark-blue"
}

max_key = max(car.items(), key=lambda x: len(x[1]))
print(max_key)

""" 
#task 33: Find the key with the minimum value in a dictionary.
"""
car = {
    "brand": "BMW",
    "model": "m5f90",
    "year": '2022',
    "colour": "dark-blue"
}
min_key = min(car.items(), key=lambda k: k[1])
print(min_key)

""" 
#task 34: Remove all key-value pairs where the value is an empty string.
"""
person = {"name": "rura", "year": 2002, "job": None, "skill": None, "language": "English"}

cleaned = {k: v for k, v in person.items() if v not in (None, "")}

print(cleaned)

""" 
#task 35: Create a dictionary where keys are numbers from 1 to 10 and values are 'even' or 'odd'.
"""
num = {n: "even" if n % 2 == 0 else "odd" for n in range(1, 11)}
print(num)
""" 
#task 36:   Given a list of dictionaries, find the dictionary with the highest value for a specific key.
"""
player = {
    "Ronaldo": 85,
    "messi": 80,
    "neymar": 70,
}

max_player = max(player, key=lambda x: x[1])
print(max_player)

""" 
#task 37: Use pop() to remove a specific key and return its value.
"""
player = {
    "Ronaldo": 85,
    "messi": 80,
    "neymar": 70,
}

deleted = player.pop("messi")
print(deleted, player)

""" 
#task 38: Zip two lists, one for keys and one for values, to create a dictionary.
"""
city = ["London", "tokyo", "berlin", "NewYork"]
state = ["albion", "futuristic", "greenary", "cyber-punk"]

cities = dict(zip(city, state))

print(cities)

""" 
#task 39: Write a function that takes a dictionary and a list of keys to remove. Remove the specified keys from the dictionary.
"""
def remover(d: dict, key_remove: list)-> dict:
    for key in key_remove:
        if key in d:
            d.pop(key)
    return d

d = {"name": "scott", "age": 17, "skill": "werewolf", "ctiy": "baconhills"}
res = remover(d, ["age", "skill"])

print(res)

""" 
#task 40: Check if two dictionaries are equal.

data = {
    "name": "rura",
    "age": 18,
    "gender": "female",
    "height": 160,
    "weight": 45
}

person = {"name": "rura", "age": 18, "gender": "female", "height": 160, "weight": 55}

print(data==person)