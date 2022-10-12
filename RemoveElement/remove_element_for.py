from typing import List

def remove_element(nums: List[int], val: int) -> int:
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
            print(nums)
    return j

ex_1 = [0,1,2,2,3,0,4,2]
ex_2 = [3, 2, 2, 3]

result = remove_element(ex_1, 2)
print(result)

result_2 = remove_element(ex_2, 3)
print(result_2)
