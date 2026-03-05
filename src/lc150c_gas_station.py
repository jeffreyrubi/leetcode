from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Greedy approach:
        # 1. If total gas < total cost, impossible to complete circuit
        # 2. If tank goes negative at station i, start fresh from i+1
        # Time: O(n), Space: O(1)
        
        total_tank = 0
        current_tank = 0
        start = 0
        
        for i in range(len(gas)):
            diff = gas[i] - cost[i]
            total_tank += diff
            current_tank += diff
            
            # If current tank is negative, 
            # can't start from any station before i+1
            if current_tank < 0:
                start = i + 1
                current_tank = 0
        
        # If total gas >= total cost, 
        # solution exists and start is the answer
        return start if total_tank >= 0 else -1