from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def traverse(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return 0
        
        if root.left is None and root.right is None:
            return 1
        
        left_level = self.traverse(root.left)
        right_level = self.traverse(root.right)

        if abs(left_level - right_level) > 1:
            raise Exception("More than 2 level difference")
        return max(left_level, right_level) + 1

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        try:
            self.traverse(root)
        except:
            return False
        return True
