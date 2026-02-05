from src.lc75_find_peak_element import Solution

def test_lc75_find_peak_element():
    solution = Solution()

    # # Test case 1: Example from LeetCode - peak in the middle
    # nums = [1, 2, 3, 1]
    # result = solution.findPeakElement(nums)
    # assert result == 2  # Index 2 has value 3, which is a peak
    
    # Test case 2: Example from LeetCode - multiple peaks
    nums = [1, 2, 1, 3, 5, 6, 4]
    result = solution.findPeakElement(nums)
    # Either index 1 (value 2) or index 5 (value 6) is valid
    assert result == 1 or result == 5
    
    # Test case 3: Single element
    nums = [1]
    result = solution.findPeakElement(nums)
    assert result == 0
    
    # Test case 4: Two elements - ascending
    nums = [1, 2]
    result = solution.findPeakElement(nums)
    assert result == 1
    
    # Test case 5: Two elements - descending
    nums = [2, 1]
    result = solution.findPeakElement(nums)
    assert result == 0
    
    # Test case 6: Ascending array (peak at end)
    nums = [1, 2, 3, 4, 5]
    result = solution.findPeakElement(nums)
    assert result == 4
    
    # Test case 7: Descending array (peak at start)
    nums = [5, 4, 3, 2, 1]
    result = solution.findPeakElement(nums)
    assert result == 0
    
    # Test case 8: Peak at the beginning
    nums = [3, 2, 1]
    result = solution.findPeakElement(nums)
    assert result == 0
    
    # Test case 9: Peak at the end
    nums = [1, 2, 3]
    result = solution.findPeakElement(nums)
    assert result == 2
    
    # Test case 10: Valley in the middle (peaks on both sides)
    nums = [1, 3, 2, 4, 1]
    result = solution.findPeakElement(nums)
    # Either index 1 or index 3 is valid
    assert result == 1 or result == 3
