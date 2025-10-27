from src.anagram import Solution

def test_anagram():
    solution = Solution()
    # Test case 1: Simple anagram
    assert solution.isAnagram("anagram", "nagaram") == True

    # Test case 2: Not an anagram
    assert solution.isAnagram("rat", "car") == False

    # Test case 3: Empty strings
    assert solution.isAnagram("", "") == True