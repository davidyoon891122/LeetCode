"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.
"""
import re
import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s is None or len(s) == 0:
            return True

        pattern_1 = r'[^a-z0-9]'
        pattern_2 = r'[' + string.punctuation + ']'
        reverse_str = s[::-1].lower().strip()
        reverse_str = re.sub(pattern_1, '', reverse_str)
        reverse_str = re.sub(pattern_2, '', reverse_str).replace(' ', '')
        compare_str = s.strip().lower()
        compare_str = re.sub(pattern_1, '', compare_str)
        compare_str = re.sub(pattern_2, '', compare_str).replace(' ', '')
    
        if reverse_str == compare_str:
            return True
        else:
            return False



s = Solution()

test_1 = "A man, a plan, a canal: Panama"
test_2 = "0P"
result = s.isPalindrome(test_1)
print("result :{}".format(result))