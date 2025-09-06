from src.two_sum import Solution

def test_two_sum():
    solution = Solution()
    # assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1] or solution.twoSum([2, 7, 11, 15], 9) == [1,0]
    # assert solution.twoSum([3, 2, 4], 6) == [1, 2] or solution.twoSum([3, 2, 4], 6) == [2, 1]
    # assert solution.twoSum([3, 3], 6) == [0, 1] or solution.twoSum([3, 3], 6) == [1, 0]
    assert solution.twoSum([2, 5, 7, 10], 9) == [0, 2] or solution.twoSum([2, 5, 7, 9], 9) == [2, 0]