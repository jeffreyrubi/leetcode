from src.combination_sum import Solution

def test_combination_sum():
    solution = Solution()


def _normalize(result):
    """Convert list of lists into a set of tuples with sorted inner lists for order-insensitive comparison."""
    return {tuple(sorted(r)) for r in result}


def test_combination_sum_example():
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    res = solution.combinationSum(candidates, target)
    expected = [[7], [2, 2, 3]]
    assert _normalize(res) == _normalize(expected)


def test_combination_sum_single_candidate_no_solution():
    solution = Solution()
    candidates = [2]
    target = 1
    res = solution.combinationSum(candidates, target)
    assert res == []


def test_combination_sum_single_candidate_multiple():
    solution = Solution()
    candidates = [1]
    target = 2
    res = solution.combinationSum(candidates, target)
    expected = [[1, 1]]
    assert _normalize(res) == _normalize(expected)


def test_combination_sum_multiple_candidates():
    solution = Solution()
    candidates = [2, 3, 5]
    target = 8
    res = solution.combinationSum(candidates, target)
    # possible combinations: [2,2,2,2], [2,3,3], [3,5]
    expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
    assert _normalize(res) == _normalize(expected)
