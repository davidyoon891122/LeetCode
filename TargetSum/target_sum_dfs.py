"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
"""

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        count = 0
        
        def dfs(index, total):
          nonlocal count
          
          if index == len(nums):
            if total == target:
              count += 1
            return
          
          dfs(index + 1, total + nums[index])  # 1, 1 -> 2, 2, 2, 0
          dfs(index + 1, total - nums[index])  # 1, -1 -> 2, -2, 2, 0
          
        dfs(0, 0)
        
        return count 
        
        


nums = [1, 1, 1, 1, 1]
target = 3  # (target + totalSum) / 2  -> 4

s = Solution()

print(s.findTargetSumWays(nums, target))