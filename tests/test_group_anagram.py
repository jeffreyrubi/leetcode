from src.group_anagram import Solution

def test_group_anagram():
    solution = Solution()

    def normalize(groups):
        return [set(group) for group in groups]

    # Test case 1: Example input
    result = solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    expected = [["eat","tea","ate"],["tan","nat"],["bat"]]
    assert sorted([sorted(list(g)) for g in result]) == sorted([sorted(list(g)) for g in expected])

    # Test case 2: Single word
    result = solution.groupAnagrams(["abc"])
    expected = [["abc"]]
    assert sorted([sorted(list(g)) for g in result]) == sorted([sorted(list(g)) for g in expected])
