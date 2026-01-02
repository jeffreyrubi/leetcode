import pytest
from src.lc75_dota2_senate import Solution

def test_lc75_dota2_senate():
    solution = Solution()

    assert solution.predictPartyVictory("RD") == "Radiant"
    assert solution.predictPartyVictory("RDD") == "Dire"
    assert solution.predictPartyVictory("RRDDD") == "Radiant"
    assert solution.predictPartyVictory("RDRDR") == "Radiant"
    assert solution.predictPartyVictory("DDRRR") == "Dire"

