from src.longest_palindromic_substring import Solution

def test_longest_palindromic_substring():
    solution = Solution()
    # Test case 1: Example input ("babad" -> "bab" or "aba")
    res = solution.longestPalindrome("babad")
    assert res in {"bab", "aba"}

    # Test case 2: Even length palindrome
    assert solution.longestPalindrome("cbbd") == "bb"

    # Test case 3: Single character
    assert solution.longestPalindrome("a") == "a"

    # Test case 4: Single character
    res = solution.longestPalindrome("ac")
    assert res in {"a", "c"} 

    # Test case 5: Single character
    res = solution.longestPalindrome("aaaa")
    assert res in {"aaaa"} 