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
    
