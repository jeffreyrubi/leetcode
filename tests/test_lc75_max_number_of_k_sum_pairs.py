from src.lc75_max_number_of_k_sum_pairs import Solution

def test_lc75_max_number_of_k_sum_pairs():
    solution = Solution()
    
    # Test case 1: LeetCode Example 1 - [1,2,3,4], k=5
    # Pairs: (1,4), (2,3) = 2 operations
    assert solution.maxOperations([1, 2, 3, 4], 5) == 2
    
    # Test case 2: LeetCode Example 2 - [3,1,3,4,3], k=6  
    # Pairs: (3,3) once = 1 operation
    assert solution.maxOperations([3, 1, 3, 4, 3], 6) == 1
    
    # Test case 3: Empty array
    assert solution.maxOperations([], 5) == 0
    
    # Test case 4: Single element (no pairs possible)
    assert solution.maxOperations([5], 10) == 0
    
    # Test case 5: No valid pairs
    assert solution.maxOperations([1, 2, 3], 10) == 0
    
    # Test case 6: All elements are k/2 (special case)
    # [3,3,3,3] with k=6 -> can form 2 pairs
    assert solution.maxOperations([3, 3, 3, 3], 6) == 2
    
    # Test case 7: Odd number of k/2 elements
    # [4,4,4] with k=8 -> can form 1 pair (one element left over)
    assert solution.maxOperations([4, 4, 4], 8) == 1
    
    # Test case 8: Multiple different pairs
    # [1,2,3,4,5,6] with k=7 -> pairs: (1,6), (2,5), (3,4) = 3 operations
    assert solution.maxOperations([1, 2, 3, 4, 5, 6], 7) == 3
    
    # Test case 9: Duplicate elements with multiple pairs
    # [2,2,2,3,1,1,4,1] with k=4 -> pairs: (3,1), (2,2) = 2 operations
    assert solution.maxOperations([2, 2, 2, 3, 1, 1, 4, 1], 4) == 2
    
    # Test case 10: Large numbers
    assert solution.maxOperations([1000, 2000, 3000], 3000) == 1
    
    # Test case 11: Negative numbers
    # [-1, 1, 0] with k=0 -> pair: (-1,1) = 1 operation
    assert solution.maxOperations([-1, 1, 0], 0) == 1
    
    # Test case 12: All pairs can be formed
    # [1,5,2,4,3,3] with k=6 -> pairs: (1,5), (2,4), (3,3) = 3 operations
    assert solution.maxOperations([1, 5, 2, 4, 3, 3], 6) == 3
    
    # Test case 13: k is 0
    # [-2, 2, 0, 0] with k=0 -> pairs: (-2,2), (0,0) = 2 operations
    assert solution.maxOperations([-2, 2, 0, 0], 0) == 2
    
    # Test case 14: k is negative
    # [-5, -3, -1] with k=-8 -> pair: (-5,-3) = 1 operation
    assert solution.maxOperations([-5, -3, -1], -8) == 1