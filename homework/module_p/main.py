import math_utils as math
import greetings as g
from converter import kg_to_lb, lb_to_kg
from string_ops import *
import logger
import config, helper
import sys, os


'''
a = math.add(7, 4)
b = math.subtract(11, 4)
c = math.multiply(5, 5)
d = math.divide(75, 5)

print(a, b, c, d)

'''
'''
res = g.say_hello("teo")
ret = g.say_goodbye("teo")
print(res,"\n",ret)
'''
'''
quantity = kg_to_lb(45)
weight = lb_to_kg(99)
print("from kg to lb: ", quantity)
print("from lb to kg: ", weight)

'''
'''
res = capitalize("python")
print(res)

ret = reverse("montana")
print(ret)

'''
'''
res = math.add(3, 3)
print(res)
r = math.square(4)
print(r)

'''
'''
print("main.py boshida: ", config.DB_NAME)

config.DB_NAME = "HACKED_DB"

print(f"main.py ozgargandan keyin: {config.DB_NAME}")

helper.check_config()

'''
'''
loaded_modules = sys.modules

if "os" in loaded_modules:
    print("os moduli ")
    
if "sys" in loaded_modules:
    print("sys moduli xotiraga yuklandi")

'''
'''
try:
    import blablabla
except ModuleNotFoundError as e:
    print(e)
    
'''
'''
current_dir = os.curdir

modultest_dir = os.path.join(current_dir, "modultest")

sys.path.append(modultest_dir)

import modultest

modultest.myfunc()

'''
import inspect

#print(sys.modules[__name__])

from myclass import User
'''
a = User("teo", "male", 22)
print(a.get_info())

'''
'''
import mymodule

print(mymodule.add)

import plugin
import my_plugins

print(plugin.registry["Hello"]())
print(plugin.registry["bye"]())

'''
'''
import cache

print("1.chaqiriq")
print(cache.expensive_computing(4))
print("2.chaqiriq")
print(cache.expensive_computing(2))
print("3.chaqiriq")
print(cache.expensive_computing(4))
print("4.chaqiriq")
print(cache.expensive_computing(4))
print("5.chaqiriq")
print(cache.expensive_computing(4))
print("6.chaqiriq")
print(cache.expensive_computing(4))

'''
'''
import a

print(a.func_a())

'''
'''
import importlib
import safe_module

print("-----reload------")

importlib.reload(safe_module)
importlib.reload(safe_module)

'''
import utulities
'''
from utulities import string_tools, math_tools

print(math_tools.cube(23))
print(string_tools.reverser("eternal"))

'''
'''
from analytics import *

stat_info()
create_graph()

'''
'''
from ecommerce import Product, Order, Payment

user = Product("iphone17", 1000)
item = Order(user, 1)
p = Payment(item)

print(p.pay())

import ecommerce

user = ecommerce.Product("name", 1)
u = ecommerce.Order(user, 1)
p = ecommerce.Payment(u)

'''
'''
import importlib

module_name = "ecommerce.products"

products_module = importlib.import_module(module_name)

Product = products_module.Product

from ecommerce.orders import Order
from ecommerce.payments import Payment

p = Product("phone", 200)
o = Order(p, 2)
pay = Payment(o)

print(pay.pay())

'''
'''
import importlib

module_name = "math_utils" #string

mod = importlib.import_module(module_name) #

myadd = mod.add

print(myadd(7, 7))

'''
'''
import ecommerce

print(dir(ecommerce))

'''

'''
import modultest

print(modultest.greet("rura"))'''



import utulities

print(utulities.cube(5))