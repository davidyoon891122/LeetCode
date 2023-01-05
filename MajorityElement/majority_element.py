"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count_dic = {}

        for i in range(len(nums)):
            if nums[i] in count_dic:
                count_dic[nums[i]] += 1
            else:
                count_dic[nums[i]] = 1
        
        return max(count_dic, key= lambda x: count_dic[x])


nums = [3,2,3]

s = Solution()
s.majorityElement(nums)


