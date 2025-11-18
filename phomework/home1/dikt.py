#task 1: 3 ta kalit-qiymat juftligidan iborat dictionary yarat.
"""
mydict = {"name": "m5f90", "model": "bmw", "year": 2020}
print(mydict)

"""
#task 2: Kalit orqali qiymatni ol.
"""
mydict = {"name": "m5f90", "model": "bmw", "year": 2020}

print(mydict["model"])
print(mydict["year"])
print(mydict["name"])

"""
#task 3: Yangi juftlik qo‘sh.
"""
mydict = {"name": "Teo", "year": 22}
mydict["city"] = "tashkent"
print(mydict)

"""
#task 4: Kalit qiymatini o‘zgartir.
"""
mydict = {"name": "Teo", "year": 22}

mydict["name"] = "Theo"
print(mydict)

"""
#task 5: Elementni del bilan o‘chir.
"""
mydict = {"name": "Teo", "year": 22}

del mydict["year"]
print(mydict)
print(mydict.get("name"))

"""
#task 6: pop() bilan elementni olib tashlab, qiymatini chiqar.
"""
mydict = {"name": "Teo", "year": 22}
mydict.pop("year")
print(mydict)

"""
#task 7: keys(), values(), items() metodlarini alohida sinab ko‘r.
"""
mydict = {"name": "m5f90", "model": "bmw", "year": 2020}

print(mydict.values())
print(mydict.keys())
print(mydict.items())

"""
#task 8: len() bilan uzunligini top.
"""
mydict = {"name": "m5f90", "model": "bmw", "year": 2020}
print(len(mydict))

"""
#task 9: Kalit mavjudligini in operatori bilan tekshir.
"""
mydict = {"name": "m5f90", "model": "bmw", "year": 2020}

if "name" in mydict:
    print("exists")
else:
    print("does not exists")
"""
#task 10: Dictionary’ni for bilan aylanib chiq.
"""
mydict = {"name": "m5f90", "model": "bmw", "year": 2020}

for key, val in mydict.items():
    print(key, val)
"""
#task 11: 5 ta talabaning ismi va bahosidan iborat dict tuz.
"""
student = {
    "st1": {"name": "eshmat", "grade": "C"},
    "st2": {"name": "teo", "grade": "A"},
    "st3": {"name": "scott", "grade": "B"},
    "st4": {"name": "styles", "grade": "A-"},
    "st5": {"name": "Guli", "grade": "B"}
}
"""
#task 12: O‘rtacha bahoni hisobla.
"""
student = {"eshmat": 75, "toshmat": 50, "gishmat": 40, "teo": 95, "guli": 98}

s, avg = 0, 0

for key, val in student.items():
    s+=val
avg = s/len(student)
print(avg)

"""
#task 13: Eng yuqori bahoga ega talabani top.
"""
student = {"eshmat": 75, "toshmat": 50, "gishmat": 40, "teo": 95, "guli": 98}
best = ""
mx = student["eshmat"]

for key , val in student.items():
    if val > mx:
        mx = val
        best = key
        
print(f"{best} - {mx}")

"""
"""
student = {"eshmat": 75, "toshmat": 50, "gishmat": 40, "teo": 95, "guli": 98}

best = max(student, key=student.get)
print(best, student[best])

"""
#task 14: Dictionary’dagi barcha qiymatlar yig‘indisini top.
"""
student = {"eshmat": 75, "toshmat": 50, "gishmat": 40, "teo": 95, "guli": 98}
s = 0

for val in student.values():
    s+=val
print(f"sum of values {s}")

"""
#task 15: Faqat kalitlarni listga aylantir.
"""
student = {"eshmat": 75, "toshmat": 50, "gishmat": 40, "teo": 95, "guli": 98}

print(list(student.keys()))

"""
#task 16: Faqat qiymatlarni listga aylantir.
"""
student = {"eshmat": 75, "toshmat": 50, "gishmat": 40, "teo": 95, "guli": 98}
print(list(student.values()))

"""
#task 17: get() metodini sinab ko‘r, mavjud bo‘lmagan kalit bilan.
"""
student = {"eshmat": 75, "toshmat": 50, "gishmat": 40, "teo": 95, "guli": 98}
print(student.get("eshmatik", "topilmadi"))

"""
#task 18: Dictionary ichidagi dictionary (nested) yarat va ichki qiymatni ol.
"""
mydict = {
    "m1": {"model": "sera7", "capacity": 300},
    "m2": {"model": "sera8", "cap": 500}
}
print(mydict["m1"]["model"])
"""
#task 19: update() yordamida yangi elementlar qo‘sh.
"""
m = {"model": "sera7", "capacity": 300}

m.update(durability = "high")

print(m)
"""
#task 20: clear() bilan tozalab tashla.
"""
m = {"model": "sera7", "capacity": 300}
m.clear()
print(m)

"""
#task 21: 1 dan 5 gacha bo‘lgan sonlar uchun {son: son**2} dictionary yarat.
"""
ndict = {x: x**2 for x in range(6)}
print(ndict)

"""
#task 22: Faqat juft sonlar uchun kvadrat dictionary yarat.
"""
ndict = {x: x**2 for x in range(1, 11, 1) if x % 2 == 0}
print(ndict)
"""
#task 23: Ismlar ro‘yxatidan {ism: len(ism)} dict tuz.
"""
l = ["teo", "eshmat", "toshmat", "gishmat"]
ndict = {i: len(i) for i in l }
print(ndict)

"""
#task 24 Ismlar ro‘yxatidan {ism: len(ism)} dict tuz.
"""
names = ["teo", "scott", "styles", "jordan"]
mydict = {k: len(k) for k in names}

print(mydict)

"""
#task 25: String ichidagi har bir harf chastotasini hisobla.
"""
s = "i know that learning for someone is hard"

md = {}

for ch in s:
    if ch in md:
        md[ch]+=1
    else:
        md[ch] = 1
print(md)

"""
#task 26: 2 ta dictni birlashtir (| yoki update()).
"""
m1 = {"teo": 1, "scott": 2}
m2 = {"python": 3, 4: "is"}

#m1.update(m2)
#print(m1)
print(m1 | m2)

"""
#task 27: Dict ichidagi qiymatlarni max() orqali top.
"""
mydict = {"apple": 3, "banana": 4, "orange": 7, "laptop": 8}

max_key = max(mydict, key = mydict.get)

print(f"{max_key}, {mydict[max_key]}")

"""
#task 28: Foydalanuvchidan kalit va qiymat kiritib, dictga qo‘shuvchi kod yoz.
"""
mydict = {}

key = input("enter key: ")
value = input("enter value: ")
mydict[key] = value

print(mydict)

"""
#task 29: Barcha kalitlarni alfavit tartibida chiqar. 
"""
mydict = {"apple": 3, "banana": 4, "orange": 7, "laptop": 8}

for key in sorted(mydict):
    print(key)
"""
"""
mydict = {"apple": 3, "banana": 4, "orange": 7, "laptop": 8}
ndict = {k: sorted(k) for k in mydict}
print(ndict)

"""
#task 30: Tuple kalitli dictionary yarat ({('A',1):'Alpha'} misolida).
"""
mydict = {("teo,"): 22, (77,): 33, ("eshmat,"): 19}

print(mydict)

"""
