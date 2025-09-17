from typing import List

class Solution:
    def get_segment(self, id: int) -> int:
        if id < 3:
            return 1
        if 3 <= id < 6:
            return 2
        if 6 <= id:
            return 3
         
    def get_block(self, row_id: int, col_id: int) -> int:
        return f"{self.get_segment(row_id)}_{self.get_segment(col_id)}"    

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
        cols = {1: set(), 2: set(), 3: set(), 4: set(), 5: set(), 6: set(), 7: set(), 8: set(), 9: set()}
        blocks = {"1_1": set(), "1_2": set(), "1_3": set(), "2_1": set(), "2_2": set(), "2_3": set(), "3_1": set(), "3_2": set(), "3_3": set()}
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                if val in rows[i+1]:
                    # value already exist in row i
                    print(f"val {val} exist in row: {i+1}")
                    return False
                elif val in cols[j+1]:
                    print(f"val {val} exist in col: {j+1}")
                    return False
                elif val in blocks[self.get_block(i, j)]:
                    print(f"val {val} exist in block: {self.get_block(i, j)}")
                    return False
                else:
                    # value not exist. add to sets
                    rows[i+1].add(val)
                    cols[j+1].add(val)
                    blocks[self.get_block(i, j)].add(val)
        
        return True

        