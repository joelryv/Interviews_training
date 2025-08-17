"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/770/
"""
from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n):
            for j in range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(n):
            matrix[i] = matrix[i][::-1]

# Unit tests
import unittest
class TestRotateImage(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_rotate(self):
        matrix1 = [
            [1,2,3],
            [4,5,6],
            [7,8,9]
        ]
        self.solution.rotate(matrix1)
        self.assertEqual(matrix1, [[7,4,1],[8,5,2],[9,6,3]])

        matrix2 = [
            [5,1,9,11],
            [2,4,8,10],
            [13,3,6,7],
            [15,14,12,16]
        ]
        self.solution.rotate(matrix2)
        self.assertEqual(matrix2, [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])

if __name__ == '__main__':
    unittest.main()