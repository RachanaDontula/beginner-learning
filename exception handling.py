"""
Errors:
1. Compile time error
2. Logical error
3. Run time error

1. Compile time Error: also called as syntactical errors
syntax error, any mistake in syntax.
we will get these errors at compile time. Most easiest to find.

2. Logical errors:
Code is syntactically correct, but logic is not correct.
it gives o/p but not correct o/p. While testing, also easy.

3. Runtime error:
code is compiled, logically correct, but if user gives wrong i/p
eg: divide by zero. tough one to find.
eg: After user deleting a file from c drive where an application is
stored, now if we open that application, we get run time error.
database connection issue, network issue, file close issue, etc.


try: tries the logic or code, if correct direct it jumps to finally block.
except: if any exception arises, execution jumps to except block,
we give error condition, code executes without error
and jumps to finally block. N num of exceptions can be written alike elif.
finally: this block executes in both conditions
we get error as well as if we don't get error.
"""

a=4
b = 5
c = 0


try:
    print(a/b)

    A = int(input("enter any integer: "))  # value error
    print(A)
    print(a/c)  # zero division error
    # only one exception is accepted in try.
except ZeroDivisionError as e:
    print("invalid division", e)

except ValueError as e:
    print("wrong type")

finally:
    print("bye")

