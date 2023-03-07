"""
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
"""


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        target = n
        
        while target > 1:
            remainder = target % 4
            if remainder != 0:
                return False
            target /= 4
        return True
    

s = Solution()


for i in range(100):
    print("{}: {}".format(i, s.isPowerOfFour(n=i)))