"""
https://leetcode.com/problems/find-triangular-sum-of-an-array/?envType=daily-question&envId=2025-09-30
"""

from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            nums = [(nums[i] + nums[i+1])%10 for i in range(n-1)]
            n -= 1
        return nums[0]
    
# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_triangularSum(self):
        self.assertEqual(self.solution.triangularSum([1,2,3,4,5]), 8)
        self.assertEqual(self.solution.triangularSum([5]), 5)
        self.assertEqual(self.solution.triangularSum([2,3,4,5,6,7]), 4)
        self.assertEqual(self.solution.triangularSum([0,1,2,3,4,5,6,7,8,9]), 4)

if __name__ == "__main__":
    unittest.main()