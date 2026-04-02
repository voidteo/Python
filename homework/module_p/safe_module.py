import sys

module = sys.modules[__name__]

if not hasattr(module, "initialized"):
    print("module birinchi ishga tushdi")
    
    module.initialized = True
else:
    print("module qayta ishlamadi: (skip)")
    

