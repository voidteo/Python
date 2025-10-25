# task 1: student nomli dictionary yarat: "name", "age", "grade" kalitlari bilan.
#So‘ng uni ekranga chiqar.
"""
student = {"name" : "Teo", "age" : 22, "grade": "A"}

for key , val in student.items():
    print(key, ":" , val)
    
"""
#task 2: student dictionarydan faqat "name" qiymatini chiqar.
"""
student = {
    "name": "Teo",
    "age": 22,
    "grade": "A"
}
print(student["name"])
print(student.get("name"))

"""
#task 3: student["grade"] qiymatini "A+" ga o‘zgartir.
"""
student = {
    "name": "Teo",
    "age": 22,
    "grade": "A"
}

student["grade"]= "A+"
print(student.get("grade"))

"""
#task 4:student dict’ga yangi "city" kaliti qo‘shib, unga "Tashkent" qiymatini ber.
"""
student = {
    "name": "Teo",
    "age": 22,
    "grade": "A"
}

student["city"] = "tashkent"
print(student)

""" 
#task 5: student dict’dan "age" kalitini o‘chir.
"""
student = {
    "name": "Teo",
    "age": 22,
    "grade": "A"
} 

student.pop("age")
print(student)

"""

#task 6: using keys(), values(), items()
"""
person = {"name" : "Ali", "age" : 21, "city": "Tashkent"}

print(person.keys())
print(person.values())
print(person.items())

"""
#task 7: for loop orqali person ichidagi kalit va qiymatlarni
#kalit : qiymat shaklida chiqarsin.
"""
person = {
    "name": "Ali",
    "age" : 22,
    "city" : "tashkent"
}
for key , val in person.items():
    print(key, val)
"""
#task 8: Agar personda "job" kaliti bo‘lmasa, "Topilmadi" deb chiqarsin.
"""
person = {
    "name": "Ali",
    "age" : 22,
    "city" : "tashkent"
}

if "job" in person:
    print("there is")
else:
    print("there is not")
"""
#task 9: if operatori bilan "age" kaliti mavjud yoki yo‘qligini tekshir.
"""
person = {
    "name": "Ali",
    "age" : 22,
    "city" : "tashkent"
}
age = person.get("age", "not found")
print(age)

print(person.get("job", "topilmadi"))

print("topilmadi") if "job" not in person.keys() else print("bor")

""" 
#task 10: dict1 dan nusxa olib dict2ga saqla, so‘ng dict1ni tozala (clear()). dict2 o‘zgarishsiz qolsin.
"""
person1 = {"name": "Teo", "age": 22, "subject": "python"}
person2 = {}

person2 = person1.copy()
person1.clear()
print(person1, person2)

""" 
#task 11: calculating average sum of dict
"""
grades = {"Ali": 90, "Vali": 80, "Soli": 100}
sm ,avg = 0, 0

for val in grades.values():
    sm+=val
avg = sm/len(grades)

print(avg)

""" 
#task 12: Yuqoridagi dict’dan eng yuqori baho olgan o‘quvchini top.
"""
grades = {"Ali": 90, "Vali": 80, "Soli": 100}
best_student = max(grades, key= grades.get)

print(f"student who got the highest grade is {best_student} : {grades[best_student]}")

"""
#task 13: students = {
"""    "s1": {"name": "Ali", "age": 18},
    "s2": {"name": "Vali", "age": 19}
}

Keyin s1 ning ismini chop et.
"""
"""
students = {
    "s1": {"name": "Ali", "age": 18},
    "s2": {"name": "Vali", "age": 19}
}
print(students["s1"]["name"])

"""
#task 14:for loop bilan students ichidagi har bir o‘quvchining
#ismi va yoshini chiqar.
"""
students = {
    "s1": {"name": "Ali", "age": 18},
    "s2": {"name": "Vali", "age": 19}
}
for key , val in students.items():
    print(f"{key}: {val["name"]} - {val["age"]} yoshda")
""" 
#task 15: Quyidagi dict’ga "job": "developer" qo‘sh:
"""
person = {"name": "Ali", "age": 21}

person["job"] = "developer"
print(person)

"""
#task 16: Matndan har bir harf necha marta uchraganini sanaydigan
#dictionary hosil qil (masalan, "hello world" uchun).
"""
tex = "Hello world"
count = {}

for ch in tex:
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1
        
print(count)

"""
#task 17: Foydalanuvchidan 3 ta ism va yosh so‘rab, ularni dictionaryga joylashtir (ism = kalit, yosh = qiymat).
"""
person = {}

for i in range(3):
    name = input("name: ")
    age = int(input("age: "))
    
    person[name] = age
print(person)
"""
#task 18: 1 dan 5 gacha bo‘lgan sonlar uchun kvadrat lug‘atini yarating (masalan {1: 1, 2: 4, ...}).
"""
square = {}

for i in range(1, 6):
    square[i] = i**2
    
print(square)
"""
#task 19: Berilgan dict’dagi kalit va qiymatlarni joyini almashtiring. Masalan: {"a": 1, "b": 2} → {1: "a", 2: "b"}.
"""
mydict = {"a": 1, "b": 2, "c": 3}
swapped = {}

for key , val in mydict.items():
    swapped[val] = key
print(swapped)

"""
#task 20: Ikki dictionary’ni birlashtir:
"""
d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}

d1.update(d2)
print(d1)

"""
