"""
Reverse bits of a given 32 bits unsigned integer.
"""

from collections import deque

class Solution:
    def reverseBits(self, n: int) -> int:
        if n == 0:
            return 0
        result = self.intToBit(n)
        return int(result[::-1],2)
    
    def intToBit(self, n: int) -> str:
        quotient = 0
        remain = 0
        bit = deque([])

        while n > 1:
            quotient = n // 2
            remain = n % 2  
            bit.appendleft(remain)
            n = quotient
        bit.appendleft(1)


        result_bit = "".join(str(e) for e in bit).zfill(32)
        print(result_bit)
        return result_bit


s = Solution()
s.reverseBits(43261596)