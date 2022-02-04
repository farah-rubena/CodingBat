# Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.


def array_front9(arr):

    end = len(arr)

    if end > 4:
        end = 4

    for _ in range(end):
        if arr[_] == 9:
            return True
    return False


x = array_front9([1, 2, 9, 3, 4])
y = array_front9([1, 2, 3, 4, 9])
z = array_front9([1, 2, 3, 4, 5])

print(x, y, z)
