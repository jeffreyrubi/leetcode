from typing import List

class Solution:
    def jump(self, nums: List[int], deadend: List[bool], pos: int) -> bool:
        if pos == len(nums) - 1:
            # arrived end
            return True
        if pos >= len(nums) or deadend[pos]:
            # mark deadended
            return False
            
        for step in range(nums[pos], 0, -1):
            # continue testing
            if self.jump(nums, deadend, pos+step):
                return True
        
        # All steps failed. Mark pos deadend.
        deadend[pos] = True        
        return False

    def canJump(self, nums: List[int]) -> bool:
        # Brutal Force: try all possibilities to see if it get to the last index.
        # Optimize: Backtrack with memory
        # DFS to the end.
        # Memory to prune all steps proof to be deadend.

        deadend = [False]*len(nums)
        return self.jump(nums, deadend, 0)

