"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_dic = dict()

        for num in nums:
            if num in count_dic:
                return True
            count_dic[num] = 1
        return False




example_1 = [1,2,3,4]

example_2 = [1, 2, 3, 3, 4, 5, 6, 7]

s = Solution()

result = s.containsDuplicate(nums=example_1)

print(result)