from src.pacific_atlantic_water import Solution

def test_pacific_atlantic_water():
    solution = Solution()
    # Test case 1: Example input
    heights = [
        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]
    ]
    res = solution.pacificAtlantic(heights)
    # check that known coordinates exist in result
    assert (0,4) in res and (4,0) in res

    # Test case 2: Flat grid
    heights = [[1,1,1],[1,1,1],[1,1,1]]
    res = solution.pacificAtlantic(heights)
    # all cells can reach both oceans
    assert len(res) == 9