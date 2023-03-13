"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        s[:] = s[::-1]
        print(s)

string_array = ['h', 'e', 'l', 'l', 'o']

s = Solution()
s.reverseString(s=string_array)
