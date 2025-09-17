from src.binary_tree_level_order_traverse import Solution, TreeNode

def build_tree_from_array(arr):
    if not arr:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in arr]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

def test_binary_tree_level_order_traverse():
    solution = Solution()

    # Test case 1: Example tree [3,9,20,None,None,15,7]
    root = build_tree_from_array([3,9,20,None,None,15,7])
    assert solution.levelOrder(root) == [[3],[9,20],[15,7]]

    # Test case 2: Single node [1]
    root = build_tree_from_array([1])
    assert solution.levelOrder(root) == [[1]]

    # Test case 3: Empty tree []
    root = build_tree_from_array([])
    assert solution.levelOrder(root) == []
