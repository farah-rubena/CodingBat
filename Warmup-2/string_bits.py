# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".


def string_bits(text):

    new_str = ""

    for char in range(0, len(text)):
        if char % 2 == 0:
            new_str += text[char]

    return new_str


x = string_bits("Hello")
y = string_bits("Hi")
z = string_bits("Heeololeo")

print(x, y, z)
