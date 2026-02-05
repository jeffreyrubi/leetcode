from src.lc75_evaluate_division import Solution


def test_lc75_evaluate_division():
    solution = Solution()

    # Test case 1: Basic example
    equations = [["a", "b"], ["b", "c"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]
    expected = [6.0, 0.5, -1.0, 1.0, -1.0]
    assert solution.calcEquation(equations, values, queries) == expected

    # Test case 2: Single equation
    equations = [["a", "b"]]
    values = [0.5]
    queries = [["a", "b"], ["b", "a"], ["a", "c"], ["x", "y"]]
    expected = [0.5, 2.0, -1.0, -1.0]
    assert solution.calcEquation(equations, values, queries) == expected

    # Test case 3: Multiple paths
    equations = [["a", "b"], ["b", "c"], ["c", "d"]]
    values = [2.0, 3.0, 4.0]
    queries = [["a", "d"], ["d", "a"]]
    expected = [24.0, 1.0 / 24.0]
    assert solution.calcEquation(equations, values, queries) == expected

    # Test case 4: Disconnected graph
    equations = [["a", "b"], ["c", "d"]]
    values = [2.0, 3.0]
    queries = [["a", "c"], ["b", "d"], ["a", "b"], ["c", "d"]]
    expected = [-1.0, -1.0, 2.0, 3.0]
    assert solution.calcEquation(equations, values, queries) == expected

    # Test case 5: Complex graph
    equations = [["a", "b"], ["b", "c"], ["a", "c"]]
    values = [2.0, 3.0, 6.0]
    queries = [["a", "c"], ["c", "a"], ["b", "c"], ["c", "b"]]
    expected = [6.0, 1.0 / 6.0, 3.0, 1.0 / 3.0]
    assert solution.calcEquation(equations, values, queries) == expected

    print("All test cases passed!")
