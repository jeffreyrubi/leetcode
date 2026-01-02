from src.lc75_max_number_of_vowels import Solution

def test_lc75_max_number_of_vowels():
    solution = Solution()
    
    # Example 1: "abciiidef", k=3 -> "iii" has 3 vowels
    assert solution.maxVowels("abciiidef", 3) == 3
    
    # Example 2: "aeiou", k=2 -> any substring of length 2 has 2 vowels
    assert solution.maxVowels("aeiou", 2) == 2
    
    # Example 3: "leetcode", k=3 -> "lee", "eet", "ode" have 2 vowels each
    assert solution.maxVowels("leetcode", 3) == 2
    
    # Edge case: single character vowel
    assert solution.maxVowels("a", 1) == 1
    
    # Edge case: single character consonant
    assert solution.maxVowels("b", 1) == 0
    
    # Edge case: k equals string length with all vowels
    assert solution.maxVowels("aeiou", 5) == 5
    
    # Edge case: k equals string length with no vowels
    assert solution.maxVowels("bcdfg", 5) == 0
    
    # Edge case: k equals string length with mixed characters
    assert solution.maxVowels("hello", 5) == 2
    
    # Test case: all consonants
    assert solution.maxVowels("bcdfg", 3) == 0
    
    # Test case: alternating vowels and consonants
    assert solution.maxVowels("abababab", 4) == 2
    
    # Test case: vowels at the end
    assert solution.maxVowels("bcdfgaeiou", 4) == 4
    
    # Test case: vowels at the beginning  
    assert solution.maxVowels("aeioubbbb", 4) == 4
    
    # Test case: scattered vowels
    assert solution.maxVowels("programming", 4) == 2  # "prog", "rogr", "ogra", "gram", "ramm", "ammi", "mmin", "ming" -> max 1 vowel
    
    # Test case: k = 1 with vowels and consonants
    assert solution.maxVowels("hello", 1) == 1
    
    # Test case: larger window
    assert solution.maxVowels("weallloveyou", 7) == 4  # "lloveyou" has 4 vowels (o,e,o,u)