"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer.

The algorithm for myAtoi(string s) is as follows:

Whitespace: Ignore any leading whitespace (" ").
Signedness: Determine the sign by checking if the next character is '-' or '+', assuming positivity is neither present.
Conversion: Read the integer by skipping leading zeros until a non-digit character is encountered or the end of the string is reached. If no digits were read, then the result is 0.
Rounding: If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then round the integer to remain in the range. Specifically, integers less than -231 should be rounded to -231, and integers greater than 231 - 1 should be rounded to 231 - 1.
Return the integer as the final result.
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        char_arr = list(s)
        print(char_arr)

        current_char = ''

        for i in range(1, len(char_arr)):
            if char_arr[i] == '':
                return 
            else:
                current_char = char_arr[i - 1]
                print(current_char)

s = Solution()

ex = "42"
ex2 = " -042"
ex3 = "1337c0d3"
ex4 = "0-1"

targets = [
    ex, ex2, ex3, ex4
]

for target in targets:
    s.myAtoi(target)

