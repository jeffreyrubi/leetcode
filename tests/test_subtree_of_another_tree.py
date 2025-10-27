from src.subtree_of_another_tree import Solution

def test_subtree_of_another_tree():
    solution = Solution()
    from src.subtree_of_another_tree import TreeNode

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

    # Test case 1: Subtree exists
    s = build_tree_from_array([3,4,5,1,2])
    t = build_tree_from_array([4,1,2])
    assert solution.isSubtree(s, t) == True

    # Test case 2: Subtree does not exist
    s = build_tree_from_array([3,4,5,1,2,None,None,None,None,0])
    t = build_tree_from_array([4,1,2])
    assert solution.isSubtree(s, t) == False

    # Test case 3: Identical trees
    s = build_tree_from_array([1,2,3])
    t = build_tree_from_array([1,2,3])
    assert solution.isSubtree(s, t) == True
