from src.lc75_lowest_common_ancester_of_binary_tree import Solution, TreeNode

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

def find_node(root, val):
    """Helper function to find a node with given value in the tree"""
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

def test_lc75_lowest_common_ancester_of_binary_tree():
    solution = Solution()

    # Test case 1: Example tree [3,5,1,6,2,0,8,null,null,7,4]
    # LCA of 5 and 1 is 3
    root = build_tree_from_array([3,5,1,6,2,0,8,None,None,7,4])
    p = find_node(root, 5)
    q = find_node(root, 1)
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 3

    # Test case 2: LCA of 5 and 4 is 5
    # When one node is ancestor of another
    root = build_tree_from_array([3,5,1,6,2,0,8,None,None,7,4])
    p = find_node(root, 5)
    q = find_node(root, 4)
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 5

    # Test case 3: Two leaf nodes with close common ancestor
    root = build_tree_from_array([3,5,1,6,2,0,8,None,None,7,4])
    p = find_node(root, 7)
    q = find_node(root, 4)
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 2

    # Test case 4: Simple tree with two nodes
    root = build_tree_from_array([1,2])
    p = find_node(root, 1)
    q = find_node(root, 2)
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 1

    # Test case 5: LCA of nodes on opposite sides
    root = build_tree_from_array([3,5,1,6,2,0,8,None,None,7,4])
    p = find_node(root, 6)
    q = find_node(root, 8)
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 3

    # Test case 6: Root is one of the nodes
    root = build_tree_from_array([3,5,1,6,2,0,8,None,None,7,4])
    p = find_node(root, 3)
    q = find_node(root, 5)
    result = solution.lowestCommonAncestor(root, p, q)
    assert result.val == 3



