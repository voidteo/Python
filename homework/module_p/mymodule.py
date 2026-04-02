
'''
def openfunc():
    print("I am open you can enter")
    
def _notopen():
    print("i am not open think about it")

def __prvt():
    print("i am private dont ever enter")

'''

def __getattr__(name):
    print(f"{name} attribute topilmadi dynamic yaratilmoqda")
    
    if name == "pi":
        return 3.14159
    elif name == "e":
        return 2.71828
    else:
        return f"{name} degan attirbute yoq"
    