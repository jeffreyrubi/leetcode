from src.decode_ways import Solution

def test_decode_ways():
    solution = Solution()

    # Standard examples
    assert solution.numDecodings("12") == 2      # "AB" (1 2), "L" (12)
    assert solution.numDecodings("226") == 3     # "BZ" (2 26), "VF" (22 6), "BBF" (2 2 6)
    assert solution.numDecodings("06") == 0      # Invalid (leading 0 after 6)
    assert solution.numDecodings("10") == 1      # Only "J" (10)
    assert solution.numDecodings("27") == 1      # Only "BG" (2 7), 27 is invalid

    # Single digit
    assert solution.numDecodings("8") == 1
    assert solution.numDecodings("0") == 0       # Invalid

    # Long valid string
    assert solution.numDecodings("1111111111") == 89  # 10 ones → Fibonacci-like

    # Many zeros
    assert solution.numDecodings("101010") == 1   # Only one way: 10 10 10
    assert solution.numDecodings("1001") == 0     # "10 0 1" → 0 is invalid alone

    # Edge cases
    assert solution.numDecodings("30") == 0       # 30 is invalid
    assert solution.numDecodings("301") == 0      # 30 invalid
    assert solution.numDecodings("1234") == 3     # "ABC", "LC", "AWD"
    assert solution.numDecodings("9999") == 1     # Only one way (all single digits)
    assert solution.numDecodings("1123") == 5     # Multiple valid combinations
