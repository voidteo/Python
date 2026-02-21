#task 1: Create and Write: Create a new file and write your name to it.
"""
f = open("files/names.txt", "w")

f.write("My name is Scott")

f.close()

""" 
#task 2: Read Entire File: Read and display the entire content of a file.
"""
f = open("files/names.txt", "r")
content = f.read()
print(content)
f.close()

""" 
#task 3: Append Text: Append a line of text to an existing file.
"""
f = open("files/names.txt", "a")

f.write("\nScott where is styles?")

f.close()

""" 
#task 4: Count Lines: Count the number of lines in a file.
"""
f = open("files/names.txt", "r")

line = f.readlines()

print(len(line))

f.close()

""" 
#task 5: Count Words: Count the number of words in a file.
"""
f = open("files/names.txt", "r")

cont = f.readlines()
word_count = 0

for i in cont:
    words = i.split()
    word_count+=len(words)
print(word_count)

f.close()

""" 
#task 6: Count Characters: Count the number of characters in a file
"""
f = open("files/names.txt", "r")

content = f.readlines()
char_count = 0

for i in content:
    char_count+=len(i)
print(char_count)
f.close()

""" 
#task 7: Copy File: Create a copy of a file with a different name.
"""
f = open("files/names.txt", "r")

content = f.read()

f.close()

f_copy = open("files/intro.txt", "w")

res = f_copy.write(content)

print(res)

f_copy.close()

""" 
#task 8: Display with Line Numbers: Display file content with line numbers.
"""
f = open("files/intro.txt", "r+")

content = f.readlines()
line_number = 1

for line in content:
    print(line_number, ":", line.strip())
    line_number+=1

f.close()

""" 
#task 9: Search Word: Check if a specific word exists in a file.
"""
f = open("files/intro.txt", "r+")

#content = f.readlines()

for line in f:
    clean = line.strip().lower()
    if clean == "derek":
        print("topildi", clean)

f.close()

""" 
#task 10: Create Multiple Files: Create 5 files with names file1.txt to file5.txt.
"""
for i in range(1, 6):
    f = open(f"files/file{i}.txt", "a+")
    f.close()
""" 
#task 11:  Merge Files: Merge contents of two files into a third file.
"""
f = open("files/names.txt", "r")
content = f.read()
f.close()

f1 = open("files/intro.txt", "r")
con = f1.read()
f1.close()

f2 = open("files/myfile.txt", "w+")

mycon = f2.write(content + "\n" + con)

print(mycon)

f2.close()

""" 
#task 12: Reverse File Content: Create a new file with content reversed line by line.
"""
f = open("files/word.txt", "w+")

f.write("world is changing fast\nis ai dangerous, or we should still learn coding")
f.seek(0)

lines = f.readlines()
print(lines)

f.close()

f1 = open("reversed_w.txt", "w+")

f1.writelines(lines[::-1])
f1.seek(0)

rev_con = f1.read()
print(rev_con)

f1.close()

""" 

#task 13: Find Longest Word: Find the longest word in a file.
"""
f = open("files/word.txt", "r")

content = f.readlines()

long_word = ""

for line in content:
    word = line.split()
    for i in word:
        if len(i) > len(long_word):
            long_word = i
print(f"the longest word in file is: {long_word}")

f.close()

""" 
#task 14: Remove Empty Lines: Remove all empty lines from a file.
"""
f = open("files/word.txt", "r")

content = f.readlines()

clean_con = []

for i in content:
    if i.strip() != "":
        clean_con.append(i)
        
f.close()

f1 = open("files/word.txt", "w")

f1.writelines(clean_con)

f1.close()
""" 
#task 15: Word Frequency: Count how many times each word appears in a file.
"""
f = open("files/word.txt", "r")

cont = f.readlines()
res = {}

for i in cont:
    for j in i.split():
        if j in res:
            res[j]+=1
        else:
            res[j] = 1
print(res)

f.close()    

""" 
#task 16: Replace Word: Replace all occurrences of a word with another word in a file.
"""
f = open("files/reversed_w.txt", "r")

word = f.read()

res = word.replace("ai", "teo")

f.close()

f1 = open("files/reversed_w.txt", "w")

f1.write(res)

f1.close()

with open("files/reversed_w.txt", "r") as file:
    print(file.read())
    
""" 
#task 17: Extract Specific Lines: Extract lines containing a specific word to a new file.
"""
f = open("files/word.txt", "r")

content = f.readlines()

res = []
for i in content:
    if "coding" in i:
        res.append(i)
    else:
        continue
    
f.close()

f1 = open("files/coder.txt", "w")

f1.writelines(res)

f1.close()

with open("files/coder.txt", "r") as f2:
    print(f2.read())

""" 

#task 18: Delete File: Delete a file after confirming with user.
"""
import os

f = open("files/codor.txt", "r")

user = input("Do you want to delete file(y/n): ")

if user.lower() == "y":
    os.remove("files/codor.txt")
else:
    res = f.read()
    print(res)

""" 
#task 19: File Size: Calculate and display the size of a file in bytes.
"""
import os
f = open("files/word.txt", "r")

size = os.path.getsize("files/word.txt")
print(size)
f.close()
""" 
#task 20: Rename File: Rename a file to a new name.
"""
import os 

old_name = "files/names.txt"
new_name = input("Enter a name you want to call: ")

if not new_name.endswith(".txt"):
    new_name+=".txt"

new_path = f"files/{new_name}"

if os.path.exists(old_name):
    os.rename(old_name, new_path)
    print("rename was successfull")
else:
    print("file topilmadi!")
"""
#task 21: Sort File Content: Sort lines in a file alphabetically.
"""
f = open("files/myfile.txt", "r")

content = f.readlines()
content.sort()

f.close()

with open("files/myfile.txt", "w") as f1:
    f1.writelines(content)

""" 
#task 22: Remove Duplicate Lines: Remove duplicate lines from a file.
"""
f = open("files/myfile.txt", "r")

content = f.readlines()
res = []

for i in content:
    if i not in res:
        res.append(i)
    else:
        continue
f.close()

f1 = open("files/myfile.txt", "w")

f1.writelines(res)
f1.close()

""" 
#task 23: CSV to Text: Convert CSV data to formatted text file.

#task 24: Student Records: Create a student database file with name and marks.
"""
f = open("files/student.txt", "a")

res_st = []
n = int(input("how many students you want to join: "))
for i in range(1, n+1):
    st_name = input("Enter a name: ")
    st_grade = input("enter your grade: ")
    res = f"name: {st_name}, grade: {st_grade}\n"
    res_st.append(res)

f.writelines(res_st)    

f.close()

""" 
#task 25: Search and Replace: Search for a pattern and replace it throughout the file.
"""
f = open("files/student.txt", "r")

content = f.read()

f.close()

f1 = open("files/student.txt", "w")
res = content.replace("Teo", "Derek")

if "Teo" in content:
    f1.write(res)
else:
    print("Not Found!")
f1.close()

""" 
#task 26: Split Large File: Split a large file into smaller files of 10 lines each.
"""
f = open("files/myfile.txt", "r+")

file_count = 1
line_count = 0
out_file = None

for line in f:
    if line_count % 10 == 0:
        if out_file:
            out_file.close()

    out_file = open(f"files/part_{line_count}.txt", "w")
    file_count+=1
    
    out_file.write(line)
    line_count+=1
    
if out_file:
    out_file.close()
f.close()

""" 
#task 27: Encrypt File: Create a simple encryption (Caesar cipher) for file content.
"""
f = open("files/word.txt", "r")
shift = 3
content = f.read()

encrypted = ""

for char in content:
    if char.isalpha():
        base = ord("a") if char.islower() else ord("A")
        encrypted_char = chr((ord(char) - base + shift) % 26 + base)
        encrypted+=encrypted_char
    else:
        encrypted_char+=char
f.close()

with open("files/encrypted,txt", "w") as f:
    f.write(encrypted)

print("files encrypted successfully")

""" 
#task 28: Count Specific Character: Count occurrences of a specific character in a file.
"""
f = open("files/word.txt", "r")

content = f.read()
count = 0
target = "o"

for char in content:
    if char == target:
        count+=1

print(f"specific character {target} occures {count} times in file")
    
f.close()

""" 
#task 29: Extract Numbers: Extract all numbers from a text file.
"""
f = open("files/student.txt", "r")

content = f.readlines()

res = []

for i in content:
    for j in i.split():
        if j.isdigit():
            res.append(j)
        else:
            continue

print(f"all numbers from file: {res}")

f.close()

""" 
#task 30: Create Backup: Create a backup of a file with timestamp in filename.
"""
from datetime import datetime

now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

original_file = "files/student.txt"
backup_file = f"files/student_{timestamp}.txt"

f = open(original_file, "r")

content = f.read()

f.close()

f1 = open(backup_file, "w")

f1.write(content)

f1.close()

""" 
