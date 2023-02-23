"""
Given an integer n, return true if it is a power of three. Otherwise, return false.
An integer n is a power of three, if there exists an integer x such that n == 3x.
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        target = n

        while target > 1:
            remainder = target % 3
            if remainder != 0:
                return False
            target /= 3
        return True


num = 28
s = Solution()
for i in range(200):
    result = s.isPowerOfThree(n=i)
    print("{} : {}".format(i, result))