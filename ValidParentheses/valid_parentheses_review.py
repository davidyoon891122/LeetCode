"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

from collections import deque

def isValid(s: str) -> bool: 
    stack = deque()

    parentheses_dictionary = {
        '[': ']',
        '(': ')',
        '{': '}'
    }

    for char in s:
        if char in parentheses_dictionary:
            stack.append(char)
        else:
            if (len(stack) and parentheses_dictionary[stack[-1]] == char):
                stack.pop()
            else:
                return False
    return len(stack) == 0



test_1 = "()" # result True case
test_2 = "()[]{}" # result True case
test_3 = "(]" # result False case
test_4 = "[" # result False case
test_5 = "" # result False case
test_6 = "[)(]" # result False case 
test_7 = "{[]}" # result True case 

tests = [
    test_1, test_2,
    test_3, test_4,
    test_5, test_6,
    test_7
]

for index, value in enumerate(tests):
    print("Test_{}: {} , Result: {}".format(index + 1, value ,isValid(value)))