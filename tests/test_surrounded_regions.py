from src.surrounded_regions import Solution

def test_surrounded_regions():
    solution = Solution()

    # Test case 1: Board with surrounded regions
    board1 = [
        ["X", "X", "X", "X"],
        ["X", "O", "O", "X"],
        ["X", "X", "O", "X"],
        ["X", "O", "X", "X"]
    ]
    expected1 = [
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "X", "X", "X"],
        ["X", "O", "X", "X"]
    ]
    solution.solve(board1)
    assert board1 == expected1

    # Test case 2: Board with no surrounded regions
    board2 = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "O", "X"]
    ]
    expected2 = [
        ["X", "O", "X"],
        ["O", "X", "O"],
        ["X", "O", "X"]
    ]
    solution.solve(board2)
    assert board2 == expected2
