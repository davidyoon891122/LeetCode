"""
Given an array of integers temperatures represents the daily temperatures,
return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, keep answer[i] == 0 instead.
"""

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        answer = [0] * len(temperatures)

        stack = []

        for i, cur in enumerate(temperatures):
            while stack and cur > temperatures[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
        return answer

temperatures = [73,74,75,71,69,72,76,73]
s = Solution()

print(s.dailyTemperatures(temperatures=temperatures))