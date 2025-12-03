from src.binary_tree_maximum_path_sum import Solution, TreeNode

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

def test_binary_tree_maximum_path_sum():
    solution = Solution()
    
    # Test case 1: Example from LeetCode [1,2,3] -> path: 2->1->3, sum = 6
    root = build_tree_from_array([1,2,3])
    assert solution.maxPathSum(root) == 6
    
    # Test case 2: Example with negative values [-10,9,20,None,None,15,7] -> path: 15->20->7, sum = 42
    root = build_tree_from_array([-10,9,20,None,None,15,7])
    assert solution.maxPathSum(root) == 42
    
    # Test case 3: Single node [1] -> path: just 1, sum = 1
    root = build_tree_from_array([1])
    assert solution.maxPathSum(root) == 1
    
    # Test case 4: Single negative node [-3] -> path: just -3, sum = -3
    root = build_tree_from_array([-3])
    assert solution.maxPathSum(root) == -3
    
    # Test case 5: All negative values [-1,-2,-3] -> path: just -1, sum = -1
    root = build_tree_from_array([-1,-2,-3])
    assert solution.maxPathSum(root) == -1
    
    # Test case 6: Path through root [2,-1,-2] -> path: just 2, sum = 2
    root = build_tree_from_array([2,-1,-2])
    assert solution.maxPathSum(root) == 2
    
    # Test case 7: Path doesn't go through root [1,-2,-3,1,3,-2,None,-1] -> path: 1->-2->3, sum = 2
    root = build_tree_from_array([1,-2,-3,1,3,-2,None,-1])
    assert solution.maxPathSum(root) == 3  # The path is just the node with value 3
    
    # Test case 8: Linear tree (skewed) [1,2,None,3,None,4,None] -> path: 4->3->2->1, sum = 10
    root = build_tree_from_array([1,2,None,3,None,4,None])
    assert solution.maxPathSum(root) == 10
    
    # Test case 9: Complex case with mixed positive/negative values [5,4,8,11,None,13,4,7,2,None,None,None,1]
    # This creates a tree where maximum path might be 7->11->4->5->8->13 = 48
    root = build_tree_from_array([5,4,8,11,None,13,4,7,2,None,None,None,1])
    assert solution.maxPathSum(root) == 48
    
    root = build_tree_from_array([9,6,-3,None,None,-6,2,None,None,2,None,-6,-6,-6])
    assert solution.maxPathSum(root) == 16

    print("All test cases passed!")