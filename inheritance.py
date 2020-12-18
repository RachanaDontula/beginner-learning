# single level inheritance
class A:
    def feature1(self):
        print('feature1 is working')

    def feature2(self):
        print('feature2 is working')


class B(A):  # inheriting A(single level)
    def feature3(self):
        print('feature3 is working')

    def feature4(self):
        print('feature4 is working')


# multilevel inheritance(inheriting B which has A)
class C(B):
    def feature5(self):
        print('feature5 is working')


class D:
    def feature6(self):
        print('feature6 is working')


# multiple inheritance(inheriting A and D)
class E(A,D):
    def feature7(self):
        print('feature7 is working')


# defining objects(constructors)
a1 = A()
b1 = B()
c1 = C()
d1 = D()
e1 = E()

# calling functions

a1.feature2()
a1.feature1()
b1.feature2()
b1.feature1()
b1.feature3()
b1.feature4()
c1.feature1()
c1.feature3()
c1.feature2()
c1.feature4()
c1.feature5()
d1.feature6()
e1.feature1()
e1.feature2()
e1.feature6()
e1.feature7()

"""Constructor behaviour: 
if we create object of sub class, it will first try to find init 
function of sub class, if it is not found, it calls init of 
super class.
Use of Super() inheritance:
If we have called Super then it will first call init of super class
then call init of subclass.(eg: super().__init__())
Method Resolution Order:
when we have multiple super classes, it takes first super class first
# execution starts from left to right.
We can use Super class to call other methods also."""
