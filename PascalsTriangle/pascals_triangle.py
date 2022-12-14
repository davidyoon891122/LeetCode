"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown
"""
from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = [[1]*(i+1) for i in range(numRows)]
        print(pascal) 

        for i in range(2, numRows):
            for j in range(1, i):
                print("{} = {} + {}".format(pascal[i][j], pascal[i-1][j-1], pascal[i-1][j]))
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        print(pascal)

numRows = 5
result = [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]

s = Solution()

s.generate(numRows)