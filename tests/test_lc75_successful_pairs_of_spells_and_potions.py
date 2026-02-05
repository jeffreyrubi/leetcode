from src.lc75_successful_pairs_of_spells_and_potions import Solution

def test_lc75_successful_pairs_of_spells_and_potions():
    solution = Solution()

    # Test case 1: Example from LeetCode
    spells = [5, 1, 3]
    potions = [1, 2, 3, 4, 5]
    success = 7
    expected = [4, 0, 3]
    assert solution.successfulPairs(spells, potions, success) == expected

    # Test case 2: Another example from LeetCode
    spells = [3, 1, 2]
    potions = [8, 5, 8]
    success = 16
    expected = [2, 0, 2]
    assert solution.successfulPairs(spells, potions, success) == expected

    # Test case 3: All pairs successful
    spells = [10, 10, 10]
    potions = [10, 10, 10]
    success = 1
    expected = [3, 3, 3]
    assert solution.successfulPairs(spells, potions, success) == expected

    # Test case 4: No pairs successful
    spells = [1, 2, 3]
    potions = [1, 1, 1]
    success = 100
    expected = [0, 0, 0]
    assert solution.successfulPairs(spells, potions, success) == expected

    # Test case 5: Single spell and potion
    spells = [5]
    potions = [3]
    success = 15
    expected = [1]
    assert solution.successfulPairs(spells, potions, success) == expected

    # Test case 6: Large numbers
    spells = [15, 8, 19]
    potions = [38, 36, 23]
    success = 328
    expected = [3, 0, 3]
    assert solution.successfulPairs(spells, potions, success) == expected
