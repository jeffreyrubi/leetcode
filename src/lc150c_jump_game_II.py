from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        # Greedy approach:
        # - Track the farthest position reachable from current window
        # - When we reach the end of current window, make a jump
        # - Update window to extend to the farthest point seen
        #
        # Time: O(n), Space: O(1)
        
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0  # End of current jump window
        farthest = 0     # Farthest position reachable
        
        for i in range(n - 1):  # Don't need to jump from last index
            farthest = max(farthest, i + nums[i])
            
            # When we reach the end of current window, we must jump
            if i == current_end:
                jumps += 1
                current_end = farthest
                
                # Early exit if we can already reach the end
                if current_end >= n - 1:
                    break
        
        return jumps