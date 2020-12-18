
# linear search
position = -1


def search(list, n):
    for i in range(len(list)):
        if list[i] == n:
            globals()['position'] = i
            return True

    return False


list = [1,5,6,8,7,4]

n = 8
if search(list, n):
    print("Found in ", position)
else:
    print("not found")


# Binary search:
#
# If there are more no of values, binary search is used
# All values should be sorted in binary search in the first.
# we have lower bound and upper bound for he values and also mid value.
# we have to find the mid value by using (L+U)/2 formula, using indexes.
# If the value of mid index matches the number we search, match found.
# If not matched, the lower bound index will shift to next value.
# Again, we have to find the mid index and find the match.
# process continues till match is found.


def Search1(list, m):
    lower = 0
    upper= len(list)-1
    while lower <= upper:
        mid = (lower + upper) // 2
        if list[mid] == m:
            globals()['position'] = mid
            return True
        else:
            if list[mid] < m:
                lower = mid+1
            else:
                upper = mid-1

    return False


list = [5,7,9,11,13,45,99,105]

m = 4

if Search1(list, m):
    print('match found', position)
else:
    print('Match not found')