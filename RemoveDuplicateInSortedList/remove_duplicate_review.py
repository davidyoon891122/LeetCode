from typing import List

def removeDuplicates(nums: List[int]) -> int:
   
    if nums is None:
       return 0
    first = 0
    for i in range(1, len(nums)):
        if nums[i] != nums[first]:
            first += 1
            temp = nums[first]
            nums[first] = nums[i]
            nums[i] = temp
            


    print(nums)

first_example = [0, 1, 1, 2, 2, 3, 3]

print(removeDuplicates(first_example))