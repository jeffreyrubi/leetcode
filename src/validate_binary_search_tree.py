from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def checkOneNode(self, lower_bound: Optional[int], upper_bound: Optional[int], node: Optional[TreeNode]) -> bool:
        if node is None:
            return True
        
        if (node.left is None or (node.left.val < node.val)) and \
        (node.right is None or node.val < node.right.val) and \
        (lower_bound is None or lower_bound < node.val) and \
        (upper_bound is None or upper_bound > node.val):
            return self.checkOneNode(lower_bound, node.val, node.left) and self.checkOneNode(node.val, upper_bound, node.right)
        else:
            return False
        
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.checkOneNode(None, None, root)