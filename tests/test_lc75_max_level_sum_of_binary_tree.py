from src.lc75_max_level_sum_of_binary_tree import Solution, TreeNode

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

def test_lc75_max_level_sum_of_binary_tree():
    solution = Solution()

    # Test case 1: Example from problem [1,7,0,7,-8,None,None]
    # Level 1: 1, Level 2: 7+0=7, Level 3: 7+(-8)=-1
    # Max sum is 7 at level 2
    root = build_tree_from_array([1,7,0,7,-8,None,None])
    assert solution.maxLevelSum(root) == 2

    # Test case 2: Example [989,None,10250,98693,-89388,None,None,None,-32127]
    # Level 1: 989, Level 2: 10250, Level 3: 98693+(-89388)=9305, Level 4: -32127
    # Max sum is 10250 at level 2
    root = build_tree_from_array([989,None,10250,98693,-89388,None,None,None,-32127])
    assert solution.maxLevelSum(root) == 2

    # Test case 3: Single node
    root = build_tree_from_array([1])
    assert solution.maxLevelSum(root) == 1

    # Test case 4: Max sum at root level
    root = build_tree_from_array([100,1,1,1,1,1,1])
    assert solution.maxLevelSum(root) == 1

    # Test case 5: Max sum at deepest level
    root = build_tree_from_array([1,2,3,100,100,100,100])
    assert solution.maxLevelSum(root) == 3
