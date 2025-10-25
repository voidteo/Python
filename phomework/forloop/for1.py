# task 1: k va n butun sonlari berilgan (n > 0). k sonini n marta chiqaruvchi programma tuzisin.

"""
k=int(input("k= ")) # i will count this
n=int(input("n= ")) # this something like duration , i'll count k n times

for i in range(n):
    if n>0:
        print(k, end=" ")
    else:
        print("you should enter number bigger than zero")     """

""" task2: 

a va b butun sonlari berilgan (a < b).
 a va b sonlari orasidagi barcha butun sonlarni (a va b ni ham) chiqaruvchi
  va chiqarilgan sonlar sonini chiqaruvchi programma tuzisin. (a va b xam chiqarilsin).
"""
"""
a=int(input("a= "))
b=int(input("b= "))
cnt=0

if a<=b:
    for i in range(a, b+1):
        cnt+=1
        print( i )
else:
    for j in range(a, b-1, -1):
        cnt+=1
        print( j )
print("all amount of numbers: ", cnt)
"""

"""task 3:
a va b butun sonlari berilgan (a < b). a va b sonlari orasidagi barcha butun 
sonlarni (a va b dan tashqari) kamayish tartibida chiqaruvchi va chiqarilgan sonlar sonini chiqaruvchi programma tuzisin.
"""
"""
a=int(input("a= "))
b=int(input("b= "))
cnt=0

for i in range(b-1, a, -1):
    print(i, end=" ")
    cnt+=1
print("quantity of numbers:", cnt)
"""

#task4: Bir kg konfetining narxi berilgan (haqiqiy son). 1, 2, ..., 10 kg konfetni narxini chiqaruvchi programma tuzisin.
"""
price=int(input("enter price 1 kg: "))
for i in range(1, 11):
    print(f"{i} kg cookie is {i*price} dollars")
"""

#task5: Bir kg konfetining narxi berilgan (haqiqiy son). 0.1, 0.2, ..., 0.9, 1 kg konfetni narxini chiqaruvchi programma tuzisin.
"""
price=float(input("enter price for 1 kg: "))

for i in range(1, 11):
    weight= i/10
    cost= weight * price
    print(f"{weight} kg cookie costs {cost} dollars")
"""

#task6: Bir kg konfetining narxi berilgan (haqiqiy son). 1.2, 1.4, ..., 2 kg konfetni narxini chiqaruvchi programma tuzisin.
"""
price=float(input("enter 1 kg price: "))

for i in range(12, 21, 2):
    weight=i/10
    cost=weight*price
    print(f"{weight} kg candy costs {cost: .2f} dollars")
"""

#task7: a va b butun sonlari berilgan (a < b). a dan b gacha bo'lgan barcha butun sonlar yig'indisini chiqaruvchi programma tuzisin.
"""
print("a<b")
a=int(input("a= "))
b=int(input("b= "))
sm=0

for i in range(a, b):
    sm+=i
    print(i, end=" ")
print(f"sum of (a,b) is {sm}")
"""

#task8: a va b butun sonlari berilgan (a < b). a dan b gacha bo'lgan barcha butun sonlar ko'paytmasini chiqaruvchi programma tuzisin.
"""
a=int(input("a= "))
b=int(input("b= "))
sm=1

for i in range(a, b):
    sm*=i
print(f"sum of numbers is {sm}")
"""

#task9:  a va b butun sonlari berilgan (a < b). a dan b gacha bo'lgan barcha butun sonlar kvadratlarining yig'indisini chiqaruvchi programma tuzisin.
"""
a=int(input("a= "))
b=int(input("b= "))
sm=0

for i in range(a, b):
    sm+=i**2
print("yigindi: ", sm)
"""
#task10:  n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma tuzisin.
#S = 1 + 1/2 + 1/3 + ... + 1/n
"""
n=int(input("n= "))
sm=float(0.0)

for i in range(1, n+1):
    sm+=1/i
    print("sequence:",  sm)
print(f"sum= {sm}")
"""
#task11: n butun soni berilgan (n > 0). Quyidagi yig'indini hisoblovchi programma tuzisin.
#S = n² +(n+1)²+(n+2)² + ... (2*n)²
"""
n=int(input("n= "))
sm=0

for i in range(n, 2*n+1):
    sm+=i**2
print(f"sm= {sm}")
"""
#task12:n butun soni berilgan (n > 0). Quyidagi ko'paytmani hisoblovchi programma tuzisin.
#S = 1.1 * 1.2 * 1.3 * ...    (n ta ko'payuvchi)
"""
n=int(input("n= "))
s=1.0

for i in range(1, n+1):
    s*=(1+i/10)
    print(s, end="\n")
print(f"res= {s: .2f}", end="\n")
"""