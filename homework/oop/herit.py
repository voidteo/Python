#=============EXERCISES FROM INHERITENCE =======================#

#task 1: Create a base class Animal with method speak(). Derive Dog and Cat classes that print different sounds.
'''
class Animal:
    
    def speak(self):
        print("Animal sound")
        

class Dog(Animal):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("GAf Gaf.....")

class Cat(Animal):
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Kiss Kiss")
    

p1 = Dog("bobik")
p2 = Cat("kiska")

p1.speak()
p2.speak() 

'''
#task 2: Define a Vehicle base class with method move(). Inherit Car and Boat, each implementing their own move() message.
'''
class Vehicle:
    
    def move(self):
        print("toot toot puup")
    

class Car(Vehicle):
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print("Driving.....")
    
class Boat(Vehicle):
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print("sailing.....")
    
toyota = Car("Land Crusier")
ferry = Boat("titanic")

toyota.move()
ferry.move()

''' 
#task 3: Create Person as a base class and Employee as a subclass with an additional attribute salary.
'''
class Person:
    def __init__(self, name, position):
        self.name = name
        self.position = position
    
    
class Employee(Person):
    def __init__(self, name, position, salary):
        self.salary = salary
        super().__init__(name, position)
    
    def __str__(self):
        return f"Employee: {self.name}, position: {self.position}, salary: {self.salary}"


worker = Employee("Haydar", "BackendDev", 2000)
print(worker)

'''
#task 4: Define a parent class Shape with method area(). Inherit Rectangle and Circle, both implementing their versions of area().
'''
from math import pi

class Shape:
    def area(self):
        print("place to calculate area")
    

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return round(pi * self.radius**2, 2)
    

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        
    def area(self):
        return self.width * self.height
    

r1 = Rectangle(4, 7)
c1 = Circle(5)

shapes = [r1, c1]

for i in shapes:
    print(i.area())
    
''' 
#task 5: Write class Child(Parent) syntax to show inheritance hierarchy between Parent, Child, and GrandChild. Print all class names using __class__.__name__.
'''
class GrandParent:
    def __init__(self, name):
        self.name = name


class Parent(GrandParent):
    pass

class Child(Parent):
    pass

class GrandCHild(Child):
    pass

p = Parent("Shis")
c = Child("abu")
gr = GrandCHild("manzara")

print(p.__class__.__name__)
print(c.__class__.__name__)
print(gr.__class__.__name__)

'''
#task 6: Demonstrate that a subclass can access attributes and methods of its parent class without redefining them.
'''
class Animal:
    def __init__(self, name, kind, age):
        self.name = name
        self.kind = kind
        self.age = age
    
    def breath(self):
        return f"{self.name} can breath"
    
    def walk(self):
        return f"{self.kind} can walk"
    

class Dog(Animal):
    def __init__(self, name, kind, age, benefit):
        self.benefit = benefit
        super().__init__(name, kind, age)
    
class Cat(Animal):
    pass


c = Cat("kiska", "blonde", 1)
print(c.breath())

d = Dog("bobik", "avcharka", 1, "smell-good")
print(d.walk())

'''
#task 7: Show that you can override a parent method by defining a method with the same name in a subclass.
'''
class Vehicle:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        print("Moving....")
        

class Car(Vehicle):
    def move(self):
        return f"{self.name} is driving...."
    

class Plane(Vehicle):
    def move(self):
        return f"{self.name} is flying...."
    
obj1 = Car("Porche")
obj2 = Plane("f50")

print(obj1.move())
print(obj2.move())

'''
#task 8: Write a superhero example: Hero class with method power(), Spiderman subclass overrides power().
'''
class Superhero:
    def __init__(self, name, capacity, skills):
        self.name = name
        self.capacity = capacity
        self.skills = skills
        
    def power(self):
        print("SuperPower")
        
        
class Spiderman(Superhero):
    
    def power(self):
        return f"{self.name}'s capacity is {self.capacity}, and skills: {self.skills}"
    

hero = Spiderman("Piter", "high", "web-shooting and flexible movement")

print(hero.power())

'''
#task 9: Create a base class Appliance with __init__() initializing brand. Inherit WashingMachine that calls super().__init__() and adds capacity.
'''
class Appliance:
    def __init__(self, brand):
        self.brand = brand
    

class WashingMachine(Appliance):
    def __init__(self, brand, capacity):
        self.capacity = capacity
        super().__init__(brand)
    
    def __str__(self):
        return f"WashingMachine: {self.brand}, Cap: {self.capacity}"
    

su = WashingMachine("samsung", "20kg")
print(su)

'''
#task 10: Extend the Person → Employee hierarchy: call super().__init__() to reuse parent initialization logic.
'''
class Person:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    

class Employee(Person):
    def __init__(self, name, gender, age, position):
        self.position = position
        super().__init__(name, gender, age)
    
    def __str__(self):
        return f"name: {self.name}, gender: {self.gender}, age: {self.age}, position: {self.position}"
    

worker = Employee("haydar", "m", 22, "software-engeneer")
print(worker)

'''
#task 11: Define a Bird class with fly() method and a Parrot subclass that calls super().fly() before printing an additional message.
'''
class Bird:
    def __init__(self, name):
        self.name = name
    
    def fly(self):
        return f"{self.name} is preparing to fly"
    

class Parrot(Bird):
    
    def fly(self):
        original_fly = super().fly()
        return f"{original_fly} and now it is flying away"

reo = Parrot("reo")
print(reo.fly())
    

'''
#task 12: Override the parent constructor but still initialize parent attributes using super().__init__().
'''
class Parent:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
    
class Child(Parent):
    def __init__(self, name, skills, user_id):
        self.user_id = user_id
        super().__init__(name, skills)

a = Child("reza", "arra", "er4545")
print(a.name, a.skills, a.user_id)

'''
#task 13: Demonstrate calling a parent method using super() when both parent and child define methods with the same name.
'''
class Phone:
    def __init__(self, name):
        self.name = name
    
    def description(self):
        return f"{self.name} is connecting..."

class Smartphone(Phone):
    
    def description(self):
        result = super().description()
        return result + " -> internet is connected now!"
    
p = Smartphone("S26")
print(p.description())

'''
#task 14: Write a subclass that modifies a parent’s attribute initialized in __init__() by first calling super().__init__().
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
        self.health = 100
        self.is_stuff = False
    
    def info(self):
        return f"{self.name}, {self.age}"

class Worker(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.health = 95
        self.is_stuff = True
    
    def __str__(self):
        return f"name: {self.name}, age: {self.age}, health: {self.health}, is_stuff: {self.is_stuff}"


a_team = Worker("haydar", 20)
print(a_team)

'''
#task 15: Create a class hierarchy: Animal → Mammal → Dog. Use issubclass() to verify relationships.

'''
class Animal:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass

print(issubclass(Dog, Animal))

'''
#task 16: Create an instance of Dog and use isinstance() to check if it’s an instance of Dog, Mammal, and Animal.
'''
class Animal:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        

class Mammal(Animal):
    pass

class Dog(Mammal):
    pass


a = Dog("simba", "bulldog")
print(isinstance(a, Animal))

'''
#task 17: Write a function that takes any object and prints whether it belongs to a given parent class using isinstance().
'''
def obj_iden(item: any, source):
    return isinstance(item, source)

class Animal:
    def __init__(self, name):
        self.name = name
        
class Mammal:
    pass

dog = Animal("reks")

print(obj_iden(dog, Mammal))

'''
#task 18: Define a parent method describe() in class Employee, override it in subclass Manager.
'''
class Employee:
    def __init__(self, name, skills):
        self.name = name
        self.skills = skills
    
    def describe(self):
        return f"{self.name}, {self.skills}"
    

class Manager(Employee):
    def __init__(self, name, skills, task):
        super().__init__(name, skills)
        self.task = task
    
    def describe(self):
        result = super().describe()
        return result + " task that have to do " +  self.task
    

a = Manager("haydar", "python", "business-bot")
print(a.describe())

'''
#task 19: Write two subclasses of Shape: Square and Circle. Each overrides area() differently.
'''
from math import pi

class Shape:
    
    def area(self):
        return "area calculation...."

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side**2
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return round(pi * self.radius**2, 2)
    

sq = Square(7)
cr = Circle(7)

shapes = [sq, cr]

for i in shapes:
    print(i.area())
    
''' 
#task 20: Create a class Device with a method status(). Override it in Phone and Laptop with specific messages.
'''
class Device:
    def __init__(self, name, is_online):
        self.name = name
        self.is_online = is_online
        
    def status(self):
        if self.is_online:
            return f"{self.name} is working...."
        else:
            return f"{self.name} is not online"
        

class Phone(Device):
    def status(self):
        if self.is_online:
            return f"{self.name} is waiting for ypu Sir"
        else:
            return f"{self.name} is turned off now"
    

class Laptop(Device):
    def status(self):
        if self.is_online:
            return f"{self.name} is ready for coding sir"
        else:
            return f"{self.name} is not answering back sir"
        
p = Phone("iphone17", False)
l = Laptop("mackbook", True)

generic = [p, l]
for i in generic:
    print(i.status())
    
'''
#task 21: Define classes Flyer and Swimmer, each with a move() method. Create Duck(Flyer, Swimmer) and demonstrate which move() runs.
'''
class Flyer:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return f"{self.name} is flying away...."

class Swimmer:
    def __init__(self, name):
        self.name = name
    
    def move(self):
        return f"{self.name} is swimming away...."

class Duck(Flyer, Swimmer):
    pass

donald = Duck("donald")
print(donald.move())

'''
#task 22: Create A, B, and C(A, B) to print a message in each constructor and observe execution order.
'''
class A:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return self.name
    
class B:
    def __init__(self, ability):
        self.ability = ability
    
    def __str__(self):
        return self.ability

class C(A, B):
    def __init__(self, name, ability):
        A.__init__(self, name)
        B.__init__(self, ability)
    
    def __str__(self):
        return f"{self.name}, {self.ability}"

x = C("haydar", "python")
print(x)

'''
#task 23: Create two base classes with same method name, inherit both in a subclass, and inspect __mro__.
'''
class Vehicle:
    def move(self):
        return "hello from Vehicle"

class Transport:
    def move(self):
        return "hello from Transport"
    
class Car(Vehicle, Transport):
    def move(self):
        result = super().move()
        return result + " and Car "


a = Car()
print(a.move())

'''
#task 24: Combine two independent classes (Loggable, Database) into one subclass (LoggableDatabase) and call both parent methods.
'''
class Loggable:
    def caller(self):
        return "This device is logged at time"

class Database:
    def caller(self):
        return "After logging data has been saved"


class LoggableDatabase(Loggable, Database):
    def __init__(self, name):
        self.name = name
    
    def caller(self):
        m1 = Loggable.caller(self)
        m2 = Database.caller(self)
        return m1, m2


secret = LoggableDatabase("fifa")
print(secret.caller())

'''
#task 25: Demonstrate using super() in multiple inheritance scenario and analyze which base class method executes first.
'''
class Loggable:
    def caller(self):
        return "This device is logged at time"

class Database:
    def caller(self):
        return "After logging data has been saved"


class LoggableDatabase(Loggable, Database):
    def __init__(self, name):
        self.name = name
    
    def caller(self):
        result =  super().caller()
        return self.name, result
    

a = LoggableDatabase("python_project")
print(a.caller())

'''
#task 26: Create classes A, B(A), C(A), and D(B, C). Print D.__mro__.
'''
class A:
    def __init__(self, name):
        self.name = name

class B(A):
    pass

class C(A):
    pass

class D(B, C):
    pass

print(D.mro())

'''
#task 27: Add same method in each of the above classes and print which one is actually executed when called from D.
'''
class A:
    def __init__(self, name):
        self.name = name

    def move(self):
        return "A has been moved"
    
class B(A):
    def move(self):
        return "B has been moved"

class C(A):
    def move(self):
        return "C has been moved"

class D(B, C):
    def move(self):
        return "D has been moved"
    
obj = D("asycnronius")
print(obj.move())

'''
#task 28: Build a diamond inheritance pattern and observe MRO.
'''
class A:
    def caller(self):
        return " Hello from A"

class B(A):
    def caller(self):
        res = super().caller()
        return res + " plus hello from B"

class C(A):
    def caller(self):
        res = super().caller()
        return res + " plus Hello from C"

class D(B, C):
    def caller(self):
        res = super().caller()
        return res + " plus hello from D"
    
detail = D()
print(D.mro())
print(detail.caller())

'''
#task 29: Write a script that prints all parent classes of a class dynamically using .__mro__.
'''
class A:
    def __init__(self, name):
        self.name = name
    
class B(A):
    pass
class C(B):
    pass
class D(C):
    pass
class E(D):
    pass
class F(E):
    def __init__(self, name, skills):
        super().__init__(name)
        self.skills = skills
    
    def __str__(self):
        return f"{self.name,} {self.skills}"

obj = F("haydar", "python")
print(F.mro())
print(obj)

'''
#task 30: Verify that object is the ultimate superclass of all classes in Python.
'''
class A:
    pass
print(A.mro())

'''
#task 31: Define Dog, Cat, and Cow each with method sound(). Write a loop calling sound() for all objects.
'''
class Dog:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Gaf Gaf...."

class Cat:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Meow, Meow..."

class Cow:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Mooooo"


bulldog = Dog("qaynar")
garik = Cat("kiska")
gallan = Cow("sigiroy")

animals = [bulldog, garik, gallan]

for i in animals:
    print(i.sound())

'''
#task 32: Write a function animal_sound(animal) that calls animal.sound()—test it with different subclasses.

'''    
class Dog:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Gaf Gaf...."

class Cat:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Meow, Meow..."

class Cow:
    def __init__(self, name):
        self.name = name
    
    def sound(self):
        return "Mooooo"

bulldog = Dog("qaynar")
garik = Cat("kiska")
gallan = Cow("sigiroy")

def animal_sound(animal):
    print(animal.sound())
    
animal_sound(bulldog)
animal_sound(garik)
animal_sound(gallan)

'''
#task 33: Create an abstract-like parent Shape class with area() method, overridden by Circle and Square.
'''
from math import pi
class Shape:
    def area(self):
        raise NotADirectoryError("subclass must have method area!")
    
    
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return round(self.radius**2 * pi, 2)

class Square(Shape):
    def __init__(self, side):
        self.side = side
        
    def area(self):
        return self.side**2

a = Circle(4)
print(a.area())

b = Square(4)
print(b.area())

'''
#task 34: Demonstrate that the same method name drive() can exist in Car and Bike with different behaviors.
'''
class Vehicle:
    def drive(self):
        raise NotADirectoryError("drive() method must have subclasses")

class Car(Vehicle):
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        return f"{self.name} is driving...."


class Bike(Vehicle):
    def __init__(self, name):
        self.name = name
    
    def drive(self):
        return f"{self.name} is riding...."


obj = Car("Malibu")
obj1 = Bike("dugati")

print(obj.drive())
print(obj1.drive())    

'''
#task 35: Write a list of mixed objects (Dog, Car, Robot) and call a method action() on all of them using duck typing.
'''
class Papa:
    def action(self):
        raise NotImplementedError("coach does not play football")

class Dog(Papa):
    def __init__(self, name):
        self.name = name
        
    def action(self):
        return f"{self.name} is running and barking..."
    
    def __str__(self):
        return f"{self.name}, {self.action()}"
    

class Car(Papa):
    def __init__(self, name):
        self.name = name
    
    def action(self):
        return f"{self.name} is driving and drifting..."

class Robot(Papa):
    def __init__(self, name):
        self.name = name
    
    def action(self):
        return f"{self.name} is constructed to do this task...."
    

bulldog = Dog("zuza")
supercar = Car("lambargini")
mkl = Robot("Bender")

mixed_obj = [bulldog, supercar, mkl]
for obj in mixed_obj:
    print(obj.action())

'''
#task 36: Define two unrelated classes Duck and Person each with quack() and walk(). Write a function make_it_quack(obj) that uses duck typing.
'''
class Person:
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return self.name + " Quack Quack..."
    
    def walk(self):
        return  self.name +  " if it walks don't touch"

class Duck:
    def __init__(self, name):
        self.name = name
    
    def quack(self):
        return f"{self.name} is Donald Duck , quack!"
    
    def walk(self):
        return f"{self.name} sometimes walks around garden"

def make_quack(obj):
    print(obj.quack())

a = Person("eshmat")
b = Duck("donald duck")

make_quack(b)
make_quack(a)

'''
#task 37: Implement a function start(obj) that calls obj.run() without checking its type—test with multiple class types that implement run().
'''
class A:
    def run(self):
        return "run run run..."

class B:
    def run(self):
        return "Run taram ram"

class C:
    def run(self):
        return "Rum pum dum"

def start(obj):
    print(obj.run())

a = A()
b = B()
c = C()

shifts = [a, b, c]
for i in shifts:
    start(i)
    
'''
#task 38: Show a failure example of duck typing where a required method is missing, and handle it with hasattr().
'''
class Person:
    def __init__(self, name):
        self.name = name
    
    def run(self):
        return f"{self.name} is running...."

class Dog:
    def __init__(self, name):
        self.name = name
    
    def run(self):
        return f"{self.name} is running...."

class Duck:
    def __init__(self, name):
        self.name = name

    def action(self):
        return f"{self.name} is running...."

a = Person("Eshmat")
b = Dog("bobik")
c = Duck("donald")

objects = [a, b, c]
for i in objects:
    if hasattr(i, "run"):
        print(i.run())
    else:
        print(f"{i.name} does not have run method")

'''
#task 39: Create two classes implementing a connect() method differently (WiFi vs Ethernet). Use one unified interface to test both.
'''
class Wifi:
    def __init__(self, name):
        self.name = name
    
    def connect(self):
        return f"{self.name} is connecting but, signal is weak "

class Ethernet:
    def __init__(self, name):
        self.name = name

    def connect(self):
        return f"{self.name} is connecting badly , maybe coz of cabel"
    

a = Wifi("uic")
b = Ethernet("super cable")

objects = [a, b]
for device in objects:
    print(device.connect())
    
'''
#task 40: Combine isinstance() and duck typing: accept only objects that have a specific method or belong to a specific base class.
'''
class Person:
    def __init__(self, name):
        self.name = name
    
    def action(self):
        return f"{self.name} is walking...."

class Dog:
    def __init__(self, name):
        self.name = name
    
    def action(self):
        return f"{self.name} is walking...."

class Lion:
    def __init__(self, name):
        self.name = name
    
    def action(self):
        return f"{self.name} is walking...."
    

a = Person("eshmat")
b = Dog("bobik")
c = Lion("Simba")
d = Person("toshmat")
e = Person("Gishmat")

objects = [a,b,c,d,e]

for obj in objects:
    if isinstance(obj, Person):
        print(obj.action())
    else:
        print("type does not match!!!!")
'''
#task 41: Redefine attack() differently in Warrior, Mage, and Archer classes—demonstrate polymorphism in an iteration loop.
'''
class Character:
    def attack(self):
        raise NotImplementedError("coach does not play!")

class Warrior(Character):
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        return f"{self.name} is preparing for counter attack"

class Mage(Character):
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        return f"{self.name} is attacking throw spell"

class Archer(Character):
    def __init__(self, name):
        self.name = name
    
    def attack(self):
        return f"{self.name} has eagle eyes , target is 100%"

warrior = Warrior("Steve")
group = Mage("Merlin")
abc = Archer("Yashil O'q")

objects = [warrior, group, abc]

for obj in objects:
    print(obj.attack())
    
'''
#task 42: Extend Shape with new subclasses and make each override perimeter().
'''
from math import pi

class Shape:
    def perimeter(self):
        raise NotImplementedError("trener futbol oynamaydi!")

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def perimeter(self):
        res = (self.width + self.height) * 2
        return res

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def perimeter(self):
        res = self.radius * 2 * pi
        return round(res, 2)

class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def perimeter(self):
        res = self.a + self.b + self.c
        return res

tortburchak = Rectangle(7, 8)
dumaloq = Circle(4)
pifagor = Triangle(3, 5, 7)

a = [tortburchak, dumaloq, pifagor]
for i in a:
    print(i.perimeter())
    
'''
#task 43: Create a Notification base class with subclasses EmailNotification and SMSNotification—each overrides send().
'''
class Notifacation:
    def __init__(self, name):
        self.name = name
    
    def send(self):
        raise NotImplementedError("trener fudbol oynamaydi")


class EmailNotification(Notifacation):
    def __init__(self, name, title):
        super().__init__(name)
        self.title = title
    
    def send(self):
        return f"{self.name} and title is {self.title}"

class SMSNotification(Notifacation):
    def __init__(self, naem, number):
        super().__init__(naem)
        self.number = number
    
    def send(self):
        return f"{self.name} Alert, has been sent code to {self.number}"

phone = SMSNotification("account horseside", "1222333444")
laptop = EmailNotification("from eshmat@gmail.com", "about python-project")

print(laptop.send())
print(phone.send())

'''
#task 44: Implement a function notify_all(notifications) that calls .send() for each element, demonstrating runtime polymorphism.
'''
class Notifacation:
    def __init__(self, name):
        self.name = name
    
    def send(self):
        raise NotImplementedError("trener fudbol oynamaydi")


class EmailNotification(Notifacation):
    def __init__(self, name, title):
        super().__init__(name)
        self.title = title
    
    def send(self):
        return f"{self.name} and title is {self.title}"

class SMSNotification(Notifacation):
    def __init__(self, naem, number):
        super().__init__(naem)
        self.number = number
    
    def send(self):
        return f"{self.name} Alert, has been sent code to {self.number}"
    
phone = SMSNotification("account horseside", "1222333444")
laptop = EmailNotification("from eshmat@gmail.com", "about python-project")


def notify_all(notification):
    
    for item in notification:
        print(item.send())

not_list = [phone, laptop]

notify_all(not_list)    

'''
#task 45: Create a class Point with __add__ to support vector addition.
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def __str__(self):
        return f"Point({self.x}, {self.y})"

p1 = Point(3, 4)
p2 = Point(5, 7)

res = p1 + p2
print(res)

'''
#task 46: Extend Point with __sub__ for vector subtraction.
'''
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        return Point(new_x, new_y)

    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        return Point(new_x, new_y)    

    def __str__(self):
        return f"Point({self.x}, {self.y})"


p1 = Point(3, 4)
p2 = Point(5, 7)

print(p1 - p2)

'''
#task 47: Overload __eq__ to compare two Book objects by title and author.
'''
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    
    def __eq__(self, other):
       return self.title == other.title and self.author == other.author
    
    def __str__(self):
        return f"Book({self.title}, {self.author})"

atomic_habits = Book("formation of habits", "Kali")
        
money_psycology = Book("how to have relationship with money", "Anton Panton")

habits = Book("formation of habits", "Kali")

print(atomic_habits == money_psycology)
print(atomic_habits == habits) 

'''
#task 48: Overload __lt__ to compare Student objects by grade.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __lt__(self, other):
        return self.age < other.age

worker1 = Person("haydar", 18)
worker2 = Person("allison", 17)

print(worker2 < worker1)

'''
#task 49: Overload __len__ in a Team class to return number of players.
'''
class Team:
    def __init__(self, players):
        self.players = players
    
    def __len__(self):
        return len(self.players)
    
members = ["Ali", "haydar", "suvayn", "sahl"]

team_a = Team(members)
print(len(team_a))

'''
#task 50: Implement a Money class that overloads __add__ and __sub__ to add/subtract currency amounts.
'''
class Money:
    def __init__(self, curr_amount):
        self.curr_amount = curr_amount
    
    def __add__(self, other):
        return self.curr_amount + other.curr_amount
    
    def __sub__(self, other):
        return self.curr_amount - other.curr_amount
        

a = Money(44)
b = Money(12)

print(a + b, a - b)

'''
#task 51: Overload __str__ and __eq__ for a Product class to allow human-readable printing and equality comparison.
'''
class Animal:
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
    
    def __eq__(self, other):
        return self.kind == other.kind
    
    def __str__(self):
        return f"Animal {self.name} kind: {self.kind}"

dog = Animal("bobik", "mammal")
horse = Animal("qorabotir", "mammal")

snake = Animal("nagayna", "reptile")

print(dog == snake)
print(dog == horse)

'''
#task 52: Create a Vector class implementing __add__, __sub__, and __eq__ for full operator support.
'''
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def __str__(self):
        return f"{self.x}, {self.y}"

p1 = Vector(4, 5)
p2 = Vector(6, 8)
print(p1 + p2)
print(p1 - p2)
print(p1 == p2)

'''
#task 53: Overload __lt__ and __eq__ in Car class to compare cars by price.
'''
class Car:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def __lt__(self, other):
        return self.price < other.price
    
    def __eq__(self, other):
        return self.price == other.price
    
    def __str__(self):
        return f"name: {self.name}, price: {self.price}"


bugatti = Car("bugatti-cheron", 3000000)
lambargini = Car("aventodor", 1000000)

print(bugatti < lambargini)
print(bugatti == lambargini)
'''
#task 54: Write a ShoppingCart class that supports len(cart) using __len__.
'''
class ShoppingCart:
    def __init__(self, items):
        self.items = items
        
    def __len__(self):
        return len(self.items)

    def __str__(self):
        return f"{self.items}"

items = ["pear", "apple", "orange", "kiwi"]

a = ShoppingCart(items)
print(len(a))

'''
#task 55: Create a BookCollection class that supports addition of two collections using __add__.
'''
class BookCollection:
    def __init__(self, item):
        self.item = item
        
    def __add__(self, other):
        return self.item + other.item

    def __str__(self):
        return f"{self.item}"

collection_a = ["shekisper", "roman"]
collection_b = ["AlisherNavoi", "rumiy"]

target_a = BookCollection(collection_a)
target_b = BookCollection(collection_b)

print(target_a + target_b)

'''
#task 56: Build a hierarchy Employee → Developer and Manager, each overriding work(). Write a loop invoking work() on a list of employees.
'''
class Employee:
    def __init__(self, name, position):
        self.name = name
        self.positon = position
        
    def work(self):
        raise NotImplementedError("trener futbol oynamaydi")


class Developer(Employee):
    
    def work(self):
        return f"{self.name} works as {self.positon}"
    
class Manager(Employee):
    
    def work(self):
        return f"{self.name} works as {self.positon}"
    

worker_a = Developer("Aron", "seniorDev")
worker_b = Manager("haydar", "ProjectManager")

jobs = [worker_a, worker_b]
for i in jobs:
    print(i.work())

'''
#task 57: Create a Shape base class and implement a polymorphic draw() method in subclasses.
'''
class Shape:
    def __init__(self, name):
        self.name = name
    
    def draw(self):
        raise NotImplementedError("trener futbol or")


class Rectangle(Shape):
    
    def draw(self):
        return f"{self.name} is for formation of rectangle"

class Triangle(Shape):
    def draw(self):
        return f"{self.name} is for formation of triangle"


a = Rectangle("ab")
b = Triangle("abc")

c = [a, b]
for i in c:
    print(i.draw())

'''
#task 58: Combine inheritance and operator overloading: a Polynomial class that supports + between two polynomials.
'''
class Expression:
    
    def __add__(self):
        raise NotImplementedError("subclasses must apply this method")
    
    def __str__(self):
        return "Expression Base class"


class Polynominial(Expression):
    def __init__(self, coffs):
        self.coffs = coffs
    
    def __add__(self, other):
        max_len = max(len(self.coffs), len(other.coffs))
        
        coeff1 = self.coffs + [0] * (max_len - len(self.coffs))
        coeff2 = other.coffs + [0] * (max_len - len(other.coffs))
        
        result_coffs = [a + b for a, b in zip(coeff1, coeff2)]
        
        return Polynominial(result_coffs)
    
    def __str__(self):
        return f"Polynomial({self.coffs})"

p1 = Polynominial([5, 4, 6, 8])
p2 = Polynominial([5, 6, 8, 8])

print(p1 + p2)

'''
#task 59: Demonstrate polymorphism by defining make_sound() in Dog, Car, and Alarm. Pass all to a single function that invokes it.
'''
class Dog:
    def __init__(self, name):
        self.name = name
    
    def make_sound(self):
        return f"{self.name} is barking...."

class Car:
    def __init__(self, brand):
        self.brand = brand
    
    def make_sound(self):
        return f"{self.brand} is signalling bip bip..."

class Alarm:
    def __init__(self, model):
        self.model = model
    
    def make_sound(self):
        return f"{self.model}'s vibration is strong...."
    
animal = Dog("reks")
malibu = Car("chevrolet")
device = Alarm("zf250")

objects = [animal, malibu, device]
for i in objects:
    print(i.make_sound())
    
'''
#task 60: Write a small “battle simulator”: classes Soldier, Tank, Helicopter, each with attack(). 
# Loop over a list of mixed objects to call their respective attacks.
'''
class Tank:
    def __init__(self, model, endurance, target_accuracy):
        self.model = model
        self.endurance = endurance
        self.target_accuracy = target_accuracy
        
    def attack(self):
        res = f"While attacking {self.model}'s {self.endurance} is amazing and target accuracy is {self.target_accuracy}"
        return res
    

class Helicopter:
    def __init__(self, model, height, weapon_cap):
        self.model = model
        self.height = height
        self.weapon_cap = weapon_cap
        
        
    def attack(self):
        res = f"{self.model} is attacking now, it can {self.height} fly, and can fire coz {self.weapon_cap} 100 rockets"
        return res

class soldier:
    def __init__(self, name, division, skills):
        self.name = name
        self.division = division
        self.skills = skills
    
    def attack(self):
        res = f"{self.name} is from {self.division} and skills for attack is {self.skills}"
        return res


group_a = soldier("haydar", "morskie kotiki", "sniper")
machine = Tank("t250", "high", 96)
fly_machine = Helicopter("xr50", 4000, 100)

objects = [group_a, machine, fly_machine]

for i in objects:
    print(i.attack())
    
'''
#encapsulation
#task 61: Create a class Person with public attributes name and age. Access and modify them directly.
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name}, age: {self.age}"

worker = Person("eshmat", 25)

worker.name = "haydar"
worker.age = 24
print(worker)

'''
#task 62: Create a class Employee with _salary (protected). Print it inside the class but not outside.
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
        
    def get_info(self):
        return f"employee: {self.name}, salary: {self._salary}"

worker = Employee("haydar", 5000)
print(worker.get_info())

'''
#task 63: Write a Student class with _grades as protected and create a method display_grades() to show them.
'''
class Student:
    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        
    def display_grades(self):
        return f"name: {self.name}, grade: {self._grade}"


st = Student("haydar", 4)
print(st.display_grades())

'''
#task 64: Demonstrate that protected members can still be accessed externally but by convention shouldn’t be.
'''
class Student:
    def __init__(self, name, grade):
        self.name = name
        self._grade = grade
        
    def display_grades(self):
        return f"name: {self.name}, grade: {self._grade}"


st = Student("haydar", 4)
print(st._grade)

'''
#task 65: Extend Employee → Manager and access _salary from the subclass to prove inheritance accessibility.
'''
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary
    

class Manager(Employee):
 
    def show_info(self):
        print(f"{self.name}'s income is {self._salary}")

a = Manager("haydar", 500)
a.show_info()

'''
#task 66: Create a class Account with _balance. Add a method deposit() that modifies _balance safely.
'''
class Account:
    def __init__(self, user_id, balance):
        self.user_id = user_id
        self._balance = balance
    
    def deposit(self, amount):
        self._balance += amount
        
    
    def __str__(self):
        return f"user_id: {self.user_id}, balance: {self._balance}"
    
tom = Account("540406", 170)
tom.deposit(20)
print(tom)

'''
#task 67: Create a class BankAccount with __balance as private. Attempt to access it directly — observe error.
'''
class BankAccount:
    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.__balance = balance
    

a = BankAccount("ABC123", 70)
print(a.__balance)

'''
#task 68: Access the same __balance using name mangling (_BankAccount__balance).
'''
class BankAccount:
    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.__balance = balance
    

a = BankAccount("ABC123", 70)
print(a._BankAccount__balance)

'''
#task 69: Write a Locker class with __pin. Add a method open_locker(pin) that checks the pin.
'''
class Locker:
    def __init__(self, pin):
        self.__pin = pin
    
    def open_locker(self):
        return f"{self.__pin}"

safe = Locker(4545)
print(safe.open_locker())

'''
#task 70: Create a class Car with __engine_number and __mileage. Add a method to print both internally.
'''
class Car:
    def __init__(self, name, brand, engine_number, mileage):
        self.name = name
        self.brand = brand
        self.__engine_number = engine_number
        self.__mileage = mileage
    
    
    def technical_info(self):
        return f"engine_number: {self.__engine_number}, mileage: {self.__mileage}"
    
    def __str__(self):
        return f"{self.name}, {self.brand}"
    

machine = Car("m5f90", "bmw", "2554565", 100000)
print(machine)

print(machine.technical_info())

'''
#task 71: Demonstrate that a private variable in base class cannot be accessed in subclass directly.
'''
class Animal:
    def __init__(self, name, kind, skills):
        self.name = name
        self.__kind = kind
        self.__skills = skills
    


class Dog(Animal):
    
    def show_info(self):
        return f"kind: {self.__kind}, skills: {self.__skills}"


d = Dog("bobik", "avcharka", "smell-good")
print(d.show_info())

'''
#task 72: Use name mangling to read a private variable from outside (educational purpose only).
'''
class Animal:
    def __init__(self, name, kind, skills):
        self.name = name
        self.__kind = kind
        self.__skills = skills
    


class Dog(Animal):
    
    def show_info(self):
        return f"kind: {self._Animal__kind}, skills: {self._Animal__skills}"


d = Dog("bobik", "avcharka", "smell-good")
print(d.show_info())
'''
#task 73: Create a private method __calculate_interest() inside BankAccount and call it from a public method.
'''
class Bank:
    def __init__(self, name, balance, rate, time):
        self.name = name
        self.__balance = balance
        self.__rate = rate
        self.__time = time
    
    def __calculate_interest(self):
        interest = (self.__balance * self.__rate * self.__time) / 100
        return interest
    
    def show_interest(self):
        interest = self.__calculate_interest()
        return f"interest: {interest}"


user = Bank("haydar", 760, 18, 2)


print(user.show_interest())

'''
#task 74: Verify private attributes do not appear in dir(obj) under their original names.
'''
class Log:
    def __init__(self, name, created_at, updated_at):
        self.name = name
        self.__created_at = created_at
        self.__updated_at = updated_at
    
    

info = Log("homestaid", "02042026", "03042026")

print(dir(info))

'''
#task 75: Print obj.__dict__ of an object with private attributes to inspect name-mangled versions.
'''
class Log:
    def __init__(self, name, created_at, updated_at):
        self.name = name
        self.__created_at = created_at
        self.__updated_at = updated_at
    
    

info = Log("homestaid", "02042026", "03042026")

print(info.__dict__)

'''
#task 76: Create a Temperature class with private _celsius attribute. Add getter and setter methods manually.
'''
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    def get_temperature(self):
        return self.__celsius
    
    def set_temperature(self, amount):
        self.__celsius = amount
        return f"it is {self.__celsius} in Celsius"

info = Temperature(0)

print(info.get_temperature())
print(info.set_temperature(50))

'''
#task 77: In setter, ensure temperature never drops below absolute zero (-273.15).
'''
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    def get_temp(self):
        return self.__celsius
    
    def set_temp(self, amount):
        if amount < -273.15:
            return "temperature never drops below (-273.15)"
        else:
            self.__celsius = amount
            return self.__celsius
        

info = Temperature(0)

info.set_temp(15)

print(info.get_temp())

print(info.set_temp(-99))
print(info.get_temp())
'''
#task 78: Add a get_fahrenheit() method that converts Celsius to Fahrenheit.
'''
class Temperature:
    def __init__(self, celsius):
        self.__celsius = celsius
    
    def get_temp(self):
        return self.__celsius
    
    def set_temp(self, amount):
        if amount < -273.15:
            return "temperature never drops below (-273.15)"
        else:
            self.__celsius = amount
            return self.__celsius
        
    def get_fahrenheit(self):
        fahrenheit = self.__celsius * 9/5 + 32
        return fahrenheit
    

info = Temperature(25)

print(info.get_fahrenheit())

'''
#task 79: Create Student class with private __marks. Use getter to read and setter to validate (0–100).
'''
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.__marks = marks
    
    def get_mark(self):
        return self.__marks
    
    def set_marks(self, val):
        if val < 0 or val > 100:
            raise ValueError("marks should be between 0 and 100!")
        else:
            self.__marks = val
          
    
    
    def __str__(self):
        return f"{self.name}, {self.__marks}"
    

st = Student("haydar", 4)

st.set_marks(102)
print(st.get_mark())

'''
#task 80: Implement a set_password() and check_password() pair with basic validation in a UserAccount class.
'''
class UserAccount:
    def __init__(self, name, age, password):
        self.name = name
        self.age = age
        self.set_password(password)
        
    
    def set_password(self, value):
        if len(value) < 8:
            raise ValueError("password should contain 8 characters!")
        
        if not any(ch.isupper() for ch in value):
            raise ValueError("at least you need one Capital letter")
        
        if value.isalnum():
            raise ValueError("at least one special charater is needed")
        
        self.__password = value
        
    
    def check_password(self, value):
        return self.__password == value
    

a = UserAccount("ali", 18, "!haydaR123")

print(a.check_password("!haydaR12"))
'''
#task 81: Demonstrate the difference between direct attribute modification vs using a setter method.

#task 82: Recreate the Temperature class using @property for cleaner access.
'''
class Temperatur:
    def __init__(self, celsius):
        self.celsius = celsius
        
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -237.15:
            raise ValueError("Temperature cannot be below -237.15")
        
        self._celsius = value
        

a = Temperatur(18)
print(a.celsius)
a.celsius = -999
print(a.celsius)

'''
#task 84: Add a @temperature.deleter that deletes the value and prints “Temperature deleted.”
'''
class Temperatur:
    def __init__(self, celsius):
        self.celsius = celsius
        
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -237.15:
            raise ValueError("Temperature cannot be below -237.15")
        
        self._celsius = value
        
    @celsius.deleter
    def celsius(self):
        del self._celsius
        print("temperature deleted successfuly")

a = Temperatur(48)
print(a.celsius)

del a.celsius

a.celsius

'''
#task 85: Create a Rectangle class with @property for area, automatically calculated from width and height.
'''
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("width should be greater than 0")
        
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("height should not be smaller than 0")
        
        self._height = value
    
    @property
    def area(self):
        return self._width * self.height
    

figure = Rectangle(8, 8)

print(figure.area)

'''
#task 86: Create a Circle class with radius as a private attribute and expose diameter and area as computed properties.
'''
from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("circle cannot have 0 or below zero radius!")
        
        self._radius = value
    
    @property
    def diameter(self):
        return self.radius * 2
    
    @property
    def area(self):
        return round(self.radius**2 * pi, 2)


a = Circle(5)

print(a.area)
print(a.diameter)

'''
#task 87: Create BankAccount with @property balance, which returns a rounded balance value.
#task 88: Add @balance.setter that prevents setting a negative balance.
#task 89: Add @balance.deleter to simulate closing an account and wiping balance.
'''
class BankAccount:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance
    
    @property
    def balance(self):
        return round(self._balance, 2)
    
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be zero")
        
        self._balance = value
    
    @balance.deleter
    def balance(self):
        del self._balance
    

user = BankAccount("haydar", 20, 7000)

user.balance = 7800
print(user.balance)

del user.balance

print(user.balance)

'''
#task 90: Implement a Person class with @property fullname combining first and last names, with custom setter and deleter.
'''
class Person:
    def __init__(self, first_name , last_name):
        self.first_name = first_name
        self.last_name = last_name
    
    @property
    def first_name(self):
        return self._first_name
    
    @first_name.setter
    def first_name(self, value):
        if not value.isalpha():
            raise ValueError("name must only contain letter")
    
        self._first_name = value
    
    @property
    def last_name(self):
        return self._last_name
    
    @last_name.setter
    def last_name(self, value):
        if not value.isalpha():
            raise ValueError("last_name must only contain letters!")
        
        self._last_name = value 
    
    @property
    def fullname(self):
        return F"{self._first_name} {self._last_name}"
    

user  = Person("haydar", "Ali")

print(user.fullname)

'''
