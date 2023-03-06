"""
Given two binary strings a and b, return their sum as a binary string.
"""

class Solution:
    def add_bianry(self, a: str, b: str) -> str:
        a_list = list(a)
        b_list = list(b)

        carry = 0
        result = ''

        while a_list or b_list or carry:
            if a_list:
                carry = carry + int(a_list.pop())
            if b_list:
                carry = carry + int(b_list.pop())

            result += str(carry % 2)
            carry = carry // 2
        return result [::-1]

        
# 1202  
s = Solution()

a_1 = "11"
b_1 = "1"
expect_1 = "100"

print("result: {}".format(s.add_bianry(a_1, b_1)))

a_2 = "1010"
b_2 = "1011"
expect_2 = "10101"

print("result: {}".format(s.add_bianry(a_2, b_2)))