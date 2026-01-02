from src.lc75_equal_row_and_column_pairs import Solution

def test_lc75_equal_row_and_column_pairs():
    solution = Solution()

    # Test case 1: Simple 2x2 grid
    grid = [
        [1, 2],
        [2, 1]
    ]
    assert solution.equalPairs(grid) == 2

    # Test case 2: Matching rows and columns
    grid = [
        [1, 2],
        [1, 2]
    ]
    assert solution.equalPairs(grid) == 0

    # Test case 3: Larger grid with multiple matches
    grid = [
        [3, 1, 2, 2],
        [1, 4, 4, 5],
        [2, 4, 2, 2],
        [2, 5, 2, 2]
    ]
    assert solution.equalPairs(grid) == 4

    # Test case 4: Single row and column
    grid = [
        [1]
    ]
    assert solution.equalPairs(grid) == 1

    # Test case 5: No matching rows and columns
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert solution.equalPairs(grid) == 0

