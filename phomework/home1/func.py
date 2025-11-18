#task 1: “Hello, World!” chiqaradigan funksiya yoz.
"""
def greet()->None:
    print("hello world")
    return None
    
greet()

""" 
#task 2: Foydalanuvchining ismini olib, unga salom beradigan funksiya.
"""
def greet():
    s = input("enter your name: ")
    return f"hello {s}, how are you?"

res = greet()
print(res)

""" 
#task 3: Ikki sonni qo‘shuvchi funksiya.
"""
def add(a: int, b: int)-> int:
    return a + b

res = add(5, 6)
print(res)

""" 
#task 4: Kvadratini qaytaruvchi funksiya.
"""
def square(a):
    return a**2

res = square(7)
print(res)

""" 
#task 5: Uch sonning eng kattasini qaytaruvchi funksiya.
"""
def big(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c
    else :
        return a, b, c
    

res = big(2, 3, 6)
print(res)

""" 
#task 6: Foydalanuvchi kiritgan so‘z uzunligini chiqaruvchi funksiya.
"""
def finder():
    s = input("enter string: ")
    return f"length of {s} is {len(s)}"

res  = finder()
print(res)

""" 
#task 7: Son juft yoki toq ekanligini tekshiruvchi funksiya.
"""
def finder(a: int)-> int:
    if a % 2 == 0:
        return f"{a} is even"
    else:
        return f"{a} is odd"
    
print(finder(5))

""" 
#task 8: Ro‘yxatdagi sonlar yig‘indisini hisoblovchi funksiya.
"""
def find_summ(l: list):
    s = 0
    for i in l:
        s+=i
    return s

print(find_summ(l = [1,2,3,4,5]))

""" 
#task 9: Ro‘yxatdagi o‘rtacha qiymatni qaytar.
"""
def find_avg(l: list):
    s, avg = 0, 0
    for i in l:
        s+=i
    avg = s / len(l)
    return f"average  is {avg}"

print(find_avg(l = [1,2,3,4,5,6,7,8,9,10]))

""" 
#task 10: String ichidagi unli harflar sonini top.
"""
def count_vovels(s: str) -> int:
    a = "aouie"
    cnt = 0
    for i in s:
        if i in a:
            cnt+=1
    return cnt
        
print(count_vovels("eshmat"))

""" 
#task 11: *args bilan istalgancha son qo‘shuvchi funksiya yoz.
"""
def adder( *args ):
    return args

res = adder(1,2,3,4,"teo", True, 5.5, (4,))
print(res)

""" 
#task 12: **kwargs bilan ma’lumotlarni chop etuvchi funksiya.
"""
def print_info(**kwargs):
    return kwargs

res = print_info(name = "teo", year = 2003)
print(res)

""" 
#task 13: Standart qiymatli argumentli funksiya yoz (def greet(name="Anon")).
"""
def greet(name = "Anon"):
    print(f"hello {name}")
greet()
greet("teo")

""" 
#task 14: Funksiyadan bir nechta qiymatni qaytar (return a, b).
"""
def ret(a, b):
    return a, b 

print(ret(5, 6))

""" 
#task 15: Funksiyani boshqa funksiya ichida chaqir. 
"""
def greet():
    return "hello"

def greet_person():
    msg = greet()
    return msg + " Teo"

print(greet_person())

""" 
#task 16: Ichki (inner) funksiya yarat.
"""
def outer():
    print("hi ")
    
    def inner():
        return "teo"
        
        outer()
        
outer()

""" 
#task 17: Lambda funksiya orqali kvadrat hisobla.



