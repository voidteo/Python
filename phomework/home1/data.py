"""
mytup = ("orange", "banana", "apple",)

mytup_lst = list(mytup)
mytup_lst[0]= "Teo"
mytup = tuple(mytup_lst)

print()

""" 

person = {
    "name" : "Teo",
    "age" : 22,
    "city" : "tashkent"
} # dict yasash
"""
print(person["name"]) # dict elementga murojat qilish
print(person["age"])

print(person.get("name")) # elementga murojat qilish , xato bermaydi None

person["age"] = 23
print(person.get("age")) # qiymatni ozgartirish

person["hobby"] = "ufc"
print(person) #yangi element qoshish

person.pop("hobby") # element ochirish kalit boyicha ochiradi
print(person)

del person["age"] # buyam ochiradi

person.clear() # butun dictni tozalaydi
print(person)
"""
"""
print(person.keys()) # kalitlarni oladi
print(person.values()) # qiymatlarni oladi
print(person.items()) # kalit qiymatni oladi
"""
"""
for key in person:
    print(key, "->", person[key])

"""
"""
for key, value in person.items():
    print(key, ":", value)
"""
"""
def outer():
    def inner():                                                # this is function inside of function , it only lives inside function
        return "Hello from inner function"                        # to call to outer function or we make it visible to outer function
    res = inner()                                                                   # we will hold value of this function in variable
    return res   # then we will return that value in the result , variable of the inner function or "return of inner" will be executed on the screen by calling outer func
print(outer())

""" 
"""
def outer():
    x = 10
    def inner():
        print(x)
    return x

#print(outer())
""" 
"""
def multiplier(n):
    def multiply(x):
        return x*n
    return multiply 

res = multiplier(3)
print(res(4))

""" 

# 10 tasks about variables: 

#task 1: x va y degan o‘zgaruvchilarni e’lon qilib, ularni almashtir.
"""
x = 10
y = "teo"
temp = x
x = y
y = temp
print(x , y)
"""
""" 
x = 10
y = 5
y , x = 10 ,5
print(x, y)

""" 
#task 2: Uchta o‘zgaruvchiga qiymat ber (name, age, city) va ularni f-string bilan chiqar.
"""
name = "Eshmatic"
age = 19
city = "tashkent"
print(f"name: {name}, age: {age}, city: {city}")

""" 
#task 3: Ikkita raqamni qo‘sh, ayir, ko‘paytir, bo‘l va natijalarni har biri uchun alohida o‘zgaruvchida saqla.
"""
x , y = 10, 5
a = x + y
b = x - y
c = x * y
d = x // y

print(a, b, c, d)
""" 
#task 4: radius ni kiritib, doiraning yuzasini (πr²) hisobla.
"""
r = int(input("enter radius: "))
p = 3.14
s = 0

s = p * (r**2)
print(f"s = {s}")

""" 
#task 5: a, b, c tomonlari berilgan uchburchakning perimetrini top.
"""
a, b, c = 5, 4, 3
p = ( a + b + c )

print(p)
""" 
#task 6: name ni kirit, va harflar sonini ekranga chiqar.
"""
name = input("enter your name: ")
print(len(name), name)
""" 
#task 7: year_of_birth ni kiritib, yoshni hisobla (2025-yil asosida).
"""
year_of_birth = int(input("Enter year of birth: "))
year = 2025
age = year - year_of_birth

print(age)

""" 
#task 8: num1, num2 ni kiritib, ularning o‘rta arifmetigini chiqar.
"""
num1, num2 = 10 , 20

s = num1+ num2
avg = s/2
print(avg)

""" 

"""
x = int(input("enter number: "))

if x > 10:
    print("eshmat")
else:
    print("toshmat")

""" 

#task 1: Create three variables of different data types and print their types.
"""
i = int(input("entrer number: "))
while i > 0:
    print(i)
    i-=1
    
""" 
"""
i = int(input("enter i: "))
j = int(input("enter: j: "))
jmp = int(input("enter jump: "))

if i < j:
    print("i cannot be smaller than j")
    
while i < j:
    print(i)
    i+=jmp
    
""" 
"""
i = 2
while i < 20:
    print(i)
    i+=2
    
""" 
"""
i = 1

while i < 20:
    if i % 2 == 1:
        i+=1
        print(i)
""" 

