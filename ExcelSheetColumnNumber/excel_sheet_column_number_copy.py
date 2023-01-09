"""
Given a string columnTitle that represents the column title as appears in an Excel sheet, return its corresponding column number.
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = 0
        for c in range columnTitle:
            column_number = column_number * 26 + ord(c) - ord('A') + 1
            print(column_number)

s = Solution()

s.titleToNumber("ALL")