"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0 : return 0
        if num % 9 == 0: return 9
        else : return (num % 9)


n_list = [38, 100, 2, 3, 52, 73, 32]

s = Solution()

for i in n_list:
    result = s.addDigits(num=i)
    print(result)
