def reverser(val: str):
    if not isinstance(val, str):
        raise ValueError("you should enter str value or string")
    return val[::-1]

def upperland(val):
    if not isinstance(val, str):
        raise ValueError("you should enter str value or string")
    return val.upper()

