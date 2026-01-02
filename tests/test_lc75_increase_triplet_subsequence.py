from src.lc75_increase_triplet_subsequence import Solution

def test_lc75_increase_triplet_subsequence():
    solution = Solution()
    
    # Test case 1: Basic triplet exists
    # assert solution.increasingTriplet([1, 2, 3, 4, 5]) == True
    
    # # Test case 2: No triplet exists (decreasing)
    # assert solution.increasingTriplet([5, 4, 3, 2, 1]) == False
    
    # # Test case 3: Given example 1 - triplet exists
    # assert solution.increasingTriplet([1, 2, 3, 4, 5]) == True
    
    # # Test case 4: Given example 2 - no triplet
    # assert solution.increasingTriplet([5, 4, 3, 2, 1]) == False
    
    # # Test case 5: Given example 3 - triplet exists
    # assert solution.increasingTriplet([2, 1, 5, 0, 4, 6]) == True
    
    # # Test case 6: Edge case - less than 3 elements
    # assert solution.increasingTriplet([1, 2]) == False
    # assert solution.increasingTriplet([]) == False
    # assert solution.increasingTriplet([1]) == False
    
    # # Test case 7: All same elements
    # assert solution.increasingTriplet([1, 1, 1, 1]) == False
    
    # Test case 8: Two increasing pairs but no triplet
    # assert solution.increasingTriplet([1, 5, 3, 4, 2]) == True
    
    # Test case 9: Complex case with triplet at the end
    assert solution.increasingTriplet([20, 100, 10, 12, 5, 13]) == True
    
    # Test case 10: Triplet with negative numbers
    assert solution.increasingTriplet([-1, 0, 1]) == True
    
    # Test case 11: Large numbers
    assert solution.increasingTriplet([1000, 999, 998, 997, 996]) == False
    
    # Test case 12: Minimum valid triplet
    assert solution.increasingTriplet([1, 2, 3]) == True
    
    # Test case 13: Non-consecutive triplet
    assert solution.increasingTriplet([1, 5, 2, 3, 4]) == True
    
    # Test case 14: Triplet with duplicates in between
    assert solution.increasingTriplet([1, 1, 2, 2, 3]) == True
    
    # Test case 15: Almost triplet but missing third element
    assert solution.increasingTriplet([1, 2]) == False
    