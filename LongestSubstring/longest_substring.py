"""
Given a string s, find the length of the longest substring without repeating characters.
"""



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        map = {}
        result = 0
        start = 0

        for i, char in enumerate(s):
            if char in map:
                result = max(result, i - start)
                start = max(start, map[char] + 1)
                # print(result, start)
            map[char] = i
        
        return max(result, len(s) - start)
    


case_1 = "abcabcbb"
case_2 = "bbbbb"
case_3 = "pwwkew"
case_4 = " "

s = Solution()

print(s.lengthOfLongestSubstring(case_1))
print(s.lengthOfLongestSubstring(case_2))
print(s.lengthOfLongestSubstring(case_3))
print(s.lengthOfLongestSubstring(case_4))
