from src.rotate_image import Solution


def test_rotate_image():
    solution = Solution()

    # 1x1 matrix (edge case)
    matrix = [[1]]
    solution.rotate(matrix)
    assert matrix == [[1]]

    # # 2x2 matrix
    matrix = [
        [1, 2],
        [3, 4],
    ]
    solution.rotate(matrix)
    assert matrix == [
        [3, 1],
        [4, 2],
    ]

    # 3x3 matrix
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
    ]
    solution.rotate(matrix)
    assert matrix == [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3],
    ]

    # 4x4 matrix (example from common LeetCode tests)
    matrix = [
        [5, 1, 9, 11],
        [2, 4, 8, 10],
        [13, 3, 6, 7],
        [15, 14, 12, 16],
    ]
    solution.rotate(matrix)
    assert matrix == [
        [15, 13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7, 10, 11],
    ]
