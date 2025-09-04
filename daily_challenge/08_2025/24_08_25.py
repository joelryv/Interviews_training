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

    
# Unittests
import unittest
class TestSolution(unittest.TestCase):
    def test_findDiagonalOrder(self):
        solution = Solution()
        self.assertEqual(solution.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]]), [1,2,4,7,5,3,6,8,9])
        self.assertEqual(solution.findDiagonalOrder([[1,2],[3,4]]), [1,2,3,4])
        self.assertEqual(solution.findDiagonalOrder([[1]]), [1])
        self.assertEqual(solution.findDiagonalOrder([]), [])
        self.assertEqual(solution.findDiagonalOrder([[1],[2],[3]]), [1,2,3])
        self.assertEqual(solution.findDiagonalOrder([[1,2,3]]), [1,2,3])
        self.assertEqual(solution.findDiagonalOrder([[1,2],[3,4],[5,6]]), [1,2,3,5,4,6])

if __name__ == "__main__":
    unittest.main()