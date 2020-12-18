# Decorators: we can change the behaviour of the exixting function at the compile time itself
# eg: without touching the function changing the function operation or condition of function
# python is a functional programming language


def div(a,b):
    print(a/b)


def smart_duv(func):  # passing parameter/augument a function
    # this is extra, so this is called decorator
    def inner(a,b):  # function inside a function
        if a<b:
            a,b =b,a
        return func(a,b)
    return inner


div = smart_duv(div)
div(2, 4)
