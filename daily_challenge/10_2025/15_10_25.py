"""
https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/submissions/1802972723/?envType=daily-question&envId=2025-10-16
"""

from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        mods = [0] * value
        for num in nums:
            mods[num % value] += 1
        min_i, min_mod = n + 1, n + 1
        for i, mod in enumerate(mods):
            if mod < min_mod:
                min_i = i
                min_mod = mod
        return min_mod * value + min_i
    

# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        nums = [1, -10, 7, 13, 6, 8]
        value = 5
        expected = 4
        self.assertEqual(self.solution.findSmallestInteger(nums, value), expected)

    def test_example2(self):
        nums = [0, 1, 2, 3]
        value = 4
        expected = 4
        self.assertEqual(self.solution.findSmallestInteger(nums, value), expected)

    def test_additional1(self):
        nums = [5, 10, 15]
        value = 5
        expected = 1
        self.assertEqual(self.solution.findSmallestInteger(nums, value), expected)

    def test_additional2(self):
        nums = [-1, -2, -3]
        value = 4
        expected = 0
        self.assertEqual(self.solution.findSmallestInteger(nums, value), expected)

    def test_additional3(self):
        nums = [0, 0, 0]
        value = 1
        expected = 3
        self.assertEqual(self.solution.findSmallestInteger(nums, value), expected)


if __name__=='__main__':
    unittest.main()