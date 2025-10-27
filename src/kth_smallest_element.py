from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Question:
        # 1. What to return for empty?
        # 2. Does k < number of nodes?
        # 3. Can i use python?
        # 4. Any cyclic?
        # 5. does the number of level fit in memory
        # 6. Are the max numbers = len?

        # thought: Get all the values O(n) Sort the list O(log(n))
        # optimize: depth first search and get the k th value

        book = {'num': -1, 'count': 0}
        def dfs(node, book, k) -> bool:
            if node is None:
                return False
            
            if dfs(node.left, book, k):
                return True

            # Check if i'm the kth smallest
            book['count'] += 1
            if book['count'] == k:
                # i'm the kth smallest
                book['num'] = node.val
                return True
            else:
                if dfs(node.right, book, k):
                    return True

        dfs(root, book, k)
        return book['num']


