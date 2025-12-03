from src.spiral_matrix import Solution

def test_spiral_matrix():
    solution = Solution()
    assert solution.spiralOrder([[1]]) == [1]
    assert solution.spiralOrder([[1,2,3]]) == [1,2,3]
    assert solution.spiralOrder([[1],[2],[3]]) == [1,2,3]
    assert solution.spiralOrder([[1,2],[3,4]]) == [1,2,4,3]
    assert solution.spiralOrder([]) == []
    assert solution.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]) == [1,2,3,6,9,8,7,4,5]
    assert solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]) == [1,2,3,4,8,12,11,10,9,5,6,7]
    assert solution.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20],[21,22,23,24]]) == [1,2,3,4,8,12,16,20,24,23,22,21,17,13,9,5,6,7,11,15,19,18,14,10]
    assert solution.spiralOrder([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]) == [2,3,4,7,10,13,16,15,14,11,8,5,6,9,12]
    