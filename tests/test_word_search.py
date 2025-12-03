from src.word_search import Solution

def test_word_search():
    solution = Solution()
    board1 = [
        ['A','B','C','E'],
        ['S','F','C','S'],
        ['A','D','E','E']
    ]
    assert solution.exist(board1, "ABCCED") == True
    assert solution.exist(board1, "SEE") == True
    assert solution.exist(board1, "ABCB") == False

    board2 = [["a"]]
    assert solution.exist(board2, "a") == True
    assert solution.exist(board2, "b") == False

    board3 = [["A","B"],["C","D"]]
    assert solution.exist(board3, "ABCD") == False
    assert solution.exist(board3, "ACDB") == True

    board4 = [["C","A","A"],["A","A","A"],["B","C","D"]]
    assert solution.exist(board4, "AAB") == True

    assert solution.exist([["a","b"],["c","d"]], "abcd") == False

    board5 = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    assert solution.exist(board5, "ABCESEEEFS") == True