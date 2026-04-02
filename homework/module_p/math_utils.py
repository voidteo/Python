
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b < 0:
        return "ZeroDivisionError"
    return a / b

def square(a):
    return a ** 2

if __name__ == "__main__":

    print(square(4))
    
    