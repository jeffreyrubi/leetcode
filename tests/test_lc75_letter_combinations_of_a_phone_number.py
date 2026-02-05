from src.lc_75_letter_combinations_of_a_phone_number import Solution

def test_lc75_letter_combinations_of_a_phone_number():
    solution = Solution()
    
    # Test case 1: Example from LeetCode - "23"
    digits = "23"
    expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    result = solution.letterCombinations(digits)
    assert sorted(result) == sorted(expected)
    
    # Test case 2: Empty string
    digits = ""
    expected = []
    assert solution.letterCombinations(digits) == expected
    
    # Test case 3: Single digit
    digits = "2"
    expected = ["a", "b", "c"]
    result = solution.letterCombinations(digits)
    assert sorted(result) == sorted(expected)
    
    # Test case 4: Three digits
    digits = "234"
    # 3 * 3 * 3 = 27 combinations
    result = solution.letterCombinations(digits)
    assert len(result) == 27
    assert "adg" in result
    assert "cfi" in result
    
    # Test case 5: Digit with 4 letters (7 or 9)
    digits = "7"
    expected = ["p", "q", "r", "s"]
    result = solution.letterCombinations(digits)
    assert sorted(result) == sorted(expected)
    
    # Test case 6: Digit 9
    digits = "9"
    expected = ["w", "x", "y", "z"]
    result = solution.letterCombinations(digits)
    assert sorted(result) == sorted(expected)
    
    # Test case 7: Combination with 7 and 9
    digits = "79"
    # 4 * 4 = 16 combinations
    result = solution.letterCombinations(digits)
    assert len(result) == 16
    assert "pw" in result
    assert "sz" in result
    
    # Test case 8: Four digits
    digits = "2345"
    # 3 * 3 * 3 * 3 = 81 combinations
    result = solution.letterCombinations(digits)
    assert len(result) == 81
