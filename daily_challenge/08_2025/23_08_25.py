"""
https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/?envType=daily-question&envId=2025-08-24
"""

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zcount = 0
        longest = 0
        start = 0

        for i in range(len(nums)):
            if nums[i]==0:
                zcount += 1
            while (zcount > 1):
                if nums[start]==0:
                    zcount -= 1
                start += 1
            if (i - start) > longest:
                longest = (i - start)
        return longest
    
# Unittests
import unittest
class TestLongestSubarray(unittest.TestCase):
    def test_example1(self):
        nums = [1,1,0,1]
        expected = 3
        self.assertEqual(Solution().longestSubarray(nums), expected)

    def test_example2(self):
        nums = [0,1,1,1,0,1,1,0,1]
        expected = 5
        self.assertEqual(Solution().longestSubarray(nums), expected)

    def test_example3(self):
        nums = [1,1,1]
        expected = 2
        self.assertEqual(Solution().longestSubarray(nums), expected)

    def test_all_zeros(self):
        nums = [0,0,0]
        expected = 0
        self.assertEqual(Solution().longestSubarray(nums), expected)

    def test_single_one(self):
        nums = [1]
        expected = 0
        self.assertEqual(Solution().longestSubarray(nums), expected)

    def test_single_zero(self):
        nums = [0]
        expected = 0
        self.assertEqual(Solution().longestSubarray(nums), expected)

    def test_alternating(self):
        nums = [1,0,1,0,1]
        expected = 2
        self.assertEqual(Solution().longestSubarray(nums), expected)

    def test_long_sequence(self):
        nums = [1]*10000 + [0] + [1]*10000
        expected = 20000
        self.assertEqual(Solution().longestSubarray(nums), expected)

if __name__ == "__main__":
    unittest.main()