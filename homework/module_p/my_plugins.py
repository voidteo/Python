from plugin import register

@register("Hello")
def say_hello():
    return "Hello Teo"

@register("bye")
def say_bye():
    return "Goodbye Teo!"

