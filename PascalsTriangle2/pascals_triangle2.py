"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [[] for _ in range(rowIndex + 1)]

        for row_index, row_array in enumerate(res):
            current_index = row_index + 1
            while len(row_array) < current_index:
                if len(row_array) == 0 or len(row_array) == current_index - 1:
                    row_array.append(1)
                else:
                    row_array.append(res[row_index-1][len(row_array) - 1] + res[row_index-1][len(row_array)])
        return res[rowIndex]          
        

rowIndex = 4
result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

s = Solution()

result = s.generate(rowIndex)

print("result: {}".format(result))