
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dictionary = {}

        for index, num in enumerate(nums):
            if target - num in result_dictionary:
                return [result_dictionary[target - num], index]
            else:
                result_dictionary[num] = index

        
                



s = Solution()


nums = [2,7,11,15]
target = 9

print(s.twoSum(nums= nums, target= target))