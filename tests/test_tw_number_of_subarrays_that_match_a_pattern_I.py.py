import pytest
from src.tw_number_of_subarrays_that_match_a_pattern_I import Solution


@pytest.fixture
def solution():
    return Solution()


def test_example_01(solution):
    nums = [1,2,3,4,5,6]
    pattern = [1,1]

    assert solution.countMatchingSubarrays(nums, pattern) == 4


def test_example_02(solution):
    nums = [1,4,4,1,3,5,5,3]
    pattern = [1,0,-1]

    assert solution.countMatchingSubarrays(nums, pattern) == 2


# test: pattern with single value for 1, 0, -1
def test_one_value_pattern(solution):


# test: nums with 2 value only.




# Constrainted: nums.length >=2
# Constrainted: pattern.length >= 1
# Constrainted: pattern are valid





