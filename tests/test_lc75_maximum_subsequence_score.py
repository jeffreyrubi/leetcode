from src.lc75_max_subsequence_score import Solution

def test_lc75_maximum_subsequence_score():
    solution = Solution()

    # Test case 1: Example from LeetCode
    nums1 = [1, 3, 3, 2]
    nums2 = [2, 1, 3, 4]
    k = 3
    expected = 12
    assert solution.maxScore(nums1, nums2, k) == expected

    # Test case 2: Another LeetCode example
    nums1 = [4, 2, 3, 1, 1]
    nums2 = [7, 5, 10, 9, 6]
    k = 1
    expected = 30
    assert solution.maxScore(nums1, nums2, k) == expected

    # Test case 3: k equals array length
    nums1 = [2, 1, 14, 12]
    nums2 = [11, 7, 13, 6]
    k = 4
    expected = 174
    assert solution.maxScore(nums1, nums2, k) == expected

    # Test case 4: Small arrays
    nums1 = [5, 3]
    nums2 = [2, 4]
    k = 1
    expected = 20
    assert solution.maxScore(nums1, nums2, k) == expected

    # Test case 5: All elements same in nums2
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 5, 5, 5]
    k = 2
    expected = 35
    assert solution.maxScore(nums1, nums2, k) == expected

    # Test case 6: Larger values
    nums1 = [10, 20, 30, 40]
    nums2 = [1, 2, 3, 4]
    k = 2
    expected = 210
    assert solution.maxScore(nums1, nums2, k) == expected

    # Test case 7: k = 2 case
    nums1 = [1, 1, 1]
    nums2 = [10, 9, 8]
    k = 2
    expected = 18
    assert solution.maxScore(nums1, nums2, k) == expected

    print("All test cases passed!")
