"""
Variable is of 2 types
1.Instance variable:
as the object changes the value also changes only for that object.
we can define a variable inside init method, inside a class
2.Class(Static) variable:
we can define a variable outside the init method, inside class.
as the value changes, all the objects are changed, because, they are shared.


namespace: space where objects and variables are created and stored
1.class namespace: class variables are stored
2.variable /instance namespace: where variables or instance are created
"""


class Car:

    wheels = 4  # static/class variable which is outside __init__ method

    def __init__(self):
        self.milage = 10   # objects: milage, company
        self.company = "BMW"  # these are instance variables


c1 = Car()
c2 = Car()

c1.milage = 5
# as milage is object/instance and has instance namespace,
# only the object value is changed


Car.wheels = 5
# as wheels is class namespace/static namespace, and shared,
# whole values of objects are changed
print("for c1 object: \nCompany: {}, Milage: {}, Wheels: {}".format(c1.company, c1.milage, c1.wheels))
print("for c2 object: \nCompany: {}, Milage: {}, Wheels: {}".format(c2.company, c2.milage, c2.wheels))
