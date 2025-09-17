from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def add(self, result: List[List[int]], level: int, node: Optional[TreeNode]):
        if node is None:
            return

        # add myself
        if node.val is not None:
            if len(result) > level:
                result[level].append(node.val)
            else:
                result.append([node.val])

        # add left and right
        self.add(result, level+1, node.left)
        self.add(result, level+1, node.right)

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        result = [[]]
        self.add(result, 0, root)
        return result
              