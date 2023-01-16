"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        ans = 0
        while n:
            n = n & (n - 1)
            print(n)
            ans += 1
        return ans
    
s = Solution()

s.hammingWeight(10)