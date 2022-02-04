# Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.


def string_match(a, b):

    # figure the shorter string

    shorter = min(len(a), len(b))

    count = 0

    for _ in range(shorter - 1):
        a_sub = a[_ : _ + 2]
        b_sub = b[_ : _ + 2]
        if a_sub == b_sub:
            count += 1

    return count


x = string_match("xxcaazz", "xxbaaz")
y = string_match("abc", "abc")
z = string_match("abc", "axc")

print(x, y, z)
