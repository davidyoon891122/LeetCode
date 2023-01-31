"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.
"""

from typing import List

class Solution:
    def summaryRange(self, nums: List[int]) -> List[str]:
        result = []

        if len(nums) == 1 :
            return ["{}".format(nums[0])]

        prev = 0
        first = prev
        for i in range(1, len(nums)):
            print(nums[prev], nums[i])
            if abs(nums[prev] - nums[i]) < 2:
                prev = prev + 1

                if i == (len(nums) - 1):
                    result.append(nums[first:])
                continue
            else:
                result.append(nums[first:i])
                first = i
                prev = prev + 1

                if i == (len(nums) - 1):
                    result.append(nums[i:])

        for i in range(len(result)):
            if len(result[i]) > 2:
                result[i] = "{}->{}".format(result[i][0], result[i][-1])
            elif len(result[i]) == 2:
                result[i] = "{}->{}".format(result[i][0], result[i][1])
            else:
                result[i] = "{}".format(result[i][0])
    
        return result



nums_1 = [0, 1, 2, 4, 5, 7]
nums_2 = [0, 2, 3, 4, 6, 8, 9]
nums_3 = [-1]

s = Solution()
result = s.summaryRange(nums=nums_3)
print(result)