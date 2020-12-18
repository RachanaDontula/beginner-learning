from array import *


vals = array('u', ['c','v','f','h','b','u'])
vals1 = array('i', [5,2,36,51,94,5,2])
print(vals)
print(vals1)
newArr = array(vals.typecode, (a for a in vals))
for b in newArr:
    print(b)


arr = array('i', [])
n = int(input("Enter the length of the array: "))
for i in range(n):
    x = int(input("Enter the next value: "))
    arr.append(x)

print(arr)
print(arr.dtype)

val = int(input("Enter the value: "))
j = 0
for j in arr:
    if j == val:
        print(j)
        break
    j += 1



