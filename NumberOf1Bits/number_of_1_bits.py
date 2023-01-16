"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(self.intToBit(n))

    def intToBit(self, n: int) -> int:
        
        result = []
        while n > 0:
            remain = n % 2
            result.append(remain)
            n = n // 2

        result.reverse()
        print(result)
        return result
    
s = Solution()

print(s.hammingWeight(10))