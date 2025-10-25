"""
try:
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    
    print(a/b)
except ZeroDivisionError:
    print("you can't divide by zero")
except ValueError:
    print("please enter number only")
    
#task 2 

def invert(l: list[int]):
    res = []
    for i in range(0, len(l)):
        try:
            res.append(l[i]**(-1))
        except ZeroDivisionError:
            print(f"l[{i}] = 0 ekan, tashlab ketyapman")
            continue
    return res

print(invert([1,2,3,4,5]))
print(invert[0,0,0,0,-1,1])

""" 

#task Create a loop that reads user input until they provide a valid integer. Use exceptions to handle invalid inputs.
"""
while(True):
    try:
        n = int(input("enter number: "))
        break
    except ValueError:
        print("please enter number!")
        continue
    
""" 

k = list()