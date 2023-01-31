"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
"""

from typing import List

class Solution:
    def summaryRange(self, nums: List[int]) -> List[str]:
        if len(nums) == 0:
            return []

        i = nums[0]
        j = nums[0]

        ans = []

        for t in range(1, len(nums)):
            if(nums[t]-j==1):
                j = nums[t]
            else:
                if (i == j):
                    ans.append(str(i))
                else:
                    ans.append(str(i)+"->"+str(j))
                i = nums[t]
                j = nums[t]
        if(i==j):
            ans.append(str(i))
        else:
            ans.append(str(i)+"->"+str(j))
        return ans



nums_1 = [0, 1, 2, 4, 5, 7]
nums_2 = [0, 2, 3, 4, 6, 8, 9]
nums_3 = [-1]

s = Solution()
result = s.summaryRange(nums=nums_2)
print(result)