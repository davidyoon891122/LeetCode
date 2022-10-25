"""
You are given a large integer represented as an integer array digits,
where each digits[i] is the ith digit of the integer.
The digits are ordered from most significant to least significant in left-to-right order.
The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""

from typing import List

class Solution:
    def plus_one(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                break
            elif digits[i] == 9:
                digits[i] = 0
                if i == 0:
                    digits.insert(0,1)
        return digits



example_1 = [1, 2, 3]
example_2 = [4, 3, 2, 1]
example_3 = [9]
example_4 = [1,9]
example_5 = [1, 9, 9]
example_6 = [1, 0, 9]
example_7 = [9, 9, 9]



s = Solution()
print(s.plus_one(example_1))
print(s.plus_one(example_2))
print(s.plus_one(example_3))
print(s.plus_one(example_4))
print(s.plus_one(example_5))
print(s.plus_one(example_6))
print(s.plus_one(example_7))