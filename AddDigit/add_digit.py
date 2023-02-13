"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.
"""

class Solution:
    def addDigits(self, num: int) -> int:
        res = num
        while res >= 10:
            temp = 0    
            num_list = list(str(res))
            print(num_list)
            for i in num_list:
                temp += int(i)
            res = temp
            print(res)
        return res            



n_list = [38, 100, 2, 3, 52, 73, 32]

s = Solution()

for i in n_list:
    result = s.addDigits(num=i)
    print(result)
