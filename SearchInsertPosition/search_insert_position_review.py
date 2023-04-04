"""
Given a sorted array of distinct integers and a target value,

return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

def search_insert(nums: List[int], target: int) -> int:
    first = 0
    last = len(nums) - 1

    while first <= last:
        pivot = (first + last) // 2
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] < target:
            first = pivot + 1 
        else:
            last = pivot - 1
    
    return len(nums) 
                
            


    
example_1 = [1, 3, 5, 6]
target_1 = 5
expected_1 = 2

example_2 = [1, 3, 5, 6]
target_2 = 2
expected_2 = 1

example_3 = [1, 3, 5, 6]
target_3 = 7
expected_3 = 4


result_1 = search_insert(example_1, target_1)
print("result: {}".format(result_1))

if result_1 == expected_1:
    print("Pass")