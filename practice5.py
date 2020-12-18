def add_sub(x, y):  # x, y are called formal arguments
    c = x+y
    d = x-y
    return c, d


result1, result2 = add_sub(4, 2)  # 4, 2  are called actual arguments
print(result1, result2)

# positions matter lot. 4 goes to x and 2 goes to y
# or we can mention the key word eg: add_sub(x = 4, y = 2)


def update(x):
    print(id(x))
    x = 1
    print(x)


a = 10
print(id(a))
update(a)
# in python for functions we do not use pass by reference or pass by value


# variable length  arguments

def sum(a, *b):  # when length of arguments is not known, first argument is fixed and second will be stared*
    c = a
    a = 0
    for i in b:
        c = c+i
    print(a)
    print(b)
    print(c)


sum(5, 4, 1, 2)


# keyword variable length arguments

def person(name, **data):
    print(name)
    print(data)
    for k, j in data.items():
        print(k, j)


person('Rachana', age=26, city='Hyderabad', num=654989)
# age, city, num are keywords





