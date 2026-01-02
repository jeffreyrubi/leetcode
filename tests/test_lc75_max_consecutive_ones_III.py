from src.lc75_max_consecutive_ones_III import Solution

def test_lc75_max_consecutive_ones_III():
    solution = Solution()

    # All zeros, k = 1
    assert solution.longestOnes([0,0,1,1], 1) == 3

    # Example 1 from LeetCode: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    # Can flip 2 zeros to get [1,1,1,0,0,1,1,1,1,1,1] -> max length = 6
    assert solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) == 6
    
    # Example 2 from LeetCode: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    # Can flip 3 zeros to get consecutive sequence of length 10
    assert solution.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3) == 10
    
    # Edge case: All ones, k = 0
    assert solution.longestOnes([1,1,1,1], 0) == 4
    
    # Edge case: All zeros, k = 2
    assert solution.longestOnes([0,0,0,0], 2) == 2
    
    # Edge case: Single element (1), k = 0
    assert solution.longestOnes([1], 0) == 1
    
    # Edge case: Single element (0), k = 1
    assert solution.longestOnes([0], 1) == 1
    
    # Edge case: Single element (0), k = 0
    assert solution.longestOnes([0], 0) == 0
    
    # k is larger than number of zeros
    assert solution.longestOnes([0,1,0,1,0], 5) == 5
    
    # k = 0, mixed array
    assert solution.longestOnes([1,1,0,1,1,0,1], 0) == 2
    
    # All zeros, k = 0
    assert solution.longestOnes([0,0,0], 0) == 0
    
    # More complex case
    assert solution.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 1) == 5
    
    # k equals exact number of zeros
    assert solution.longestOnes([1,0,1,0,1], 2) == 5
    
    # Large k value
    assert solution.longestOnes([0,0,0,1,1,1,0,0], 10) == 8


