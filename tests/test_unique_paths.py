from src.unique_paths import Solution

def test_unique_paths():
    solution = Solution()
    assert solution.uniquePaths(3, 7) == 28
    assert solution.uniquePaths(3, 2) == 3
    assert solution.uniquePaths(7, 3) == 28
    assert solution.uniquePaths(3, 3) == 6
    assert solution.uniquePaths(1, 1) == 1
    assert solution.uniquePaths(1, 5) == 1
    assert solution.uniquePaths(5, 1) == 1
    assert solution.uniquePaths(10, 10) == 48620
    