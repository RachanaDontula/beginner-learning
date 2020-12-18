""" we can create object of inner class outside the
inner class and inside the outer class

or

we can create object of inner class outside the outer class
but by using outer class name to call it, eg: Student.Laptop()
"""


class Student:

    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        # creating inner class object outside inner
        # class and inside outer class
        self.lap = self.Laptop()

    # show function helps in place of print function outside class or function
    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    # creating inner class
    class Laptop:

        def __init__(self):
            self.config = 'i5'
            self.ram = 8
            self.gen = 7

        def show(self):
            print(self.config, self.ram, self.gen)


s1 = Student('Rachana',4)
s2 = Student('Sony', 27)

s1.show()
s2.show()
print(id(s1))
print(id(s2))

# creating inner class object outside
# outer class using outer class name to call it
"""
lap1 = Student.Laptop()
"""