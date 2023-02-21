"""
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in s.
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        sList = s.split(" ")
        dic = {}

        if len(pattern) != len(sList) or len(set(pattern)) != len(set(sList)):
            return False
        
        for i, c in enumerate(pattern):
            if c in dic:
                if dic[c] != sList[i]:
                    return False
            else:
                dic[c] = sList[i]
        return True


pattern = "abba"
word = "dog cat cat dog"

s = Solution()

result = s.wordPattern(pattern=pattern, s=word)
print(result)