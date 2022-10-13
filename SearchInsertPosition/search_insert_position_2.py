"""
Given a sorted array of distinct integers and a target value,

return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.
"""

from typing import List

def search_insert(nums: List[int], target: int) -> int:
    low = 0
    high = len(nums) - 1

    while low <= high:
        pivot = (low + high) // 2
        print("pivot: {}".format(pivot))
        if nums[pivot] == target:
            return pivot
        elif nums[pivot] > target:
            high = pivot - 1
        else:
            low = pivot + 1
    return pivot + 1


    
example_1 = [1, 3, 5, 6]
target_1 = 5
expected_1 = 2

example_2 = [1, 3, 5, 6]
target_2 = 2
expected_2 = 1

example_3 = [1, 3, 5, 6]
target_3 = 7
expected_3 = 4

example_4 = [1, 3]  
target_4 = 2
expected_4 = 1

examples = [example_1, example_2, example_3, example_4]
targets = [target_1, target_2, target_3, target_4]
expecteds = [expected_1, expected_2, expected_3, expected_4]

for i in range(len(examples)):
    result = search_insert(examples[i], targets[i])
    print("result: {}".format(result))
    if result == expecteds[i]:
        print("Pass")
    else:
        print("Fail")

