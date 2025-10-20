"""
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k].

If no such indices exists, return false.
"""

from typing import List

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')
        second = float('inf')

        for num in nums:
            if num <= first:
                first = num
            elif num <= second:
                second = num
            else:
                return True
            
        return False 
            


s = Solution()

print(s.increasingTriplet([1,2,3,4,5]))
print(s.increasingTriplet([5,4,3,2,1]))
print(s.increasingTriplet([2,1,5,0,4,6]))