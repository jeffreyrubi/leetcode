from src.diameter_of_BST import Solution

def test_diameter_of_BST():
    solution = Solution()
    from src.diameter_of_BST import TreeNode

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

    # Test case 1: Example tree [1,2,3,4,5] -> diameter 3
    root = build_tree_from_array([1,2,3,4,5])
    assert solution.diameterOfBinaryTree(root) == 3

    # Test case 2: Single node -> diameter 0
    root = build_tree_from_array([1])
    assert solution.diameterOfBinaryTree(root) == 0

    # Test case 3: Skewed tree -> diameter n-1
    root = build_tree_from_array([1,2,None,3,None,4,None])
    assert solution.diameterOfBinaryTree(root) == 3

