"""
Given a string s, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']

        vowels_list = []

        result = ""
        for char in s:
            if char.lower() in vowels:
                vowels_list.append(char)
        print(vowels_list)
        
        for index in range(len(s)):
            if s[index].lower() in vowels:
                result += vowels_list.pop()
            else:
                result += s[index]
        
        print(result)
        return result





s_1 = "hello"
s_2 = "leetcode"
s_3 = "aA"

s = Solution()
s.reverseVowels(s=s_3)