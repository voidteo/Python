#=============THIS IS EXTRA EXERCISES FOR DICT TO UNDERSTAND WELL=================

#task 1: Bo‘sh dictionary yarat va print qil.

'''
empty = {} # ductionary is a data type it is  key=value datatype
print(empty)

'''
#task 2: person nomli dictionary yarat: name, age, city.
'''
person = {"name": "Styles", "age": 22, "city": "baconhills"}
print(person)
'''
#task 3: person ichidan faqat name qiymatini chiqar.
"""
person = {"name": "Styles", "age": 22, "city": "baconhills"}
print(person["name"])
print(person.get("name"))

""" 
#task 4: person ga yangi job kalitini qo‘sh.
"""
person = {"name": "Styles", "age": 22, "city": "baconhills"}
person["job"] = "police"

print(person)

""" 
#task 5: age qiymatini o‘zgartir.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
person["age"] = 18

print(person)

""" 
#task 6: city kalitini o‘chir.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
person.pop("city")

print(person)

""" 
#task 7: name kaliti bormi — tekshir.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}

print("name" in person)

""" 
#task 8: Dictionary nechta elementdan iboratligini chiqar.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
print(len(person))

""" 
#task 9: Barcha kalitlarni alohida satrlarda chiqar.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
print(person.keys())

""" 
#task 10: Barcha qiymatlarni alohida satrlarda chiqar.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
print(person.values())
""" 
#task 11: Har bir kalit va qiymatni: key -> value formatida chiqar.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
print(person.items())

""" 
#task 12: person dictionary’dan nusxa (copy) yarat.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
p1 = person.copy()
print(p1)

""" 
#task 13: Original dict o‘zgarsa, nusxa o‘zgaradimi — tekshir.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
p1 = person.copy()

person["name"] = "allison"

print(person, p1)

""" 
#task 14: get() bilan mavjud kalitni o‘qi.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
print(person.get("name"))

""" 
#task 15: get() bilan mavjud bo‘lmagan kalitni o‘qi (default bilan).
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
print(person.get("job", "NOjob"))
""" 
#task 16: setdefault() orqali yangi kalit qo‘sh.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
person.setdefault("skill", "sarcasm")
print(person)

""" 
#task 17: setdefault() mavjud kalitda nima qilishini tekshir.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
person.setdefault("name", "allison")
print(person)

""" 
#task 18: Dictionary’ni butunlay tozalab tashla.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
person.clear()
print(person)

""" 
#task 19: Tozalangan dictionary bo‘shmi — tekshir.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}
person.clear()
print(person)

""" 
#task 20: 3 ta turli yo‘l bilan dictionary yarat.
"""
d1 = {"name": "lisa", "age": 18}
d2 = dict(name="Jenny", age=18)
d3 = dict(zip(["name", "age"], ["rura", 18]))

print(d1,d2,d3)
""" 
#task 21: Faqat kalitlarni for bilan chiqar.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}

for k in person:
    print(k)
""" 
#task 22: Faqat qiymatlarni for bilan chiqar.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}

for v in person.values():
    print(v)
""" 
#task 23: Kalit va qiymatni birga for bilan chiqar.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}

for k, v in person.items():
    print(k, ":", v)
""" 
#task 24: Qiymati int bo‘lgan elementlarni chiqar.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}

for k, v in person.items():
    if  isinstance(v, int):
        print(k, v)
""" 
#task 25: Qiymati str bo‘lgan elementlarni chiqar.
"""
person = {"name": "styles", "age": 22, "city": "baconhills"}

for k, v in person.items():
    if isinstance(v, str):
        print(k, v)
""" 
#task 26: Qiymati None bo‘lgan kalitlarni top.
"""
person = {"name": "styles", "age": 22, "city": "baconhills", "aim": None, "task": None}

for k, v in person.items():
    if v is None:
        print(k)
""" 
#task 27: Qiymati None bo‘lgan juftliklarni o‘chir.
"""
person = {"name": "styles", "age": 22, "city": "baconhills", "aim": None, "task": None}

keys_remove = []

for k, v in person.items():
    if v is None:
        keys_remove.append(k)

for k in keys_remove:
    person.pop(k)
print(person)

""" 
#task 28: Qiymati bo‘sh string ("") bo‘lganlarni o‘chir.
"""
person = {"name": "styles", "age": 22, "city": "baconhills", "aim": "", "task": ""}

keys_remove = []

for k, v in person.items():
    if v == "":
        keys_remove.append(k)

for k in keys_remove:
    person.pop(k)

print(person)

""" 
#task 29: Qiymati 10 dan katta bo‘lganlarni chiqar.
"""
rating = {"blackhat": 5, "5wave": 6, "storm": 11, "istar": 15}

for k, v in rating.items():
    if v > 10:
        print(k, v)
""" 
#task 30: Kaliti uzunligi 4 dan katta bo‘lganlarni chiqar.
"""
rating = {"blackhat": 5, "5wave": 6, "sto": 11, "iar": 15}

for k, v in rating.items():
    if len(k)> 4:
        print(k, v)
""" 
#task 31: Qiymati list bo‘lganlarni top.
"""
rating = {"blackhat": 5, "5wave": 6, "sto": ["moon"], "iar": ["nature"]}

for k, v in rating.items():
    if isinstance(v, list):
        print(k, v)
""" 
#task 32: Qiymati dictionary bo‘lganlarni top
"""
rating = {"blackhat": 5, "5wave": 6, "sto": {"man": "warrior", "aim": "fame"}, "iar": ["nature"]}

for k, v in rating.items():
    if isinstance(v, dict):
        print(k, v)
""" 
#task 33: Barcha raqamli qiymatlarning yig‘indisini hisobla.
"""
rating = {"blackhat": 5, "5wave": 6, "sto": 11, "iar": 15}
res = 0

for k, v in rating.items():
    res+=v
print(res)
"""
"""
rating = {"blackhat": 5, "5wave": 6, "sto": 11, "iar": 15}
print(sum(rating.values()))
""" 
#task 34: Eng katta qiymatni top.

#rating = {"blackhat": 5, "5wave": 6, "sto": 11, "iar": 15}

#print(max(rating.values()))
"""
max_value = None
max_key = None

for k, v in rating.items():
    if max_value is None or v > max_value:
        max_value = v
        max_key = k
print(max_key, max_value)

""" 
#task 35: Eng kichik qiymatni top.
"""
rating = {"blackhat": 5, "5wave": 6, "sto": 11, "iar": 15}

min_key = None
min_value = None

for k, v in rating.items():
    if min_value is None or v < min_value:
        min_value = v
        min_key = k
print(min_key, min_value)

""" 
#task 36: Eng katta qiymatga ega kalitni top.
"""
rating = {"blackhat": 5, "5wave": 6, "sto": 11, "iar": 15}

max_key = None
max_value = None

for k, v in rating.items():
    if max_value is None or v > max_value:
        max_value = v
        max_key = k
print(max_key)

"""
"""
rating = {"blackhat": 5, "5wave": 6, "sto": 11, "iar": 15}
print(max(rating.keys()))

""" 
#task 37: Eng kichik qiymatga ega kalitni top.
"""
rating = {"blackhat": 5, "5wave": 6, "sto": 11, "iar": 15}

min_value = None
min_key = None

for k, v in rating.items():
    if min_value is None or v < min_value:
        min_value = v
        min_key = k
print(min_key, min_value)

""" 
#task 38: Qiymatlar orasida nechta int borligini sanab chiq.
"""
rating = {"blackhat": 5, "5wave": 6, "sto": 11, "iar": 15}
cnt = 0

for v in rating.values():
    if isinstance(v, int):
        cnt+=1
print("int objects are: ", cnt)

""" 
#task 39: Qiymatlar orasida nechta str borligini sanab chiq.
"""
rating = {"blackhat": 5, "5wave": "rep", "sto": "isa", "iar": "toop"}
cnt = 0

for v in rating.values():
    if isinstance(v, str):
        cnt+=1
print(f"there are {cnt} values which are string")

""" 
#task 40: Loop ichida dictionary’ni o‘zgartirib ko‘r va xatoni tushun.
"""
rating = {"blackhat": 5, "5wave": "rep", "sto": "isa", "iar": "toop"}

for k, v in rating.items():
    rating.pop("5wave")
    print(k, v)
""" 
#task 41: 1 dan 5 gacha sonlar va ularning kvadratlaridan dictionary yarat.
"""
num = {v: v**2 for v in range(1, 6)}
print(num)

""" 
#task 42: 1 dan 10 gacha sonlar uchun even / odd dict yarat.
"""
nums = {x: "even" if x % 2 == 0 else "odd" for  x in range(1, 11)}
print(nums)

""" 
#task 43: Berilgan listdan: son -> son * 2 dict yarat.
"""
l = [1,2,3,4,5,6,7,8,9]

num = {i: i*2 for i in l}
print(num)

"""
#task  44 So‘zlar listidan: so‘z -> uzunligi dict yarat.
"""
l = ["python", "c", "learning", "not", "easy", "but", "doable"]

res = {i: len(i) for i in l}
print(res)
""" 
#task 45: Faqat juft sonlar kvadratidan dict yarat
"""
res = {i: i**2 for i in range(1, 11) if i % 2 == 0}
print(res)
""" 
#task 46: Faqat toq sonlar kubidan dict yarat.
"""
res = {i: i**3 for i in range(1, 11) if i % 2 == 1}
print(res)
""" 
#task 47: Qiymati 5 dan katta bo‘lganlarni saqlab qol.
"""
n = {1: 2, 2: 3, 3: 4, 4: 5, 5: 5, 6: 5, 7: 6, 8: 7, 8: 8, 9: 9}

res = {k: v for k, v in n.items() if v > 5}
print(res)

""" 
#task 48: String ichidagi harflar sonini sanab dict qil.
"""
word = "asynchronius"

res = {i: word.count(i) for i in word}
print(res)
""" 
#task 49: Gap ichidagi so‘zlar sonini sanab dict qil.
"""
sentence = "i started learning python i wanna have better skills"
result = sentence.split()

res = {ch: result.count(ch) for ch in result}

print(res)

""" 
#task 50: Dictionary’ni teskari qil: value -> key.
"""
mydict = {"apple": 1, "orange": 2, "banana": 3, "kiwi": 4}

res = {v: k for k, v in mydict.items()} # asosiy qism ikki nuqta tarafda

print(res)
""" 
#task 51: Bir xil value’lar bo‘lsa, listda saqla.
"""
empty = {}

mydict = {"ball": 2, "chair": 2, "phone": 2, "rura": 1, "tv": 3, "apple": 1}

for k, v in mydict.items():
    if v not in empty:
        empty[v] = [k]
    else:
        empty[v].append(k)
print(empty)

""" 
#task 52: Dictionary’ni kalit bo‘yicha sort qil.
"""
mydict = {"ball": 2, "chair": 2, "phone": 2, "rura": 1, "tv": 3, "apple": 1}

res = {k: v for k, v in sorted(mydict.items())}
print(res)

"""
#task 53: Dictionary’ni qiymat bo‘yicha sort qil.
"""
person = {"name": "styles", "age": "bob", "city": "baconhills", "aim": "ar", "task": ""}

res = {k: v for k, v in sorted(person.items(), key=lambda item: item[1])}
print(res)
""" 
#task 54: Dictionary’dan faqat kalitlar listini yarat.
"""
mydict = {"ball": 2, "chair": 2, "phone": 2, "rura": 1, "tv": 3, "apple": 1}

res = [k for k in mydict.keys()]
print(res)

""" 
#task 55: Dictionary’dan faqat qiymatlar listini yarat.
"""
mydict = {"ball": 2, "chair": 2, "phone": 2, "rura": 1, "tv": 3, "apple": 1}

res = [v for v in mydict.values()]
print(res)

""" 
#task 56: enumerate() yordamida dict yarat.
"""
l = ["rura", "west", "east", "north", "south"]
res = {k: v for k, v in enumerate(l)}
print(res)

""" 
#task 57: zip() yordamida ikki listdan dict yarat.
"""
names = ["rura", "teo", "scott", "styles"]
ages = [18, 19, 20, 22]

res = dict(zip(names, ages))
print(res)
""" 
#task 58: Nested comprehension bilan dict yarat.
"""
nested_dict = {'first':{'a':1}, 'second':{'b':2}}
float_dict = {outer_k: {float(inner_v) for (inner_k, inner_v) in outer_v.items()} for (outer_k, outer_v) in nested_dict.items()}
print(float_dict)

""" 
"""
student = {
    "st1": {"name": "rura", "age": 18, "field": "computer science"},
    "st2": {"name": "teo", "age": 19, "field": "atomic engineer"},
    "st3": {"name": "lisa", "age": 23, "field": "medicine"}
}

res = {
    outer_k: {
        inner_k: inner_v
        for inner_k, inner_v in outer_v.items()
        if inner_k == "name"
    }
    for outer_k, outer_v in student.items()
}
""" 
#task 59: Dictionary ichidan yangi filtered dict yarat.
"""
student = {
    "st1": {"name": "rura", "age": 18, "field": "computer science"},
    "st2": {"name": "teo", "age": 19, "field": "atomic engineer"},
    "st3": {"name": "lisa", "age": 23, "field": "medicine"}
}

res = {
    outer_k: {inner_k: inner_v for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in student.items()
    if outer_v["age"] > 18
}

print(res)

""" 
#task 60: Bir dictdan boshqa dict yasab ko‘r.
"""
person = {"name": "rura", "age": 18, "skill": "math", "city": "baconhills"}

res = {k: v for k, v in person.items() if k == "age" and v > 18}

print(res)

""" 
#task 61: Barcha qiymatlar unique ekanini tekshir.
"""
person = {"name": "rura", "age": "18", "skill": "math", "city": "baconhills"}

values = list(person.values())

if len(values) == len(set(values)):
    print("dict is unique")
else:
    print("dict is not unique")

""" 
# solution number 2
"""
person = {"name": "rura", "age": "18", "skill": "math", "city": "baconhills"}

seen = []
unique = True

for v in person.values():
    if v in seen:
        unique = False
        break
    else:
        seen.append(v)

if unique:
    print("dict is unique")
else:
    print("dict is not unique")
""" 
#task 62: Eng katta qiymatli juftlikni top.
"""
mydict = {"ball": 2, "chair": 2, "phone": 2, "rura": 1, "tv": 3, "apple": 1}

max_value = None
max_key = None

for k, v in mydict.items():
    if max_value is None or v > max_value:
        max_key = k
        max_value = v
print(max_key, max_value)

k, v = max(mydict.items(), key=lambda item: item[1])
print(k, v)

""" 
#task 63: Eng kichik qiymatli juftlikni top.
"""
mydict = {"ball": 2, "chair": 2, "phone": 2, "rura": 1, "tv": 3, "apple": 1}

k, v = min(mydict.items(), key=lambda item: item[1])
print(k, v)

min_value = None
min_key = None

for k, v in mydict.items():
    if min_value is None or v < min_value:
        min_value = v
        min_key = k
print(min_key, min_value)

""" 
#task 64: Ikkita dictionary’ni bittaga birlashtir.
"""
dict1 = {"name": "rura", "age": 18}
dict2 = {"city": "dubai", "skill": "DevOp"}

res = dict1 | dict2
print(res)

""" 
#task 65: Bir xil kalitlar bo‘lsa, qiymatlarini qo‘sh.
"""
dict1 = {"d": 1, "a": 6, "e": 4}
dict2 = {"a": 1, "b": 2, "c": 3}

res = {}

for k in dict1 | dict2:
    res[k] = dict1.get(k, 0) + dict2.get(k, 0)
print(res)

""" 
#task 66: Dictionary ichidan ma’lum kalitlarni o‘chir.
"""
d1 = {"apple": 5, "strawberry": 1, "banana": 3, "kiwi": 3, "grape": 2}

res = {k: v for k, v in d1.items() if len(k)>5}

print(res)

""" 
#task 67: Function yoz: dict qabul qilsin va statistik qaytarsin.
"""
def static_data(d: dict)->dict:
    values = list(d.values())

    return {
        "total_items": len(d),
        "max_value": len(d.values()),
        "min_value": len(d.values()),
        "average": sum(values) / len(values),
        "unique_values": len(set(values))   
    }

res = d = {
    "name": "rura",
    "age": 18,
    "skill": "devop",
    "grade": "rura"
}
print(res)

""" 
#task 68: Qiymatlari faqat int bo‘lgan yangi dict yarat.
"""
d1 = {"python": 1, "c": 2, "mysql": "4", "fast": 4}

res = {k: v for k, v in d1.items() if isinstance(v, int)}

print(res)

""" 
#task 69: Qiymatlari faqat str bo‘lgan yangi dict yarat.
"""
d1 = {"python": "good", "c": 2, "mysql": "4", "fast": "framework"}

res = {k: v for k, v in d1.items() if isinstance(v, str)}

print(res)
""" 
#task 70: Dictionary ichida search qil.
"""
person = {"name": "haydar", "age": 22, "skill": "backend", "city": "tashkent", "is_hacker": True}

print("name" in person) # it searches according to the key

if "age" in person:
    print(person.get("age", None))

print("tashkent" in person.values())

for k, v in person.items():
    if k == "age" and v == 22:
        print("topildi")

for k, v in person.items():
    if v == 22:
        print(k)

""" 
#task 71: Nested dictionary bilan ishlash.
"""
student = {
    "st1": {"name": "rura", "age": 18, "major": "medical-surgary", "grade": 88},
    "st2": {"name": "lisa", "age": 19, "major": "architect", "grade": 77},
    "st3": {"name": "haydar", "age": 22, "major": "computer science", "grade": 90},
    "st4": {"name": "eshmat", "age": 21, "major": "software engineer", "grade": 66}
}
print(student)
""" 
#task 72: Nested dictionary’dan ma’lumot chiqar.
"""
student = {
    "st1": {"name": "rura", "age": 18, "major": "medical-surgary", "grade": 88},
    "st2": {"name": "lisa", "age": 19, "major": "architect", "grade": 77},
    "st3": {"name": "haydar", "age": 22, "major": "computer science", "grade": 90},
    "st4": {"name": "eshmat", "age": 21, "major": "software engineer", "grade": 66}
}

res = {outer_k: {inner_k: inner_v for inner_k, inner_v in outer_v.items()} for outer_k, outer_v in student.items()}

print(res)

""" 
#task 73: Nested dictionary’ga yangi element qo‘sh.
"""
student = {
    "st1": {"name": "rura", "age": 18, "major": "medical-surgary", "grade": 88},
    "st2": {"name": "lisa", "age": 19, "major": "architect", "grade": 77},
}

student["st3"] = {"name": "haydar", "age": 22, "major": "Computer-sc", "grade": 88}

for v in student.values():
    v["active"] = True

print(student.get("st1").get("active"))

print(student["st1"]["active"])

""" 
#task 74: Har bir nested element uchun o‘rtacha hisobla.
"""
student = {
    "st1": {"math": 60, "physics": 55, "english": 88},
    "st2": {"math": 65, "physics": 60, "english": 93},
    "st3": {"math": 90, "physics": 95, "english": 100}
}

for key , val in student.items():
    avg = sum(val.values()) / len(key)
    print(key, round(avg, 2))

print(len(student["st1"]))

""" 
#task 75: Dictionary validatsiya qil (bo‘sh emasmi).
"""
person = {
    "name": "rura", "age": 18, "city": "tashkent", "field": "computer science"
}

if person:
    print("False")
else:
    print("True")
""" 
#task 76: Dictionary’dagi xatoli ma’lumotlarni tozalash.
"""
person = {
    "name": "rura", "age": 18, "city": None, "field": "computer science", "aim": ""
}

clean = {k: v for k, v in person.items() if v is not None and v != ""}

print(clean)

""" 
#task 77: API response ko‘rinishidagi dict bilan ishlash.
"""
api = {
    "status": "success",
    "data": {
        "products": [
            {"name": "phone", "price": 500},
            {"name": "laptop", "price": None},
            {"name": "", "price": 300}
        ]
    }
}

products = api["data"]["products"]
invalid_products = []

for p in products:
    if not p["name"] or p["price"] is None:
        invalid_products.append(p)

print("xatoli productlar: ")
print(invalid_products)

valid_products = []

for p in products:
    if p["name"] and isinstance(p["price"], int):
        valid_products.append(p)
        
print(f"togri produktlarl: {valid_products}")

""" 
#task 78: 