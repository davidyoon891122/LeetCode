"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.
"""

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):    
            result.append(self.getBinary(n=i))

        return result


    def getBinary(self, n: int):
        target = n
        result = []
        while target > 0:
            result.append(target % 2)
            target //= 2
        return result.count(1)

n = 5
s = Solution()

result = s.countBits(n=n)
print(result)

