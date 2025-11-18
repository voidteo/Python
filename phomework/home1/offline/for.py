
#task 1:

"""
for i in range(1, 11, 1):
    print(i)
""" 

#task 2: 
"""
for i in range(10, 0, -1):
    print(i)
""" 
#task 3: 
"""
for i in range(2, 21, 2):
    print(i)
""" 
#task 4: 
"""
for i in range(1, 21, 1):
    if i % 2 == 1:
        print(i)
""" 
#task 5: print square 1 to 10
"""
for i in range(1, 11):
    print(i**2)
""" 
#task 6: 
"""
for i in range(1, 6):
    print(i**3)
""" 
#task 7: 
"""
for i in range(1, 51):
    if i % 5 == 0:
        print(i)
""" 
#task 8: .Print numbers from 1 to 50 that are not divisible by 3.
"""
for i in range(1, 51):
    if i % 3 != 0:
        print(i)
""" 
#task 9: 
"""
a, b = map(int, input().split()) # it is alternative for a = int(input()) it can ask multiple inputs and store it to multiple variables
print(a, b)                                             #b = int(input())
""" 
"""
for i in range(1, 20):
    if i % 2 == 0:
        print("even: ", i)
    else:
        print("odd: ",   i)
""" 
#task 10: 
"""
s = 0
for i in range(1, 101):
    s+=i
print(s)

"""
#task 11: Ask the user for a number n, and print numbers from 1 to n.
"""
n = int(input("enter number: "))

for i in range(1, n+1):
    print(i)
""" 
#task 12: Ask the user for a number n, and print numbers from n down to 1.
"""
n = int(input("enter number: "))

for i in range(n, -1, -1):
    print(i)
""" 
#task 13: Print numbers from 1 to 100, but only those divisible by 3 and 5.
"""
for i in range(1, 100+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)
"""
#task 14: Print the cube of all numbers from 1 to 10.
"""
for i in range(1, 11):
    print(i**3)
""" 
#task 15: Find the sum of numbers from 1 to 10.
"""
s = 0
for i in range(1, 11):
    s+=i
print(s)
""" 
#task 16: Find the sum of even numbers between 1 and 20.
"""
s = 0

for i in range(1, 21):
    if i % 2 == 0:
        s+=i
        
        
print(s)
""" 
#task 17: Find the sum of odd numbers between 1 and 20.
"""
s = 0

for i in range(1, 21):
    if i % 2 == 1:
        s+=i
print(s)

""" 
#task 18: Find the factorial of a number using a for loop.
"""
n = int(input("enter n: "))
fac = 1

for i in range(1, n+1):
    fac*=i
print(fac)
""" 
#task 19: Find the sum of squares from 1 to 10.
"""
s = 0
for i in range(1, 11):
    s+=i**2
print(s)
""" 
#task 20: Ask the user for a number n, and print the sum of numbers from 1 to n.
"""
n = int(input("enter number: "))
s = 0

for i in range(1, n+1):
    s+=i
    
print("the sum of numbers: ", s)

""" 
#task 21: Find the average of numbers from 1 to 10.
"""
s, avg = 0, 0

for i in range(1, 11):
    s+=i
avg = s / 10
print(avg)

""" 
#task 22: Count how many numbers between 1 and 50 are divisible by 7.
"""
cnt = 0

for i in range(1, 51):
    if i % 7 == 0:
        cnt+=1
        print(i)
print("numbers that divisble to 7 are: ", cnt)
""" 
#task 23: Print all numbers from 1 to 100 and show their running total (progressive sum).
"""
s = 0

for i in range(1, 101):
    s+=i
    print(f"number: {i} = sum: {s}")    
""" 
#task 24: Print the product (multiplication) of numbers from 1 to 5.
"""
product = 1

for i in range(1, 5+1):
    product*=i
print(product)
""" 
#task 25: Print "Hello" 5 times.
"""
for i in range(1, 6):
    print("hello world")
"""
#task 26: Print "Teo" as many times as the user enters a number n.
"""
n = int(input("enter number: "))

for i in range(1, n+1):
    print("teo")
""" 
#task 27: Print numbers from 1 to 10 on one line, separated by spaces.
"""
for i in range(1, 11):
    print(i, end= " ")
print("\n")

"""
#task 28: 
"""
row = 5
for i in range(1, row+1):
    print("*" * i)
""" 
#task 29: 
"""
row = 5
for i in range(row, -1, -1):
    print("*" * i)
""" 
#task 30: 
"""
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()
"""
#task 31: Count how many numbers from 1 to 100 are divisible by 5.
"""
cnt = 0
for i in range(1, 100+1):
    if i % 5 == 0:
        cnt+=1
print(cnt)

""" 
#task 32: Print each character of a string "python".
"""
for c in "python":
    print(c)
""" 
#task 33: Count vowels in a string entered by the user.
"""
vovel = "aieou"
s = input("enter string: ")
cnt = 0

for c in s.lower():
    if c in vovel:
        cnt+=1
print("number of vovels: ", cnt)

"""
#task 34: Count digits in a string (e.g., "a2b3c4" → count 3).
"""
cnt = 0
st = "a2b3sn4n6"

for ch in st:
    if ch.isdigit():
        cnt+=1
print(cnt)
""" 
#task 35: Print the string reversed using a for loop.
"""
n = input("enter string: ")
res = ""

for ch in n:
    res = ch + res
print(res)
"""
"""
n = input("enter string: ")
res = ""

for ch in range(len(n, -1, -1)):
    res+=n[ch]
print(res)

""" 
#task 36: Count how many uppercase letters are in a string.
"""
st = input("enter string: ")
cnt = 0

for ch in st:
    if ch.isupper():
        cnt+=1
print(cnt)

"""
#task 37: Print numbers from 1 to 50 but skip numbers divisible by 4.
"""
for i in range(1, 50+1):
    if i % 4 == 0:
        continue
    print(i)
""" 
#task 38: Print numbers from 1 to 100 but stop at 60 (use break).
"""
for i in range(1, 101):
    if i == 60:
        break
    print(i)
"""
#task 39: Print numbers 1–30 but continue (skip) multiples of 3.
"""
for i in range(1, 31):
    if i % 3 == 0:
        continue
    print(i)
""" 
#task 40: 
"""
row = 5
for i in range(1, row+1):
    print("*" * i)
"""

#task 40: Print multiplication table 1–5 (nested loop but NO LISTS).
"""
for i in range(1, 5):
    for j in range(1, 6):
        print(i * j, end=" ")
    print()
""" 
#task 41: Count how many numbers from 1 to 100 are prime (only using for loops).
"""
cnt = 0

for num in range(2, 101):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        cnt+=1
print(cnt)

"""
#task 42: Print all 2-digit numbers whose digits add up to 10 (e.g., 28, 55).
"""
for num in range(10, 100):
    i = num // 10
    k = num % 10
    if i + k == 10:
        print(num)
""" 
#task 43: Print all numbers from 1 to 200 that are divisible by both 3 and 7.
"""
for i in range(1, 201):
    if i % 3 == 0 and i % 7 == 0:
        print(i)
""" 
#task 44: Print the first 10 Fibonacci numbers using a for loop (no lists).
"""
f1, f2 = 0, 1

for i in range(11):
    print(f1)
    next = f1 + f2
    f1 = f2
    f2 = next
""" 
#task 45: Print all pairs (i, j) where both go from 1 to 3 (nested loop, no lists).
"""
for i in range(1, 4):
    for j in range(1, 4):
        print(i, j)
""" 
