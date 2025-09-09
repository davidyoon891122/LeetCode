"""
You are given an integer array nums consisting of n elements, and an integer k.

Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""


# nums = [1, 12, -5, -6, 50, 3] k = 4
# output = 12.75000

from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        array_sum = sum(nums[:k])
        result = array_sum / k

        for i in range(k, len(nums)):
            array_sum += nums[i] - nums[i - k]
            result = max(result, array_sum / k)

        return result


        



example1_array = [1, 12, -5, -6, 50, 3]
example1_k = 4

example2_array = [5]
example2_k = 1

example3_array = [0,1,1,3,3]
example3_k = 4

example4_array = [8860,-853,6534,4477,-4589,8646,-6155,-5577,-1656,-5779,-2619,-8604,-1358,-8009,4983,7063,3104,-1560,4080,2763,5616,-2375,2848,1394,-7173,-5225,-8244,-809,8025,-4072,-4391,-9579,1407,6700,2421,-6685,5481,-1732,-8892,-6645,3077,3287,-4149,8701,-4393,-9070,-1777,2237,-3253,-506,-4931,-7366,-8132,5406,-6300,-275,-1908,67,3569,1433,-7262,-437,8303,4498,-379,3054,-6285,4203,6908,4433,3077,2288,9733,-8067,3007,9725,9669,1362,-2561,-4225,5442,-9006,-429,160,-9234,-4444,3586,-5711,-9506,-79,-4418,-4348,-5891]
example4_k = 93

s = Solution()
# print(s.findMaxAverage(nums=example1_array, k=example1_k))
# print(s.findMaxAverage(nums=example2_array, k=example2_k))
# print(s.findMaxAverage(nums=example3_array, k=example3_k))
print(s.findMaxAverage(nums=example4_array, k=example4_k))
