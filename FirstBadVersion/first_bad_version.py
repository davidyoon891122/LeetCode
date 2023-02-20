"""
You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.
"""

import random

class Solution:
    def __init__(self, n: int, badVersion: int):
        self.n = 50
        self.badVersion = badVersion

    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right:
            mid = (left + right) >> 1
            if not self.isBadVersion(t=mid):
                left = mid + 1
            else:
                if not self.isBadVersion(mid - 1):
                    return mid
                else:
                    right = mid - 1
              
            
    def isBadVersion(self, t: int) -> bool:
        return t >= self.badVersion

num = 50
num2 = 200

s = Solution(n=50, badVersion=25)

result = s.firstBadVersion(n=num)

print("result: {}".format(result))