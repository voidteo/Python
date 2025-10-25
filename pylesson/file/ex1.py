#task 1:  open a text file using with and print all lines
"""
with open("file2.txt", "w") as f:
    f.write("hello eshmat\n")
    
print("file closed?", f.closed)

"""
#task 2:
"""
with open("file2.txt", "w+") as f:
    f.write("hello eshmat\nhello from toshmat\nhello from toshmat")

print(f.closed)

"""
#task 3: 
"""
with open("output.txt", "r") as f, open("input.txt", "w") as l:
    l.write("hello world\n")
    f.read()
"""
#task 4: use a with block to open multiple files in a single statement
import os

print(os.name)