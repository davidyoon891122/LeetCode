"""
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        return n > 0 and pow(3, 32) % n == 0


num = 28
s = Solution()
for i in range(200):
    result = s.isPowerOfThree(n=i)
    print("{} : {}".format(i, result))