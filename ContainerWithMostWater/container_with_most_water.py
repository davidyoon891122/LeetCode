"""
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.
Notice that you may not slant the container.
"""

from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r, area = 0, len(height) - 1, 0

        while l < r:
            area = max(area, (r - l) * min(height[l], height[r]))

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        print("area: {}".format(area))
        return area

s = Solution()

height_1 = [1,8,6,2,5,4,8,3,7]
height_2 = [2, 3, 5, 2]
s.maxArea(height=height_1)
s.maxArea(height=height_2)