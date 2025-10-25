#task 1: Uchta elementdan iborat tuple yarat.
"""
tupl = ("teo", 22, "python")
print(tupl, type(tupl))

"""
#task 2: index orqali element chiqarish
"""
tupl = ("teo", 22, "python")
print(tupl[0])

"""
#task 3: Tuple uzunligini top.
"""
tup = (1,2,3,4,5,6,7,)
print(len(tup))

"""
#task 4: Tuple ichida ma’lum qiymat borligini in operatori bilan tekshir.
"""
tupl = ("teo", 22, "python")
print("teo" in tupl)

"""
#task 5: Tupleni listga aylantir.
"""
tupl = ("teo", 22, "python")
print(list(tupl))

"""
#task 6: Listni tuplega aylantir.
"""
l = ["teo", "python", "intro"]
t = tuple(l)
print(t)

"""
#task 7: Tuple ichidagi barcha elementlarni for orqali chiqar.
"""
mytup = ("teo", "eshmat", 1, 2, 3, 4,)

for i in mytup:
    print(i, end= " ")
    
""" 
#task 8: Tuple ichidagi minimal va maksimal qiymatni top.
"""
mytup = (3, 4, 1, 2, 44, 6, 4, 5)
print(min(mytup), max(mytup))

min = mytup[0]
max = mytup[0]

for i in mytup:
    if i > max:
        max = i
    elif i < min:
        min = i

print(f"max value {max}, min value {min}")

"""
#task 9: Tupledagi elementlar sonini sanash (count()).
"""
mytup = (3, 4, 1, 2, 44, 6, 4, 5)
print(len(mytup))
"""
#task 10: Tupledagi element indeksini top (index()).
"""
l = ("teo", "python", "intro", "backend",)

print(l.index("python"))

"""
#task 11: Tuple unpacking orqali qiymatlarni ajrat (a, b, c = tuple).
"""
mytup = ("teo", "learns", "python")

a, b, c = mytup
print(a, b, c)

"""
#task 12: Tuple ichida boshqa tuple bo‘lsa, ichki elementga kirish.
"""
mytup = (("teo", 22), (1,2,), (3,4,),)
print(mytup[1][1])

"""
#task 13: Ikki tuple’ni birlashtir (+ operatori bilan).
"""
tup = (1,2,)
tup1 = (3, 4,)
res = tup + tup1
print(res)

"""
#task 14: Tuple’ni 3 marta takrorla (* operatori).
"""
mytup = ("teo", "learns", "python")
tmp = mytup*3
print(tmp)
"""
#task 15: Tuple ichidagi stringlarni join() yordamida bitta matnga aylantir.
"""
mytup = ("teo", "learns", "python")

r = " ".join(mytup)
print(r)

"""
#task 16: Tuple ichidagi raqamlar yig‘indisini top.
"""
mytup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10,)

s = 0
for i in mytup:
    s+=i
print(f"sum of tuple equals {s}")

print(sum(mytup))

""" 
#task 17: Tuple ichidagi turlarni (data types) aniqlab chiq.
"""
mytup = ("teo", [1, 2], 3, (3, 4), {1: "python"}, 5.5,)

for i in mytup:
    print(type(i))
"""
#task 18:Tuple ichidagi faqat unikal qiymatlarni set() orqali ajrat.
"""
mytup = (1,1,2,2,3,3,4,5,6,6,7,)
print(tuple(set(mytup)))

""" 
#task 19: Tuple comprehension nega mavjud emasligini tushuntiruvchi misol yoz.

tuple(x**2 for x in range(5)) → tuple comprehension emas, generatorni tuplega aylantirish

#task 20: Tuple ichida faqat immutable turlar ishlatilishini isbotlovchi misol yoz.