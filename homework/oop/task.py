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

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    @