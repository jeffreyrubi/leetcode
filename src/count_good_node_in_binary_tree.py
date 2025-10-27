import math

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def countGoodNode(self, node: TreeNode, max: int) -> int:
        if node is None:
            # Do not mark anything and end the traverse
            return 0
        
        good_to_increment = 0
        # If current node value >= max, no other nodes greater than itself, good.
        # otherwise, its a bad nodes. keep max and continue to traverse
        if node.val >= max:
            max = node.val # update max
            good_to_increment = 1

        # For Leave node: left = 0, right = 0, return 1 and
        # For 2nd leave node: left = 1, right = 1, myself if i'm > received max
        return self.countGoodNode(node.left, max) + good_to_increment + self.countGoodNode(node.right, max) 

    def goodNodes(self, root: TreeNode) -> int:
        # dfs the tree, keep propagate the max value of previous nodes. 
        # Each time, it compares with the max. If bigger than max, then add good node.

        # If root carries nothing, return 0
        if root is None:
            return 0

        # Step 1: Make max == - infinity for root node to always considered good. 
        max = -math.inf

        return self.countGoodNode(root, max)
    