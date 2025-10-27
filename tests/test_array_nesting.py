from src.array_nesting import Solution

def test_array_nesting():
    solution = Solution()

    # Test case 1: Example input
    assert solution.arrayNesting([5,4,0,3,1,6,2]) == 4

    # Test case 2: All elements point to themselves
    assert solution.arrayNesting([0,1,2,3]) == 1

    # Test case 3: Single cycle
    assert solution.arrayNesting([1,2,3,4,0]) == 5
