from src.binary_tree_right_hand_side import Solution, TreeNode

def test_binary_tree_right_hand_side():
    solution = Solution()

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

    # Test case 1: Example tree [1,2,3,None,5,None,4]
    root = build_tree_from_array([1,2,3,None,5,None,4])
    assert solution.rightSideView(root) == [1,3,4]

    # Test case 2: Single node [1]
    root = build_tree_from_array([1])
    assert solution.rightSideView(root) == [1]

    # Test case 3: Empty tree []
    root = build_tree_from_array([])
    assert solution.rightSideView(root) == []
