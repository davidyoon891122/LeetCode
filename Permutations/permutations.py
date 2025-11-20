"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""

from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        prev_elements = []
      
        def dfs(elements):
          if len(elements) == 0:
            result.append(prev_elements[:])
            
          for e in elements:
            next_elements = elements[:]
            next_elements.remove(e)
            prev_elements.append(e)
            dfs(next_elements)
            prev_elements.pop()
        
        dfs(nums)
        
        return result
      
      
nums = [1,2,3]

s = Solution()
s.permute(nums)