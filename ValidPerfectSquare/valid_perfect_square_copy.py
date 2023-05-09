"""
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.
"""

from typing import Optional

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left, right = 0, num

        while left <= right:
            print("left: {}, right: {}".format(left, right))
            mid = (left + right) // 2
            if mid * mid == num:
                return True
            elif mid * mid < num:
                left = mid + 1
            else:
                right = mid - 1
        return False

        



num_ex1 = 16
num_ex2 = 14

s = Solution()
print(s.isPerfectSquare(num=num_ex1))

