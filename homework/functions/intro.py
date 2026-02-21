#================== SHOPPING CART PROGRAMM
"""
foods = []
prices = []
total = 0

while True:
    food = input("enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"enter a price of a {food}: $"))
        foods.append(food)
        prices.append(price)
       
print("-----YOUR CART-----") 
for food in foods:
    print(food, end=" ")
    
for price in prices:
    total+=price
print()

print(f"your total is: ${total}")

"""
# menu with dict and after ordering presenting order with total sum
"""
import random

number = random.randint(1, 100)

options = [1,2,3,4,5]

res = random.choice(options)
print(res)

""" 

l = [1,2,3,4,5,6,7,8]

l.reverse()
print(l)