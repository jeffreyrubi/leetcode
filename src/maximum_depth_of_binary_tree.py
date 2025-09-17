from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        return max(self.traverse(root.left) + 1, self.traverse(root.right) + 1)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.traverse(root)
