
from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        highest = 0
        result = 0

        for i in gain:
            result = result + i
            if highest < result:
                highest = result
        
        return highest



s = Solution()

example_1 = [-5, 1, 5, 0, -7]

result_1 = 1

example_2 = [-4, -3, -2, -1, 4, 3, 2]
result_2 = 0


print(s.largestAltitude(example_1))
print(s.largestAltitude(example_2))
