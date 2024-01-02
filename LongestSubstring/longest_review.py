"""
Given a string s, find the length of the longest substring without repeating characters.
"""



class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        res, start = 0, 0

        for i, ch in enumerate(s):
            if ch in hash_map and hash_map[ch] + 1 > start:
                start = hash_map[ch] + 1
            hash_map[ch] = i

            res = max(res, i - start + 1)
            print("result: {}, start: {}".format(res, start))
        return res
    


case_1 = "abcabcbb"
case_2 = "bbbbb"
case_3 = "pwwkew"
case_4 = " "

s = Solution()

print(s.lengthOfLongestSubstring(case_1))
print(s.lengthOfLongestSubstring(case_2))
print(s.lengthOfLongestSubstring(case_3))
print(s.lengthOfLongestSubstring(case_4))
