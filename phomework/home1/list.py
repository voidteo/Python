#task 1: 5 ta meva nomidan iborat ro‘yxat tuz va ekranga chiqar.
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]
print(l)
""" 
#task 2: 2-elementni o‘zgartir.
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]
l[1] = "Teo"
print(l)
""" 
#task 3: Listga yangi element qo‘sh.
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]

l.append("mango")
print(l)

""" 
#task 4: Oxirgi elementni o‘chir.
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]
l.remove("grape")
print(l)

""" 
#task 5: insert() orqali element qo‘sh.
"""
l = ["teo", "tima", "apple"]

l.insert(1, "Steve")
print(l)

""" 
#task 6: remove() bilan ma’lum elementni o‘chir.
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]

l.remove("pineapple")
l.pop(-1)
print(l)

""" 
#task 7: sort() orqali tartibla.
"""
l = [4, 1, 5, 7, 2, 9, 8, 6]

l.sort()
print(l)

""" 
#task 8: reverse() bilan teskari tartibda chiqar.
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]

l.reverse()
print(l)

""" 
#task 10: List uzunligini top.
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]
print(len(l))

""" 
#task 11: 1-3 indeks oralig‘idagi elementlarni chiqar.
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]

print(l[1:3])

""" 
#task 12: Oxirgi elementni indeks orqali ol.
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]
print(l[-1])
""" 
#task 13: Har ikkinchi elementni chiqar (::2).
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]

print(l[::2])
"""
#task 14: Listni nusxalab olish uchun slicing ishlat.
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]
#l1 = l[:]
#print(l1)

nl = l.copy()
print(nl)

"""
#task 15: listni teskari chiqar
"""
l = ["apple", "orange", "pineapple", "banana", "grape"]
print(l[::-1])

"""
#task 16: 10 tadan raqamli list tuz va ularning yig‘indisini chiqarsin.
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0

for i in lst:
    s+=i
print(f"sum of numbers in list is {s}")

""" 
#task 17: O‘rtacha qiymatni top.
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = 0
avg = 0

for i in lst:
    s+=i
avg = s/len(lst)

print(avg)

""" 
#task 18: Faqat juft sonlarni chiqar.
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newlst = []

for i in lst:
    if i % 2 == 0:
        newlst.append(i)
        
print(newlst)

""" 
#task 19: Minimal va maksimal qiymatni top.
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print( min(lst),  max(lst))

""" 
#task 20: Elementlar sonini sanovchi kod yoz.
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cnt = 0

for i in lst:
    cnt+=1
print(f"the amount of elements: {cnt}")

""" 
#task 21: 1 dan 10 gacha bo‘lgan sonlarning kvadratlarini list comprehension yordamida tuz.
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nlst = [n**2 for n in lst]
print(nlst)

""" 
#task 22: 1 dan 20 gacha bo‘lgan faqat juft sonlar ro‘yxatini tuz.
"""
nlst = [n for n in range(1, 21, 1) if n % 2 == 0]
print(nlst)

""" 
#task 23: Faqat 3 ga bo‘linadigan sonlar ro‘yxatini yarat.
"""
nlst = [n for n in range(1, 31) if n % 3 == 0]
print(nlst)

""" 
#task 24: Harflar ro‘yxatini upper() shaklida qaytar.
"""
lst = ["python", "is", "good"]

nlst = [n.upper() for n in lst]

print(nlst)

""" 
#task 25: [‘apple’, ‘banana’, ‘kiwi’] dan faqat uzunligi 5 dan katta so‘zlarni ol.
"""
lst = ["apple", "banana", "kiwi"]

nlst = [n for n in lst if len(n) > 5]

print(nlst)

""" 
#task 26: 3x3 o‘lchamdagi nested list yarat (matrix).
"""
lst = [[1,2], [3, 4], [5, 6]]
print(lst[0][1])
print(lst[1][1])
print(lst[2][1])
print(lst)

""" 
#task 27: Har qatordagi elementlar yig‘indisini chiqar.
"""
lst = [[1,2], [3, 4], [5, 6]]

for row in lst:
    s = 0
    for num in row:
        s+=num
    print(f"sum: {s}")
    
""" 
#task 28: Barcha elementlarni bitta ro‘yxatga yig‘ (flatten).
"""
lst = [[1,2], [3, 4], [5, 6]]
nlst = []

for i in lst:
    for j in i:
        nlst.append(j)
print(nlst)

""" 
#task 29: Har qatordagi maksimal qiymatni chiqar.
"""
lst = [[1,2], [3, 4], [5, 6]]

nlst = [max(row) for row in lst]
print(nlst)

""" 
#task 30: 10 ta ism bor, ularni alfavit bo‘yicha tartibla.
"""
names = ["ali", "bille", "jay", "timon", "dima", "scott", "styles", "eshmat"]
names.sort()

print(names)

""" 
#task 31: Ikki listni birlashtir.
"""
l1 = [1, 2]
l2 = [3, 4]

l1.extend(l2)

print(l1)

""" 
#task 32: Element ro‘yxatda bor-yo‘qligini in operatori bilan tekshir..
"""
names = ["ali", "bille", "jay", "timon"]

print("james" in names)

""" 
#task 34: Ro‘yxatdagi unikal elementlardan iborat yangi ro‘yxat tuz.
"""
l = [1,1,2,2,3,3,4,5,6,6,5,6,7]
l1 = []

for i in l:
    if i not in l1:
        l1.append(i)
print(l1)

""" 
#task 35: split() va join() orqali string-list o‘zgarishini bajar.
"""
word = "I am learning python"

wor = word.split()
print(wor, type(wor))

l = ["Teo", "is", "learning", "python"]

n = " ".join(l)
print(n)

""" 
#task 36: 0 dan 50 gacha bo‘lgan sonlar ichidan faqat 5 ga karralilarni chiqar.
"""
newls = [n for n in range(1, 51) if n % 5 == 0 ]
print(newls)

""" 
#task 37: Foydalanuvchidan 5 ta son olib, listga joyla.
"""
lst = []
for i in range(1, 6):
    n = int(input("enter number: "))
    lst.append(n)
    
print(lst)

""" 
#task 38: List elementlarini indeksi bilan birga chiqar.
"""
l = ["Teo", "is", "learning", "python"]

for index , word in enumerate(l):
    print(index, word)
    
""" 
#task 39: Listni tozalab tashla (clear()).
"""
l = ["Teo", "is", "learning", "python"]
l.clear()

print(l)

"""
#task 40: Har bir elementni kvadrat qilib, yangi list qaytar.
"""
lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

nlst = [n**2 for n in lst]
print(nlst)

"""