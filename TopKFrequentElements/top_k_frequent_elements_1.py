"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from typing import List
import collections


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = list(zip(*collections.Counter(nums).most_common(k)))[0]
        
        return result
        
s = Solution()

nums = [1,1,1,2,2,3]
k = 2

print(s.topKFrequent(nums, k))