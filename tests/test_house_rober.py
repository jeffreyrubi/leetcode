from src.house_robber import Solution


def test_house_rober():
    solution = Solution()
    assert solution.rob([1,2,3,1]) == 4
    assert solution.rob([2,7,9,3,1]) == 12
    assert solution.rob([1,2]) == 2
    assert solution.rob([2,1]) == 2
    assert solution.rob([1]) == 1
    assert solution.rob([2,1,1,2]) == 4
    assert solution.rob([1,3,1,3,100]) == 103