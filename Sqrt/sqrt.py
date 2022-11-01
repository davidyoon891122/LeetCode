"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.
You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
"""
class Solution:
    def my_sqrt(self, x: int) -> int:
        r = x
        while r * r > x:
            r = (r + x/r) / 2
            print(r)
        return r 


x_1 = 4
x_2 = 8
x_3 = 25

s = Solution()
print(s.my_sqrt(25))