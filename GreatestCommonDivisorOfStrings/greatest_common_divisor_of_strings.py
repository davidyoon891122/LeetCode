"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.
"""

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if not str1 or not str2:
            return str1 if str1 else str2
        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        elif str1[: len(str2)] == str2:
            print(str1[:len(str2)])
            return self.gcdOfStrings(str1[len(str2) :], str2)
        else:
            return ''
                


s_1 = "ABCABC"
t_1 = "ABC"

s_2 = "ABABAB"
t_2 = "ABAB"

s_3 = "LEET"
t_3 = "CODE"

s_4 = "TAUXXTAUXXTAUXXTAUXXTAUXX"
t_4 = "TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"


s = Solution()

print(s.gcdOfStrings(str1=s_1, str2=t_1))
print(s.gcdOfStrings(str1=s_2, str2=t_2))
print(s.gcdOfStrings(str1=s_3, str2=t_3))
print(s.gcdOfStrings(str1=s_4, str2=t_4))
