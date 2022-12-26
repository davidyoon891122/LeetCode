"""
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        print("sigleNumber: {}".format(nums))
        nums_dic = {}

        for i in range(len(nums)):
            if nums[i] not in nums_dic:
                nums_dic[nums[i]] = 1
            else:
                nums_dic[nums[i]] += 1
        print(nums_dic)

        for key, value in nums_dic.items():
            if value == 1:
                return key





nums_1 = [2, 2, 1]
nums_2 = [4, 1, 2, 1, 2]
nums_3 = [1]


s = Solution()

result = s.singleNumber(nums_1)
print("result: {}".format(result))