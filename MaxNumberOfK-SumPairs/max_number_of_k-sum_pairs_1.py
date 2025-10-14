"""
1679. Max Number of K-Sum Pairs

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.
"""

from typing import List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dic = {} 
        operations = 0
        
        for num in nums:
            if dic.get(k - num, 0) > 0:
                dic[k - num] -= 1
                operations += 1
            else:
                dic[num] = dic.get(num, 0) + 1
        
        return operations

s = Solution()

nums = [1, 2, 3, 4]
k = 5

s.maxOperations(nums, k)
