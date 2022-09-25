from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if not nums:
        return 0
    length = 1
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[j], nums[i] = nums[i], nums[j]
            length += 1
            print(nums)
    return length

first_example = [0, 1, 1, 2, 2, 3, 3]

print(removeDuplicates(first_example))