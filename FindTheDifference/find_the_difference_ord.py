"""
String t is generated by random shuffling string s and then add one more letter at a random position.
Return the letter that was added to t.
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0

        for letter in s:
            res ^= ord(letter)
        for letter in t:
            res ^= ord(letter)
        return chr(res)

s_1 = "abcd"
t_1 = "abcde"

s = Solution()
print(s.findTheDifference(s=s_1, t=t_1))

