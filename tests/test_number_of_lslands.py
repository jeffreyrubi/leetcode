from src.number_of_islands import Solution

def test_number_of_islands():
    solution = Solution()

    # Test case 1: Multiple islands
    grid1 = [
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
    ]
    assert solution.numIslands(grid1) == 1

    # Test case 2: Two islands
    grid2 = [
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
    ]
    assert solution.numIslands(grid2) == 3

