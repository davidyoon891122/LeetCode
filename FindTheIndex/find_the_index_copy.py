"""
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        m = len(haystack)
        n = len(needle)

        # 8 - 6 + 1 = 3  0, 1, 2
        for i in range(m - n + 1):
            print(i)
            if haystack[i: i + n] == needle:
                return i
        return -1





s = Solution()

result = s.strStr(haystack="Hello", needle="lo")
print(result)