from src.lc75_reverse_words_in_string import Solution

def test_lc75_reverse_words_in_string():
    solution = Solution()
    
    # Test case 1: Basic example
    assert solution.reverseWords("the sky is blue") == "blue is sky the"
    
    # Test case 2: Leading and trailing spaces
    assert solution.reverseWords("  hello world  ") == "world hello"
    
    # Test case 3: Multiple spaces between words
    assert solution.reverseWords("a   good   example") == "example good a"
    
    # Test case 4: Single word
    assert solution.reverseWords("hello") == "hello"
    
    # Test case 5: Single word with spaces
    assert solution.reverseWords("  hello  ") == "hello"
    
    # Test case 6: Two words
    assert solution.reverseWords("hello world") == "world hello"
    
    # Test case 7: Empty-like string (only spaces)
    # Note: This edge case depends on problem constraints, 
    # but typically should return empty string
    
    # Test case 8: Words with different lengths
    assert solution.reverseWords("a bb ccc dddd") == "dddd ccc bb a"
    
    # Test case 9: Mixed spacing
    assert solution.reverseWords("  Bob    Loves  Alice   ") == "Alice Loves Bob"
    
    # Test case 10: LeetCode example
    assert solution.reverseWords("Let's take LeetCode contest") == "contest LeetCode take Let's"