"""
Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.
"""

def length_of_last_word(s: str) -> int:
    first_list = s.split(" ")
    print(" ".join(first_list).split())
    return len(" ".join(first_list).split()[-1])


print(length_of_last_word("4214 1 23 1 32 32 test of  34 3   "))