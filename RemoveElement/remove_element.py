"""
Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
"""

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    result = 0
    j = 0
    for i in range(1, len(nums)):
        if nums[i] != val:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
            result += 1
        print(nums)
    return result




ex_1 = [5, 2, 3, 0, 0, 2, 0]
# ex_2 = [3, 2, 2, 3]
result = removeElement(ex_1, 0)
# result_2 = removeElement(ex_2, 3)
print(result)