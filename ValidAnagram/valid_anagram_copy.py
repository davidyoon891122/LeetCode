"""
Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""

"""
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = "abcdefghijklmnopqrstuvwxyz"

        for char in letters:
            if s.count(char) != t.count(char):
                return False
        
        return True

s1 = "anagram"
t1 = "nagaram"


s2 = "rat"
t2 = "car"

s = Solution()

result = s.isAnagram(s=s2, t=t2)
print(result)