"""
494. Target Sum
You are given an integer array nums and an integer target.

You want to build an expression out of nums by adding one of the symbols '+' and '-' before each integer in nums and then concatenate all the integers.

For example, if nums = [2, 1], you can add a '+' before 2 and a '-' before 1 and concatenate them to build the expression "+2-1".
Return the number of different expressions that you can build, which evaluates to target.
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)

        if (total + target) % 2 != 0 or abs(target) > total:
            return 0

        p = (total + target) // 2


        dp = [0] * (p + 1)
        dp[0] = 1

        for num in nums:
            for i in range(p, num - 1, -1):
                dp[i] += dp[i - num]

        return dp[p]




s = Solution()

print(s.findTargetSumWays([1, 1, 1], 1))  # Output: 5