"""
Reverse bits of a given 32 bits unsigned integer.
"""

from collections import deque

class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            print("ans: {}".format(ans))
            n >>= 1
        return ans


s = Solution()
print(s.reverseBits(43261596))