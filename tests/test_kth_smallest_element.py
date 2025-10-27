from src.kth_smallest_element import Solution

def test_kth_smallest_element():
    solution = Solution()
    from src.kth_smallest_element import TreeNode

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

    # Test case 1: Example BST
    root = build_tree_from_array([3,1,4,None,2])
    assert solution.kthSmallest(root, 1) == 1

    # Test case 2: Larger BST
    root = build_tree_from_array([5,3,6,2,4,None,None,1])
    assert solution.kthSmallest(root, 3) == 3

    # Test case 3: Single node
    root = build_tree_from_array([1])
    assert solution.kthSmallest(root, 1) == 1

