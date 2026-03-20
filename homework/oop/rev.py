#task 1: Create a Car class with brand and year attributes. Print them.
'''
class Car:
    cnt = 0
    
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        Car.cnt+=1
    
    def __str__(self):
        return f"Car <{self.brand}><{self.year}>"
    
    def __del__(self):
        Car.cnt-=1

malibu = Car("Chevrolet", 2012)
print(Car.cnt)

cobalt = Car("chevrolet", 2016)

del cobalt

print(Car.cnt)

''' 
#task 2: Add a method info() that returns formatted car info.
'''
class Car:
    def __init__(self, brand, year, horse_power):
        self.brand = brand
        self.year = year
        self.horse_power = horse_power
    
    def info(self):
        return f"brand: {self.brand}, year: {self.year}, hp: {self.horse_power}"
    

aventador = Car("lambargini", 2015, 900)
print(aventador.info())

''' 
#task 3: Create a Book class and add a method is_long() that returns True if pages > 300.
'''
class Book:
    def __init__(self, name, author, page, year):
        self.name = name
        self.author = author
        self.page = page
        self.year = year
    
    def is_long(self):
        if self.page > 300:
            return True
        return False

b1 = Book("DSA", "robert kim", 301, 2002)
b2 = Book("otkan kunlar", "abdulla hoshimov", 250, 1995)

print(b1.is_long())
print(b2.is_long())

''' 
#task 4: Create a Rectangle class with width and height and method area().
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def __str__(self):
        return f"Rectangle <{self.width}><{self.height}>"
    

p1 =  Rectangle(7, 5)
print(p1.area())

''' 
#task 5: Add a method perimeter() to Rectangle.
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return (self.width + self.height) * 2
    

p2 = Rectangle(7, 8)
print(p2.perimeter())
'''
#task 6: Create a Student class with name and grade. Add passed() method (>= 60).
'''
class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def passed(self):
        if self.grade >= 60:
            return True
    
    def __str__(self):
        return f"Student: <{self.name}><{self.grade}>"
    

st1 = Student("haydar", 90)
st2 = Student("teo", 55)

st1.passed()
st2.passed()

'''
#task 7: Create a Dog class with name and age. Add method to convert age to dog years.
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def dog_year(self):
        return self.age * 7
    

d = Dog("bobik", 2)
print(d.dog_year())

'''
#task 8: Create a Circle class and implement area().
#task 9: Add method diameter() to Circle.
'''
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        res = pi * self.radius** 2
        return round(res, 2)
    
    def diameter(self):
        return self.radius * 2
    
    
a = Circle(5)
print(a.area())
print(a.diameter())

''' 
#task 10: Print __dict__ of an object and explain what you see.
'''
class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    def passed(self):
        if self.grade >= 60:
            return True
    
    def __str__(self):
        return f"Student: <{self.name}><{self.grade}>"
    
st1 = Student("rura", 56)
print(st1.__dict__)

''' 
#task 11: Create a User class that counts total users created.
'''
class User:
    total_user = 0
    
    def __init__(self, name, user_id):
        self.anme = name
        self.user_id = user_id
        User.total_user+=1
        
    
a = User("rura", "r234")
b = User("haydar", "rs4545")
c = User("buzu", "x5x7")

print(User.total_user)

'''
#task 12: Create a Product class with class variable tax_rate.
'''
class Product:
    tax_rate = 0.1
    
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    
    def calculate_tax(self):
        return self.price * self.tax_rate
    

p = Product("milk", 1.2)
print(p.calculate_tax())

''' 
#task 13: Change class variable from outside the class.
'''
class Student:
    university = "MIT"
    
    def __init__(self, name, age, iq):
        self.name = name
        self.age = age
        self.iq = iq
    
    def info(self):
        return self.university, self.name, self.age, self.iq
    
    
st1 = Student("walter", 33, 197)
st2 = Student('tobias', 30, 160)

st2.university = "harvard"
print(st2.info())
print(st1.info())

Student.university = "priston"

st3 = Student("cabe", 56, 120)

print(st3.info())
print(Student.university)

''' 
#task 15: Create a Company class with class variable company_name.
'''
class Company:
    company_name = "Alpha_labs"
    
    def __init__(self, name, gender, age, skill):
        self.name = name
        self.gender = gender
        self.age = age
        self.skill = skill
        
    def info(self):
        return self.company_name, self.name, self.gender, self.age, self.skill
    
user = Company("haydar", "male", 22, "python_dev")
print(user.info()) 

'''
#task 16: Create 3 objects and show they share class variable.
'''
class Company:
    company_name = "Alpha_labs"
    
    def __init__(self, name, gender, age, skill):
        self.name = name
        self.gender = gender
        self.age = age
        self.skill = skill
        
    def info(self):
        return self.company_name, self.name, self.gender, self.age, self.skill
    
user = Company("haydar", "male", 22, "python_dev")
user1 = Company("walter", "male", 30, "programmist")
user2 = Company("page", "female0", 26, "soft-skills")

print(user.info(),"\n",user1.info(),"\n",user2.info())

''' 
#task 17: Create a class with mutable class variable (list). Observe behavior.
'''
class Project:
    generic_tech = ["python", "c", "c++"]
    
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
    
    def info(self):
        return self.generic_tech, self.name
    
Project.generic_tech.append("go")

p1 = Project("titan", "to imrpove life")
print(p1.info())

p2 = Project("axl", "war-dog")
p2.generic_tech[2] = "automation"
print(p2.info())

p3 = Project("ubicom", "make-stronger")

''' 
#task 18: Fix the mutable class variable problem properly.
'''
class Project:
    generic_tech = "python"
    
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
    
    def info(self):
        return self.generic_tech, self.name

Project.generic_tech = "c/c++"

p = Project("iron-man", "good goal")
print(p.info())

'''
#task 19: Implement __str__ in a Person class.
'''
class Person:
    def __init__(self, name, age, skill):
        self.name = name
        self.age = age
        self.skill = skill
    
    def __str__(self):
        return f"{self.name}, {self.age}, {self.skill}"
    

p = Person("haydar", 22, "python-dev")
print(p)

''' 
#task 20: Implement __repr__ properly.
'''
class Person:
    def __init__(self, name, age, skill):
        self.name = name
        self.age = age
        self.skill = skill
    
    def __repr__(self):
        return f"{self.name}, {self.age}, {self.skill}"
    
p = Person("girgit", 25, "rust")
print(p)

''' 
#task 21: Show difference between __str__ and __repr__.

#task 22: Implement __len__ for a custom class.
'''
class Playlist:
    def __init__(self, song):
        self.song = song
    
    def __len__(self):
        return len(self.song)

music = Playlist(["attention", "cigarettes after s", "catch if you can"])
print(len(music))

'''
#task 23: Implement __eq__ to compare two objects.
'''
class Book:
    def __init__(self, title):
        self.title = title
    
    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return self.title == other.title

HarryPotter = Book("philosopher's stone")
Hamsa = Book("Insonni bilish uchun")
rumsa = Book("Insonni bilish uchun")

a = 6

print(Hamsa == rumsa)

''' 
#task 24: Implement __lt__ to compare two objects by value.
"""
class Book:
    
    def __init__(self, title, page):
        self.title = title
        self.page = page
    
    def __lt__(self, other):
        return self.page < other.page
    

p1 = Book("hamsa", 500)
p2 = Book("how linux works", 450)

print(p2 < p1)

""" 
#task 25: Implement __add__ in a Vector class.  
'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __add__(self, other):
        if not isinstance(other, Vector):
            return NotImplemented
        return Vector(self.x + other.x, self.y + other.y)
    
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

p1 = Vector(4, 5)
p2 = Vector(7, 9)

print(p1 + p2)
'''
#task 26: Override __contains__ in a custom container class.
'''
class Konteyner:
    def __init__(self, name):
        self.name = name
        
    def __contains__(self, item):
        return item in self.name
    

p = Konteyner(["haydar", "ali", "teo", "lydia", "scott", "derek"])

print("haydar" in p)

'''
#task 27: Print object inside list and observe which method runs.
'''
class Konteyner:
    def __init__(self, name):
        self.name = name
        

    def __repr__(self):
        return f"Konteyner{self.name}"
    

p = Konteyner(["haydar", "ali", "teo", "lydia", "scott", "derek"])

print([p])

'''
#task 28: Create a class where print(obj) gives clean readable output.
'''
class Animal:
    def __init__(self, name, type, gender):
        self.name = name
        self.type = type
        self.gender = gender
    
    def __str__(self):
        return f"name: {self.name}, type: {self.type}, gender: {self.gender}"
    

obj = Animal("lion", "mammal", "male")
print(obj)

''' 
#task 29: Create a class with class variable counter and classmethod to show it.
'''
class Book:
    counter = 0
    
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate
        Book.counter+=1
        
    @classmethod
    def show(cls):
        return cls.counter
    

b1 = Book("harry potter", 8)
b2 = Book("rings", 8)
b3 = Book("brainstorm", 10)

print(Book.show())

'''
#task 30: Create a User class with from_string() classmethod.
'''
class User:
    def __init__ (self, username, email, age):
        self.username = username
        self.email = email
        self.age = age
    
    @classmethod
    def from_string(cls, user_string):
        username, email, age = user_string.split(",")
        return cls(username, email, int(age))
    
    def __str__(self):
        return f"Username: {self.username}, email: {self.email}, age: {self.age}"

u = User("haydar", "haydar@gamil.com", 22)
u1 = User.from_string("tony,tony@gamil.com,22")

print(u1)

'''
