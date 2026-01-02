from src.lc75_decode_string import Solution

def test_decode_string():
    solution = Solution()
    assert solution.decodeString("3[a]2[bc]") == "aaabcbc"
    assert solution.decodeString("3[a2[c]]") == "accaccacc"
    assert solution.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"

