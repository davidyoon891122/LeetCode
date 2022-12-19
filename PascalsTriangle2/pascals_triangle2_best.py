"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""
from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]        
        
        last_row = self.getRow(rowIndex -1)
        res = [1] * (len(last_row) + 1)
        for i in range(len(last_row) - 1):
            res[i+1] = last_row[i] + last_row[i+1]
        return res


rowIndex = 3
result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

s = Solution()

result = s.getRow(rowIndex)

print("result: {}".format(result))