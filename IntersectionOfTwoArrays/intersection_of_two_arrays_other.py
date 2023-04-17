"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.
"""

from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        result = set()

        for num in nums1:
            if num not in hash_map:
                hash_map[num] = 1
        
        for num in nums2:
            if num in hash_map:
                result.add(num)
        
        print(result)
        return result





case1_num1 = [1, 2, 2, 1]
case1_num2 = [2, 2]

case2_num1 = [4, 9, 5]
case2_num2 = [9, 4, 9, 8, 4]



s = Solution()

s.intersection(nums1=case1_num1, nums2=case1_num2)

s.intersection(nums1=case2_num1, nums2=case2_num2)