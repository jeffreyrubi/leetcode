from src.validate_binary_search_tree import Solution
from src.validate_binary_search_tree import TreeNode

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

def test_validate_binary_search_tree():
    solution = Solution()
    # Test case 1: Valid BST [2,1,3]
    valid_bst = build_tree_from_array([2,1,3])
    assert solution.isValidBST(valid_bst) == True

    # Test case 2: Invalid BST [5,1,4,null,null,3,6]
    invalid_bst = build_tree_from_array([5,1,4,None,None,3,6])
    assert solution.isValidBST(invalid_bst) == False

    invalid_bst = build_tree_from_array([5,4,6,None,None,3,7])
    assert solution.isValidBST(invalid_bst) == False
