class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7
        
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Base cases
        complete_two_back = 1  # ways to fully tile 2x0 board
        complete_one_back = 1  # ways to fully tile 2x1 board
        partial_one_back = 0  # ways to tile with one cell protruding (none possible at n=1)
        
        for i in range(2, n + 1):
            complete_curr = (complete_one_back + complete_two_back + 2 * partial_one_back) % MOD
            partial_curr = (partial_one_back + complete_two_back) % MOD
            
            # Shift for next iteration
            complete_two_back = complete_one_back
            complete_one_back = complete_curr
            partial_one_back = partial_curr
        
        return complete_curr