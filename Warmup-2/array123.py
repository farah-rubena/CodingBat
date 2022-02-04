# Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.


def array123(arr):

    for _ in range(len(arr) - 2):
        if arr[_] == 1 and arr[_ + 1] == 2 and arr[_ + 2] == 3:
            return True
    return False


x = array123([1, 1, 2, 3, 1])
y = array123([1, 1, 2, 4, 1])
z = array123([1, 1, 2, 1, 2, 3])

print(x, y, z)
