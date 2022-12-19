"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[] for _ in range(numRows)]
        for numRow, row in enumerate(ret): # [[], [], [], [], []]
            currentRow = numRow + 1
            while len(row) < currentRow: # row should be bigger than currentRow if 1 len(row) must be 2
                if len(row) == 0 or len(row) == currentRow-1: # Add append(1) when first index and last index
                    row.append(1)
                else:
                    print(row)
                    row.append(ret[currentRow-2][len(row) - 1] + ret[currentRow-2][len(row)])
        return ret

numRows = 5
result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

s = Solution()

result = s.generate(numRows)

print("result: {}".format(result))