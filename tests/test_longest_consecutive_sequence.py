from src.longest_consecutive_sequence import Solution

def test_longest_consecutive_sequence():
    solution = Solution()

    # Test case 1: Example input
    assert solution.longestConsecutive([100,4,200,1,3,2]) == 4

    # Test case 2: No consecutive sequence
    assert solution.longestConsecutive([10,30,20]) == 1

    # Test case 3: Empty array
    assert solution.longestConsecutive([]) == 0

