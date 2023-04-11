"""
Given a string s, find the length of the longest substring without repeating characters.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic, res, start = {}, 0, 0
        for i, ch in enumerate(s):
            if ch in dic:
                res = max(res, i-start)
                start = max(start, dic[ch]+1)
                print("res: {}, start: {}".format(res, start))
            dic[ch] = i
        print(dic)
        return max(res, len(s)-start)



s = Solution()

case_1 = "abcabcbb" # abc
case_2 = "bbbbb" # b
case_3 = "pwwkew" # wke
print(s.lengthOfLongestSubstring(s=case_1))
print(s.lengthOfLongestSubstring(s=case_2))
print(s.lengthOfLongestSubstring(s=case_3))