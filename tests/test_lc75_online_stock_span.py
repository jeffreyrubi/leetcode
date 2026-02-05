from src.lc75_online_stock_span import Solution

def test_lc75_online_stock_span():
    solution = Solution()
    # Test case 1: Basic functionality
    assert solution.next(100) == 1
    assert solution.next(80) == 1
    assert solution.next(60) == 1
    assert solution.next(70) == 2
    assert solution.next(60) == 1
    assert solution.next(75) == 4
    assert solution.next(85) == 6

    # Test case 2: Increasing prices
    assert solution.next(90) == 7
    assert solution.next(95) == 8

    # Test case 3: Decreasing prices
    assert solution.next(50) == 1
    assert solution.next(40) == 1
