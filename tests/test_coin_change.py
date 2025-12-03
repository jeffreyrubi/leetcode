from src.coin_change import Solution

def test_coin_change():
    solution = Solution()
    assert solution.coinChange([1,2,5], 11) == 3    # 5+5+1
    assert solution.coinChange([2], 3) == -1
    assert solution.coinChange([1], 0) == 0
    assert solution.coinChange([1], 1) == 1
    assert solution.coinChange([1], 2) == 2
    assert solution.coinChange([2,5], 10) == 2     # 5+5
    assert solution.coinChange([186,419,83,408], 6249) == 20
    assert solution.coinChange([1,2147483647], 2) == 2