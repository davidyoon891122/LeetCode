from typing import List

def remove_element(nums: List[int], val: int) -> int:
    for i in range(nums.count(val)):
        nums.remove(val)
    print(nums)
    return len(nums)

ex_1 = [0,1,2,2,3,0,4,2]
ex_2 = [3, 2, 2, 3]

result = remove_element(ex_1, 3)
print(result)

result_2 = remove_element(ex_2, 3)
print(result_2)
