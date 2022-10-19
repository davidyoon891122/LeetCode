"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

# s = What can i get for you ?
def length_of_last_word(s: str) -> int:
    lenLast = 0

    for i in range(len(s) - 1, -1, -1):
        if s[i] != ' ':
            lenLast += 1
        elif lenLast > 0:
            break
    return lenLast



s = "What can i get for you ?    "
test_2 = "4214 1 23 1 32 32 test of  34 3   test  "
print(length_of_last_word(s))
print(length_of_last_word(test_2))
