"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your result is the smallest in lexicographical order among all possible results.

"""

from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter, seen, stack = Counter(s), set(), []

        for char in s:
            counter[char] -= 1
            
            if char in seen:
                continue
            
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())

            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)



test = "bcabc"

test2 = "cbacdcbc"

s = Solution()
print(s.removeDuplicateLetters(test2))