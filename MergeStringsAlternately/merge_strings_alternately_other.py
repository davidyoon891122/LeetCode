"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
"""

import collections

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        max_length = max(len(word1), len(word2))

        for i in range(max_length):
            if i < len(word1):
                result += word1[i]
            if i < len(word2):
                result += word2[i]
        
        print(result)
        return result


word1_1 = "abc"
word2_1 = "pqr"

s = Solution()

s.mergeAlternately(word1=word1_1, word2=word2_1)