from src.top_k_frequent_element import Solution

def test_top_k_frequent_element():
    solution = Solution()
    # Test case 1: Example input
    res = solution.topKFrequent([1,1,1,2,2,3], 2)
    assert set(res) == {1,2}

    # Test case 2: All elements same frequency
    res = solution.topKFrequent([1,2,3,4], 2)
    assert len(res) == 2 and set(res).issubset({1,2,3,4})

    # Test case 3: k equals unique count
    res = solution.topKFrequent([1,1,2,2,3], 3)
    assert set(res) == {1,2,3}
