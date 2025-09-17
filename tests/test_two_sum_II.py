from src.two_sum_II import Solution

def test_two_sum_II():
    solution = Solution()

    # Test case 1: Example input
    assert solution.twoSum([2,7,11,15], 9) == [1,2]

    # Test case 2: Target at the end
    assert solution.twoSum([1,2,3,4,4,9,56,90], 8) == [4,5]

    # Test case 3: Minimal input
    assert solution.twoSum([1,2], 3) == [1,2]
