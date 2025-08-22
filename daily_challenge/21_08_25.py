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
