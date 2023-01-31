"""
Given an integer n, return true if it is a power of two. Otherwise, return false.
An integer n is a power of two, if there exists an integer x such that n == 2x.
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        if n < 0:
            return False
        
        target = n

        while target > 1:
            remainer = target % 2
            target = target // 2 

            if remainer == 1:
                return False
        return True
            



n = 2
s = Solution()

for i in range(100):
    print("{}: {}".format(i,s.isPowerOfTwo(n=i)))