"""
Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:

answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
Note that the integers in the lists may be returned in any order.
"""

from typing import List

class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1, s2 = set(nums1), set(nums2)
        
        res1 = []
        res2 = []

        for x in nums1:
            if x not in s2 and x not in res1:
                res1.append(x)

        for x in nums2:
            if x not in s1 and x not in res2:
                res2.append(x)

        return [res1, res2]
        


# [[1,3], [4,6]]

s = Solution()


example_1_first = [1,2,3]
example_1_second = [2,4,6]

result = s.findDifference(example_1_first, example_1_second)
print(result)