from typing import List

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # Thoughts:
        # Use DP with two states:
        # - cash: max profit when NOT holding stock
        # - hold: max profit when holding stock
        # Time Complexity: O(n) - single pass through prices
        # Space Complexity: O(1) - only two variables
        
        cash = 0  # not holding any stock initially
        hold = -prices[0]  # if we buy on day 0
        
        for i in range(1, len(prices)):
            # Update both states
            cash = max(cash, hold + prices[i] - fee)
            hold = max(hold, cash - prices[i])
        
        return cash  # max profit is when we're not holding stock