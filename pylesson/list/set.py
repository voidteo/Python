#task 1: {1,2,3,3,2,1} → takrorlarni olib tashla.
"""
st = {1, 2, 3, 3, 2, 1,}
print(st) """
# task 2: fruits = {"apple", "banana"} → "cherry" qo‘sh.
"""
fruits = {"apple", "banana"}
fruits.add("cherry")
print(fruits)
"""
#task 3: "orange" bor yoki yo‘qligini tekshir.
"""
fruits = {"apple", "banana"}
print("orange" in fruits)
"""
# task 4: Foydalanuvchidan 3 ta meva nomi olib setga joyla.
"""
myset = set()
for i in range(3):
    n = input("Enter: ")
    myset.add(n)
print(myset)
"""
#task 5: 2 ta setni birlashtir.
"""
myset1 = {1, 2, 3, 4}
myset2 = {5, 6, 7, 8}
myset1.update(myset2) # it adds myset2 to myset1
print(myset1)
"""
#task 6: 2 ta setning kesishmasini top.
"""
st1 = {1, 2, 3, 4, }
st2 = {2, 3, 5, 6, 7}
print(st1.intersection(st2))
"""
#task 7: 2 ta setning farqini top.

st1 = {1, 2, 3, 4, }
st2 = {2, 3, 5, 6, 7}
print(st1.difference(st2))