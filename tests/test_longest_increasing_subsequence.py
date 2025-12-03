from src.longest_increasing_subsequence import Solution


def test_longest_increasing_subsequence():
    solution = Solution()

    # Test case 1: Standard case with mixed numbers
    assert solution.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
    # LIS could be [2, 3, 7, 101] or [2, 3, 7, 18]

    # Test case 2: Strictly decreasing sequence
    assert solution.lengthOfLIS([0]) == 1

    # Test case 3: Single element
    assert solution.lengthOfLIS([5]) == 1

    # Test case 4: All increasing
    assert solution.lengthOfLIS([1, 2, 3, 4, 5]) == 5

    # Test case 5: All decreasing
    assert solution.lengthOfLIS([5, 4, 3, 2, 1]) == 1

    # Test case 6: Two elements
    assert solution.lengthOfLIS([1, 2]) == 2

    # Test case 7: Two elements decreasing
    assert solution.lengthOfLIS([2, 1]) == 1

    # Test case 8: Multiple same values
    assert solution.lengthOfLIS([3, 3, 3, 3]) == 1

    # Test case 9: Complex case with duplicates
    assert solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 8]) == 6
    # LIS could be [1, 3, 6, 7, 9, 10] or similar

    # Test case 10: Large numbers
    assert solution.lengthOfLIS([0, 1, 0, 4, 4, 4, 3, 5, 9]) == 5

    # Test case 11: Failed
    assert solution.lengthOfLIS([1,3,6,7,9,4,10,5,6]) == 6

def test_failed():
    solution = Solution()
    assert solution.lengthOfLIS([1, 3, 6, 7, 9, 4, 10, 5, 8]) == 6