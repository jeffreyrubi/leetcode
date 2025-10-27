# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Question:
        # q is p's common ancestor?

        # BF: Find all ancestor of p O(n), Find all ancestor of q O(n). For each ancestor of p O(log n ^ 2), go up q and get the first ancestor.
        # Optimize: Find p/q, once find, set target to another, backtrack = ancestor, go right to find q. if not find, backtrack until find q.
        smaller, bigger = (p, q) if p.val < q.val else (q, p)

        def dfs(node):

            if smaller.val <= node.val <= bigger.val:
                return node

            if node.val > bigger.val:
                return dfs(node.left)

            if node.val < smaller.val:
                return dfs(node.right)



        return dfs(root)
        