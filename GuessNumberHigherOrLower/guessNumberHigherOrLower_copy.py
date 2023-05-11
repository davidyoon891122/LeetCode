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
        def search(low, high):
            if low <= high:
                mid = (low + high) // 2
                x = self.guess(mid)
                if x == 0:
                    return mid
                elif x == -1:
                    return search(low, mid - 1)
                else:
                    return search(mid + 1, high)
            return 0
        return search(1, n)

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