"""
Write an algorithm to determine if a number n is happy.
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        mem = set()
        while n not in mem:
            mem.add(n)
            n = sum([int(x) ** 2 for x in str(n)])
            print(mem)
        
        return n == 1
            

    

s = Solution()
print(s.isHappy(2312))