"""
https://leetcode.com/problems/sort-matrix-by-diagonals/submissions/1750905085/?envType=daily-question&envId=2025-08-28
"""

from typing import List

class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        for i in range(n):
            tmp = [grid[i+j][j] for j in range(n - i)]
            tmp.sort(reverse=True)
            for j in range(n - i):
                grid[i + j][j] = tmp[j]
        for j in range(1, n):
            tmp = [grid[i][j + i] for i in range(n - j)]
            tmp.sort()
            for i in range(n - j):
                grid[i][j + i] = tmp[i]
        return grid
    
# Unittests
import unittest

class TestSolution(unittest.TestCase):
    
    def test_case_1(self):
        grid = [[1,7,3],[9,8,2],[4,5,6]]
        expected = [[8,2,3],[9,6,7],[4,5,1]]
        self.assertEqual(Solution().sortMatrix(grid), expected)
    
    def test_case_2(self):
        grid = [[0,1],[1,2]]
        expected = [[2,1],[1,0]]
        self.assertEqual(Solution().sortMatrix(grid), expected)
        
    def test_case_3(self):
        grid = [[1]]
        expected = [[1]]
        self.assertEqual(Solution().sortMatrix(grid), expected)

if __name__ == "__main__":
    unittest.main()