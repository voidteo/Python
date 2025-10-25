"""

f = open("even.txt", "w+")

l = []
for i in range(10):
    n = int(input("Enter number: "))
    l.append(n)

for j in l:
    if j % 2 == 0:
        f.write(f"{j}\n")

f.close()

"""
"""
f = open("name.txt", "r")
lines = f.readlines()
f.close

f = open("new_name.txt", "a")

for l in lines:
    l = l[:-1]
    f.write(l[::-1]+ "\n")

f.close

"""

f = open