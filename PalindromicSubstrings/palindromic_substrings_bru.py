"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
"""

from typing import List

import collections

class Solution:
  def countSubstrings(self, s: str) -> int:
    count = 0
    for i in range(len(s)):
      for j in range(i, len(s)):
        if self.isPalindromic(s[i:j+1]):
          count += 1
    return count
    
    
  def isPalindromic(self, s: str) -> bool:
    if len(s) == 1: return True
    
    start = 0
    end = len(s) - 1
    while start < end:
      if s[start] == s[end]:
        start += 1
        end -= 1
      else: 
        return False
      
    return True
      
    
    
s = Solution()

example = "abc"

print(s.countSubstrings(example))
