import inspect
import sys

def seefunc(val):
    return inspect.getsource(val)

me = sys.modules[__name__]

print(seefunc(me))