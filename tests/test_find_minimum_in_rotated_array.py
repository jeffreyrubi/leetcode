from src.find_minimum_in_rotated_array import Solution

def test_find_minimum_in_rotated_array():
    solution = Solution()

    # Test case 1: Rotated array
    assert solution.findMin([3,4,5,1,2]) == 1

    # Test case 2: Not rotated
    assert solution.findMin([1,2,3,4,5]) == 1

    # Test case 3: Single element
    assert solution.findMin([10]) == 10

    assert solution.findMin([2,1]) == 1
