"""
We are playing the Guess Game. The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.
Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.
You call a pre-defined API int guess(int num), which returns three possible results:

-1: Your guess is higher than the number I picked (i.e. num > pick).
1: Your guess is lower than the number I picked (i.e. num < pick).
0: your guess is equal to the number I picked (i.e. num == pick).
Return the number that I picked.
"""
import random

class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 0, n

        while left <= right:
            mid = (left + right) // 2
            res = self.guess(mid)
            if res < 0:
                right = mid - 1
            elif res > 0:
                left = mid + 1
            else:
                return mid

    def guess(self, n: int) -> int:
        pick = 30
        if n > pick:
            return - 1
        elif n < pick:
            return 1
        else:
            return 0
        


s = Solution()

print(s.guessNumber(n=100))