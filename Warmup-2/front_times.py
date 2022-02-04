# Given a string and a non-negative int n, we'll say that the front of the string is the first 3 chars, or whatever is there if the string is less than length 3. Return n copies of the front;


def front_times(text, n):

    if len(text) < 3:
        return text
    return text[:3] * n


x = front_times("Chocolate", 2)
y = front_times("Chocolate", 3)
z = front_times("Abc", 3)

print(x, y, z)
