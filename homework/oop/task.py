#task 1: Define a Car class with attributes brand and model. Create two objects and print their attributes.
'''
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def __str__(self):
        return f"Brand: {self.brand}, model: {self.model}"
    
mycar = Car(brand="BMW", model="f90 competetion")

print(mycar.brand)
print(mycar.model)

print(mycar)

''' 
#task 2: Create a Person class with name and age attributes. Instantiate it and print formatted output using f-strings.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age}"

eshmat = Person("Styles", 22)
print(eshmat.name)
print(eshmat.age)

'''
#task 3: Define a Book class and create three different Book objects representing different titles.
'''
class Book:
    def __init__(self, title):
        self.title = title
        
    def __str__(self):
        return f"Book<title={self.title}>"

after = Book("colledge life romance")
harry_potter = Book("orphan boy who inhireted magic")
troya = Book(title="destroyed nation due to women")

print(after.title)
print(harry_potter.title)
print(troya.title)

print(after)

''' 
#task 4:  Create a Dog class with a method bark() that prints “Woof!”. Call it from an object.
'''
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def bark(self):
        print("Gaf Gaf Gaf.....")
    
    def __str__(self):
        return f"Dog< name: {self.name}, age: {self.age}"


d1 = Dog(
    name="reks",
    age= 7
)
d1.bark()

'''
#task 5: Define a Student class where __init__ prints “New student created.” when a new object is created.
'''
class Student:
    student_count = 0
    
    def __init__(self, name, age, st_id):
        self.name = name
        self.age = age
        self.st_id = st_id
        
        Student.student_count+=1
        print(f"New Student Created, count: {self.student_count}")
    

st1 = Student("Merlin", 18, "mg4545")
st2 = Student("Artur", 20, "kg4546")

''' 
#task 6: Add a method introduce() to Person that prints “Hi, I am .” and test it.
'''
class Person:
    def __init__(self, name):
        self.name = name
    
    def introduce(self):
        print(f"hello i am {self.name}")

p1 = Person("Tony Stark")
p1.introduce()

''' 
#task 7: Write a class Rectangle that calculates and prints its area and perimeter using instance methods.
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def calc_perimeter(self):
        return (self.width + self.height) * 2
    
    def area(self):
        return self.width * self.height
    

rec1 = Rectangle(width=7, height=8)

print(rec1.calc_perimeter())
print(rec1.area())

''' 
#task 8: Create a Circle class with a radius attribute and a method area() that returns the circle’s area.
'''
from math import pi
class Circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        res = self.radius**2 * pi
        return round(res, 2)

a = Circle(8)

print(a.area())

'''
#task 9: Define a Laptop class with instance variables brand, ram, and price. Create two laptops and print details.
'''
class Laptop:
    def __init__(self, brand, ram, price):
        self.brand = brand
        self.ram = ram
        self.price = price
        
    def system_design(self):
        print("this laptop is designing the system...")
    
    def __str__(self):
        return f"Laptop < brand: {self.brand}, ram: {self.ram}"

silver = Laptop("Hp", 16, 400)

asus_vivo = Laptop("Asus", 16, 750)

print(silver.brand, silver.ram, silver.price)
silver.system_design()

print(asus_vivo.brand, asus_vivo.ram, asus_vivo.price)
asus_vivo.system_design()

'''
#task 10: Create a Movie class where __init__ takes title, year, and genre. Add a method info() to return a formatted string.
'''
class Movie:
    def __init__(self, title, year, genre):
        self.title = title
        self.year =  year
        self.genre = genre
        
    def info(self,):
        print(f"this movie's title is {self.title}, released in {self.year}, genre is {self.genre}")
    
    def __str__(self):
        return f"this is about Movie"
    

film = Movie(
    "the Island",
    2005,
    "fantastic, meladramma"
)

film.info()

''' 
#task 11: Write a BankAccount class with methods deposit() and withdraw() modifying an instance variable balance.
'''
class BankAccount:
    total_balance = 0
    
    def __init__(self, card_number, card_holder, balance):
        self.card_number = card_number
        self.card_holder = card_holder
        self.balance = balance
        BankAccount.total_balance+=self.balance
        
    def deposit(self, amount: int):
        if amount < 0:
            raise ValueError("you can't deposit below zero")
        self.balance+=amount
        BankAccount.total_balance+=amount

    def withdraw(self, amount: int):
        if amount > self.balance:
            raise ValueError("insufficiant balance")
        self.balance-=amount
        BankAccount.total_balance-=amount

user1 = BankAccount(
    "9860180105605521",
    "Anasbek",
    0
)

user2 = BankAccount("123412341234", "teo", 100)

user1.deposit(85)
print(user1.balance)
user1.withdraw(30)
print(user1.balance)

print(BankAccount.total_balance)
'''

#task 12: Create a Player class that tracks name and score. Write a method add_score(points) to increase the score.
'''
class Player:
    
    def __init__(self, name, score):
        self.name = name
        self.score = score
        
    def add_score(self, point: int):
        self.score+=point

    def __str__(self):
        return f"Player: {self.name}, score: {self.score}"
    

user1 = Player("teo", 0)
user2 = Player("Scott", 0)

print("==================\n")
print("1. what is the class in python?")

game1 = input("Teo, enter answer: ")
game2 = input("Scott, enter answer: ")

if game1.lower() == "blueprint":
    user1.add_score(5)
    print(f"Teo's score is {user1.score}")
else:
    print(f"wrong answer {user1.score}")
    
if game2.lower() == "blueprint":
    user2.add_score(5)
    print(f"Scott's score is {user2.score}")
else:
    print(f"wrong answer {user2.score}")
    
print("==========================")

''' 
#task 13: Define a Point class representing x, y coordinates. Add a method distance_from_origin() returning Euclidean distance.
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def distance_from_origin(self):
        distance = (self.x**2 + self.y**2) ** 0.5
        return distance
    

coord = Point(3, 4)
print(coord.distance_from_origin())

''' 
#task 14: Implement __str__ in the Book class to return "<title> by <author>".
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    def __str__(self):
        return f"Book <{self.title}> by <{self.author}>"
    
b1 = Book("Introduction to DSA", "Percy Jackson")

print(b1)

'''
#task 15: Check if Triangle is Valid Make a static method that checks if 3 sides can make a triangle
'''
class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def is_triangle(self):
        sides = sorted([self.a, self.b, self.c])
        return sides[0] + sides[1] > sides[2]
    
figure = Triangle(3,4,5)
print(figure.is_triangle())

'''
#task 16: Calculate Dog Years Create a static method that converts human years to dog years (×7)
'''
class Dog:
    def __init__(self, name, human_year):
        self.name = name
        self.human_year = human_year
    
    def dog_year(self):
        return self.human_year * 7
    
    def __str__(self):
        return f"Converter human_year: <{self.human_year}> to Dog_year"
    

pet = Dog("bobik", 7)
print(pet.dog_year())

''' 
#task 17: Check Strong Password Make a static method that checks if password has at least 8 characters
'''
class Password:
    def __init__(self, name, pssword):
        self.name = name
        self.pssword = pssword
    
    @staticmethod
    def is_valid(pssword):
        if len(pssword) > 8:
            print("Password is good")
        else:
            print("Your password is weak!")

user = Password("teo", "te33")
Password.is_valid(user.pssword)

'''
#task 18: Define a Student class with a class variable school = "Greenwood High".
'''
class Student:
    school = "Greenwood High"
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def __str__(self):
        return f"school: {Student.school}, name: {self.name}, age: {self.age}, grade: {self.grade}"


user1 = Student("bill", 18, 4)
user2 = Student("rura", 19, 4)

print(user1)
print(user2)

'''
#task 19: Change Student.school to "Bluebell Academy" and show how all instances reflect the change.
'''
class Student:
    school = "Greenwood High"
    
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
    
    def __str__(self):
        return f"school: {Student.school}, name: {self.name}, age: {self.age}, grade: {self.grade}"


user1 = Student("bill", 18, 4)
user2 = Student("rura", 19, 4)

Student.school = "Bluebell Academy"

print(user1)
print(user2)

'''
#task 20: Add a class variable count to Car that keeps track of how many cars have been created.
'''
class Car:
    car_count = 0
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
        Car.car_count+=1
    

    

bwm = Car("m5f90", "dark-blue")
mers = Car("mers-s-63", "black")

print(Car.car_count)

'''
#task 21: Increment count in the constructor and print it after creating several objects.
'''
class One:
    count = 0
    
    def __init__(self, name):
        self.name = name
        One.count+=1
    
    def __str__(self):
        return f"{self.name}, {One.count}"

p = One("one")
p1 = One("two")

print(One.count)

'''
#task 22: Create Student from String Make a class method that creates a Student from "name,grade" string like "Anna,95"
'''
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    @classmethod
    def from_string(cls, value):
        name, grade = value.split(",")
        
        return cls(name, int(grade))
    
    def __str__(self):
        return f"{self.name}, {self.grade}"
    

new_student = Student.from_string("Anna, 95")
print(new_student)

'''
#task 23: Count How Many Pets Created Create a class method that tells how many Pet instances have been made
'''
class Pet:
    total_count = 0
    
    def __init__(self, name):
        self.name = name
        Pet.total_count+=1
        
        
    @classmethod
    def count(cls):
        return f"total count of pets are {cls.total_count}"
    

dog = Pet("bobik")
horse = Pet("maximus")

print(Pet.total_count)

'''
#task 24: Make Default Book Create a class method that makes a Book with title "Unknown" and author "Unknown"
'''
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        
    @classmethod
    def default_make(cls):
        return cls(title="Unknown", author="Unknown")
    
    def __str__(self):
        return f"{self.title}, {self.author}"
    
    
a = Book("ab", "abv")
print(a)
print(Book.default_make())

'''
#task 25: Create Circle from Diameter Make a class method that creates a Circle when you give it diameter instead of radius
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @classmethod
    def from_diameter(cls, diameter):
        radius = diameter / 2
        return cls(radius)
    

a = Circle.from_diameter(10)

print(a.radius)

''' 
#task 26: Create Birthday Person Make a class method that creates a Person with age 0 (newborn)
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    
    @classmethod
    def newborn(cls, name):
        return cls(name, 0)
    
p = Person("ALi", 29)
baby = Person.newborn("abi")

print(p.name, p.age)
print(baby.name, baby.age)

'''
#task 27: Make Random Color Create a class method that makes a Color with random RGB values
'''
import random

class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b
    
    @classmethod
    def rando_color(cls):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return cls(r, g, b)

    def __str__(self):
        return f"{self.r} {self.g} {self.b}"


a = Color.rando_color()
print(a)

'''
#task 28: Create Square from Area Make a class method that creates a Square when you know the area
'''
class Square:
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side ** 2
    
    @classmethod
    def from_area(cls, area):
        return cls(area**0.5)

a = Square.from_area(16)
print(a.side)
b = Square(4)
print(b.area())

'''
#task 29: Default Settings Create a class method that makes GameSettings with easy difficulty
'''
class Game:
    def __init__(self, name, mode):
        self.name = name
        self.mode = mode
    
    @classmethod
    def gamesettings(cls, name):
        return cls(name, "Easy")
    

gta = Game("vice_city", "hard")
gta5 = Game.gamesettings("gta6")

print(gta5.name, gta5.mode)
print(gta.name, gta.mode)

'''
#task 30: Create from List Make a class method that creates a Fruit from a list like ["apple", "red"]
'''
class Fruit:
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    @classmethod
    def from_list(cls, fruit_list: list):
        name = fruit_list[0]
        color = fruit_list[1]
        
        return cls(name, color)

    def __str__(self):
        return f"{self.name}, {self.color}"
    

a = Fruit("banana", "yellow")
b = Fruit.from_list(["apple", "red"])
print(a)
print(b)

'''
#task 31: Student from Dictionary Create a class method that makes a Student from {"name": "Tom", "grade": 88}
'''
class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
    
    @classmethod
    def from_dict(cls, data: dict):
        name = data.get("name")
        grade = data.get("grade")
        return cls(name, grade)
    
    def __str__(self):
        return f"{self.name}, {self.grade}"

p = Student.from_dict({"name": "Ron", "grade": 88})
print(p)

'''
#task 32: Check if Number is Even Make a static method that checks if a number is even
'''
class Number:
    
    @staticmethod
    def is_even(num: int):
        return num % 2 == 0
    

print(Number.is_even(9))

'''

from math import pi

#task 33: Calculate Circle Area Create a static method that calculates area when given radius
'''
class Circle:
    
    @staticmethod
    def area(radius):
        return round(pi * radius**2, 2)
    
a = Circle()
print(a.area(5))

'''
#task 34: Check Valid Email Make a static method that checks if email has "@" symbol
'''
class Email:
    
    @staticmethod
    def checker(email):
        if "@" in email:
            return email
        else:
            return"Invalid Email!!!"


print(Email.checker("user@gmail.com"))

'''
#task 35: Convert Celsius to Fahrenheit Create a static method for temperature conversion
'''
class Temprature:
    
    @staticmethod
    def from_celsius_to_fahrenheit(celsius):
        res =  (celsius * 9/5) + 32
        return res
    
print(Temprature.from_celsius_to_fahrenheit(36))

'''
#task 36: Check if Triangle is Valid Make a static method that checks if 3 sides can make a triangle
'''
class Triangle:
    
    @staticmethod
    def is_valid(a, b, c):
        a, b, c = sorted([a, b, c])
        return a + b > c
    

print(Triangle.is_valid(3, 4, 5))

'''
#task 37: Calculate Dog Years Create a static method that converts human years to dog years (×7)
'''
class Dog:
    
    @staticmethod
    def from_human_to_dog(num: int):
        return num * 7
    
print(Dog.from_human_to_dog(2))

'''
#task 38: Check Strong Password Make a static method that checks if password has at least 8 characters
'''
class Password:
    
    @staticmethod
    def checker(value):
        if len(value) > 8:
            return value
        return "Your password should have 8 characters!"

print(Password.checker("eshmat123"))

'''
#task 39: Calculate Pizza Slices Create a static method that calculates slices per person
'''
class Pizza:
    
    @staticmethod
    def calculater(pizza, person):
        res = pizza / person
        return f"{res} slice for per person"


print(Pizza.calculater(12, 3))

'''
#task 40: Check Palindrome Make a static method that checks if a word reads same forwards and backwards
'''
class Palidrome:
    
    @staticmethod
    def checker(value):
        if value == value[::-1]:
            return "Palidrome"
        return "Not Palidrome"

print(Palidrome.checker("wkiyik"))

'''
#task 41: Calculate Discount Create a static method that calculates final price after discount
'''
class Discount:
    
    @staticmethod
    def calculate(price):
        discount_sum = price * 0.1
        final_sum = price - discount_sum
        return final_sum    
    
print(Discount.calculate(100))

'''
#task 42: Create a TempFile class whose __del__ prints “File deleted” when object is garbage collected.
'''
class TempFile:
    def __init__(self, name):
        self.name = name
    
    def __del__(self):
        print("File deleted succesfully")
    
    def __str__(self):
        return f"TempFile<><{self.name}"


data = TempFile("BankLogHistory")
print(data)

'''
#task 43: Create an object, delete it with del, and observe the destructor message.
'''
class Secret:
    def __init__(self, name):
        self.name = name
    
    
    def __del__(self):
        print("LogDeleted")
    
data = Secret("BankLog")

print(data.name)
del data
print(data.name)

'''
#task 44: Add a delete_account() method to BankAccount that deletes the balance attribute using del self.balance.
'''
class BankAccount:
    def __init__(self, user_id, name, balance):
        self.name = name
        self.user_id = user_id
        self.balance = balance
    
    def delete_account(self):
        del self.balance
    
    def __str__(self):
        return f"Account: {self.name}, balance: {self.balance}"
    
user = BankAccount("smp250", "tom", 1450)

user.delete_account()
print(user.balance)

'''
#task 45: Use vars() to print all attributes of a Car object as a dictionary.
'''
class BankAccount:
    def __init__(self, user_id, name, balance):
        self.name = name
        self.user_id = user_id
        self.balance = balance
    
    def delete_account(self):
        del self.balance
    
    def __str__(self):
        return f"Account: {self.name}, balance: {self.balance}"
    
user = BankAccount("smp250", "tom", 1450)
print(vars(user))

'''
#task 46: Use hasattr() to check if a Person object has the attribute age.
'''
class BankAccount:
    def __init__(self, user_id, name, balance):
        self.name = name
        self.user_id = user_id
        self.balance = balance
    
    def delete_account(self):
        del self.balance
    
    def __str__(self):
        return f"Account: {self.name}, balance: {self.balance}"
    
user = BankAccount("smp250", "tom", 1450)
print(hasattr(user, "balance"))

'''
#task 47: Use getattr() to safely retrieve height from a Person object with default "Unknown".
'''
class Person:
    def __init__(self, name):
        self.name = name
        

user = Person("tom")

print(getattr(user, "age", "unknown"))

'''
#task 48: Use setattr() to dynamically add a new attribute nationality = "Uzbek" to a Person instance.
'''
class Person:
    def __init__(self, name):
        self.name = name
        

user = Person("tom")
setattr(user, "natinality", "uzbek")

print(user.natinality)
print(vars(user))

'''
#task 49: Use delattr() to remove an attribute from an existing object and verify using hasattr().
'''
class Person:
    def __init__(self, name, age, skill):
        self.name = name
        self.age = age
        self.skill = skill
    

user = Person("tom", 18, "hacking")
print(hasattr(user, "age"))

delattr(user, "age")
print(hasattr(user, "age"))

'''
#task 50: Combine everything: write a Vehicle class with class variable vehicle_count, instance variables make and year, 
# a static method is_motorized(), a class method from_string(), and a custom __str__—demonstrate all functionality.
'''
class Vehicle:
    vehicle_count = 0
    
    def __init__(self, make, year):
        self.make = make
        self.year = year
        Vehicle.vehicle_count+=1
    
    @classmethod
    def from_string(cls, data):
        make, year = data.split(",")
        return cls(make, year)
    
    @staticmethod
    def is_motorized():
        return True
    
    def __str__(self):
        return f"Vehicle: {self.make}, year: {self.year}"
    
v1 = Vehicle("BMW", 2020)
v2 = Vehicle.from_string("AUDI, 2002")

print("Motorized: ", Vehicle.is_motorized())
print("Total vehicles: ", Vehicle.vehicle_count)
print(v1, v2)

'''
