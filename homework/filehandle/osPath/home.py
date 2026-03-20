# exercises from offline course os, pathlib
import os
import time
#task 1: Print the current working directory using os.getcwd().
'''
print(os.getcwd())
'''
#task 2: Change the current working directory to a subfolder and verify with os.getcwd().
"""
print("current dir: ", os.getcwd())

os.chdir("./..")

print("changed dir: ", os.getcwd())

""" 
#task 3: List all files and directories in the current directory using os.listdir().
"""
print(os.listdir("./.."))

""" 
#task 4: Create a new directory named practice_dir with os.mkdir().
'''
os.mkdir("practice_dir")
'''
#task 5: Create a file inside practice_dir, then check existence using os.path.exists().
'''
print(os.path.exists("practice_dir/test.py"))
'''
#task 6: Rename the directory practice_dir to test_dir using os.rename().
'''
os.rename("practice_dir", "test_dir")
'''
#task 7: Remove a file using os.remove().
'''
os.remove("test_dir/test.py")
'''
#task 8: Remove the test_dir directory using os.rmdir().
'''
os.rmdir("test_dir")
'''
#task 9: Print os.name and explain its meaning.
'''
print(os.name)
'''
#task 10: Use os.path.join() to safely construct a path to a file named notes.txt inside a directory data/.
'''
path = os.path.join("data", "note.txt")
'''
#task 11: Split a path using os.path.split() and print its head and tail.
'''
res = os.path.split("data/note.txt")

print(res)
'''
#task 12: Extract only the file name from a full path using os.path.basename().
'''
res = os.path.basename("FILEHANDLE/osPath/home.py")
print(res)
'''
#task 13: Extract only the directory name using os.path.dirname().
'''
res = os.path.dirname("FILEHANDLE/osPath/intro.py")
print(res)
'''
#task 14: Check if a path points to a directory using os.path.isdir().
'''
print(os.path.isdir(os.curdir))
'''
#task 15: Check if a path points to a file using os.path.isfile().
'''
res = os.path.isfile("home.py")
print(res)
'''
#task 16: Create nested directories using os.makedirs("a/b/c"), then remove them.
'''
import shutil

os.makedirs("a/b/c")

time.sleep(10)

shutil.rmtree("a")
'''
#task 17: Iterate through all files in the current directory and print only .txt files.
"""
working_dir = "../files"


for item in os.listdir(working_dir):
    if item.endswith(".txt"):
        print(item)
print(os.getcwd())

os.chdir("../files")
print(os.getcwd())
""" 
#task 18: Write a script that renames all .txt files in a directory to .bak extensions.
"""
import shutil

os.chdir("../")
os.mkdir("test_dir")
os.chdir("test_dir")

for i in range(1, 6):
    with open(f"file_{i}.txt", "x") as f:
        pass

time.sleep(10)

crd = os.curdir
for name in os.listdir(crd):
    if name.endswith(".txt"):
        old_path = os.path.join(crd, name)
        new_path = os.path.join(crd, name.replace(".txt", ".bak"))
        os.rename(old_path, new_path)

time.sleep(10)

os.chdir("..")
shutil.rmtree("test_dir")

""" 
#task 19: Create a function that prints the absolute path of every file in a directory tree using recursion and os.listdir().
"""
def abcgiver(path):
    for i in os.listdir(path):
        full_path = os.path.join(path, i)
        
        if os.path.isfile(full_path):
            print(os.path.abspath(full_path))
        
        if os.path.isdir(full_path):
            print(abcgiver(full_path))

abcgiver(os.curdir)
""" 
#task 20: Use os.curdir and os.pardir to navigate relative to the current working directory.
"""
print(os.getcwd())

fdir = os.pardir

os.chdir(fdir)
print(os.getcwd())

"""  
#task 21: Print the current working directory using Path.cwd().
"""
from pathlib import Path 

print(Path.cwd())

""" 
#task 22: Print your home directory using Path.home().
"""
from pathlib import Path

print(Path.home())
""" 
#task 23: Check if a file example.txt exists using Path.exists().
"""
from pathlib import Path

res = Path.exists("example.txt")
print(res)
print(Path.cwd())

""" 
#task 24: Create a directory temp_data using Path.mkdir().
"""
from pathlib import Path

Path.mkdir("temp_data")

""" 
#task 25: Write “Hello, World!” to temp_data/greeting.txt using Path.write_text().
'''
from pathlib import Path

p = Path("temp_data")

file_path = p / "greeting.txt"

file_path.write_text("Hello , World")

''' 
#task 26:  Read the contents of that file using Path.read_text().
"""
from pathlib import Path

p = Path("temp_data/greeting.txt")
print(p.read_text())
print(type(p))
""" 
#task 27: Rename greeting.txt to welcome.txt using Path.rename().
"""
from pathlib import Path

p = Path("temp_data/greeting.txt")
p.rename(p.with_name("welcome.txt"))
p.rename("temp_data/welcome.txt")

""" 
#task 28: Delete welcome.txt using Path.unlink().
'''
from pathlib import Path

p = Path("temp_data/welcome.txt")
if p.exists():
    p.unlink()

''' 
#task 29: Iterate through the current directory using Path.iterdir() and print names of all items.
'''
from pathlib import Path

p = Path(".")

for i in p.iterdir():
    print(i.name)

''' 
#task 30: Use Path.glob("*.py") to list all Python files in the current directory.
'''
from pathlib import Path

p = Path(".")

for f in p.glob("*_data"):
    print(f)

'''
#task 31: Use Path.rglob("*.py") to list all Python files recursively.
'''
from pathlib import Path

p = Path(".")


for f in p.rglob("*.txt"):
    print(f)
'''
#task 32: Print the .suffix, .stem, and .name of a file path.
'''
from pathlib import Path

p = Path("home.py")
pr = 12
print(p.suffix)
print(p.stem)
print(p.name)

'''
#task 33: Join two paths using Path.joinpath().
'''
from pathlib import Path

p = Path("files")

full_path = p / "rev.py"

print(full_path)


#task 34: Print the parent of a given path.

print(full_path.parent)

''' 
#task 35: Print all parts of a path using Path.parts.
'''
from pathlib import Path

p = Path("os.Path")
print(p.parts)

''' 
#task 36: Combine Path.is_dir() and Path.is_file() to count how many files and directories exist in the current folder.
'''
from pathlib import Path

cnt_file = 0
cnt_dir = 0

p = Path(".")   

for item in p.iterdir():
    if item.is_file():
        cnt_file+=1
    elif item.is_dir():
        cnt_dir+=1

print(f"directories: {cnt_dir}, files: {cnt_file}")

'''
#task 37: Write a function that deletes all .log files in a folder using pathlib.
'''
import time
from pathlib import Path

p = Path("temp_data")
p.mkdir(exist_ok=True)

for i in range(1, 6):
    with open(f"{p}/files_{i}.log", "w") as f:
        f.write(f"log_{i}\n")

time.sleep(3)

for item in p.iterdir():
    if item.is_file() and item.suffix == ".log":
        item.unlink()
''' 
#task 38: Write a recursive script using Path.rglob() that finds all .txt files and prints their absolute paths.
'''
from pathlib import Path

p = Path(__file__).parent

filehandle = p.parent

files_dir = filehandle / "files"

for i in files_dir.rglob("*.txt"):
    print(i.resolve())

''' 
#task 39: Implement a backup script: copy all .txt files from current directory to a new directory backup/ using pathlib.

from pathlib import Path

p = Path(".")

files_dir = None

for i in range(1, 6):
    with open(f"{files_dir}/files_{i}.txt", "w") as f:
        f.write(f"backup file_{i}\n")

