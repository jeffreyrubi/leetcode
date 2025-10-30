from src.sum_of_two_integers import Solution

def test_sum_of_two_integers():
    solution = Solution()

    # Test positive numbers
    assert solution.getSum(1, 2) == 3
    assert solution.getSum(4, 5) == 9
    assert solution.getSum(10, 20) == 30
    
    # Test negative numbers
    assert solution.getSum(-1, -2) == -3
    assert solution.getSum(-5, -7) == -12
    
    # Test mixing positive and negative numbers
    assert solution.getSum(1, -1) == 0
    assert solution.getSum(-5, 3) == -2
    assert solution.getSum(10, -7) == 3
    
    # Test cases with zero
    assert solution.getSum(0, 0) == 0
    assert solution.getSum(0, 5) == 5
    assert solution.getSum(-7, 0) == -7
    
    # Test larger numbers
    assert solution.getSum(100, 200) == 300
    assert solution.getSum(-150, 50) == -100