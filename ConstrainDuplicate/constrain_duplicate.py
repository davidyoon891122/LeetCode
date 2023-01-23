"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
"""

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if not nums:
            return True

        count_dic = {}

        for i in nums:
            if i in count_dic:
                count_dic[i] += 1
            else:
                count_dic[i] = 1
        
        for value in count_dic.values():
            if value > 1:
                return True
        return False



example_1 = [1,2,3,4]

example_2 = [1, 2, 3, 3, 4, 5, 6, 7]

s = Solution()

result = s.containsDuplicate(nums=example_1)

print(result)