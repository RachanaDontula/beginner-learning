# outside function, global variable, innside a function, local variable
# if we want to change global variable value inside the function, mention 'global_variablename'
# if local should be present and change global variable value in the same function, use keyword called 'globals()'
# using globals(), we can access all the global variables at once. To specify particular vaariable,
# use 'globals()['variable name']'


a = 10  # global variable
print(id(a))
print('global: ', a)


def function():
    a = 9  # local variable
    print('local : ', a)
    print(id(a))
    x = globals()['a']
    print(id(x))
    print('inside function: ', a)  # print local a

    globals()['a'] = 15  # changing global value


function()
print('outside function: ', a)


# passing list to a function

def count(list):
    even = 0
    odd = 0

    for j in list:
        if j % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


list = [1,2,3,4,5,6,7,8,9,10]

even, odd = count(list)

print('even:{} and odd:{}'.format(even, odd))


# detecting letters more than 5 in names

def names(lst):
    greater = 0
    less = 0

    for a in range(len(lst)):
        if len(lst[a]) >= 5:
            greater += 1
        else:
            less += 1
    return greater, less


lst=[]
n = int(input("enter range of names: "))
for users in range(n):
    users = input("enter names: ")
    lst.append(users)


greater, less = names(lst)
print('greater:{} and less:{}'.format(greater, less))





