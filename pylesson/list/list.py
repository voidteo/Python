# 30 list exercises to understand better

# task 1:fruits = ["apple", "banana", "cherry"] → oxiriga "mango" qo‘sh va chiqar.
"""
fruits=
fruits.append("mango")
print(fruits)
"""
#task 2: fruits ichida "banana"ni "orange"ga almashtir.
"""
fruits= ["apple", "banana", "cherry"]
fruit1=[i if i != "banana" else "orange" for i in fruits]
print(fruits)
print(fruit1)
"""
#task 3: fruits ro‘yxatidagi oxirgi elementni o‘chir (pop).
"""
fruit = ["apple", "banana", "cherry"]
fruit.pop(2)
print(fruit)
"""
#task 4: numbers = [10, 20, 30, 40] → uzunligini top (len).
"""
numbers = [10, 20, 30, 40]
print(len(numbers))
"""
#task 5: numbers ichida nechta 20 borligini hisobla (count).
"""
numbers= [1, 20, 2, 20, 3, 20, 4, 20, 5, 20]
print(numbers.count(20))
"""
#task 6: numbers ichida 30 qaysi indexda ekanini top (index)
"""
number= [10, 20, 30, 40]
print(number.index(30))
"""
#task 7: colors = ["red", "green", "blue"] → "yellow"ni boshiga qo‘sh (insert).
"""
colors = ["red", "green", "blue"]
colors.insert(0, "yellow")
print(colors)
"""
#task 8: colorsdan "green"ni o‘chir (remove).
"""
colors = ["red", "green", "blue"]
colors.remove("green")
print(colors)
"""
#task 9: colorsning oxirgi elementini o‘chir va alohida chiqar (pop).
"""
colors = ["red", "green", "blue"]
print(colors.pop(-1))
print(colors)
"""
#task 10: Bo‘sh list yarat va foydalanuvchidan 3 ta ism olib listga qo‘sh.
"""
l=[]
for i in range(3):
    n=input("name: ")
    l.append(n)
print(end= "\n")
print(l)
"""
#task 11: nums = [5, 1, 9, 3, 7] → tartibla (sort).
"""
nums = [5, 1, 9, 3, 7]
nums.sort()
print(nums)
"""
#task 12: numsni teskari qilib chiqar (reverse).
"""
nums = [1, 2, 3, 4, 5]
nums.reverse()
print(nums)
"""
#task 13: words = ["banana", "apple", "cherry"] → alfavit bo‘yicha tartibla.
"""
words = ["banana", "apple", "cherry"]
words.sort()
print(words)
"""
#task 14: nums = [100, 50, 75, 25] → eng katta va eng kichik elementni top (max, min).
"""
nums = [100, 50, 75, 25]
nums.sort()
min = nums[0]
print(min)

nums.reverse()
max=nums[0]
print("max = ", max)
"""
"""
nums = [100, 50, 75, 25]
min_num = nums[0]
max_num = nums[0]

for n in nums:
    if n < min_num:
        min_num = n
    if n > max_num:
        max_num = n

print("min_num= ", min_num)
print("max_num= ", max_num)
"""
#task 15: letters = ["a","b","c","d","e"] → faqat dastlabki 3 elementni ol.
"""
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[:3])
"""
#task 16: lettersning oxirgi 2 elementini ol.
"""
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[-2::])
"""
#task 17: lettersni teskari tartibda chiqar ([::-1]).
"""
letters = ['a', 'b', 'c', 'd', 'e']
print(letters[::-1])
"""
#task 18: cities = ["Tashkent", "Samarkand", "Bukhara"] → har bir shaharni alohida qatorda chiqar
"""
cities = ["Tashkent", "Samarkand", "Bukhara"]

for i in cities:
    print(i)
"""
#task 19: numbers = [2, 4, 6, 8] → barcha elementlarning yig‘indisini top (sum).
"""
numbers = [2,4,6,8]
s=0

for i in numbers:
    s+=i
print(s)
"""
#task 20: numbersdagi faqat juft sonlarni chiqar (if).
"""
numbers = [1, 2, 3, 4, 5, 6, 7,8 ,9 ,10]
even = [ i for i in numbers if i % 2 == 0]
print(even)
"""
#task 21: numbersdagi har bir sonni kvadrat qilib yangi listga joyla.
# solution 1 below
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num1 = []

for i in numbers:
    num1.append(i**2)
print(num1)
"""
#solution 2 below: 
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square = [i**2 for i in numbers]
print(square)
"""
#task 22: Talabalar baholari listi: [56, 78, 90, 45, 88] → o‘rtacha bahoni hisobla.
"""
grade = [56, 78, 90, 45, 88]
avg = 0
s = 0

for i in grade:
    s+=i
    avg = s / len(grade)
print(avg)
"""

#task 23: names = ["Ali", "Vali", "Sami", "Ali"] → takrorlangan "Ali"ni nechta ekanini top.
"""
name = ["Ali", "Vali", "Sami", "Ali"]
cnt = 0

for i in name:
    if i == "Ali":
        cnt+=1
print(cnt)
"""
"""
names = ["Ali", "cali", "sali", "Ali"]
print(names.count("Ali"))
"""
#task 24: names ichidan takrorlarni olib tashla (unikal list qil).
"""
names = ["Ali", "Vali", "Ali", "Sali", "Sali"]
unique_names = list(set(names))
print(unique_names)
"""
"""
names = ["Ali", "Vali", "Ali", "Sali", "Sali"]
u_names =[]

for i in names:
    if i not in u_names:
        u_names.append(i)
print(u_names)
"""

#task 25: Telefon raqamlar ro‘yxati bor: ["+99890", "+99891", "+99893"] → hammasini for orqali chiqar.
"""
phone_n = ["+99890", "+99891", "+99893"]

for i in phone_n:
    print(i)
"""
#task 26: words = ["python", "java", "c++"] → uzunligi eng katta so‘zni top.
"""
words = ["python", "java", "c++"]
longest = ""
for i in words:
    if len(i) > len(longest):
        longest = i
print("the longest word: ", longest)
"""
#task 27: words ichida "python" bormi yo‘qmi tekshir (in).
"""
words = ["python", "java", "c++"]

if "python" in words:
    print(True)
else:
    print(False)
"""
#task 28: Sonlardan iborat listdan faqat manfiy sonlarni ajratib chiq.
"""
nums = [1, 2, 3, -4, -5, -6, -7]
for i in nums:
    if i < 0:
        print(i, end= " ")
print(end="\n")
"""
#task 29: Ikki listni qo‘sh: [1,2,3] + [4,5,6].
"""
l1 = [1,2,3]
l2 = [4,5,6]
l3 = []
l3 = l1 + l2
print(l3)
"""
"""l1 = [1,2,3]
l2 = [4,5,6]
l1.extend(l2)
print(l1)"""
#task 30: Matn: "apple, banana, cherry" → vergul orqali bo‘lib listga aylantir (split).
"""
tex = "apple , banana ,cherry"
ls = tex.split(" ,")
print(ls)

"""