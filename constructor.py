# in a class, if we create an object everytime we run, it takes different space
# in computer, we will have a heap memory, everytime we create an object it is allocated to a new memory space
# size of object depend upon size of variables used
# constructor defines the size of memory allocation to any object
# whenever we write constructor, it calls init method internally
# self is a current instance. if n num of objects present, self helps to point to
# particular object. so self is very important


class Computer:

    def __init__(self):
        self.age = 26
        self.name = 'Rachana'

    def compare(self, other):  # comparing self object with other object
        if self.age == other.age:  # compare takes 2 objects(who is calling, whom to compare)
            return True
        else:
            return False


c1 = Computer()  # c1,c2 are objects, Computer() is a constructor
c2 = Computer()  # creating 2 objects with different variables

if c1.compare(c2):
    print('they are same')

c1.name = 'Sandeep'  # changing data
c1.age = 32


print(c1.name)
print(c1.age)
print(c2.name)
print(c2.age)
