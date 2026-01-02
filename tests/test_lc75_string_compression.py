from src.lc75_string_compression import Solution

def test_lc75_string_compression():
    solution = Solution()
    
    # Test case 1: Example from LeetCode - ["a","a","b","b","c","c","c"]
    chars1 = ["a","a","b","b","c","c","c"]
    result1 = solution.compress(chars1)
    assert result1 == 6
    assert chars1[:result1] == ["a","2","b","2","c","3"]
    
    # Test case 2: Single character
    chars2 = ["a"]
    result2 = solution.compress(chars2)
    assert result2 == 1
    assert chars2[:result2] == ["a"]
    
    # Test case 3: Example from LeetCode - ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    chars3 = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
    result3 = solution.compress(chars3)
    assert result3 == 4
    assert chars3[:result3] == ["a","b","1","2"]
    
    # Test case 4: No compression needed (all single characters)
    chars4 = ["a","b","c"]
    result4 = solution.compress(chars4)
    assert result4 == 3
    assert chars4[:result4] == ["a","b","c"]
    
    # Test case 5: All same character
    chars5 = ["a","a","a","a"]
    result5 = solution.compress(chars5)
    assert result5 == 2
    assert chars5[:result5] == ["a","4"]
    
    # Test case 6: Mix of single and multiple characters
    chars6 = ["a","b","b","c","c","c","d"]
    result6 = solution.compress(chars6)
    assert result6 == 6
    assert chars6[:result6] == ["a","b","2","c","3","d"]
    
    # Test case 7: Large count (double digits)
    chars7 = ["a"] * 15 + ["b"] * 2
    result7 = solution.compress(chars7)
    assert result7 == 5
    assert chars7[:result7] == ["a","1","5","b","2"]
    
    # Test case 8: Empty array (edge case)
    chars8 = []
    result8 = solution.compress(chars8)
    assert result8 == 0
    
    # Test case 9: Very large count (triple digits)
    chars9 = ["a"] * 100
    result9 = solution.compress(chars9)
    assert result9 == 4
    assert chars9[:result9] == ["a","1","0","0"]