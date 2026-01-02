from src.lc75_path_sum_III import Solution, TreeNode


def test_lc75_path_sum_III():
    solution = Solution()

    # Test case 1: Example input
    root = TreeNode(10, TreeNode(5, TreeNode(3), TreeNode(2, None, TreeNode(1))), TreeNode(-3, None, TreeNode(11)))
    target_sum = 8
    assert solution.pathSum(root, target_sum) == 3

    # Test case 2: Empty tree
    root = None
    target_sum = 0
    assert solution.pathSum(root, target_sum) == 0

    # Test case 3: Single node equals target sum
    root = TreeNode(5)
    target_sum = 5
    assert solution.pathSum(root, target_sum) == 1

    # Test case 4: No paths equal to target sum
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    target_sum = 10
    assert solution.pathSum(root, target_sum) == 0