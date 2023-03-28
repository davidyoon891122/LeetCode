"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""

from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDic = {}
        for index, num in enumerate(nums):
            if target - num in numDic:
                return [numDic[target - num], index]
            else:
                numDic[num] = index
        return []
    

s = Solution()

print(s.twoSum(nums=[2,7,11,15], target=9))