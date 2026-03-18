"""
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
"""

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        
        if (target + total) % 2 != 0 or total < abs(target):
          return 0
        
        s = (target + total) // 2
        dp = [0] * (s + 1)
        dp[0] = 1
        
        for num in nums:
          for i in range(s, num - 1, -1):
            dp[i] += dp[i - num]
            
        return dp[s]
        
        
        
        


nums = [1, 1, 1, 1, 1]
target = 3  # (target + totalSum) / 2  -> 4

s = Solution()

s.findTargetSumWays(nums, target)