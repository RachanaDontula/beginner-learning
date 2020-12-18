"""
Poly: many
Morphism: forms
polymorphism: one thing with different forms
Objects have different forms.
uses:
1. Loose Coupling
2. Dependency Injection
3. Interface

four ways of defining polymoorphism:
1. Duck typing
2. Operator Overloading
3. Method overloading
4. Method overriding
"""

# Duck Typing:
'''If it looks like a duck, swims like a duck and quacks like a duck,
it is probably duck.
If any behaviour of dck type exists, it is duck typing
if we have an object, and it has a method eg: execute(), that is it.
we  doesn't concern about which class it is from, it is called as 
duck typing '''


class Pycharm:

    def execute(self):
        print("Compiling")
        print("Running")


class Myeditor:

    def execute(self):
        print("Spell check")
        print("Convention check")


class Laptop:

    def code(self, ide):
        ide.execute()


ide = Myeditor()
# ide = Pycharm()  ide is dynamic.
lap1 = Laptop()
lap1.code(ide)


'''
Operator overloading:
operator(or method) is constant, arguments(no of arguments/
types of arguments) are different
'''

a = 3
b = 5
c = 'Rachana'
d = 'Dontula'
print(a+b)  # simple way
print(int.__add__(a, b))  # operator overloading, add is a method which
# belongs to int class
print(str.__add__(c,d))
print(int.__sub__(a, b))


class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):  # operator overloading
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)

        return s3

    def __gt__(self, other):  # operator overloading
        r1 = self.m1+self.m2
        r2 = other.m1+other.m2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {}'.format(self.m1, self.m2)


s1 = Student(56,65)  # defining objects
s2 = Student(52,45)

s3 = s1+s2
print(s3.m2)

if s1>s2:
    print("s1 wins")
else:
    print("s2 wins")


print(s1.__str__())
print(s1)
print(s2)


"""
Method Overriding:
same methods with same names and same arguments/parameters but different classes
can be created, this is called method overriding.
method overriding:
Parent class has a method eg: show()
Child class is inherited first from parent class, so, when we call method
it prints parent class method
when child class also has the same method with same arguments, now when 
we call the method, it prints child class method which has same parent 
class method name. This process of child class method overriding parent class
method(both of same name and same arguments) is called 
method overriding. 
"""


class A:

    def show(self):
        print("in A show")


class B:  # just passing
    pass


a1 = A()
a1.show()


class B(A):  # inheriting
    pass


a1 = B()
a1.show()


class B(A):

    def show(self):  # method overriding
        print("in B show")


a1 = B()
a1.show()  # when we call show(), it shows child class show method
# if child class has that method, if not it shows parent class show method.


"""
Method overloading:
In one class, we have two methods with same name but different 
parameters/arguments.
eg:
Student class:
def average(a,b):
def average(a,b,c):
"""


class Students:

    def __init__(self, marks1,marks2):
        self.marks1 = marks1
        self.marks2 = marks2

    def sum(self, g=None,h=None,i=None):

        f = 0

        if g is not None and h is not None and i is not None:
            f = g+h+i
        elif g is not None and h is not None:
            f = g+h
        else:
            f = g

        return f


d1 = Students(56,25)
# print(d1.sum(4,5)) doesn't work
print(d1.sum(5,6,9))
print(d1.sum(5,6))
print(d1.sum(8))
