"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
"""

import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return not math.log2(n) % 1
            


s = Solution()

for i in range(100):
    print("{}: {}".format(i,s.isPowerOfTwo(n=i)))