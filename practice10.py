"""
__main__ is a starting point of execution of any code

value of   __name__   is    __main__

eg:
print(__name)
o/p: __main__
"""

import demo

print("this code says:" + __name__)

'''
this code has imported other module, so __name__ prints, 
name of the module and then the value of __name__ i.e., __main__


if  __name__   is used as main code in the file, it prints it's value as __main__
if __name__   is imported into other file/module, it prints name of the module
'''

