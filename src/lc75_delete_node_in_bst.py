from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        # Find the node
        if not root:
            return None
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            # match and only one sided child or no child at all
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            
            # match with two child
            # => find the smallest value at the right, copy its value and remove that child
            cur = root.right
            while cur.left:
                cur = cur.left
            
            # copy the value of smallest to root
            root.val = cur.val

            # delete the smallest
            root.right = self.deleteNode(root.right, cur.val)

        return root 
