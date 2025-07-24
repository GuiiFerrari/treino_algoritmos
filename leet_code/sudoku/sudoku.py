from typing import List


class Solution:
    def validateObj(self, obj: List[str]) -> bool:
        obj2 = [value for value in obj if value != "."]
        return len(set(obj2)) == len(obj2)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            if not self.validateObj(row):
                return False
        for column_index in range(len(board)):
            column = [board[i][column_index] for i in range(len(board))]
            if not self.validateObj(column):
                return False
        for i in range(0, len(board), 3):
            for j in range(0, len(board), 3):
                subbox = []
                for ii in range(i, i + 3):
                    subbox.extend(board[ii][j : j + 3])
                if not self.validateObj(subbox):
                    return False
        return True
