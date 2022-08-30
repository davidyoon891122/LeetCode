"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
"""

def isValid(s: str) -> bool: 
    parentheses_dictionary = {
        ']': '[',
        ')': '(',
        '}': '{'
    }
    stack = []
    opening = set('([{')
    closing = set(')]}')

    for char in s:
        if char in opening:
            stack.append(char)
        if char in closing:
            if not stack:
                return False
            elif stack.pop() != parentheses_dictionary[char]:
                return False
            else:
                continue
    if not stack:
        return True
    else:
        return False 




test_1 = "()" # result True case
test_2 = "()[]{}" # result True case
test_3 = "(]" # result False case
test_4 = "[" # result False case
test_5 = "" # result False case
test_6 = "[)(]" # result False case 
test_7 = "{[]}" # result True case 
print("Test Result: {}".format(isValid(test_1)))
print("Test Result: {}".format(isValid(test_2)))
print("Test Result: {}".format(isValid(test_3)))
print("Test Result: {}".format(isValid(test_4)))
print("Test Result: {}".format(isValid(test_5)))
print("Test Result: {}".format(isValid(test_6)))
print("Test Result: {}".format(isValid(test_7)))
# print("Test Result: {}".format(isValid(test_2)))