"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

from typing import List

class Solution:
    def moveZeros(self, nums: List[int]) -> None:
        zero = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero] = nums[zero], nums[i] 
                print(nums)
                zero += 1

        print(nums)
        


nums = [0, 1, 0, 3, 12]
s = Solution()

s.moveZeros(nums=nums)