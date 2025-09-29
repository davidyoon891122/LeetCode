
"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        
        count_dic = {}

        target_set = set(arr)

        for i in target_set:
          count_dic[i] = arr.count(i)

          
        values = count_dic.values()

        return len(values) == len(set(values))


s = Solution()

example_1 = [1, 2, 2, 1, 1, 3]

result_1 = s.uniqueOccurrences(arr=example_1)
print(result_1)