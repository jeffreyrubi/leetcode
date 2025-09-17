from src.best_time_to_buy_and_sell_stocks import Solution

def test_best_time_to_buy_and_sell_stocks():
    solution = Solution()

    # Test case 1: Example input
    assert solution.maxProfit([7,1,5,3,6,4]) == 5

    # Test case 2: No profit possible
    assert solution.maxProfit([7,6,4,3,1]) == 0

    # Test case 3: Profit at the end
    assert solution.maxProfit([2,4,1]) == 2
