# notes from decorators: 

Python’dagi professional qoida (OLTIN QOIDA)

🔑 Decorator asl funksiyaning
semantik hulqini saqlashi kerak,
faqat qo‘shimcha kuzatuv yoki yon effekt qo‘shishi mumkin.

#this is a factory decorator , in other words parametric decorator , decorator that takes parametr

def check_access(access_level_required): # 1. The outer function (decorator factory) takes parameters
    def decorator(func): # 2. The middle function (decorator) takes the function
        def wrapper(*args, **kwargs): # 3. The inner function (wrapper) handles the decorated function's arguments
            # Use the parameter from the outer function
            if access_level_required == "admin":
                print(f"Admin access granted. Calling '{func.__name__}'...")
                return func(*args, **kwargs)
            else:
                print(f"Access Denied: Need 'admin' level to call '{func.__name__}'.")
                return None
        return wrapper
    return decorator

@check_access("admin")
def get_admin_dashboard_data():
    return "Secret Admin Data"

@check_access("user")
def get_user_dashboard_data():
    return "User Data"

# Calling the decorated functions
print(get_admin_dashboard_data())
print(get_user_dashboard_data())


1️⃣ LRU Cache nima o‘zi?

LRU = Least Recently Used

👉 Cache to‘lib qolsa, eng oxirgi ishlatilgan emas, balki
eng uzoq vaqtdan beri ishlatilmagan element o‘chiriladi.

Misol:

Capacity = 3
Access: A → B → C → A → D


Cache: A, B, C

A qayta ishlatildi → u “eng yangi”

D keldi → joy yo‘q → B o‘chadi (eng kam ishlatilgan)