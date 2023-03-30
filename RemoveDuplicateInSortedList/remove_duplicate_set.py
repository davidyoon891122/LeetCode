from typing import List

def removeDuplicates(nums: List[int]) -> int:
    nums[:] = sorted(set(nums))
    print(nums)
    return len(nums)


first_example = [0, 1, 1, 2, 2, 3, 3]

print(removeDuplicates(first_example))