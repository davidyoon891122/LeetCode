"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
"""

# abcdefghijklm  numRows: 3
# 1232123212321
# aeim
# bdfhl
# cgk

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        
        idx, d = 0, 1

        rows = [[] for _ in range(numRows)]


        for char in s:
            rows[idx].append(char)

            if idx == 0:
                d = 1
            elif idx == numRows - 1:
                d = -1

            idx += d

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)



s = Solution()

result = s.convert("PAYPALISHIRING", 3)
print(result)
