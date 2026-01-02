from src.lc75_longest_subarray_of_1_after_deleting_1_element import Solution

def test_lc75_longest_subarray_of_1_after_deleting_1_element():
    solution = Solution()

    # Test case 1: Example 1 from LeetCode
    assert solution.longestSubarray([1,1,0,1]) == 3
    # After deleting the 0 at position 2, we get [1,1,1] with length 3

    # Test case 2: Example 2 from LeetCode
    assert solution.longestSubarray([0,1,1,1,0,1,1,0,1]) == 5
    # After deleting the 0 at position 4, we get [0,1,1,1,1,1,0,1] 
    # and the longest subarray of 1's is [1,1,1,1,1] with length 5

    # Test case 3: Example 3 from LeetCode - all 1's
    assert solution.longestSubarray([1,1,1]) == 2
    # Must delete one element, so we get length 2

    # Test case 4: Single element 1
    assert solution.longestSubarray([1]) == 0
    # Must delete the only element, leaving empty array

    # Test case 5: Single element 0
    assert solution.longestSubarray([0]) == 0
    # After deleting 0, we get empty array

    # Test case 6: All zeros
    assert solution.longestSubarray([0,0,0,0]) == 0
    # No matter which 0 we delete, no 1's remain

    # Test case 7: One 1 surrounded by zeros
    assert solution.longestSubarray([0,1,0]) == 1
    # Best case is deleting one 0, leaving [1,0] or [0,1] with max length 1

    # Test case 8: Two 1's with one 0 between
    assert solution.longestSubarray([1,0,1]) == 2
    # Delete the 0, get [1,1] with length 2

    # Test case 9: Multiple zeros
    assert solution.longestSubarray([1,1,0,0,1,1,1]) == 3
    # Best option is to delete one 0 to connect segments, max length 3

    # Test case 10: Long array with strategic placement
    assert solution.longestSubarray([1,1,1,0,1,1,1,1]) == 7
    # Delete the 0 to connect [1,1,1] and [1,1,1,1], total length 7