from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def visit(self, right_view: List[int], level: int, node: Optional[TreeNode]):
        if node is None:
            return
        if level > len(right_view): 
            # Its visible
            right_view.append(node.val)
        
        # Always visit right view first
        self.visit(right_view, level+1, node.right)
        self.visit(right_view, level+1, node.left)
        
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        right_view = []
        self.visit(right_view, 1, root)
        return right_view