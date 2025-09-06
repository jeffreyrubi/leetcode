from src.three_sum import Solution

def test_three_sum():
    solution = Solution()

    # Test case 1: Example input
    result = solution.threeSum([-1,0,1,2,-1,-4])
    expected = [[-1,-1,2],[-1,0,1]]
    assert {tuple(sorted(triplet)) for triplet in result} == {tuple(sorted(triplet)) for triplet in expected}

    # Test case 2: No solution
    result = solution.threeSum([0,1,1])
    expected = []
    assert result == expected

    # Test case 3: All zeros
    result = solution.threeSum([0,0,0,0])
    expected = [[0,0,0]]
    assert {tuple(sorted(triplet)) for triplet in result} == {tuple(sorted(triplet)) for triplet in expected}
