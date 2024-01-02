from typing import List

def removeDuplicates(nums: List[int]) -> int:
    if nums is None:
        return 0
    
    length = 1
    j = 0 
    for i in range(1, len(nums)):
        if nums[i] != nums[j]:
            j += 1
            nums[j], nums[i] = nums[i], nums[j]
            length += 1
    
    print(nums)

first_example = [0, 1, 1, 2, 2, 3, 3]

print(removeDuplicates(first_example))