"""
1. **Count to 10:** Print numbers from 1 to 10.
2. **Countdown:** Print numbers from 10 down to 1.
3. **Even Numbers:** Print all even numbers from 2 to 20.
4. **Odd Numbers:** Print all odd numbers from 1 to 19.
5. **Multiples of 3:** Print all multiples of 3 less than or equal to 30.
6. **Sum of a Range:** Calculate the sum of all numbers from 1 to 50.
7. **Average of a Range:** Calculate the average of numbers from 1 to 100.
8. **Multiplication Table:** Print the 9 times table up to 10.
9. **Factorial:** Calculate the factorial of a user-entered number (e.g., 5! = 120).
10. **Countdown with Steps:** Count down from 100 to 0, decreasing by 10 each time.

"""
#tas 1:
"""
i=1
while i<=10:
    print(i)
    i+=1
"""
#task 2:
"""
i=11
while i>1:
    i-=1
    print(i)
"""
#task 3: 
"""
i=0
while i<20:
    i+=2
    print(i)
"""
#task 4: 
"""
i=0
while i<=19:
    if i%2==1:
        print(i)
    i+=1
"""
#task 5:      
"""
i=0
while i<=30:
    print(i)
    i+=3
"""
#task 6:
"""
i=0
sm=0
while i<=50:
    sm+=i
    i+=1
print("sum of i:", sm)
"""
#task 7: 
"""
i=1
avg=0
sm=0
while i<=100:
    sm+=i
    i+=1
avg=sm/100
print(avg)
"""
#task 8: 
"""
i=1
sm=1
while i<=10:
    sm =9*i
    print(f"9 x {i}= {sm}")
    i+=1
"""
#task 9: 
"""
n=int(input("n= "))
fac=1
i=1

while i<=n:
    fac*=i
    i+=1
print(f"{n} factorial= {fac}")
"""
#task 10: 
"""
i=100
while i>=0:
    print(i)
    i-=10
"""

#task 11: Ask the user for five numbers and print "Positive" or "Not Positive" for each one.
"""
i=0
while i<=5:
    num=int(input("enter: "))
    if num >= 0:
        print("positive:", i)
    else:
        print("negative:", i)
    i+=1
"""
"""
for i in range(5):
    num=int(input("enter number: "))
    if num>=0:
        print("positive", i)
    else:
        print("negative", i)
"""

#task 12: Count the number of vowels (`a`, `e`, `i`, `o`, `u`) in a user-provided string.
"""
vovels="aeiou"
tx="strange thing is happening"
cnt=0

for i in tx:
    if i in vovels:
        cnt+=1

print("vovels count: ", cnt)
"""

#task 13:  Count the number of consonants in a user-provided string.
"""
st=input("Enter: ")
vovels="aeiou"
cnt=0

for i in st:
    if i.isalpha() and i.lower() not in vovels:
        cnt+=1
print(cnt)
"""

#task14: For numbers from 1 to 20, print "Fizz" for multiples of 3, "Buzz" for multiples of 5, and "FizzBuzz" for multiples of both. Otherwise, print the number.
"""
n=int(input("number (1,20): "))

for i in range(1, n+1):
    if i % 3 == 0 and i % 5 == 0 :
        print("FizzBuzz")
    elif i % 3 == 0 :
        print("Fizz")
    elif i % 5 == 0 :
        print("Buzz")
    else:
        print(i)
"""

#task 15:Prime Number Check:** Ask the user for a number and use a `for` loop to determine if it is a prime number.
"""
n=int(input("enter number: "))

if n <= 1:
    print(n, "is not a prime number")
else:
    is_prime=True
    for i in range(2, n):
        if n % i == 0:
            is_prime=False
            break
    if is_prime:
        print(n, "Prime number")
    else:
        print(n, " not a prime number")
"""

#task 16:Find and print all numbers between 1 and 100 that are divisible by both 7 and 13.
"""
for i in range(1, 101):
    if i % 7 ==0 and i % 13 == 0:
        print(i)
"""

#task 17:Iterate through a string and check if it contains any uppercase letters.
"""
string=input("enter string: ")
has_upper=False

for c in string:
    if c.isupper():
        has_upper=True
        break

if has_upper:
    print("string contains uppercase")
else:
    print("string doesn't contain uppercase")
"""

#task 18: Count the number of digits in a user-entered number.
"""
n=input("n= ")
if n.startswith("-"):
   n = n[1:]
if n.isdigit():
    print("number of digits: ", len(n))
else:
    print("ERROR ENTER WHOLE NUMBERS!")
"""

#task 19: Calculate the sum of the digits of a number.
"""
n=int(input("n= "))

if n < 0:
    n=-n
s=0
digit=0
while n>0:
    digit = n % 10
    s+=digit
    n//=10
print("summ of digits: ", s)
"""
"""
n=input("n= ")
s=0
for i in (n):
    if i.isdigit():
        s+=int(i)
print("sum of digits: ", s)
"""
#task 20:  Print a right-aligned triangle of asterisks () with a base of 5.
"""
rows=int(input("rows= "))
n='*'
for i in range(1, 5):
    print(" " * (rows-i) + n* i )
"""

#task 21: Iterate through a string and print each character on a new line.
"""
string=input("string: ")

for ch in string:
    print(ch)
"""

#task 22: Ask for a character and a string. Count how many times the character appears in the string.
"""
n=input("string: ")
c=input("char: ")

cnt = n.count(c)

if cnt > 0:
    print(f"{c} appears {cnt} times")
else:
    print(f"{c} not found")
"""
"""
text=input("string: ")
c=input("char: ")
cnt=0

for ch in text:
    if ch==c:
        cnt+=1
        
if cnt>0:
    print(f"{c} appears {cnt} times")
else:
    print(c, "not found")
"""

#task 23: Check if a string is a palindrome (e.g., "madam").
"""
text=input("string: ")

if text == text[::-1]:
    print(f"{text} is palidrome")
else:
    print(f"{text} is not palidrome")
"""

#task 24: Create a new string with all spaces removed from the original string.
"""
s=input("string: ")
print(s.replace(" ", ""))
"""
#task 25: Convert a string to lowercase without using built-in methods.
"""
n=input("enter: ")
res=""
for ch in n:
    asci_code=ord(ch)
    if 65<= asci_code <= 90:
        res+=chr(asci_code+32)
    else:
        res+=ch
print(f"lovercase: {res}")
"""
#task 26: Convert a string to uppercase without using built-in methods.
"""
n=input("string: ")
res=""

for ch in n:
    asci_code = ord(ch)
    if 97 <= asci_code <=122:
        res+=chr(asci_code - 32)
    else:
        res+=ch
print(res)
"""
#task 27:  count the number of words in a sentence, assuming words are separated by single spaces. 
"""
n=input("string: ")
words = n.split()
print(len(words))
"""
#task 28: Shift each character in a string forward by one letter (e.g., `a` becomes `b`, `b` becomes `c`).
"""
n=input("enter: ")
res=""
for ch in n:
    asci=ord(ch)
    res=chr(asci+1)
    print(res)
"""
#task 29: Check if a user-provided character is present in a string.
"""
tx=" i wanna be more"
n=(input("enter: "))[0]
found=False

for ch in tx:
    if ch == n:
        found = True
        break
    

if found:
    print(f"{n} is in text")
else:
    print(f"{n} is not in text")
"""

#task 30: Replace all vowels in a string with a different character, like an asterisk ().
"""
n=input("string: ")
vovels="aeouiAEOUI"

for ch in vovels:
    n=n.replace(ch, "*")
print(n)
"""
#task 31 Iterate from 1 to 100 and print the first number that is divisible by 13. Use `break` to exit the loop.
"""
for i in range(1, 101):
    if i % 13 == 0:
        print(i)
        break
"""
#task 32: Iterate from 1 to 20. If the number is a multiple of 3, skip it and continue to the next iteration.
"""
for i in range(1, 21):
    if i % 3 == 0:
        continue
    print(i)
"""

#task 33: Find and print the common divisors of two numbers entered by the user.
"""
a=int(input("a= "))
b=int(input("b= "))
limit= min(a,b)

for i in range(1, limit+1):
    if a % i==0 and b%i==0: # this finds common divisor of a and b 
        print(i) # this shows common divisors on screen
"""
#task 34: Find the smallest divisor of a number, other than 1.
"""
a=int(input("a= "))

for i in range(2, a+1):
    if a % i == 0:
        print(f"the smallest divisor is {i}")
        break
"""

#task 35: Simulate a loan repayment process. Given a principal, monthly payment, 
#and interest rate, use a `for` loop to calculate how many months it takes to pay off the loan.z
"""
principal=float(input("enter the loan amount(principial): "))
monthly_payment=float(input("enter the monthly payment: "))
annual_interest=float(input("enter annual interest (in %): "))

monthly_interest= annual_interest / 12 / 100
months=0
max_months=1000

print("\n month-by-month-repayment:")

for months in range(1, max_months+1):
    principal+=principal * monthly_interest
    principal-=monthly_payment
    

    if principal > 0:
        print(f"Month {months}: Remaining loan = {principal: .2f}")
    else:
        print(f"Months {months}: Loan fully paid")
        break
"""

#task 36: Use a `for` loop to give a user a fixed number of attempts (e.g., 5) to guess a secret number.
"""
secret_num=99424

for i in range(1, 6):
    num=int(input("enter number: "))
    if num == secret_num:
        print(f"secret num was {secret_num} right")
        break
    else:
        print(f"ERROR attemps left {5-i}")
"""
#task 37: Use a `for` loop to give a user 3 attempts to enter the correct password.

pssword = "Teo"
for i in range(1, 4):
    n=input("password: ")
    if n == pssword:
        print("you are right")
        break
    else:
        print(f"error   attemps left: {3-i}")