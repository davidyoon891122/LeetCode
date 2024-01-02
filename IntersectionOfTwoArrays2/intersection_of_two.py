from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hash_map = {}
        result = []
        for num in nums1:
            if num not in hash_map:
                hash_map[num] = 1
            else:
                hash_map[num] += 1
        for num in nums2:
            if num in hash_map:
                result.append(num)
                hash_map[num] -= 1
                if hash_map[num] == 0:
                    hash_map.pop(num)
        print(result)
        return result





case1_num1 = [1, 2, 2, 1]
case1_num2 = [2, 2]

case2_num1 = [4, 9, 5]
case2_num2 = [9, 4, 9, 8, 4]

case3_num1 = [2, 2, 2, 2]
case3_num2 = [2]

case4_num1 = [1, 1]
case4_num2 = [1, 2]

s = Solution()

s.intersect(nums1=case1_num1, nums2=case1_num2)

s.intersect(nums1=case2_num1, nums2=case2_num2)

s.intersect(nums1=case3_num1, nums2=case3_num2)

s.intersect(nums1=case4_num1, nums2=case4_num2)