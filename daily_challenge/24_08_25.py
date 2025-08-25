"""
https://leetcode.com/problems/diagonal-traverse/?envType=daily-question&envId=2025-08-25
"""
from typing import List
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]:
            return []
        prev = {}
        result = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i + j not in prev.keys():
                    prev[i + j] = [mat[i][j]]
                else:
                    prev[i + j].append(mat[i][j])
        for k in range(len(prev)):
            if k % 2 == 0:
                result += prev[k][::-1]
            else:
                result += prev[k]
        return result

