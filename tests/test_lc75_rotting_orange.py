from src.lc75_rotting_orange import Solution

def test_lc75_rotting_orange():
    solution = Solution()

    # Test case 1: Example from LeetCode
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    expected = 4
    assert solution.orangesRotting(grid) == expected

    # Test case 2: Impossible to rot all oranges
    grid = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
    expected = -1
    assert solution.orangesRotting(grid) == expected

    # Test case 3: No fresh oranges
    grid = [[0, 2]]
    expected = 0
    assert solution.orangesRotting(grid) == expected

    # Test case 4: All oranges are already rotten
    grid = [[2, 2, 2], [2, 2, 2]]
    expected = 0
    assert solution.orangesRotting(grid) == expected

    # Test case 5: Single fresh orange with no rotten oranges
    grid = [[1]]
    expected = -1
    assert solution.orangesRotting(grid) == expected

    # Test case 6: Single rotten orange with no fresh oranges
    grid = [[2]]
    expected = 0
    assert solution.orangesRotting(grid) == expected

    # Test case 7: All empty cells
    grid = [[0, 0, 0], [0, 0, 0]]
    expected = 0
    assert solution.orangesRotting(grid) == expected

    # Test case 8: Fresh orange isolated by empty cells
    grid = [[2, 1, 0, 1]]
    expected = -1
    assert solution.orangesRotting(grid) == expected

    # Test case 9: Larger grid
    grid = [
        [2, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 2]
    ]
    expected = 3
    assert solution.orangesRotting(grid) == expected

    # Test case 10: Multiple rotten oranges initially
    grid = [[2, 1, 1], [1, 1, 1], [1, 1, 2]]
    expected = 2
    assert solution.orangesRotting(grid) == expected

    # Test case 11: Linear spread
    grid = [[2, 1, 1, 1, 1, 1]]
    expected = 5
    assert solution.orangesRotting(grid) == expected

    print("All test cases passed!")
