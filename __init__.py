"""
__init__  is a special method of class
__init__ is also called as constructor/method

eg:

def __init__(self):



init is called automatically, no need of calling seperately.
for every object it gets called once
values assigned to auguments in __init__ method, will be assigned to objects
we have to declare the augument values with self

eg:

"""


class Computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu  # declaring arguments in __init__ method
        self.ram = ram

    def config(self):
        print("config is: ", self.cpu, self.ram)


com1 = Computer("i5", 16)
com2 = Computer("Rysen 3", 8)

com1.config()
com2.config()  # binding methods with data
# one object will have its own methods and own variables, they work together




