from numpy import *
import numpy as np
arr = np.array([[1,2,3], [4,5,6], [9,4,8]], np.float)
arr1 = np.array([1,2,3,4,5,6])
print(arr)
print(arr.dtype)
print(arr.shape)
x=np.reshape(arr1,(3,2))
print(x)
y = np.ravel(arr)
print(y)

arr2 = linspace(0,15, 16) # divides into 16 parts
print(arr2)
arr3 = arange(0,15,3) # skips 3 nums in between
print(arr3)
arr4 = logspace(0,40,5) # space will be log2 calue in between
print(arr4)
print(arr4[1])
arr5 = zeros(5)  # to create an array with all values starts with zero
print(arr5)
arr6 = ones(6)
print(arr6)
arr7 = [1,9,6,4,8,7]
print(arr1)
for a in arr1:
    arr1 += 5
    print(arr1)
    break

arr8 = arr1+ arr7
print(arr8)

print(sin(arr8))
print(cos(arr8))
print(log(arr8))
print(sqrt(arr8))
print(min(arr8))
print(max(arr8))
print(sort(arr8))
print(unique(arr8))
print(concatenate([arr8,arr1]))

arr8 = arr7  # copy
print(arr7)
print(arr8)
print(id(arr8))
print(id(arr7))

arr7[1] = 10

print(arr7)  # shallow copy
print(arr8)

# arr8 = arr7.copy()  # deep copy
# arr8 = arr7.view()  # address different

arr10 = array([[1,2,3,4,5,6],[4,5,6,7,8,9]])
arr9 = arr10.reshape(2,2,3)
print(arr9)
print(arr10.ndim)
print(arr10.size)
print(arr10.flatten())

arr11 = array([[1,2,3,4],[5,6,7,8]])
m = matrix(arr11)
print(m)
m1 = matrix('1,2,3,4; 5,6,7,8; 7,8,5,6')
print(m1)
print(diagonal(m1))
print(m.min())
print(m.max())
m2 = matrix('1,2,3,4; 4,5,6,7; 5,6,7,8')
print(m1+m2)

# matrix multiplication:

