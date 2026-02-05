from src.lc75_delete_node_in_bst import Solution, TreeNode

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

def tree_to_array(root):
    """Convert tree to level-order array representation"""
    if not root:
        return []
    result = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

def test_lc75_delete_node_in_bst():
    solution = Solution()
    
    # Test case 1: Delete node with two children
    # Tree: [5,3,6,2,4,None,7], delete key=3
    # Expected: [5,4,6,2,None,None,7] or [5,2,6,None,4,None,7]
    root = build_tree_from_array([5,3,6,2,4,None,7])
    result = solution.deleteNode(root, 3)
    result_arr = tree_to_array(result)
    # Either successor (4) or predecessor (2) can replace deleted node
    assert result_arr in [[5,4,6,2,None,None,7], [5,2,6,None,4,None,7]]

    # Test case 2: Delete root node
    # Tree: [5,3,6,2,4,None,7], delete key=5
    root = build_tree_from_array([5,3,6,2,4,None,7])
    result = solution.deleteNode(root, 5)
    result_arr = tree_to_array(result)
    # Root can be replaced by successor (6) or predecessor (4)
    assert result_arr in [[6,3,7,2,4], [4,3,6,2,None,None,7]]

    # Test case 3: Delete leaf node
    # Tree: [5,3,6,2,4,None,7], delete key=7
    root = build_tree_from_array([5,3,6,2,4,None,7])
    result = solution.deleteNode(root, 7)
    assert tree_to_array(result) == [5,3,6,2,4]

    # Test case 4: Delete node not in tree
    # Tree: [5,3,6,2,4,None,7], delete key=0
    root = build_tree_from_array([5,3,6,2,4,None,7])
    result = solution.deleteNode(root, 0)
    assert tree_to_array(result) == [5,3,6,2,4,None,7]

    # Test case 5: Delete from single node tree
    root = build_tree_from_array([5])
    result = solution.deleteNode(root, 5)
    assert tree_to_array(result) == []

    # Test case 6: Delete from empty tree
    root = build_tree_from_array([])
    result = solution.deleteNode(root, 5)
    assert tree_to_array(result) == []
