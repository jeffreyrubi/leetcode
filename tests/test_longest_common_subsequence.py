from src.longest_common_subsequence import Solution

def test_longest_common_subsequence():
    solution = Solution()

    # Standard examples
    assert solution.longestCommonSubsequence("abcde", "ace") == 3    # "ace"
    assert solution.longestCommonSubsequence("abc", "abc") == 3      # "abc"
    assert solution.longestCommonSubsequence("abc", "def") == 0      # no common

    # One character match
    assert solution.longestCommonSubsequence("a", "a") == 1
    assert solution.longestCommonSubsequence("a", "b") == 0

    # One string empty
    assert solution.longestCommonSubsequence("", "abc") == 0
    assert solution.longestCommonSubsequence("abc", "") == 0
    assert solution.longestCommonSubsequence("", "") == 0

    # Repeated characters
    assert solution.longestCommonSubsequence("aaa", "aaa") == 3
    assert solution.longestCommonSubsequence("aaa", "a") == 1
    assert solution.longestCommonSubsequence("aaaba", "aaa") == 3

    # Classic examples
    assert solution.longestCommonSubsequence("bl", "yby") == 1       # "b" or "l"
    assert solution.longestCommonSubsequence("oxcpqrsvwf", "shmtulqrypy") == 2

    # LeetCode hard cases
    assert solution.longestCommonSubsequence("ezupkr", "ubmrapg") == 2  # "up" or "ur"
    assert solution.longestCommonSubsequence("hofubmnylkra", "pqhobk") == 4  # "hobk"

    # Long similar strings
    assert solution.longestCommonSubsequence("abcdbef", "abecdbf") == 6  # "abcdbf"
