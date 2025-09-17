from src.same_tree import Solution, TreeNode

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

def test_same_tree():
    solution = Solution()

    # Test case 1: Same trees [1,2,3] and [1,2,3]
    p = build_tree_from_array([1,2,3])
    q = build_tree_from_array([1,2,3])
    assert solution.isSameTree(p, q) == True

    # Test case 2: Different structure [1,2] and [1,null,2]
    p = build_tree_from_array([1,2])
    q = build_tree_from_array([1,None,2])
    assert solution.isSameTree(p, q) == False

    # Test case 3: Different values [1,2,1] and [1,1,2]
    p = build_tree_from_array([1,2,1])
    q = build_tree_from_array([1,1,2])
    assert solution.isSameTree(p, q) == False
