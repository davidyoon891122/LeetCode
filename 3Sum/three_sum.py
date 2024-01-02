"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
"""

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        negative, positive, zero = [], [], []
        result = set()
        for num in nums:
            if num == 0:
                zero.append(num)
            elif num < 0:
                negative.append(num)
            elif num > 0:
                positive.append(num)

        print("negative: {}, positive: {}, zero: {}".format(negative, positive, zero))

        negative_set = set(negative)
        positive_set = set(positive)

        if zero:
            for num in negative:
                if num * -1 in positive:
                    result.add((0, num, num * -1))

        if len(zero) >= 3:
            result.add((0, 0, 0))

        for i in range(len(positive)):
            for j in range(i + 1, len(positive)):
                target = -1 * (positive[i] + positive[j])
                if target in negative_set:
                    result.add((positive[i], positive[j], target))
        
        for i in range(len(negative)):
            for j in range(i+1, len(negative)):
                target = -1 * (negative[i] + negative[j])
                if target in positive:
                    result.add((negative[i], negative[j], target))

        print(list(result))




nums_1 = [-1, 0, 1, 2, -1, -4]
nums_2 = [0, 1, 1]
nums_3 =  [0, 0, 0]

s = Solution()

s.threeSum(nums=nums_1)

s.threeSum(nums=nums_2)

s.threeSum(nums=nums_3)
