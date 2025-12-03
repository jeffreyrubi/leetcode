from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Use dynamic programming approach
        # dp[i] represents the minimum number of coins needed to make amount i
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # 0 coins needed to make amount 0
        
        # For each amount from 1 to target amount
        for i in range(1, amount + 1):
            # Try each coin
            for coin in coins:
                if coin <= i:
                    # If we can use this coin, update dp[i] with minimum
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # Return -1 if impossible, otherwise return the minimum coins needed
        return dp[amount] if dp[amount] != float('inf') else -1