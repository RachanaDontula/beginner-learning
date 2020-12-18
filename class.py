class Matrimony:

    def properties(self):
        print("Black, 5.7', 58")


match1 = Matrimony()
match2 = Matrimony()  # can create many objects for same class

a = 'sd'
print(type(a))  # here str is also an object
print(type(match1))  # prints method name as class

b = 9
print(type(b))  # int is also an object

Matrimony.properties(match1)  # calling method
match1.properties()   # calling method type2
match2.properties()
