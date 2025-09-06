from src.valid_parenthesis import Solution

def test_valid_parenthesis():
    solution = Solution()

    # Test case 1: Valid parentheses
    assert solution.isValid("()[]{}") == True

    # Test case 2: Invalid parentheses
    assert solution.isValid("(]") == False

    # Test case 3: Edge case - empty string
    assert solution.isValid("") == True
