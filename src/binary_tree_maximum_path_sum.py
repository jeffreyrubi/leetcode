from typing import Optional
import math

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def dfs(self, root: Optional[TreeNode], max_sum: list) -> int:
        if not root:
            return 0
        
        # update max with sum of self + left + right
        longest_left = self.dfs(root.left, max_sum)
        longest_right = self.dfs(root.right, max_sum)

        max_sum[0] = max(max_sum[0], root.val, root.val + longest_left, root.val + longest_right, root.val + longest_left + longest_right)

        # return self + max(dfs(left), dfs(right))
        return root.val + max(0, longest_left, longest_right)
        
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = [-math.inf]
        self.dfs(root, max_sum)
        return max_sum[0]