from typing import List 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        leftPointer = 0
        maxProfit = 0
        for rightPointer in range(1, len(prices)):
            profit = prices[rightPointer] - prices[leftPointer]
            if profit > 0:
                maxProfit = max(maxProfit, profit)
            else:
                leftPointer = rightPointer
        return maxProfit