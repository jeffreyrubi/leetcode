from src.product_of_array import Solution

def test_product_of_array():
    solution = Solution()
    # Test case 1: Example input
    assert solution.productExceptSelf([1,2,3,4]) == [24,12,8,6]

    # Test case 2: Contains zero
    assert solution.productExceptSelf([0,1,2,3]) == [6,0,0,0]

    # Test case 3: Single element
    assert solution.productExceptSelf([5]) == [1]