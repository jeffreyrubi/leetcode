from src.lc75_reorder_routes import Solution

def test_lc75_reorder_routes():
    solution = Solution()

    # Test case 1: Example from LeetCode
    # Tree: 0 <- 1 <- 2, 0 <- 3 <- 4 <- 5
    # Need to reorder: 1->0, 3->0, 4->3 (3 edges)
    n = 6
    connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
    expected = 3
    assert solution.minReorder(n, connections) == expected

    # Test case 2: All edges already point toward city 0
    n = 5
    connections = [[1, 0], [1, 2], [3, 2], [3, 4]]
    expected = 2
    assert solution.minReorder(n, connections) == expected

    # Test case 3: All edges point away from city 0
    n = 5
    connections = [[0, 1], [1, 2], [2, 3], [3, 4]]
    expected = 4
    assert solution.minReorder(n, connections) == expected

    # Test case 4: Simple case with 3 cities
    n = 3
    connections = [[1, 0], [2, 0]]
    expected = 0
    assert solution.minReorder(n, connections) == expected

    # Test case 5: Another simple case
    n = 3
    connections = [[0, 1], [0, 2]]
    expected = 2
    assert solution.minReorder(n, connections) == expected

    # Test case 6: Mixed directions
    n = 4
    connections = [[0, 1], [2, 1], [3, 2]]
    expected = 1
    assert solution.minReorder(n, connections) == expected

    # Test case 7: Larger tree
    n = 7
    connections = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6]]
    expected = 6
    assert solution.minReorder(n, connections) == expected

    print("All test cases passed!")
