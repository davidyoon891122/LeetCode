"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
"""

from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict = {}
        freqs_heap = []
        for num in nums:
          if num in dict:
            dict[num] += 1
          else:
            dict[num] = 1   
          
        for key, value in dict.items():
          heapq.heappush(freqs_heap, ((-value), key))
        
        print(freqs_heap)
        
        topk = list()
        for _ in range(k):
          topk.append(heapq.heappop(freqs_heap)[1])
        
        return topk
        
s = Solution()

nums = [1,1,1,2,2,3]
k = 2

print(s.topKFrequent(nums, k))