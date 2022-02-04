# Given a non-empty string like "Code" return a string like "CCoCodCode".


def string_splosion(text):

    new_str = ""

    for char in range(len(text)):
        new_str += text[: char + 1]
    return new_str


x = string_splosion("Code")
y = string_splosion("abc")
z = string_splosion("ab")

print(x, y, z)
