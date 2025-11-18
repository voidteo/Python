#task 5: 5. **Multiples of 5:** Print all multiples of 5 less than or equal to 50.
"""
i = 5
while i <= 50:
    print(i)
    i+=5
    
"""
#task 6: 6. **User Input Loop:** Prompt the user to enter a number and keep asking until they enter 0.
"""
while True:
    n = int(input("enter specific number: "))
    if n == 0:
        break
""" 
#task 7: 7. **Positive Numbers Only:** Ask the user for a number. If it's negative, ask again. Keep asking until a positive number is entered.
"""
while True:
    n = int(input("enter number: "))
    if n > 0:
        break
    else:
        print("requirements aren't met")
""" 
#task 8: 8. **Secret Number:** Use a `while` loop to let the user guess a secret number (e.g., 7). Print "Too high!" or "Too low!" until they guess correctly.
"""
while True:
    secret = int(input("enter secret number (1 - 100): "))
    
    if secret > 100 or secret < 1:
        print("you should enter (1 - 100)")
        continue
    break
      
while True:     
    guessed = int(input("enter number you think: "))
    if guessed > secret:
        print("too high")
    elif guessed < secret:
        print("too low")
    else:
        print("you are right", guessed, secret)
        break      
""" 
#task 9: *Simple Calculator:** Use a loop to perform simple calculations. Ask the user for two numbers and an operator (+, -, *, /). Print the result. Continue #until the user enters 'q' to quit.
"""
while True:
    a = int(input("enter number: "))
    b = int(input("enter number: "))
    c = input("enter operator('+', '-', '/', '*') or q: ")
    res = 0
    if c == "q":
        print("good bye")
        break
    if c == "+":
        res = a + b
        print(res)
    elif c == "-":
        res = a - b
        print(res)
    elif c == "*":
        res = a * b
        print(res)
    elif c == "/":
        if a < 0:
            print("a cant be smaller than zero")
        else:
            print(a / b)
    else:
        print("you entered invalid sign")
        
""" 
#task 10: 10. **Password Check:** Prompt the user for a password. Use a `while` loop to give them **three attempts**. If they get it right, print a success #message. If not, print a failure message.
"""
psword = "teo77"
i = 0
attemps = 3

while i < attemps:
    n = input("enter password: ")
    i+=1
    if n == psword:
        print("welcome")
        break
    else:
        remaining = attemps - i
        if remaining > 0:
            print("failure! attemps: ", remaining)
        else:
            print("too many wrong attemps! access danied")
""" 
#task 11:  **Sum of First 10 Numbers:** Use a `while` loop to calculate the sum of the numbers from 1 to 10.
"""
sm, i = 0, 0

while i <= 10:
    sm+=i
    i+=1
print(f"sum is {sm}")

""" 
#task 12: 2. **Average of 5 Numbers:** Prompt the user to enter five numbers and calculate their average using a `while` loop.
"""
i = 1
avg = 0
sm = 0

while i <= 5:
    n = int(input(f"enter number{i}: "))
    sm+= n
    i+=1
avg = sm / 5
print(avg)

""" 
#task 13:   3. **Factorial:** Calculate the factorial of a number entered by the user. (e.g., 5! = 5 * 4 * 3 * 2 * 1)
"""
i = 1
fact = 1
n = int(input("enter number: "))

while i <= n:
    fact*=i
    i+=1
print(fact)

""" 
#task 14: 4. **Count Digits:** Count the number of digits in an integer entered by the user.
"""
n = int(input("enter number: "))

i = 0
cnt = 0

while n > i:
    n = n // 10
    cnt+=1
print(cnt)

""" 

#task 15: 5. **Reverse a Number:** Reverse a number entered by the user (e.g., 123 becomes 321).
"""
n = int(input("enter number you want reverse: "))
rev = 0

while n > 0:
    digit = n % 10 # oxirgi sonni olib tashlash
    rev = rev * 10 + digit # teskari sonni qurish 
    n = n // 10 #oxirgi raqamni olib tashlash
    
print("reversed number is: ", rev)

""" 
#task 16: 6. **Sum of Digits:** Calculate the sum of the digits of a number entered by the user.
"""
n = int(input("enter number: "))
sm = 0

while n > 0:
    digit = n % 10
    sm+=digit
    n = n // 10
    
print("sum of digits : ", sm)

""" 
#task 17:7. **Greatest Common Divisor (GCD):** Find the GCD of two numbers using the Euclidean algorithm with a `while` loop.
"""
a = int(input("enter a: "))
b = int(input("enter b: "))
""" 

#while b != 0:
#   a, b = b, a % b
    
#print("gcd is ", a)
"""
while b != 0:
    temp = a # a ni yuqotib qoymaslik uchun
    a = b 
    b = temp % b
print("gcd is ", a)

""" 
#task 18: 8. **Fibonacci Sequence:** Print the first 10 numbers of the Fibonacci sequence (0, 1, 1, 2, 3...).
"""
count = 0
a, b = 0, 1

while count <= 10:
    print(a)
    a, b = b, a + b
    count+=1
""" 
#task 19: 9. **Triangle Perimeter:** Ask the user for three lengths. Check if they can form a valid triangle using `if` statements (sum of any two sides must be #greater than the third). Keep asking
"""
while True:
    a = float(input("enter a: "))
    b = float(input("enter b: "))
    c = float(input("enter c: "))
    
    if a + b > c and a + c > b and c + b > a:
        print("this sides can create triangle!")
        break
    else:
        print("this sides cannot create triangle !!! ")
""" 
#task 20: Bank Account:** Simulate a simple bank account. Start with a balance of $100. Use a `while` loop to let the user deposit or withdraw money. The loop should #stop if the balance drops below $0.
"""
balance = 100
choice = None

while balance >= 0 and choice != "4":
    print("\n====Bank Account==== ")
    print("1. Deposit money")
    print("2. Withdraw money")
    print("3. Show balance")
    print("4. Exit")
    
    choice = input("choose option (1-4): ")
    
    if choice == "1":
        amount = float(input("enter amount to deposit: "))
        balance+=amount
        print("deposited: ", amount)
    elif choice == "2":
        amount = float(input("enter amount to withdraw: "))
        balance-=amount
        print("withdrawed amount: ", amount)
        if balance < 0:
            print("the balance below 0 , account overdrawn!")
    
    elif choice == "3":
        print("current balance: ", balance)
    elif choice == "4":
        print("exiting....")
    else:
        print("invalid chocie !!!, try again")
""" 
#task 21: 1. **Count Vowels:** Count the number of vowels (a, e, i, o, u) in a string entered by the user.
"""
st = input("enter string: ")
i, cnt = 0, 0 # boshlanish
vovel = "aeiou"

while i < len(st):  # shart
    if st[i].lower() in vovel:
        cnt+=1
    i+=1 # ozgarish
print(cnt)

""" 
#task 22: 2. **Count Consonants:** Count the number of consonants in a string.
"""
st = input("enter string: ")
i, cnt = 0, 0
vovel = "aeiouAEIOU"

while i < len(st):
    if st[i].isalpha() and st[i] not in vovel:
        cnt+=1
    i+=1
print(cnt)

""" 
#task 23: 3. **String Reversal:** Reverse a string entered by the user.
"""
st = input("enter string: ")
rev = ""
i = len(st)-1

while i >= 0:
    rev+=st[i]
    i-=1
print(rev)

""" 
#task 24: 4. **Palindrome Checker:** Check if a string is a palindrome (reads the same backward as forward).
"""
st = input("enter string: ")
rev = ""
i = len(st)-1

while i >= 0:
    rev+=st[i]
    i-=1

if rev == st:
    print("string is palidrome !")
else:
    print("string is not palidrome")
""" 
#task 25: 5. **Remove Whitespace:** Remove all spaces from a string entered by the user.
"""
st = input("enter string: ")
res = ""
i = 0

while i < len(st):
    if st[i] != " ":
        res+=st[i]
    i+=1
print(res)

""" 
#task 26: 6. **First Vowel:** Find the index of the first vowel in a string.
"""
st = input("enter string: ")
vovel = "aioueAIEOU"
i = 0

while i <= len(st):
    if st[i] in vovel:
        print(f"the first vovel in string <{st[i]}> index: {i}")
        break
    i+=1
""" 
#task 27: 7. **Character Counter:** Count how many times a specific character (e.g., 'a') appears in a string.
"""
st = input("enter string: ")
ch = input("enter charachter you wanna count: ")
cnt , i = 0, 0

while i < len(st):
    if ch == st[i]:
        cnt+=1
    i+=1
print(cnt)

""" 
#task 28: 8. **String Truncation:** Ask the user for a string and a maximum length. Truncate the string if it's longer than the max length, adding "..." to the end.
"""
st = input("enter string: ")
max_len = int(input("enter max length: "))
i = 0
newst = ""

while i < len(st) and i < max_len:
    newst+=st[i]
    i+=1
    
if len(st) > max_len:
    newst+= "...."
print(newst) 

""" 
#task 29: 9. **Basic Encryption:** Shift each character in a string forward by one letter (a->b, b->c, etc.).
"""
st = input("enter string: ")
i = 0
newst = ""

while i < len(st):
    ch = st[i]
    if "a" <= ch <= "z" or "A" <= ch <= "Z":
        newst+=chr(ord(ch)+3)
    else:
        newst += ch
    i+=1
print(f"original: {st}, made: {newst}")

""" 
#task 30: 10. **Simple Search:** Check if a substring exists within a larger string.

