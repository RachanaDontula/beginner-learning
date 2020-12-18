
print("Hello " + __name__)

'''
__name__ is special variable
__name__   helps to print the statements or execute the function only when 
value of __name__   is   __main__
If user doesn't want to print first file every time or if imported as a module
first file will not executed, every time when file is imported in other file/module

eg:

def main():
    
    print("Hello")
    print("Welcome user")
    

if __name__ == __main__:
    main()


now if we import this demo in other file, which has it's own code

eg:
practice10.py

import demo

print("It's time to calculate")

o/p:
it's time to calculate


output is only the print statement in practice10.py even after importing 
demo file. This is because __name__ value here is not __main__.

So, __name__ function helps in either ways. 
'''
