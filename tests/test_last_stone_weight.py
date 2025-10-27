from src.last_stone_weight import Solution

def test_last_stone_weight():
    solution = Solution()
    # Test case 1: Example
    assert solution.lastStoneWeight([2,7,4,1,8,1]) == 1

    # Test case 2: All equal
    assert solution.lastStoneWeight([3,3,3,3]) == 0

    # Test case 3: Single stone
    assert solution.lastStoneWeight([5]) == 5

