from typing import Optional 
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Question
        # 1. is there any unbalanced node?
        
        if not root:
            return None
        
        # BFS in inverted order
        queue = deque([root])

        def bfs():
            while queue:
                node = queue.popleft()
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                temp = node.right
                node.right = node.left
                node.left = temp

        bfs()
        return root