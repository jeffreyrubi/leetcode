from src.binary_search import Solution

def test_binary_search():
    solution = Solution()
    # Test case 1: Target exists
    assert solution.search([-1,0,3,5,9,12], 9) == 4

    # Test case 2: Target does not exist
    assert solution.search([-1,0,3,5,9,12], 2) == -1

    # Test case 3: Empty array
    assert solution.search([], 1) == -1
