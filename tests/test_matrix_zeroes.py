from src.set_matrix_zeroes import Solution

def test_set_matrix_zeroes():
    solution = Solution()

    # Example 1
    matrix1 = [[1,1,1],[1,0,1],[1,1,1]]
    solution.setZeroes(matrix1)
    assert matrix1 == [[1,0,1],[0,0,0],[1,0,1]]

    # Example 2
    matrix2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    solution.setZeroes(matrix2)
    assert matrix2 == [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

    # Single element with zero
    matrix3 = [[0]]
    solution.setZeroes(matrix3)
    assert matrix3 == [[0]]

    # Single element non-zero
    matrix4 = [[5]]
    solution.setZeroes(matrix4)
    assert matrix4 == [[5]]

    # No zeros
    matrix5 = [[1,2,3],[4,5,6],[7,8,9]]
    solution.setZeroes(matrix5)
    assert matrix5 == [[1,2,3],[4,5,6],[7,8,9]]

    # Zero in corner
    matrix6 = [[1,0],[2,3]]
    solution.setZeroes(matrix6)
    assert matrix6 == [[0,0],[2,0]]