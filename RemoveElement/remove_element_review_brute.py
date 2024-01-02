"""
Given an integer array nums and an integer val,
remove all occurrences of val in nums in-place.
The relative order of the elements may be changed.
"""

from typing import List

def removeElement(nums: List[int], val: int) -> int:
    i = 0

    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
        print(nums)
    return i




ex_1 = [0,1,1,2 ,3]
ex_2 = [3, 2, 2, 3]

# 3 2 2 3 
# 2 3 2 3
result = removeElement(ex_1, 1)
print(result)
print("================")
result_2 = removeElement(ex_2, 2)
print(result_2)