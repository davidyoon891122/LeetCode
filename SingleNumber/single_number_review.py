"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = {}

        for num in nums:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        
        for key, value in dic.items():
            if value == 1:
                return key



s = Solution()



s.singleNumber([2,2,1])
