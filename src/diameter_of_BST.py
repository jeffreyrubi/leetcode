from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Traverse the left deepest and right deepest
        # Brutal force: ??
        # Game plan: traverse all nodes and for each node, calculate the deepest from left and right.
        #            do dfs
        max_dia = 0
        def dfs(root):
            if not root:
                return 0
            
            nonlocal max_dia
            depth_left = dfs(root.left)
            depth_right = dfs(root.right)
            max_dia = max(depth_left + depth_right, max_dia)
            return max(depth_left, depth_right) + 1

        dfs(root)

        return max_dia

        