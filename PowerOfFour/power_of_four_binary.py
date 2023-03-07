"""
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

import re

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return bool(re.match(r'0b1(00)*$', bin(n)))


num = 28
s = Solution()
for i in range(200):
    result = s.isPowerOfThree(n=i)
    print("{} : {}".format(i, result))