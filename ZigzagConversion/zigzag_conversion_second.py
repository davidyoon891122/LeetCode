class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < 0 or numRows > len(s):
            return s

        idx, d = 0, 1

        rows = [[] for _ in range(numRows)]
        
        for char in s:
            rows[idx].append(char)

            if idx == numRows - 1:
                d = -1
            elif idx == 0:
                d = 1
            
            idx += d
        

        for i in range(numRows):
            rows[i] = ''.join(rows[i])

        return ''.join(rows)



s = Solution()
result = s.convert("PAYPALISHIRING", 3)
print(result)