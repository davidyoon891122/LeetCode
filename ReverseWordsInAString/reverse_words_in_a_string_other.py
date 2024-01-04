"""
Given an input string s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by at least one space.
Return a string of the words in reverse order concatenated by a single space.
Note that s may contain leading or trailing spaces or multiple spaces between two words. The returned string should only have a single space separating the words. Do not include any extra spaces.
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(reversed(s.split()))






s_1 = "the sky is blue"
s_2 = "  hello world  "
s_3 = "a good   example"

s = Solution()

print(s.reverseWords(s=s_1))
print(s.reverseWords(s=s_2))
print(s.reverseWords(s=s_3))