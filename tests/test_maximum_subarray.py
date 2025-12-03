from src.maximum_subarray import Solution

def test_maxiumum_subarray():
    solution = Solution()
    assert solution.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]) == 6
    assert solution.maxSubArray([1]) == 1
    assert solution.maxSubArray([5,4,-1,7,8]) == 23
    assert solution.maxSubArray([-1]) == -1
    assert solution.maxSubArray([-2,-1]) == -1
    assert solution.maxSubArray([0, -1, 5, -3, 4]) == 6
