"""
https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/description/?envType=daily-question&envId=2025-10-14
"""

from typing import List

class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        prev = 0
        current = 1
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                current += 1
            else:
                prev = current
                current = 1
            if (current >= k and prev >= k) or current >= (2*k):
                return True
        return False
    
# Unittest
import unittest 

class TestSolution(unittest.TestCase):
    def test_hasIncreasingSubarrays(self):
        solution = Solution()
        self.assertTrue(solution.hasIncreasingSubarrays([2,4,5,3,4,5,6], 3))
        self.assertFalse(solution.hasIncreasingSubarrays([1,1,1,1], 2))
        self.assertTrue(solution.hasIncreasingSubarrays([1,2,3,4,5], 2))
        self.assertFalse(solution.hasIncreasingSubarrays([5,4,3,2,1], 2))
        self.assertTrue(solution.hasIncreasingSubarrays([1,2,1,2,1,2], 2))
        self.assertFalse(solution.hasIncreasingSubarrays([1,2,3], 2))
        self.assertTrue(solution.hasIncreasingSubarrays([1,2], 1))
        self.assertFalse(solution.hasIncreasingSubarrays([2,1], 2))
        self.assertTrue(solution.hasIncreasingSubarrays([1,2,3,4], 2))
        self.assertFalse(solution.hasIncreasingSubarrays([3,2,1], 2))

if __name__ == "__main__":
    unittest.main()