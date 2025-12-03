from src.construct_binary_tree_preorder_inorder import Solution, TreeNode

def test_construct_binary_tree_preorder_inorder():
    solution = Solution()
    
    # Test case 1: Empty arrays
    assert solution.buildTree([], []) is None
    
    # Test case 2: Single node
    root = solution.buildTree([1], [1])
    assert root.val == 1
    assert root.left is None
    assert root.right is None
    
    # Test case 3: Example from LeetCode
    # Tree:     3
    #          / \
    #         9  20
    #           /  \
    #          15   7
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = solution.buildTree(preorder, inorder)
    
    assert root.val == 3
    assert root.left.val == 9
    assert root.left.left is None
    assert root.left.right is None
    assert root.right.val == 20
    assert root.right.left.val == 15
    assert root.right.right.val == 7
    
    # Test case 4: Left-skewed tree
    # Tree: 1
    #      /
    #     2
    #    /
    #   3
    preorder = [1, 2, 3]
    inorder = [3, 2, 1]
    root = solution.buildTree(preorder, inorder)
    
    assert root.val == 1
    assert root.left.val == 2
    assert root.left.left.val == 3
    assert root.right is None
    assert root.left.right is None
    assert root.left.left.left is None
    assert root.left.left.right is None
    
    # Test case 5: Right-skewed tree
    # Tree: 1
    #        \
    #         2
    #          \
    #           3
    preorder = [1, 2, 3]
    inorder = [1, 2, 3]
    root = solution.buildTree(preorder, inorder)
    
    assert root.val == 1
    assert root.right.val == 2
    assert root.right.right.val == 3
    assert root.left is None
    assert root.right.left is None
    assert root.right.right.left is None
    assert root.right.right.right is None
    
    # Test case 6: Balanced tree with negative values
    # Tree:    -1
    #         /  \
    #       -2   -3
    #       /   /  \
    #     -4   -5  -6
    preorder = [-1, -2, -4, -3, -5, -6]
    inorder = [-4, -2, -1, -5, -3, -6]
    root = solution.buildTree(preorder, inorder)
    
    assert root.val == -1
    assert root.left.val == -2
    assert root.right.val == -3
    assert root.left.left.val == -4
    assert root.left.right is None
    assert root.right.left.val == -5
    assert root.right.right.val == -6
    
    # Test case 7: Two nodes - parent and left child
    preorder = [1, 2]
    inorder = [2, 1]
    root = solution.buildTree(preorder, inorder)
    
    assert root.val == 1
    assert root.left.val == 2
    assert root.right is None
    assert root.left.left is None
    assert root.left.right is None
    
    # Test case 8: Two nodes - parent and right child
    preorder = [1, 2]
    inorder = [1, 2]
    root = solution.buildTree(preorder, inorder)
    
    assert root.val == 1
    assert root.right.val == 2
    assert root.left is None
    assert root.right.left is None
    assert root.right.right is None