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
      count += self.expand(s, i, i) # (0,0), (1,1), (2,2)
      count += self.expand(s, i, i+1) # (0,1), (1,2), (2,3)
      
    return count
    
  def expand(self, s, left, right):
    count = 0
    
    while left >= 0 and right < len(s) and s[left] == s[right]:
      count += 1
      left -= 1
      right += 1
    
    return count
    
    
s = Solution()

example = "abba"

print(s.countSubstrings(example))
