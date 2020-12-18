"""
Generators gives iterator, no need to create iter and next functions.
In place of return inside a function, yield should be written, yield works as
generator.
return terminates the loop, yield doesn't terminate loop.
Using Generator, we can fetch one by one value at a time instead
of fetching entire list unlike iterator.
"""


def topten():
    n = 1

    while n <= 10:
        sq = n*n
        yield sq
        n+=1


vals = topten()
for i in vals:
    print(i)
