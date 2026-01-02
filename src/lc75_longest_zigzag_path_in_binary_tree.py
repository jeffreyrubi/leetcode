from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.max_length = 0

        def traverse(root, to_go: str) -> int:
            if not root:
                return 0
            
            if to_go == 'left':
                continue_length = 1 + traverse(root.left, to_go='right')
                new_length = 1 + traverse(root.right, to_go='left')
            else:
                continue_length = 1 + traverse(root.right, to_go='left')
                new_length = 1 + traverse(root.left, to_go='right')

            self.max_length = max(self.max_length, continue_length, new_length)
            return continue_length
        
        traverse(root, 'left')
        traverse(root, 'right')
        return self.max_length - 1