from src.longest_substring_without_repeating_character import Solution


def test_longest_substring_without_repeating_character():
    solution = Solution()
    # Test case 1: Example input
    assert solution.lengthOfLongestSubstring("abcabcbb") == 3  # "abc"

    # Test case 2: All characters the same
    assert solution.lengthOfLongestSubstring("bbbbb") == 1  # "b"

    # Test case 3: Longest substring in the middle
    assert solution.lengthOfLongestSubstring("pwwkew") == 3  # "wke"

    # Test case 4: Longest substring in the middle
    assert solution.lengthOfLongestSubstring("") == 0  # "wke"

    # Test case 4: Longest substring in the middle
    assert solution.lengthOfLongestSubstring("au") == 2  # "wke"

