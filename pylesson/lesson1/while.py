"""
i=2
while(i<20):
    i+=2
    print(i)
"""

#task4:
"""
i=1
while(i<=19):
    if(i%2==1):
        print(i)
    i+=1
    
"""
"""
secret=int(input("enter secret num: "))
while(True):
    num=int(input("enter guessed num: "))
    if(num>secret):
        print("too high")
    elif (num<secret):
        print("too low")
    else:
        print(f"you are right {secret}")
        break
"""

string=input("enter string: ")
count_char=input("enter letter: ")

i=0
cnt=0
while(string[i]==count_char):
    print(i)
    cnt+=1