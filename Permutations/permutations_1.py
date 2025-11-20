"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

from typing import List
import itertools

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums))
      
      
nums = [1,2,3]

s = Solution()
print(s.permute(nums))