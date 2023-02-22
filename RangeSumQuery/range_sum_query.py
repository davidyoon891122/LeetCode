"""
Given an integer array nums, handle multiple queries of the following type:

Calculate the sum of the elements of nums between indices left and right inclusive where left <= right.
Implement the NumArray class:

NumArray(int[] nums) Initializes the object with the integer array nums.
int sumRange(int left, int right) Returns the sum of the elements of nums between indices left and right inclusive (i.e. nums[left] + nums[left + 1] + ... + nums[right]).
"""
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = nums
        for i in range(len(nums) - 1):
            self.preSum[i+1] += self.preSum[i]      

    def sumRange(self, left: int, right: int) -> int:
        print(self.preSum)
        if left == 0: return self.preSum[right]
        return self.preSum[right] - self.preSum[left-1]
        
        # return sum(self.nums[left: right + 1])

nums = [-2, 0, 3, -5, 2, -1]

s = NumArray(nums=nums)
result = s.sumRange(0, 5)
print(result)
