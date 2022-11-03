"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""

class Solution:
    def climb_stairs(self, n: int) -> int:
        if n < 3:
            return n
        first = 1
        second = 2
        for _ in range(2, n):
            current = first + second
            first = second
            second = current
        return second




s = Solution()
print(s.climb_stairs(5))
# fibo