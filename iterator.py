"""
iter is a inbuilt method.
iter.__next__() or next(iter) returns value in list.
iter gives object of iterator, next gives next value in iterator.
creating own iterator: can create only by using iter and next methods.
"""


class TopTen:
    def __init__(self):
        self.nums = 1

    def __iter__(self):  # creating iter method
        return self

    def __next__(self):  # creating next method

        if self.nums <= 10:  # here condition is necessary to give an end in output
            val = self.nums
            self.nums+= 1

            return val
        else:
            raise StopIteration  # we can stop running in output continuously
            # only by raising an exception.


values = TopTen()  # creating object
print(next(values))  # one way of printing iterator value
for i in values:
    print(i)


"""
class Topten:
def __init__(self):
self.nums = 1
def __iter__(self):
return self
def __next__(self):
if val <= 10:
val = self.nums
self.nums += 1
return value
else:
raise stopiterator

val = Topten()
for i in val:
print(i)

"""
