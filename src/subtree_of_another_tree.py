from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def serialize(node):
            if not node:
                return "NULL"
            return f"({node.val},{serialize(node.left)},{serialize(node.right)})"
        
        se_root = serialize(root)
        se_sub = serialize(subRoot)

        if se_sub in se_root:
            return True
        return False
