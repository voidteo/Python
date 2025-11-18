#task 1: 5 ta elementdan iborat set yarat.
"""
myset = {1 , "orange", "apple", "banana", "teo"}
print(myset, type(myset))
"""
#task 2: Takrorlanuvchi element qo‘shib, set qanday ishlashini kuzat.
"""
myset = {1, 1, 2, "teo", "teo", "apple", "engine", "system"}

print(myset)

"""
#task 3: Element qo‘sh (add()).
"""
myset = {1, 2, "teo"}

myset.add("apple")

print(myset)

"""
#task 4: Bir nechta element qo‘sh (update()).
"""
myset = {1, 2, 3}
myset.update(["teo", "theo", "styles"])

print(myset, type(myset))
""" 
#task 5: Element o‘chir (remove()).
"""
myset = {1, 1, 2, "teo", "teo", "apple", "engine", "system"}

myset.remove("teo")
print(myset)

"""
#task 6: Yo‘q elementni discard() bilan o‘chir (xato bermasligi uchun).
"""
myset = {1, 1, 2, "teo", "teo", "apple", "engine", "system"}

myset.discard("theo")
print(myset)

"""
#task 7: Set uzunligini top.
"""
myset = {1, 1, 2, "teo", "teo", "apple", "engine", "system"}
print(len(myset))

"""
#task 8: Setni bo‘shat (clear()).
"""
myset = {1, 1, 2, "teo", "teo", "apple", "engine", "system"}
myset.clear()
print(myset)

""" 
#task 9: in operatori bilan element mavjudligini tekshir.
"""
myset = {1, 1, 2, "teo", "teo", "apple", "engine", "system"}
print("moon" in myset)

"""
#task 10: Setni for bilan aylanib chiq.
"""
myset = {1, 2, "teo", "apple", "engine", "system"}

for i in myset:
    print(i)
"""
#task 11: Ikki set yaratib, ularning kesishmasini (intersection()) top.
"""
myset = {"teo", "theo"}
yourset = {"system", "engine"}
c = myset.intersection(yourset)
print(c)

"""
#task 12: Birikmasini (union()) top.
"""
myset = {"teo", "theo"}
yourset = {"system", "engine"}

c = myset.union(yourset)
print(c)

"""
#task 13: Farqini (difference()) top.
"""
myset = {"teo", "theo"}
yourset = {"system", "engine"}
c = myset.difference(yourset)
print(c)

"""
#task 15: Bir set ikkinchisining ichida bor-yo‘qligini (issubset()) tekshir.

#task 17: Setni listga aylantir.
"""
myset = {1, 2, 3, 4}

l = list(myset)
l[0] = 7
myset = set(l)
print(myset)

"""
#task 18: Listdagi takroriy elementlarni set yordamida olib tashla.
"""
l = [1, 2, 3, 3, 1, 3, 2, "teo", "teo"]
print(list(set(l)))
"""
#task 19: Set comprehension orqali 1 dan 10 gacha kvadratlarni hosil qil.
"""
myset = {1, 2, 2, 2, 4, 4, 3, 3, 6, 6}

nset = {i**2 for i in myset}
print(nset)

"""
#task 20: Bo‘sh set yaratishning to‘g‘ri usulini yoz (va set() bilan {} farqini tushun).

mset = set()
print(mset)