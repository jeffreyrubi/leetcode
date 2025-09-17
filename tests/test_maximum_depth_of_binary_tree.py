from src.maximum_depth_of_binary_tree import Solution, TreeNode

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

def test_maximum_depth_of_binary_tree():
    solution = Solution()

    # Test case 1: Example tree [3,9,20,None,None,15,7]
    root = build_tree_from_array([3,9,20,None,None,15,7])
    assert solution.maxDepth(root) == 3

    # Test case 2: Single node [1]
    root = build_tree_from_array([1])
    assert solution.maxDepth(root) == 1

    # Test case 3: Empty tree []
    root = build_tree_from_array([])
    assert solution.maxDepth(root) == 0
