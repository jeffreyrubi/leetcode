from src.lc75_nearest_exist_from_entrance import Solution

def test_lc75_nearest_exist_from_entrance():
    solution = Solution()

    # Test case 1: Example from LeetCode
    maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
    entrance = [1, 2]
    expected = 1
    assert solution.nearestExit(maze, entrance) == expected

    # Test case 2: Example with longer path
    maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
    entrance = [1, 0]
    expected = 2
    assert solution.nearestExit(maze, entrance) == expected

    # Test case 3: No exit available
    maze = [["+", "+", "+"], ["+", ".", "+"], ["+", "+", "+"]]
    entrance = [1, 1]
    expected = -1
    assert solution.nearestExit(maze, entrance) == expected

    # Test case 4: Exit immediately adjacent
    maze = [[".", "+"]]
    entrance = [0, 0]
    expected = -1  # The entrance itself doesn't count as an exit
    assert solution.nearestExit(maze, entrance) == expected

    # Test case 5: Simple case with exit on border
    maze = [[".", "."], [".", "+"]]
    entrance = [1, 0]
    expected = 1
    assert solution.nearestExit(maze, entrance) == expected

    # Test case 6: Larger maze
    maze = [
        [".", "+", "+", "+", "+"],
        [".", ".", ".", ".", "."],
        ["+", "+", ".", "+", "."],
        [".", ".", ".", ".", "."],
        ["+", "+", "+", "+", "."]
    ]
    entrance = [0, 0]
    expected = 1  # Entrance is already on border, but doesn't count
    assert solution.nearestExit(maze, entrance) == expected

    # Test case 7: Multiple possible exits
    maze = [
        [".", ".", "."],
        [".", "+", "."],
        [".", ".", "."]
    ]
    entrance = [1, 1]
    expected = 1  # Blocked by wall, can't reach any border
    assert solution.nearestExit(maze, entrance) == expected

    # Test case 8: Valid path to exit
    maze = [
        ["+", ".", "+", "+", "+", "+", "+"],
        ["+", ".", "+", ".", ".", ".", "+"],
        ["+", ".", "+", ".", "+", ".", "+"],
        ["+", ".", ".", ".", "+", ".", "+"],
        ["+", "+", "+", "+", "+", ".", "+"]
    ]
    entrance = [0, 1]
    expected = 12
    assert solution.nearestExit(maze, entrance) == expected

    print("All test cases passed!")
