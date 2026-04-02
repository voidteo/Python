# plugin system module

registry = {}

def  register(name):
    def inner(func):
        registry[name] = func
        return func
    return inner

