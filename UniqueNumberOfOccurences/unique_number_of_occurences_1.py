
"""
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
"""

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count_dic = {}

        for i in arr:
            if i in count_dic:
                count_dic[i] += 1
            else:
                count_dic[i] = 1
        values = set(count_dic.values())
        return len(values) == len(count_dic)
        


s = Solution()

example_1 = [1, 2, 2, 1, 1, 3]

result_1 = s.uniqueOccurrences(arr=example_1)
print(result_1)