"""
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.
"""

import math

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        a = math.sqrt(num)

        front = int(a)

        back = a - front
        

        print("front: {}, back: {}".format(front, back))

        if back == 0:
            print("True")            
            return True
        else:
            return False



num_ex1 = 16
num_ex2 = 14

s = Solution()
s.isPerfectSquare(num=num_ex1)

