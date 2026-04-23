"""
https://leetcode.com/problems/adjacent-increasing-subarrays-detection-ii/description/?envType=daily-question&envId=2025-10-15
"""

from typing import List 

class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        longest, current, prev = 1, 1, 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                current += 1
            else:
                longest = max(longest, min(current, prev), current//2)
                prev = current
                current = 1
        longest = max(longest, min(current, prev), current//2)
        return longest
    
# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def test_maxIncreasingSubarrays(self):
        sol = Solution()
        self.assertEqual(sol.maxIncreasingSubarrays([9, 6, 5, 8, 7, 10]), 2)
        self.assertEqual(sol.maxIncreasingSubarrays([2, 2, 2, 2, 2]), 1)
        self.assertEqual(sol.maxIncreasingSubarrays([1, 2, 3, 4, 5]), 2)
        self.assertEqual(sol.maxIncreasingSubarrays([5, 4, 3, 2, 1]), 1)
        self.assertEqual(sol.maxIncreasingSubarrays([1, 3, 5, 4, 6, 8]), 3)
        self.assertEqual(sol.maxIncreasingSubarrays([10, 20, 30, 25, 35, 45]), 3)

if __name__ == "__main__":
    unittest.main()