#THIS IS EXERCISES FROM TRY EXCEPT FROM OFFLINE PYTHON COURSE.....

#task 1: Write a program that divides two numbers input by the user and handles ZeroDivisionError and ValueError.
"""
try:
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    
    print(a / b)
except ZeroDivisionError:
    print("you cannot devide by zero!")
except ValueError:
    print("you cannot enter different types!")
    
""" 
#task 2: Create a function that takes a list of integers and returns their inverses, skipping zeros using exception handling.
"""
def inverter(l: list[int])-> list:
    res = []
    for i in l:
        try:
            inv = 1 / i
            res.append(inv)
        except ZeroDivisionError:
            continue
    return res

print(inverter([1,2,0,34,0]))

""" 
#task 3: Int Conversion: Prompt for a string and try to convert it to an integer; catch the ValueError.
"""
risky_code = "str_to_int"

try:
    print(int(risky_code))
except ValueError:
    print("you cannot change this to int")

""" 
#task 4: List Indexer: Create a list of 3 items. Ask the user for an index and catch IndexError.
"""
fruit = ["apple", "banana", "orange"]
user = int(input("Enter index of thing you want: "))

try:
    print(fruit[user])
except ValueError:
    print("you can only enter numbers")
except IndexError:
    print("there is no such index , you are out of range")
    
""" 
#======================================================================================================================================#

#task 1: Write a program that asks for a number and prints 10 / number.
"""
try:
    number = int(input("enter a number: "))

    print(10/ number)
except ZeroDivisionError:
    print("you can't devide by zero")
except ValueError:
    print("you cant devide two different types")
    
""" 
#task 3: Write a function that converts a string to int. If it fails, return None instead of crashing.
"""
def converter(s: str)->int:
    try:
        res = int(s)
        return res
    except Exception as e:
        print(f"Error {e}")
    
res = converter("rura")
print(res)

""" 
#task 4: Loop through a list of strings and convert each to int. Skip the ones that raise an exception.
"""
l = ["rura", "1", "2", "3", "teo", "reo"]
res = []

for i in l:
    try:
        res.append(int(i))
    except ValueError:
        continue
print(res)

""" 
#Task 5: Ask the user for two numbers and divide them. Use two separate except blocks.
"""
try:
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    
    print(a / b)
except ZeroDivisionError:
    print("you can't devide number by zero")
except ValueError:
    print("you can't enter str , you can only enter int")
    
""" 
#task 6: Catch an exception and print the exception message.
"""
try:
    a = "s"
    print(int(a))
except ValueError as v:
    print(v)
""" 
#task 7: What happens if you put code after the failing line inside try? Demonstrate this with a print.
"""
try:
    a = "s"
    print(int(a))
    print(5+5)
except ValueError as v:
    print(v)
""" 
#task 8: Rewrite a small program where try is too large, then refactor it so try is minimal.
"""
try:
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    print("task has been started!")
    res = a / b
    print(res)
    print("task has been finished")
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("zerodevisionerror")


print("task has been started!")

try:
    a = int(input("enter a number: "))
    b = int(input("enter a number: "))
    res = a / b
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("ZeroDivisionError")
else:
    print(res)

print("task has been finished")

""" 
#task 9: Handle division in a loop so that one failure does not stop the loop.
"""
l = ["a", 0, 4, 6, 20, 0, 10, "ax", "."]
divisor = 0

for i in l:
    try:
        res = i / divisor
    except ZeroDivisionError as z:
        print(z)
    except TypeError as t:
        print(t)
    else:
        print(res)

""" 
#task 10: Explain (in comments) why this is bad practice:
"""
except:
    pass

""" 
#task 11: Write a program that prints “Success” only if no exception occurs.
"""
try:
    a = "5"
    print(int(a))
except ValueError:
    print("str cannot be converted into int")
else:
    print("success")

""" 
    #task 12: Use else to separate error logic from success logic.
""
"""
try:
    a = int(input("enter a number: "))
    res = 2003 / a
except ZeroDivisionError:
    print("nolga bolish mumkun emas!")
except ValueError:
    print("boshqa type kiritilgan , int kutyapti")
else:
    print(f"success!, answer: {res}")
 
""" 
#task 13: Write a function that opens a file, reads it, and always prints “Done” at the end.
"""
def opener(filename):
    try:
        f = open(filename, "r")
    except FileNotFoundError:
        print("file topilmadi")
    else:
        content = f.read()
        print(content)
    finally:
        print("done")

opener("hello.txt")

""" 
#task 14: Show the difference between: code inside try , code inside else

"""
if code works without error , else part also works, if error occurs except part will work
"""
#task 15:  Use finally to close a resource (file or mock resource).
"""
def opener(file):
    f = None
    try:
        f = open(file, "r")
    except FileNotFoundError:
        print("file topilmadi")
    else:
        content = f.read()
        print(content)
    finally:
        if f:
        
            f.close()
            print("file was closed successfully")
        
opener("he.txt")

""" 
#task 16: Write a loop that: tries to divide numbers, prints result if successful, prints error if not, always prints "Next number" after each iteration
"""
l = ["a", "c", 1, 2, 3, "t", 0, -6, 20, 30]

for i in l:
    try:
        res = i / 3
    except TypeError:
        print("boshqa typega bolib bolmaydi")
    else:
        print("result: ", res)
    finally:
        print("next number: ", i)

""" 
#task 17: Can finally run if you return inside try? prove it
"""
l = ["a", 3, "e", 5, -5]

for i in l:
    try:
        print(i / 1)
    except TypeError:
        print("boshqa type ga bolaolmaydi")
    except ZeroDivisionError:
        print("0 ga bolib bolmaydi")
    finally:
        print("try ichi ishlasa ishlamasayam ishlayman")
""" 
#task 18: Write a program where finally overrides a return value.
"""
def greet():
    try:
        return "try dan salom"
    except TypeError:
        print("you cannot add two different types")
    finally:
        print("finally dan salom")
    
greet()

""" 
#task 19: Catch an exception, log it, then re-raise it.
"""
try:
    a = int(input("enter a number: "))
    res = 77 // a
except Exception as e:
    print("error: ", e)
    raise
else:
    print("success: ", res)
""" 
#task 20: Explain in comments when else is better than putting code inside try.

# else : is success logic and increases readibility

#task 21: Iterate through a list and calculate inverses. Skip invalid operations using exceptions.
"""
l  = ["a", "c", 1, 2, 0, 0, 6, 0, 4]

for i in l:
    try:
        inv = 1 / i
    except TypeError:
        print("type error occured", i)
    except ZeroDivisionError:
        print("Zero devision error", i)
    else:
        print("result: ", inv)
        
""" 
#task 22: Access dictionary keys safely using exception handling.
"""
info = {
    "course": "backend",
    "duration": 8,
    "level": "from foundation",
    "language": "python"
}

try:
    res = info["level"]
except KeyError:
    print("there is no such kinda key in dict")
else:
    print(res)
    
""" 
#task 23: Parse a list of dictionaries where some keys are missing.
"""
info = [
    {"name": "teo", "age": 22, "skills": "python"},
    {"name": "reo", "age": 21, "skills": "python"},
    {"skills": "python"},
    {"name": "scott", "skills": "python"},
    {"age": 18, "skills": 'python'}
]

for i in info:
    try:
        res = [i["name"], i["age"]]
    except KeyError as e:
        print("kalit qiymatli malumot topilmadi", e)
    else:
        print(res)
        
""" 
#task 24: Write a function that sums numbers from a mixed list (int, str, None).
"""
number = ["a", 1, 2, 3, 4, 5, None, None, 6, "d", "ff"]

res = 0

for i in number:
    try:
        res+=i
        #print(res)
    except TypeError as e:
        print("cannot sum to other type", e)
print(res)

""" 
#task 25: Handle nested exceptions inside nested loops.
"""
l = [[1, "a"], [2, '2', 4, "4"], ["a", "r", 5]]

res = []
for row in l:
    for i in row:
        try:
            res.append(i ** 2)
        except TypeError as e:
            print("typeError", e)

print(res)

""" 
#task 26: Safely convert user input into a list of integers.
"""
res = []
user = input("enter a number by space: ")


for i in user.split():
    try:
        res.append(int(i))
    except ValueError as e:
        print("can't turn other type into int", e)
print(res)

""" 
#task 27: Write a function that merges two dictionaries but skips invalid entries.
"""
def merger(d1, d2):
    result = {}
    
    for d in (d1, d2):
        for k, v in d.items():
            try:
                if  not isinstance(k, str):
                    raise TypeError("key must be string here")
                if not isinstance(v, (int, float)):
                    raise ValueError("value must be integer")
                if v is None:
                    raise ValueError("value is None")
                result[k] = v
            except (ValueError, TypeError):
                continue
    return result
    
print(merger({"name": None, "age": "22","skill": "python"}, {"city": 777, "durability": 66, "age": 22}))

""" 
#task 29: Demonstrate how a single bad element can crash a program without try/except.
"""
l = [1, "a", "a", "c", 2, 4, None]
s = 0

for i in l:
    try:
        s+=i
    except Exception as e:
        print(e)
print(s)

""" 
#task 30: Type Safety: Try to add a string and an integer together; catch TypeError.
"""
def add(a, b):
    return a + b
    
try:
    res = add(5, "a")
except TypeError:
    print("you can't add int and str")
else:
    print (res)

""" 
#task 31: Input Interruption: Write a loop that catches KeyboardInterrupt (Ctrl+C) and prints "Goodbye!" instead of crashing.
"""
try:
    user = input("Enter: ")
except KeyboardInterrupt:
    print("GOODBYE!")
    
""" 
#task 32: Attribute Error: Try to call a method like .append() on a string and catch the AttributeError.
"""
word = "i will learn this one day In Shaa Allah"

try:
    print(word.append("rura"))
except AttributeError:
    print("this method exists in List not in String")
    
""" 
#task 33: Import Failure: Try to import non_existent_module and catch the ImportError.
"""
try:
    import blabla

    print(blabla.haha())
except ImportError:
    print("there is no such kind of import module")
"""
#task 34: The Catch-All: Use a generic Exception block to catch an unknown error, but print the error message using as e.
"""
l = [1, 2, None, "d", "d", "g"]

for i in l:
    try:
        res = 4 / i
    except Exception as e:
        print(e)
print(res)

""" 
#task 35: The Clean Exit: Open a file, read it, and use finally to ensure the file is closed even if a crash occurs.
"""
f = None
try:
    f = open("hello.txt", "r")
    f.read()
except FileNotFoundError:
    print("file not found")
finally:
    if f:
        f.close()
""" 

#task 36: Success Logic: Ask for a number; use the else block to square the number only if the input was valid.
"""
try:
    user = input("Enter a number: ")
    res = int(user) ** 2
except ValueError:
    print("error valueError")
else:
    print(res)

""" 
#task 37: Loop Breaker: Create a while loop that only breaks if the try block completes without an error.
"""
while True:
    try:
        user = int(input("enter a number: "))
        res = user ** 2
    except ValueError:
        print("you can't pow to another type only int")
    else:
        print("success: ", res)
        break

""" 
#task 38: Nested Try: Put a try-except inside another try block’s except clause (Error handling during error handling).
"""
person = {
    1: {"name": "teo", "age": 22, "skills": None},
    2: {"name": "reo", "age": None, "skills": "Python"},
    3: {"name": "styles", "age": 18, None: "Python"},
    4: {"name": None, "age": 23, "skills": "Go"}
}

info = {}

try:
    user = int(input("Enter a key: "))
    for k, v in person.items():
        try:

""" 
#task 39: The Calculator: Build a function that performs division but uses else to print the result and finally to print "Calculation attempted."
"""
def divcalculate():
    cnt = 0
    def calcultae(a, b):
        nonlocal cnt
        try:
            res = a / b
        except ZeroDivisionError:
            print("cannot divide by zero")
        except TypeError:
            print("typeError")
        except ValueError:
            print("you cannot enter other types ")
        else:
            print("success: ", res)
        finally:
            cnt+=1
            print("attempt: ", cnt)
    return calcultae
    
f = divcalculate()
f(2, "3")
f(4, 0)
f("r", 4)
f(4, 4)

""" 
#task 40: Math Domain: Try to calculate the square root of -1 using math.sqrt and catch the ValueError.
"""
import math

try:
    user = int(input("enter number: "))
    res = math.sqrt(user)
except ValueError:
    print("value error occured")
else:
    print("success: ", res)
    
""" 

x = "teo"
res= x.encode()
print(type(res))
print(res)

newres = res.decode()
print(type(newres), newres)

