from src.lc75_determine_close_strings import Solution

def test_lc75_determine_close_strings():
    solution = Solution()
    
    # Test case 10: Complex case with multiple character swaps needed
    assert solution.closeStrings("aaabbbbccddeee", "aabbccddeeebbb") == False
    # Same chars {a,b,c,d,e}, can rearrange frequencies

    # Test case 1: Example 1 from LeetCode - simple reordering
    assert solution.closeStrings("abc", "bca") == True
    # Can reorder characters: "abc" -> "acb" -> "bca"
    
    # Test case 2: Example 2 from LeetCode - different lengths
    assert solution.closeStrings("a", "aa") == False
    # Different lengths, impossible to make close
    
    # Test case 3: Example 3 from LeetCode - character frequency transformation
    assert solution.closeStrings("cabbba", "abbccc") == True
    # Same characters {a,b,c}, frequencies [1,4,1] can become [1,2,3]
    
    # Test case 4: Empty strings
    assert solution.closeStrings("", "") == True
    # Both empty strings are close
    
    # Test case 5: Same strings
    assert solution.closeStrings("abc", "abc") == True
    # Identical strings are close
    
    # Test case 6: Different character sets
    assert solution.closeStrings("abc", "def") == False
    # Completely different characters, cannot be close
    
    # Test case 7: Same characters, different frequencies that can be swapped
    assert solution.closeStrings("aabbcc", "ccbbaa") == True
    # Same chars {a,b,c} with frequencies [2,2,2] - just reordering
    
    # Test case 8: Same characters, frequencies can be transformed
    assert solution.closeStrings("aab", "bba") == True
    # Same chars {a,b}, frequencies [2,1] and [1,2] can be swapped
    
    # Test case 9: Different character sets with same frequencies
    assert solution.closeStrings("aab", "ccd") == False
    # Different character sets {a,b} vs {c,d}
    

    
    # Test case 11: Same chars but impossible frequency transformation
    assert solution.closeStrings("a", "b") == False
    # Different character sets
    
    # Test case 12: Single character repeated
    assert solution.closeStrings("aaa", "aaa") == True
    # Identical strings
    
    # Test case 13: Different lengths with same character set
    assert solution.closeStrings("ab", "aba") == False
    # Different lengths, cannot be close