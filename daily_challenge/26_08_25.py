"""
https://leetcode.com/problems/length-of-longest-v-shaped-diagonal-segment/submissions/1749733280/?envType=daily-question&envId=2025-08-27
"""

from typing import List
from functools import cache
class Solution:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(cx, cy, direction, turn, target):
            nx, ny = cx + DIRS[direction][0], cy + DIRS[direction][1]
            # If it goes beyond the boundary or the next node's value is not the target value, then return
            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny] != target:
                return 0
            turn_int = 1 if turn else 0
            # Continue walking in the original direction.
            max_step = dfs(nx, ny, direction, turn, 2 - target)
            if turn:
                # Clockwise rotate 90 degrees turn
                max_step = max(
                    max_step,
                    dfs(nx, ny, (direction + 1) % 4, False, 2 - target),
                )
            return max_step + 1

        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for direction in range(4):
                        res = max(res, dfs(i, j, direction, True, 2) + 1)
        return res

# Unittests
import unittest
class TestSolution(unittest.TestCase):
    def test_lenOfVDiagonal1(self):
        grid = [[2,2,1,2,2],
                [2,0,2,2,0],
                [2,0,1,1,0],
                [1,0,2,2,2],
                [2,0,0,2,2]]
        expected = 5
        self.assertEqual(Solution().lenOfVDiagonal(grid), expected)

    def test_lenOfVDiagonal2(self):
        grid = [[2,2,2,2,2],
                [2,0,2,2,0],
                [2,0,1,1,0],
                [1,0,2,2,2],
                [2,0,0,2,2]]
        expected = 4
        self.assertEqual(Solution().lenOfVDiagonal(grid), expected)

    def test_lenOfVDiagonal3(self):
        grid = [[1]]
        expected = 1
        self.assertEqual(Solution().lenOfVDiagonal(grid), expected)

    def test_lenOfVDiagonal4(self):
        grid = [[1,2,2,2,2],
                [2,2,2,2,0],
                [2,0,0,0,0],
                [0,0,2,2,2],
                [2,0,0,2,0]]
        expected = 5
        self.assertEqual(Solution().lenOfVDiagonal(grid), expected)

if __name__ == "__main__":
    unittest.main()