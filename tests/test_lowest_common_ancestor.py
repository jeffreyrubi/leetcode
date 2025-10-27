from src.lowest_common_ancestor import Solution

def test_lowest_common_ancestor():
    solution = Solution()
    from src.lowest_common_ancestor import TreeNode

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
        if not root:
            return None
        if root.val == val:
            return root
        left = find_node(root.left, val)
        if left:
            return left
        return find_node(root.right, val)

    # Test case 1: Example tree [3,5,1,6,2,0,8,None,None,7,4]
    root = build_tree_from_array([3,5,1,6,2,0,8,None,None,7,4])
    p = find_node(root, 5)
    q = find_node(root, 1)
    assert solution.lowestCommonAncestor(root, p, q).val == 3

    # Test case 2: Nodes in same subtree (LCA is one of them)
    p = find_node(root, 5)
    q = find_node(root, 4)
    assert solution.lowestCommonAncestor(root, p, q).val == 5

    # Test case 3: Root and another node
    p = find_node(root, 3)
    q = find_node(root, 4)
    assert solution.lowestCommonAncestor(root, p, q).val == 3
