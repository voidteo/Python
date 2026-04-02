import time

print("Cache modul yuklandi!")

cache = {}

def expensive_computing(val):
    if val in cache:
        print("We got it from cache!")
        return cache[val]
    
    print("i'm calculating....")
    time.sleep(3)
    
    res = val**2
    cache[val] = res
    return res

