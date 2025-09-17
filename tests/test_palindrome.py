from src.valid_palindrome import Solution

def test_valid_parlindrome():
    solution = Solution()

    # Test case 1: Simple palindrome
    assert solution.isPalindrome("A man, a plan, a canal: Panama") == True

    # Test case 2: Not a palindrome
    assert solution.isPalindrome("race a car") == False

    # Test case 3: Empty string
    assert solution.isPalindrome("") == True
