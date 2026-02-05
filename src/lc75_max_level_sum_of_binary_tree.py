from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        # Analyze: All level must be travel to obtain the largest. No skip level. For each level, all node needs to be visited once to get the sum.
        # Best possible solution => O(n): travel every node once.
        max_level = 1
        max_value = root.val
        queue = deque([root])
        level = 0

        while queue:
            level_size = len(queue)
            level_sum = 0
            level += 1
            for _ in range(level_size):
                # Take left
                ele = queue.popleft()
                # Append child
                if ele.left:
                    queue.append(ele.left)
                if ele.right:
                    queue.append(ele.right)
                
                level_sum += ele.val
            
            if level_sum > max_value:
                max_value = level_sum
                max_level = level
            
        return max_level


        