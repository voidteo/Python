
def convert_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            func()
        except KeyError as e:
            raise ValueError(e)
    return wrapper

@convert_exceptions
def myfunc():
    d = {}
    
    print(d["key1"])
    
