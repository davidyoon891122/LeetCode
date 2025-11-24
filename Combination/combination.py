"""
Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

You may return the answer in any order.
"""

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        
        def dfs(elements, start: int, k: int):
          if k == 0:
            result.append(elements[:])
            return
          
          for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k -1)
            elements.pop()

        dfs([], 1, k)
        return result
            