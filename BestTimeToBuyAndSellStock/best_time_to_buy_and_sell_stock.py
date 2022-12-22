"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit, min_price = 0, float('inf')
        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(max_profit, profit)
            print("min_price: {}, profit: {}, max_profit: {}".format(min_price, profit, max_profit))
        return max_profit




             



example_1 = [7,1,5,3,6,4]
example_2 = [7,6,4,3,1]
example_3 = [2,4,1]
example_4 = [3,2,6,5,0,3]

s = Solution()
# result_1 = s.maxProfit(example_1)
# result_2 = s.maxProfit(example_2)
# result_3 = s.maxProfit(example_3)
result_4 = s.maxProfit(example_3)
print("result: {}".format(example_3))
# print("result: {}, {}, {}".format(result_1, result_2, result_3))