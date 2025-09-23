"""
https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2025-09-22
"""
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        max_freq = max(freq.values())
        total = 0
        for value in freq.values():
            if value == max_freq:
                total += value

        return total
    
# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxFrequencyElements(self):
        self.assertEqual(self.solution.maxFrequencyElements([1,2,3,1,2,3,3]), 3)
        self.assertEqual(self.solution.maxFrequencyElements([1,1,1,2,2,3]), 3)
        self.assertEqual(self.solution.maxFrequencyElements([1,2,3,4]), 4)
        self.assertEqual(self.solution.maxFrequencyElements([5,5,5,5,5]), 5)
        self.assertEqual(self.solution.maxFrequencyElements([]), 0)

if __name__ == "__main__":
    unittest.main()