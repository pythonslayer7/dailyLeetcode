from typing import List
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for currAmount in range(1, amount + 1):
            for currCoin in coins:
                if currAmount - currCoin >= 0:
                    dp[currAmount] = min(dp[currAmount], dp[currAmount - currCoin] + 1)

        return dp[amount] if dp[amount] != float("inf") else -1
