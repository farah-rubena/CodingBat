# Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).


def last2(text):

    if len(text) < 2:
        return 0

    last_two = text[-2:]

    count = 0

    for _ in range(len(text) - 2):
        if text[_ : _ + 2] == last_two:
            count += 1

    return count


x = last2("hixxhi")
y = last2("xaxxaxaxx")
z = last2("axxxaaxx")

print(x, y, z)
