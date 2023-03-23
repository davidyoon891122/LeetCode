"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Given a roman numeral, convert it to an integer.
"""


# 
class Solution:
    def romanToInt(self, s: str) -> int:
        romanDic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0
        

        for i in range(0,len(s)-1):
            if romanDic[s[i]] > romanDic[s[i+1]]:
                result += romanDic[s[i]]
            else:
                result -= romanDic[s[i]]

        result += romanDic[s[-1]]
        return result
        
s = Solution()

result = s.romanToInt("MCMXCIV")
print(result)