from src.lc75_combination_sum_III import Solution

def test_combination_sum_3():
    solution = Solution()
    # Test case 1
    assert solution.combinationSum3(3, 7) == [[1, 2, 4]]

    # Test case 2
    assert solution.combinationSum3(3, 9) == [[1, 2, 6], [1, 3, 5], [2, 3, 4]]

    # Test case 3
    assert solution.combinationSum3(4, 1) == []
    