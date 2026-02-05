# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    
    def visit(self, subroot: TreeNode) -> int:
        # Return true if node = p or q
        if not subroot:
            return False
        
        self_found = 1 if subroot.val == self.p.val or subroot.val == self.q.val else 0
        
        # visit left and right of subroot. If both return true. Answer is found.
        left_found = self.visit(subroot.left)
        right_found = self.visit(subroot.right)

        if (left_found + right_found + self_found) >= 2 and self.target is None:
            self.target = subroot

        return left_found + right_found + self_found

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Brutal Force: For every node as the root, visit both left and right. If left find p and right find q, it is the root node.
        # highly duplicate because every node re-travel the whole subtree.

        self.target = None
        self.p = p
        self.q = q
        self.visit(root)
        return self.target
