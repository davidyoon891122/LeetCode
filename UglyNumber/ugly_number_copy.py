"""
An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.
Given an integer n, return true if n is an ugly number.
"""


class Solution:
    def isUgly(self, n: int) -> bool:
        while n != 0 and n % 2 == 0:
            n //= 2
        while n != 0 and n % 3 == 0:
            n //= 3
        while n != 0 and n % 5 == 0:
            n //= 5
        if n == 1:
            return True
        return False

            




s = Solution()

result = s.isUgly(11)

print(result)