from src.parlindormic_substring import Solution

def test_parlindormic_substring():
    solution = Solution()

    # Test Case 1
    assert solution.countSubstrings("abc") == 3
    
    # All same characters: "aaa" -> 6 palindromic substrings
    assert solution.countSubstrings("aaa") == 6

    # Odd length palindrome
    assert solution.countSubstrings("aba") == 4  # a, b, a, aba

    # Even length palindrome
    assert solution.countSubstrings("abba") == 6  # a, b, b, a, bb, abba

    # No multi-char palindromes, only single characters
    assert solution.countSubstrings("abc") == 3

    # All same characters: "aaa" -> 6 palindromic substrings
    assert solution.countSubstrings("aaa") == 6

    # Odd length palindrome
    assert solution.countSubstrings("aba") == 4  # a, b, a, aba

    # Even length palindrome
    assert solution.countSubstrings("abba") == 6  # a, b, b, a, bb, abba


    assert solution.countSubstrings("") == 0

    # Single character -> 1
    assert solution.countSubstrings("x") == 1

    # Single character repeated -> 1
    assert solution.countSubstrings("a") == 1

    # Two same characters -> 3
    assert solution.countSubstrings("aa") == 3



