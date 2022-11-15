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
        while m > 0 and n > 0:
            if nums1[m - 1] >= nums2[n - 1]:
                nums1[m+n-1] = nums1[m-1]
                m -= 1
            else:
                nums1[m+n-1] = nums2[n-1]
                n -= 1
            
        print(n)
        if n > 0:
            nums1[:n] = nums2[:n]
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