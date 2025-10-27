from src.count_good_node_in_binary_tree import Solution

def test_count_good_node_in_binary_tree():
    solution = Solution()
    from src.count_good_node_in_binary_tree import TreeNode

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

    # Test case 1: Example from problem
    root = build_tree_from_array([3,1,4,3,None,1,5])
    assert solution.goodNodes(root) == 4

    # Test case 2: Single node
    root = build_tree_from_array([1])
    assert solution.goodNodes(root) == 1

    # Test case 3: Left-heavy where some nodes are not good
    root = build_tree_from_array([3,3,None,4,2])
    assert solution.goodNodes(root) == 3
