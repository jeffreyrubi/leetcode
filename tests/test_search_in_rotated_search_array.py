from src.search_in_rotated_search_array import Solution

def test_search_in_rotated_search_array():
    solution = Solution()

    assert solution.search([4,5,6,7,0,1,2], 6) == 2

    # # Test case 1: Target found
    # assert solution.search([4,5,6,7,0,1,2], 0) == 4

    # Test case 2: Target not found
    # assert solution.search([4,5,6,7,0,1,2], 3) == -1

    # # Test case 3: Single element array
    # assert solution.search([1], 1) == 0

    # # Test case 4: Single element array
    # assert solution.search([1], 0) == -1

    # # Test case 3: Single element array
    # assert solution.search([1, 3], 0) == -1
