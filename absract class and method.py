"""
Python doesn't support abstract classes and methods directly,
we have module(ABC) to support abstract classes.
ABC - Abstract base classes, we can create our own abstract class by using this.
Abstract methods:   A method which has only declaration but no body
is called abstract method.
Abstract class: A class which has abstract methods is called Abstract class.
we cannot create object for abstract class


"""

from abc import ABC, abstractmethod


class A(ABC):
    @abstractmethod  # decorator
    def B(self):
        pass        # abstract class


class D(A):

    def B(self):
        print("Hi")


b1 = D()
b1.B()
# TypeError: Can't instantiate abstract class B with abstract methods B
# this error occurs if child class also doesn't have anything in it
