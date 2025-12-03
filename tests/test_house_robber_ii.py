from src.house_robber_ii import Solution

def test_house_robber_ii():
    solution = Solution()

    # Example 1
    assert solution.rob([2, 3, 2]) == 3

    # Example 2
    assert solution.rob([1, 2, 3, 1]) == 4

    # Example 3
    assert solution.rob([1, 2, 3]) == 3

    # Single house
    assert solution.rob([1]) == 1

    # Two houses
    assert solution.rob([1, 2]) == 2
    assert solution.rob([2, 1]) == 2

    # All same value
    assert solution.rob([5, 5, 5, 5]) == 10

    # Optimal: skip first or last
    assert solution.rob([1, 2, 1, 2, 1]) == 4  # rob 2nd and 4th

    # Large gap in middle
    assert solution.rob([4, 1, 2, 7, 5, 3, 1]) == 14  # rob 4, 7, 1 or 4, 5, 1 → max 12

    # All zeros
    assert solution.rob([0, 0, 0, 0]) == 0

    # Best at ends
    assert solution.rob([10, 1, 1, 10]) == 11
    assert solution.rob([10, 1, 1, 20]) == 21