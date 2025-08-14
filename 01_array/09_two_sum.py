"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
from typing import List

class Solution(object):
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []
    
# Unit tests
import unittest
class TestTwoSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_two_sum(self):
        self.assertEqual(self.solution.twoSum([2, 7, 11, 15], 9), [0, 1])
        self.assertEqual(self.solution.twoSum([3, 2, 4], 6), [1, 2])
        self.assertEqual(self.solution.twoSum([3, 3], 6), [0, 1])
        self.assertEqual(self.solution.twoSum([1, 5, 3, 4], 8), [1, 2])
        self.assertEqual(self.solution.twoSum([0, 4, 3, 0], 0), [0, 3])

if __name__ == "__main__":
    unittest.main()