"""
https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/?envType=daily-question&envId=2025-08-26
"""

from typing import List
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        max_d = 0 
        max_p = [0,0]
        for pair in dimensions:
            d = pair[0]**2 + pair[1]**2
            if d > max_d:
                max_d = d
                max_p = pair
            elif d == max_d:
                if pair[0]*pair[1] > max_p[0]*max_p[1]:
                    max_p = pair
        return max_p[0]*max_p[1]
    
# Unittests
import unittest
class TestSolution(unittest.TestCase):
    def test_areaOfMaxDiagonal(self):
        solution = Solution()
        self.assertEqual(solution.areaOfMaxDiagonal([[1,2],[3,4],[2,3]]), 12)
        self.assertEqual(solution.areaOfMaxDiagonal([[1,1],[2,2],[3,3]]), 9)
        self.assertEqual(solution.areaOfMaxDiagonal([[1,2],[2,1],[1,1]]), 2)
        self.assertEqual(solution.areaOfMaxDiagonal([[5,5],[3,7],[6,4]]), 21)
        self.assertEqual(solution.areaOfMaxDiagonal([[1,10],[10,1],[5,5]]), 10)

if __name__ == "__main__":
    unittest.main()