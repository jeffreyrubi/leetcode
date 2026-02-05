from src.lc75_edit_distance import Solution

def test_min_distance():
    solution = Solution()

    # Test case 1: Both strings are empty
    assert solution.minDistance("", "") == 0

    # Test case 2: One string is empty
    assert solution.minDistance("abc", "") == 3
    assert solution.minDistance("", "def") == 3

    # Test case 3: Identical strings
    assert solution.minDistance("leetcode", "leetcode") == 0

    # Test case 4: General case
    assert solution.minDistance("horse", "ros") == 3
    assert solution.minDistance("intention", "execution") == 5
    