"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int):
        if m == 0:
            nums1 = nums2
            print(nums1)
            return
        elif n == 0:
            print(nums1)
            return
        elif m == 0 and n == 0:
            nums1 = []
            return

        nums1 = nums1[:m]
        nums2 = nums2[:n]
        nums1[m:] = nums2
        first = 0
        last = m
        pivot = (first + last) // 2
        for i in range(n):
            target = nums2[i]
            while True:
                # 2
                last = len(nums1)
                pivot = (first + last) // 2
                if target == nums1[pivot]:
                   nums1.insert(pivot, target)
                   break
                elif target > nums1[pivot]:
                    if first != m: 
                        first = pivot + 1
                    else:
                        nums1.insert(pivot + 1, target)
                        break
                elif target < nums1[pivot]:
                    if last != 0:
                        last = pivot - 1
                    else:
                        nums1.insert(pivot, target)
                        break
        print(nums1)


# test_case_1 
ex_num1 = [1,2,3,0,0,0]
ex_m = 3

ex_num2 = [2,5,6]
ex_n = 3

result1 = [1,2,2,3,5,6]

# test_case_2
ex2_num1 = [1]
ex2_m = 1

ex2_num2 = []
ex2_n = 0

result2 = [1]

# test_case_3
ex3_num1 = [0]
ex3_m = 0

ex3_num2 = [1]
ex3_n = 1

result2 = [1]

s = Solution()
s.merge(ex_num1, ex_m, ex_num2, ex_n)
print("----------------")
s.merge(ex2_num1, ex2_m, ex2_num2, ex2_n)
print("----------------")
s.merge(ex3_num1, ex3_m, ex3_num2, ex3_n)