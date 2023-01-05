"""
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
"""


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        dic = {0: 'A', 1: 'B', 2: 'C', 3: 'D', 4: 'E', 5: 'F', 6: 'G', 7: 'H', 8: 'I', 9: 'J', 10: 'K', 11: 'L', 12: 'M', 13: 'N', 14: 'O', 15: 'P', 16: 'Q', 17: 'R', 18: 'S', 19: 'T', 20: 'U', 21: 'V', 22: 'W', 23: 'X', 24: 'Y', 25: 'Z'}
        result = []
        num = columnNumber
        while num > 0:
            result.append(dic[(num - 1) % 26])
            num = (num - 1) // 26
        result.reverse()
        return ''.join(result)
    
            


s = Solution()

result = s.convertToTitle(1000)
print(result)