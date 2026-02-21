#=============FILE HANDLING==================

"""
with open("files/word.txt", "r") as f:
    content = f.read()
    print(content)

""" 
"""
with open("files/ismlar.txt", "w") as f:
    for _ in range(3):
        f.write("Hello World\n")
print(f.closed)

""" 

