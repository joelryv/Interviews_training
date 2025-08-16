"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            seen = ''
            for n in row:
                if n in seen:
                    return False
                if n != '.':
                    seen += n
        for i in range(9):
            seen = ''
            for j in range(9):
                n = board[j][i]
                if n in seen:
                    return False
                if n != '.':
                    seen += n
        for a in range(3):
            for b in range(3):
                seen = ''
                for i in range(3):
                    for j in range(3):
                        n = board[(3*a)+i][(3*b)+j]
                        if n in seen:
                            return False
                        if n != '.':
                            seen += n
        return True
    
# Unit tests
import unittest
class TestIsValidSudoku(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isValidSudoku(self):
        board1 = [
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        board2 = [
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]
        board3 = [
            [".",".","4",".",".",".","6","3","."],
            [".",".",".",".",".",".",".",".","."],
            ["5",".",".",".",".",".",".","9","."],
            [".",".",".","5","6",".",".",".","."],
            ["4",".","3",".",".",".",".",".","1"],
            [".",".",".","7",".",".",".",".","."],
            [".",".",".","5",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."],
            [".",".",".",".",".",".",".",".","."]
        ]

        self.assertTrue(self.solution.isValidSudoku(board1))
        self.assertFalse(self.solution.isValidSudoku(board2))

if __name__ == "__main__":
    unittest.main()