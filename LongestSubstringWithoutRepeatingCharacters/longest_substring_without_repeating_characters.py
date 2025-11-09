"""
Given a string s, find the length of the longest substring without duplicate characters.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        
        max_length = start = 0
        
        for index, char in enumerate(s):
            if s[index] in used and start <= used[char]:
              start = used[char] + 1
            else:
              max_length = max(max_length, index - start + 1)
            
            used[char] = index
        
        
        return max_length
        
        

s = Solution()

a = "abcabcbbdefgh"

print(s.lengthOfLongestSubstring(a))