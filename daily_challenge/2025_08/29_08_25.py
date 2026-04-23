"""
https://leetcode.com/problems/valid-sudoku/description/?envType=daily-question&envId=2025-08-30
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
    
# Unittest
import unittest
class TestSolution(unittest.TestCase):
    def test_isValidSudoku(self):
        solution = Solution()
        self.assertTrue(solution.isValidSudoku([
            ["5","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".","5"],
            [".",".",".",".","8",".",".","7","9"]
        ]))
        self.assertFalse(solution.isValidSudoku([
            ["8","3",".",".","7",".",".",".","."],
            ["6",".",".","1","9","5",".",".","."],
            [".","9","8",".",".",".",".","6","."],
            ["8",".",".",".","6",".",".",".","3"],
            ["4",".",".","8",".","3",".",".","1"],
            ["7",".",".",".","2",".",".",".","6"],
            [".","6",".",".",".",".","2","8","."],
            [".",".",".","4","1","9",".",".",'5'],
            [".",".",".",".",'8','.','.','7','9']
        ]))

if __name__ == "__main__":
    unittest.main()