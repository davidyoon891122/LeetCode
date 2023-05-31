"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.
"""

import collections

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = ""
        word1_dequeue = collections.deque(word1)
        word2_dequeue = collections.deque(word2)

        while word1_dequeue or word2_dequeue:
            if word1_dequeue:
                result += word1_dequeue.popleft()
            if word2_dequeue:
                result += word2_dequeue.popleft()
            
        return result


word1_1 = "abc"
word2_1 = "pqr"

s = Solution()

s.mergeAlternately(word1=word1_1, word2=word2_1)