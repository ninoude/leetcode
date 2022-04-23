from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(0,9):
            if self.isValidRow(board[i]):
                return False

            column = []
            for j in range(0,9):
                column.append(board[j][i])
            if self.isValidRow(column):
                return False

        for i in range(0, 9, 3):
            block = {}
            for j in range(0, 9):
                if j//3 in block:
                    block[j//3].extend(board[j][i:i+3])
                else:
                    block[j//3] = board[j][i:i+3]

            for k in range(0,3):
                if self.isValidRow(block[k]):
                    return False
        return True

    def isValidRow(self, row: List[str]):
        # Create an array that does not contain the char '.'
        tmp = [s for s in row if s != '.']
        return len(tmp) != len(set(tmp))
