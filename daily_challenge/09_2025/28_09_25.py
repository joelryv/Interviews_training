"""
https://leetcode.com/problems/largest-perimeter-triangle/description/?envType=daily-question
"""

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums) >= 3:
            if (nums[-3]+nums[-2]) > nums[-1]:
                return nums[-3] + nums[-2] + nums[-1]
            nums = nums[:-1]
        return 0
    
# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_largestPerimeter(self):
        self.assertEqual(self.solution.largestPerimeter([2,1,2]), 5)
        self.assertEqual(self.solution.largestPerimeter([1,2,1]), 0)
        self.assertEqual(self.solution.largestPerimeter([3,2,3,4]), 10)
        self.assertEqual(self.solution.largestPerimeter([3,6,2,3]), 8)

if __name__ == "__main__":
    unittest.main()