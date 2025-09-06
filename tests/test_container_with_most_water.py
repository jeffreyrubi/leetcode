from src.container_with_most_water import Solution

def test_container_with_most_water():
    solution = Solution()

    # Test case 1: Example input
    assert solution.maxArea([1,8,6,2,5,4,8,3,7]) == 49

    # Test case 2: Smallest input
    assert solution.maxArea([1,1]) == 1

    # Test case 3: Increasing heights
    assert solution.maxArea([1,2,3,4,5,6,7,8,9,10]) == 25
