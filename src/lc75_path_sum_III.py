from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSumWithRoot(self, root, targetSum) -> int:
        if root is None:
            return 0
        
        count = 0
        if root.val == targetSum:
            count += 1
        
        count += self.pathSumWithRoot(root.left, targetSum - root.val)
        count += self.pathSumWithRoot(root.right, targetSum - root.val)

        return count
    
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        # Optimization:
        # - Path left and right doesn't imply values of subsequent nodes. 
        # - Value could be negative.
        # - => All path should be visited once at least
        # - Optimization can only be done based on non-duplication.
        # Problem is essentially to do a traversal with all combinations.
        # How to uniquely identify a path? => Use the head!

        # Function 1: return sum of 1. if current is null, return 0
        #                    2. taking left node as start, find all possible path with sum = target by function 1
        #                    3. taking right node as start, find all possible path with sum = target by function 1
        #                    4. taking current node as start, find all possible path with sum = target by function 2
        #
        #
        # Function 2: given a sum and the head, count myself if == target + left with target = target - myself. 
        if root is None:
            return 0
        
        count = self.pathSumWithRoot(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        return count




        