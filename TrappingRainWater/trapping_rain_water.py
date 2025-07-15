"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
"""


from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        volume = 0
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]

        while left < right:
            print("left :{}, right:{}".format(left, right))
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            print("left_max :{}, right_max:{}".format(left_max, right_max))
            if left_max < right_max:
                volume += left_max - height[left]
                print("left_max{} - height[left]{}: {}".format(left_max, height[left], left_max - height[left]))
                print("left + plus:{},".format(left_max - height[left]))
                left += 1
            else:
                volume += right_max - height[right]
                print("right_max{} - height[right]{}: {}".format(right_max, height[right], right_max - height[right]))
                print("right + plus:{},".format(right_max - height[right]))
                right -= 1
        
        print(volume)
        return volume




s = Solution()


height = [0,1,0,2,1,0,1,3,2,1,2,1] 

s.trap(height=height)