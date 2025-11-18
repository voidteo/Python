#====================THIS IS RE-ENHANCING WHAT I LEARNT FROM WHILE AND FOR LOOP==================#


#TASK 1: Print all numbers from 1 to 200 that are divisible by 3 and 7 both.
"""
for i in range(1, 201):
    if i % 3 == 0 and i % 7 == 0:
        print(i)
""" 
#task 2: Count how many numbers between 1–1000 contain the digit “7”.
"""
cnt = 0

for i in range(1, 1001):
    if "7" in str(i):
        cnt+=1
print(cnt)

""" 
#task 3: Print all numbers whose sum of digits is divisible by 3.
"""
n = int(input("n: "))

for i in range(1, n+1):
    s = 0
    for ch in str(i):  # i gacha yurib har bir ch ni string qilyapmiz
        s+=int(ch) # string qilingan sonni qoshib chiqyapmiz int ga aylantirib
    if s % 3 == 0: # yigindini tekshiryapmiz
        print(i)

""" 
#====================WELL ORDERED EXCERSICES====================#

#TASK 1: Generate all pairs (i, j) where i = 1..3, j = 1..3.
"""
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
""" 
#task 2: Generate all triplets (i, j, k) where i = 1..2, j = 1..2, k = 1..2.
"""
for i in range(1, 3):
    for j in range(1, 3):
        for k in range(1, 3):
            print(i, j, k)
""" 
#task 3: Print the first 20 Fibonacci numbers.
"""
f1, f2 = 0, 1

for i in range(20):
    print(f1)
    nxt = f1 + f2
    f1 = f2
    f2 = nxt
""" 
#task 4: Print all 2-digit numbers whose digits add up to 10.
"""
for i in range(10, 100):
    a = i % 10
    b = i // 10
    if (a+b) == 10:
        print(i)
"""
#task 5: Print numbers from 1 to 100 and print “Fizz” if divisible by 3, “Buzz” if divisible by 5.
"""
for i in range(1, 100+1):
    if i % 3 == 0:
        print(f"fizz[{i}]")
    elif i % 5 == 0:
        print(f"buzz[{i}]")
""" 
#======================WHILE LOOP====================#

#task 6: Print numbers from 1 to 50 using a while loop.
"""
i = 0
while i < 50:
    print(i)
    i+=1
""" 
#task 7: Print numbers from 50 down to 1 using while.
"""
i = 50
while i > 0:
    print(i)
    i-=1
""" 
#task 8: Print all even numbers from 1 to 100 using while.
"""
i = 0
while i <= 100:
    print(i)
    i+=2
"""
#task 9: Sum numbers from 1 to 100 using while.
"""
i, s = 0, 0
while i <= 100:
    s+=i
    i+=1
print(s)
""" 
#task 10: Calculate the factorial of a number using while.
"""
fac = 1
i = 1

n = int(input("n: "))
while i <= n:
    fac*=i
    i+=1
print(fac)
"""
#task 11: Ask the user to enter numbers until they enter 0, then print the sum.
"""
s = 0

while True:
    n = int(input("n: "))
    if n == 0:
        print(n)
        break
    else:
        s+=n
print(s)

""" 
#task 12: Ask the user for a password and give them 3 attempts using while.
"""
pswrd = "teo77"
attemps = 3
i = 1

while i <= attemps:
    n = input("enter password: ")
    if n == pswrd:
        print("welcome")
        break
    else:
        print(attemps - i, "left")
        i+=1
""" 
#task 13: Ask the user to enter numbers until their sum exceeds 100; print how many numbers they entered.
"""
s = 0
cnt = 0

while s < 100:
    n = int(input("n: "))
    s+=n
    cnt+=1
print(cnt)

""" 
#task 14: Count digits of a user-entered number using while.
"""
cnt = 0 
n = int(input("n: "))
num = abs(n)

while num > 0:
    num = num // 10
    cnt+=1
print(cnt)

""" 
#task 15: Reverse a user-entered number using while.

st = input("enter string:  ")
i = len(st)-1
res = ""

while i >= 0:
    res+=st[i]
    i-=1
print(res)
