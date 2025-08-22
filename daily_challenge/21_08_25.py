"""
https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/?envType=daily-question&envId=2025-08-22
"""

from typing import List
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        top, bot, left, right = len(grid), 0, len(grid[0]), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    if i < top:
                        top = i
                    if i > bot:
                        bot = i
                    if j < left:
                        left = j
                    if j > right:
                        right = j
        return((bot-top+1)*(right-left+1))

# Unit tests
import unittest
class TestSolution(unittest.TestCase):
    def test_minimumArea(self):
        solution = Solution()
        self.assertEqual(solution.minimumArea([[0,0,0,0,0],[0,1,1,0,0],[0,1,1,0,0],[0,0,0,0,0]]), 4)
        self.assertEqual(solution.minimumArea([[1]]), 1)
        self.assertEqual(solution.minimumArea([[0]]), 0)
        self.assertEqual(solution.minimumArea([[0,0,0],[0,1,0],[0,0,0]]), 1)
        self.assertEqual(solution.minimumArea([[1,1,1],[1,1,1],[1,1,1]]), 9)

        self.assertEqual(solution.minimumArea([[0,1,0],[1,1,1],[0,1,0]]), 9)

if __name__ == "__main__":
    unittest.main()