import sys
# fibonacci numbers


def fib(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n <= 0:
        print('invalid')
    else:
        print(a)
        print(b)

        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print(c)
        print()


n = int(input("enter range: "))
fib(n)


# printing nth value: use formula 'fib(n-1)+fib(n-2)'


def fact(m):
    x = 1
    for k in range(1,m+1):
        x = k*x
    return x


x = int(input('enter number: '))
print(fact(x))


# recursion: function calling itself

sys.setrecursionlimit(100)
print(sys.getrecursionlimit())


def rec():
    print('Hello')
    rec()  # recursion


rec()


# factorial using recursion


def fact1(u):
    if u == 0:
        return 1
    return u*fact1(u-1)  # recursion, calling same function


result = fact1(5)
print(result)