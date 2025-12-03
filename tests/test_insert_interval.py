from src.insert_interval import Solution

def test_insert_interval():
    solution = Solution()
    assert solution.insert([[1,3],[6,9]], [2,5]) == [[1,5],[6,9]]
    assert solution.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) == [[1,2],[3,10],[12,16]]
    assert solution.insert([], [5,7]) == [[5,7]]
    assert solution.insert([[1,5]], [2,3]) == [[1,5]]
    assert solution.insert([[1,5]], [6,8]) == [[1,5],[6,8]]
    assert solution.insert([[1,5]], [0,0]) == [[0,0],[1,5]]
    assert solution.insert([[3,5],[6,8],[10,12]], [1,2]) == [[1,2],[3,5],[6,8],[10,12]]
