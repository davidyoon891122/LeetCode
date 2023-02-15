"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        print(nums)
        if nums[0] != 0:
            return 0
        if len(nums) == 1:
            if nums[0] != 0:
                return nums[0] - 1

        for i in range(1, len(nums)):
            if (nums[i] - nums[i - 1]) != 1:
                return nums[i-1] + 1 
        return nums[-1] + 1


nums = [1, 4, 3, 2, 6]
nums_2 = [3,0,1]
nums_3 = [0, 1]
s = Solution()

print(s.missingNumber(nums=nums_3))