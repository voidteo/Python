#===========revison from file handling============

#task 1: Create a text file and write your name and age into it.
"""
with open("files/myname.txt", "w") as f:
    f.write("my name is Suliman\ni am at 22")
""" 
#task 2: Read a file and print its entire content.
"""
with open("files/word.txt", "r") as f:
    content = f.read()
    print(content)
""" 
#task 3: Read a file line by line and print each line.
"""
with open("files/word.txt", "r") as f:
    for line in f:
        print(line.strip())

""" 
#task 4: Count how many lines are in a file.
"""
with open("files/word.txt", "r") as f:
    count = 0
    for line in f:
        count+=1
    print("counts of line are: ", count)

""" 
#task 5: Count how many characters are in a file.
"""
with open("files/myfile.txt", "r") as f:
    content = f.read()
    count = 0
    for i in content:
        count+=1
    print(f"there are: {count} characters in file")
""" 
#task 6: Write 5 lines to a file using with.
"""
with open("files/risk.txt", "w") as f:
    content = f.writelines("i should change\nchange will be how\nbiohucking is real?\nrura is 18\nbelieve")
""" 
#task 7: Append a new line to an existing file. 
"""
with open("files/risk.txt", "a") as f:
    f.write("\nHello Programming")
""" 
#task 8: Read only the first line of a file.
"""
with open("files/word.txt", "r") as f:
    res = f.readline()
    print(res)
""" 
#task 9: Read only the last line of a file.
"""
with open("files/risk.txt", "r") as f:
    last_line = ""
    for line in f:
        last_line = line
    print(last_line)
    
""" 
#task 10: Copy content from one file to another.
"""
with open("files/risk.txt", "r") as f:
    content = f.read()

with open("files/intro.txt", "a") as f:
    f.write(f"\n{content}")
""" 
#task 11: Create a file only if it does not exist.
"""
import os

if not os.path.exists("files/himfile.txt"):
    with open("files/himfile.txt", "x") as f:
        print("file yaratildi")
else:
    print("file mavjud")

""" 
#task 12: Read a file and remove extra spaces from each line.
"""
with open("files/myname.txt", "r") as f:
    lines = f.readlines()
    clean_line = [" ".join(line.strip().split()) for line in lines]
    
    for line in clean_line:
        print(line)
""" 
#task 13: Write numbers from 1 to 10 into a file (one per line).
"""
with open("files/himfile.txt", "a") as f:
    for i in range(1, 11):
        f.write(str(i) + "\n")
""" 

#task 14: Read numbers from a file and print them as integers.
"""
with open("files/student.txt", "r") as f:
    content = f.read()
    res = []
    for i in content:
        if i.isdigit():
            res.append(int(i))
    print(res)
""" 
#task 15: Read a file and print lines that are not empty.
"""
with open("files/risk.txt", "r") as f:
    content = f.readlines()
    for line in content:
        if line.strip():
            print(line, end="")
""" 
#task 16: Count how many words are in a file.
"""
with open("files/student.txt", "r") as f:
    content = f.read()
    words = content.split()
    print(len(words))
""" 
#task 17: Count how many times a specific word appears in a file.
"""
target = input("enter word to search: ")

count = 0 
with open("files/risk.txt", "r") as f:
    content = f.read()
    for line in content.split():
        if line.lower() == target.lower():
            count+=1
    print(f"{target}: {count}")

""" 
#task 18: Find the longest line in a file.
"""
with open("files/intro.txt", "r") as f:
    longest_line = ""
    for line in f:
        if len(line) > len(longest_line):
            longest_line = line
    print(f"result: {longest_line}")

""" 
#task 19: Find the shortest line in a file.
"""
with open("files/intro.txt", "r") as f:
    content = f.readlines()
    shortes_line = content[0]
    for line in content:
        if len(line) < len(shortes_line):
            shortes_line = line
    print(f"result: {shortes_line}")

""" 
#task 20: Read a file and reverse each line.
"""
with open("files/intro.txt", "r") as f:
    for line in f:
        print(line.rstrip())
""" 
#task 21: Reverse the order of lines in a file.
"""
with open("files/intro.txt", "r") as f:
    content = f.readlines()
    for line in content[::-1]:
        print(line, end=" ")
""" 
#task 22: Read numbers from a file and write only even numbers to another file.
"""
with open("files/himfile.txt", "r") as f:
    content = f.readlines()
    res = []
    for line in content:
        for j in line.split():
            if j.isdigit():
                res.append(int(j))

with open("files/number.txt", "w") as f:
    ret = [i for i in res if i % 2 == 0]
    f.write(str(ret))
""" 
#task 23: Read numbers and calculate their sum.
"""
with open("files/himfile.txt", "r") as f:
    res = 0
    content = f.readlines()
    for line in content:
        for i in line.split():
            if i.isdigit():
                res+=int(i)
    print(res)

""" 
#task 24: Read numbers and calculate average.
"""
with open("files/himfile.txt", "r") as f:
    res = 0
    cnt = 0

    for line in f:
        for i in line.split():
            try:
                num = int(i)
                res+=num
                cnt+=1
            except ValueError:
                pass
                
    if cnt == 0:
        print("filedan son topilmadi")
    else:
        avg = res / cnt
    print(f"file dagi sonlarning o'rtacha qiymati: {round(avg, 2)}")

""" 
#task 25: Separate digits and letters into two different files.
"""
with open("files/himfile.txt", "r") as f:
    content = f.readlines()
    letter = []
    number = []
    for line in content:
        for i in line.split():
            if i.isdigit():
                number.append(i)
            elif i.isalpha():
                letter.append(i)
            else:
                continue

with open("files/letters.txt", "w") as f:
    f.write(str(letter))
with open("files/number.txt", "w") as f:
    f.write(str(number))

""" 
#task 26: Remove duplicate lines from a file.
"""
with open("files/myfile.txt", "r") as f:
    seen = set()
    unique_line = []
    
    for line in f:
        if line not in seen:
            seen.add(line)
            unique_line.append(line)

with open("files/myfile.txt", "w") as f:
    f.writelines(unique_line)

""" 
#task 27: Read a file and convert all text to uppercase.
"""
with open("files/intro.txt", "r") as f:
    for line in f:
        for i in line.split():
            print(i.upper(), end=" ")
        print()
""" 
#task 28: Convert all text to lowercase and save to another file.
"""
with open("files/himfile.txt", "r") as f:
    content = f.read()

with open("files/coder.txt", "a") as f:
    print(f.seek(44)) # it won't work because of mode 'a' , no matter what it appends
    print(f.tell())
    f.write(content.lower())
""" 
print("hello from Path")

#task 29: Find all lines that contain a specific character.

