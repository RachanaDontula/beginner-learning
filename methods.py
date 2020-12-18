"""
methods:
1. Instance methods
2. Static methods
3. Class methods

Instance method works with the object, works with instance variables
1.Accessor methods: to fetch values we use this, get method
2. Mutators methods: to modify values, set method
working with instance methods, use instance variable(self)


Class methods: use class keyword(cls)
               use decorators for using class methods i.e.,
               (@classmethod)

when we are not concerned about instance variable and class variable
use static methods. We can use static methods, when there is some operation with
other class objects.
we use decorator called (@staticmethod)

 """


class Students:

    school = 'Saraswathi'

    def __init__(self, m1, m2, m3):
        self.m1 = m1
        self.m2 = m2
        self.m3 = m3

    # defining constructor
    def avg(self):
        return (self.m1+self.m2+self.m3)/3

    # defining accessors and mutator methods
    def __get__(self):
        return self.m1

    def __get1__(self):
        return self.m2

    def __get2__(self):
        return self.m3

    def __set__(self, value):
        self.m1 = value

    def __set1__(self, value1):
        self.m2 = value1

    def __set2__(self, value2):
        self.m3 = value2

    # defining class or creating class method
    @classmethod
    def getSchool(cls):
        return cls.school

    # defining static method
    @staticmethod
    def info():
        print("this is duplicate school")


# defining objects
s1 = Students(23,58,65)
s2 = Students(56,15,89)

print(s1.avg())
print(s2.avg())
print(Students.getSchool())
Students.info()