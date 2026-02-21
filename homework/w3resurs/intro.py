# exercises from w3resources........................

#task 4: Write a Python program that calculates the area of a circle based on the radius entered by the user. 
"""
# A =pr(square2)
from math import pi, pow

user_radius = int(input("enter radius of circle: "))

#area = pi * pow(user_radius, 2)

area = pi * (user_radius**2)
#a = 3.14 * (user_radius**2)

print(f"Area of circle is: {area: .2f}")

""" 
#task 5: Write a Python program that accepts the user's first and last name and prints them in reverse order with a space between them. 
"""
user = input("Enter first and last name: ")

print(user[::-1])

""" 
"""
user = input("enter a filename: ")

f_user = user.split(".")

print(f"extencion of file is: {f_user[-1]}")

""" 
#task 8: Write a Python program to display the first and last colors from the following list.
"""
color_list = ["Red","Green","White" ,"Black"]

first_color = color_list[0]
last_color = color_list[-1]

print(f"first: {first_color}, last: {last_color}")

""" 
#task 9: Write a Python program to display the examination schedule. (extract the date from exam_st_date). 
"""
exam_st_date = (11, 12, 2014)

print("exam starts from: %i/%i/%i" % exam_st_date)

""" 
#task 10: Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 
"""
n = input("enter number: ")

n1 = int(n)
n2 = int(n+n)
n3 = int(n+n+n)

res = n1 + n2 + n3
print(res)

""" 
#task 11  Write a Python program to print the documents (syntax, description etc.) of Python built-in function(s). 

#print(max.__doc__)

#task 12: calendar
"""
import calendar

m = int(input("enter a month: "))
y = int(input("enter a year: "))

print(calendar.month(m, y))

""" 