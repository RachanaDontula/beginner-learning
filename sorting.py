# Bubble sort
# Swapping: a swap to b is done with taking third variable eg: c
# a assign to c, b assign to a, t assign to a
# smallest value comes first.
# we will have 2 iterations. one for sorting,
# one for repeating iterations.


def sort(l):

    for i in range(len(l)-1,0, -1):
        for j in range(i):
            if l[j] > l[j+1]:
                temp = l[j]
                l[j] = l[j+1]
                l[j+1] = temp


l = [1,6,9,8,5,4,2,3,2254,12,95,51,0]

sort(l)
print(l)


# Selection sort:
# we should find minimum value in the list for every iteration,
# finally we will get sorted array/list.
# min value is found by comparing 2 values and swap direct positions.


def sort1(list):
    for k in range(len(list)):
        min = k
        for g in range(k+1, len(list)):
            if list[g] < list[min]:
                min = g

        list[k], list[min] = list[min], list[k]
        print(list)


list = [5,9,1,6,10,2]
sort1(list)
print(list)

