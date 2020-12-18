from functools import reduce
#  Lambda : functions without names, also called as anonymous functons
#  functions are objects in python. so we can pass fncns like objects and values
# normal:
from builtins import map


def square(n):
    return n*n  # only one line of code so, defining a function is not necessary


result = square(5)
print(result)


# lambda:


f = lambda a : a*a
# f is a anonymous function without any name, lambda fncn can be passed to f function
result = f(5)
print(result)


"""
lambda function reduces no of lines in code
instead of defining a complete function and returning the function,
directly use lambda and expression
eg:

def even(n):
    return n%2 == 0
    
nums = [2,3,5,6,8,4,1,8]
evens = list(filter(even,nums))    here filter is in-buit function
print(evens)

this code without using functions, we can write using lambda
"""

nums = [2,3,5,6,8,4,1,8]
evens = list(filter(lambda m: m % 2 == 0, nums))
# 'filter' is in-built functon which filters the data
# no functions defined, direct expression m%2==0 using lambda.

doubles = list(map(lambda m: m+4, evens))
# 'maps' is in-built function, which takes the data and apply some operation

sum = reduce(lambda a,b: a+b, doubles)
# for reduce, import reduce from functools

print(evens)
print(doubles)
print(sum)

"""
filter
map
reduce
these three operations are done generally in big data:
if there is a data, we first filter it, then do some operations using map
then we will reduce it by applying any function or any logic like adding all values of data etc.
 """
