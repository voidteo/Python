class User:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    
    def get_info(self):
        return f"User's name: {self.name}, gender: {self.gender}, age: {self.age}"
    

def unrelated_func(a, b):
    return a * b

