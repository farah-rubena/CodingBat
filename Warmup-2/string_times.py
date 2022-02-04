# Given a string and a non-negative int n, return a larger string that is n copies of the original string.


def string_times(text, n):

    return text * n


x = string_times("Hi", 2)
y = string_times("Hi", 3)
z = string_times("Hi", 1)

print(x, y, z)
