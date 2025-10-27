from src.max_area_of_island import Solution

def test_max_area_of_island():
    solution = Solution()

    grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
    assert solution.maxAreaOfIsland(grid) == 4

    # Test case 1: Example from LeetCode (expected max area 6)
    grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
    ]
    assert solution.maxAreaOfIsland(grid) == 6

    # Test case 2: All water
    grid = [[0,0,0],[0,0,0],[0,0,0]]
    assert solution.maxAreaOfIsland(grid) == 0

    # Test case 3: Single land cell
    grid = [[1]]
    assert solution.maxAreaOfIsland(grid) == 1

    # Test case 4: 

