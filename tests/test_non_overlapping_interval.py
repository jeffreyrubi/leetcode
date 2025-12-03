from src.non_overlapping_interval import Solution

def test_non_overlapping_interval():
    solution = Solution()

    # assert solution.eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]) == 1
    # assert solution.eraseOverlapIntervals([[1,2],[1,2],[1,2]]) == 2
    # assert solution.eraseOverlapIntervals([[1,100],[11,22],[1,11],[2,12]]) == 2
    # assert solution.eraseOverlapIntervals([[1,2]]) == 0
    # assert solution.eraseOverlapIntervals([]) == 0
    # assert solution.eraseOverlapIntervals([[1,2],[3,4],[5,6]]) == 0
    assert solution.eraseOverlapIntervals([[0,2],[1,3],[2,4],[3,5],[4,6]]) == 4
    