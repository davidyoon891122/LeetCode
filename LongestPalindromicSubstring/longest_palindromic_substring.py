"""
Given a string s, return the longest palindromic substring in s.
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:    
        if len(s) == 0:
            return 0
        
        maxLen = 1
        start = 0

        for i in range(len(s)):
            if i - maxLen >= 1 and s[i-maxLen-1:i+1] == s[i-maxLen-1:i+1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and s[i-maxLen:i+1] == s[i-maxLen:i+1][::-1]:
                start = i-maxLen
                maxLen += 1

        print(s[start: start+maxLen])
        return s[start: start+maxLen]




            




s_1 = "babad"

s_2 = "cbbd"

s_3 = "c"

s_4 = "ac"

s_5 = "bbbccd"

s = Solution()
s.longestPalindrome(s=s_1)
s.longestPalindrome(s=s_2)
s.longestPalindrome(s=s_3)
s.longestPalindrome(s=s_4)
s.longestPalindrome(s=s_5)