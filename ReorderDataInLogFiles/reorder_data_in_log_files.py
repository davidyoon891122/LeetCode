"""
You are given an array of logs. Each log is a space-delimited string of words, where the first word is the identifier.
There are two types of logs:
Letter-logs: All words (except the identifier) consist of lowercase English letters.
Digit-logs: All words (except the identifier) consist of digits.
Reorder these logs so that:
The letter-logs come before all digit-logs.
The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
The digit-logs maintain their relative ordering.
Return the final order of the logs.
"""

from typing import List
import re

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        return sorted(logs, key = self.sort)
    
    def sort(self, logs):
        a, b = logs.split(' ', 1)
        if b[0].isalpha():
            return (0, b, a)
        else:
            return (1, None, None)


s = Solution()
# "let1 art can", "let2 own kit dig", "let3 art zero", "aet1 art can"
logs_1 = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero", "aet1 art can"]
logs_2 = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]

print(s.reorderLogFiles(logs=logs_1))



