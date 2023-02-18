
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        print(nums)
        left = [1]
        p = 1

        for i in range(1, len(nums)):
            p *= nums[i - 1]
            left.append(p) 
        print(left)

        p = 1

        for i in range(len(nums) - 1, -1, -1):
            left[i] = left[i] * p
            p = p * nums[i]

        return left


nums = [1, 2, 3, 4]

s = Solution()
result = s.productExceptSelf(nums=nums)
print(result)

