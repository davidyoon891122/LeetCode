"""
Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
"""

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    i, k = 0, 0

    while k < len(nums):
        if nums[k] != val:
            nums[i] = nums[k]
            i += 1
        k += 1
        print(nums)
    return i


ex_1 = [0,1,2,2,3,0,4,2]
ex_2 = [3, 2, 2, 3]

# 3 2 2 3 
# 2 3 2 3
result = removeElement(ex_1, 2)
print(result)
print("================")
result_2 = removeElement(ex_2, 2)
print(result_2)