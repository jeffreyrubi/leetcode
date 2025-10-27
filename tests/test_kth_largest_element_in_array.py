from src.kth_largest_element_in_array import Solution

def test_kth_largest_element_in_array():
    solution = Solution()

    # Test case 1: Example input
    assert solution.findKthLargest([3,2,1,5,6,4], 2) == 5

    # Test case 2: k is 1 (largest element)
    assert solution.findKthLargest([3,2,3,1,2,4,5,5,6], 1) == 6

    # Test case 3: k is length of array (smallest element)
    assert solution.findKthLargest([7,10,4,3,20,15], 6) == 3

