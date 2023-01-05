"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
"""

class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
        result = []

        while columnNumber > 0:
            print(result)
            result.append(capitals[(columnNumber - 1)% 26])
            columnNumber = (columnNumber - 1) // 26
        result.reverse()
        return ''.join(result)
    

s = Solution()

result = s.convertToTitle(1000)
print(result)