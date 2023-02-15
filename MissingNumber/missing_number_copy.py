"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)

        return n * (n + 1) / 2 - sum(nums)


nums = [1, 4, 3, 2, 6]
nums_2 = [3,0,1]
nums_3 = [0, 1]
s = Solution()

print(s.missingNumber(nums=nums_3))