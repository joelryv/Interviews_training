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


class Solution2:
    def lenOfVDiagonal(self, grid: List[List[int]]) -> int:
        # Dynamic Programming
        # Let dp(x, y, t, d) be the longest segment starting with (x, y) where the segment has been turned or not (indicated by the binary flag t) and the current direction is d.
        # When grid(x, y) == 1:
        # dp(x, y, t, *) = max(dp(x', y', true, d) if grid(x', y') == 2, 1)
        # Otherwise:
        # dp(x, y, t, d) = max(dp(x', y', t, d) if grid(x',y') == 2 - grid(x, y) else 1, dp(x'', y'', false, d') if d is true and grid(x'',y'') == 2 - grid(x, y))
        # The overall complexity is O(m * n * 4 * 2) ~ O(2 * 10^6).
        dirs = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        n = len(grid)
        m = len(grid[0])
        nv = [2, 2, 0] # Next expected value

        @cache
        def helper(x, y, turned, dir):
            # First, we do not change the direction
            res = 1
            dx, dy = dirs[dir]
            if 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == nv[grid[x][y]]:
                res = helper(x + dirs[dir][0], y + dirs[dir][1], turned, dir) + 1
            if not turned:
                dx, dy = dirs[(dir + 1) % 4]
                if 0 <= x + dx < n and 0 <= y + dy < m and grid[x + dx][y + dy] == nv[grid[x][y]]:
                    res = max(res, helper(x + dx, y + dy, True, (dir + 1) % 4) + 1)
            return res

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    # Optimization: we can compute the theorically longest path. If the current answer is already better than this, we do not need to make the DFS.
                    tm = (n - i, j + 1, i + 1, m - j)
                    for d in range(4):
                        if tm[d] > ans:
                            ans = max(ans, helper(i, j, False, d))
        return ans

class TestSolution2(unittest.TestCase):
    def test_lenOfVDiagonal1(self):
        grid = [[2,2,1,2,2],
                [2,0,2,2,0],
                [2,0,1,1,0],
                [1,0,2,2,2],
                [2,0,0,2,2]]
        expected = 5
        self.assertEqual(Solution2().lenOfVDiagonal(grid), expected)

    def test_lenOfVDiagonal2(self):
        grid = [[2,2,2,2,2],
                [2,0,2,2,0],
                [2,0,1,1,0],
                [1,0,2,2,2],
                [2,0,0,2,2]]
        expected = 4
        self.assertEqual(Solution2().lenOfVDiagonal(grid), expected)

    def test_lenOfVDiagonal3(self):
        grid = [[1]]
        expected = 1
        self.assertEqual(Solution2().lenOfVDiagonal(grid), expected)

    def test_lenOfVDiagonal4(self):
        grid = [[1,2,2,2,2],
                [2,2,2,2,0],
                [2,0,0,0,0],
                [0,0,2,2,2],
                [2,0,0,2,0]]
        expected = 5
        self.assertEqual(Solution2().lenOfVDiagonal(grid), expected)

if __name__ == "__main__":
    unittest.main()