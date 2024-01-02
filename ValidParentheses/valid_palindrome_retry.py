"""
A phrase is a palindrome if,
after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters,
it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.
"""
import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = s.lower()
        regex = re.compile("[^a-zA-Z0-9]")
        word = regex.sub('', word)


        if word == word[::-1]:
            return True
        else:
            return False

        


s = Solution()

ex1 = "A man, a plan, a canal: Panama"
ex2 = "race a car"
ex3 = " "

print(s.isPalindrome(s=ex1))  
print(s.isPalindrome(s=ex2))
print(s.isPalindrome(s=ex3))