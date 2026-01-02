from src.lc75_removing_stars_from_string import Solution


def test_lc75_removing_stars_from_string():
    solution = Solution()
    # assert solution.removeStars("leet**cod*e") == "lecoe"
    assert solution.removeStars("erase*****") == ""
    assert solution.removeStars("**ab**cd**") == ""
    assert solution.removeStars("a*b*c*") == ""
    assert solution.removeStars("****") == ""

