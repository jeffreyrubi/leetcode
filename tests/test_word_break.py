from src.word_break import Solution


def test_word_break_examples():
    solution = Solution()

    # Example 1
    assert solution.wordBreak("leetcode", ["leet", "code"]) == True

    # Example 2
    assert solution.wordBreak("applepenapple", ["apple", "pen"]) == True

    # Example 3
    assert solution.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False


def test_word_break_edge_cases():
    solution = Solution()

    # Empty string should be segmentable (zero words)
    assert solution.wordBreak("", []) == True

    # Single character with matching dict
    assert solution.wordBreak("a", ["a"]) == True

    # Single character without matching dict
    assert solution.wordBreak("a", ["b"]) == False


def test_time_complexity_cases():
    # Time complexity test
    solution = Solution()

    s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
    wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]

    assert solution.wordBreak(s, wordDict) == False
    

