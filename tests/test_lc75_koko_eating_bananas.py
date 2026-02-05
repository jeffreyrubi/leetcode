from src.lc75_koko_eating_bananas import Solution

def test_min_eating_speed():
    solution = Solution()

    # Test case 1: Basic case
    piles = [3, 6, 7, 11]
    h = 8
    assert solution.minEatingSpeed(piles, h) == 4

    # Test case 2: Single pile
    piles = [30]
    h = 5
    assert solution.minEatingSpeed(piles, h) == 6

    # Test case 3: Large number of piles
    piles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    h = 15
    assert solution.minEatingSpeed(piles, h) == 5

    # Test case 4: Minimum speed is 1
    piles = [1, 1, 1, 1]
    h = 4
    assert solution.minEatingSpeed(piles, h) == 1

    # Test case 5: All piles are the same
    piles = [10, 10, 10]
    h = 6
    assert solution.minEatingSpeed(piles, h) == 5