from src.lc75_longest_zigzag_path_in_binary_tree import Solution, TreeNode

def test_lc75_longest_zigzag_path_in_binary_tree():
    solution = Solution()

    # Test case 1: Single node tree
    root1 = TreeNode(1)
    assert solution.longestZigZag(root1) == 0

    # Test case 2: Zigzag path of length 3
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.right = TreeNode(4)
    root2.left.right.left = TreeNode(5)
    assert solution.longestZigZag(root2) == 3

    # Test case 3: No zigzag path
    root3 = TreeNode(1)
    root3.left = TreeNode(2)
    root3.left.left = TreeNode(3)
    root3.left.left.left = TreeNode(4)
    assert solution.longestZigZag(root3) == 1

    # Test case 4: Zigzag path of length 1
    root4 = TreeNode(1)
    root4.right = TreeNode(2)
    assert solution.longestZigZag(root4) == 1
