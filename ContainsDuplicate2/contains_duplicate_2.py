"""
Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
"""

from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            else:
                dic[v] = i
        return False

example = [1, 2, 3, 1]
k = 4

example_2 = [1,2,3,1,2,3]
k_2 = 2

example_3 = [1,0,1,1]
k_3 = 1


s = Solution()
result = s.containsNearbyDuplicate(nums=example_3, k=k_3)
print(result)