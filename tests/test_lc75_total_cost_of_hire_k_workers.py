from src.lc75_total_cost_of_hire_k_workers import Solution

def test_lc75_total_cost_of_hire_k_workers():
    solution = Solution()
    
    # Test case 1: Basic example
    assert solution.totalCost([17,12,10,2,7,2,11,20,8], k=3, candidates=4) == 11
    
    # Test case 2: Another basic example
    assert solution.totalCost([1,2,4,1], k=3, candidates=3) == 4
    
    # Test case 3: All candidates cover the entire array
    assert solution.totalCost([10,1,11,2,3,4], k=2, candidates=3) == 3
    
    # Test case 4: Single worker
    assert solution.totalCost([5], k=1, candidates=1) == 5
    
    # Test case 5: Hire all workers
    assert solution.totalCost([1,2,3,4,5], k=5, candidates=2) == 15
    
    # Test case 7: Workers with same cost
    assert solution.totalCost([5,5,5,5,5], k=3, candidates=2) == 15
    
    # Test case 8: Only choose from left side
    assert solution.totalCost([1,2,3,100,101,102], k=3, candidates=3) == 6
    
    # Test case 9: Only choose from right side
    assert solution.totalCost([100,101,102,1,2,3], k=3, candidates=3) == 6
    
    # Test case 10: Mixed selection
    assert solution.totalCost([31,25,72,79,74,65,84,91,18,59,27,9,81,33,17,58], k=11, candidates=2) == 423
    