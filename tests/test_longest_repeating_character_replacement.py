from src.longest_repeating_character_replacement import Solution

def test_longest_repeating_character_replacement():
    solution = Solution()
    # Brutal Force: try all combinations and count.
    # Test case 1: Example input
    assert solution.characterReplacement("ABAB", 2) == 4

    # Test case 2: K allows full replacement
    assert solution.characterReplacement("AABABBA", 1) == 4

    # Test case 3: Larger K
    assert solution.characterReplacement("AAAA", 2) == 4

    # Test case 4: Example input
    assert solution.characterReplacement("ABAB", 0) == 1