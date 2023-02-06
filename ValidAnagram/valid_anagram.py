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
        sDic = {}
        tDic = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if s[i] in sDic:
                sDic[s[i]] += 1
            else:
                sDic[s[i]] = 1
            
            if t[i] in tDic:
                tDic[t[i]] += 1
            else:
                tDic[t[i]] = 1
        for key, value in sDic.items():
            if key in tDic:
                if tDic[key] != value:
                    return False
            else:
                return False
        return True

s1 = "anagram"
t1 = "nagaram"


s2 = "rat"
t2 = "car"

s = Solution()

result = s.isAnagram(s=s2, t=t2)
print(result)