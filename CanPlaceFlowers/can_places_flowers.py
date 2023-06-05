"""
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""



from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        result ,prev = 0, 0

        for cur in flowerbed:
            if cur == 1:
                if prev == 1:
                    result -= 1
                prev = 1
            else:
                if prev == 1:
                    prev = 0
                else:
                    result += 1
                    prev = 1

        return result >= n 

            





flowered_1 = [1,0,0,0,1]
n_1 = 1

flowered_2 = [1,0,0,0,1]
n_2 = 2

flowered_3 = [0,0,0,0,1]
n_3 = 1

flowered_4 = [1,0,0,0,0]
n_4 = 2



s = Solution()

print(s.canPlaceFlowers(flowerbed=flowered_1, n=n_1))
print(s.canPlaceFlowers(flowerbed=flowered_2, n=n_2))
print(s.canPlaceFlowers(flowerbed=flowered_3, n=n_3))
print(s.canPlaceFlowers(flowerbed=flowered_4, n=n_4))