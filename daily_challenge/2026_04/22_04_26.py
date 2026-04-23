"""
You are given a 0-indexed integer array nums. There exists an array arr of length nums.length,
where arr[i] is the sum of |i - j| over all j such that nums[j] == nums[i] and j != i. If there is no such j, set arr[i] to be 0.

Return the array arr.

https://leetcode.com/problems/sum-of-distances/description/?envType=daily-question&envId=2026-04-23
"""
from typing import List

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        arr = [0] * len(nums)
        look_up = dict()
        for i in range(len(nums)):
            if nums[i] not in look_up:
                look_up[nums[i]] = []
            look_up[nums[i]].append(i)
        for group in look_up.values():
            total = sum(group)
            prefix_total = 0
            sz = len(group)
            for i, idx in enumerate(group):
                arr[idx] = total - prefix_total * 2 + idx * (2 * i - sz)
                prefix_total += idx
        return arr
    
# Test cases
import unittest

class TestSolution(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(Solution().distance([1, 3, 1, 1, 2]), [5, 0, 3, 4, 0])
        self.assertEqual(Solution().distance([0, 5, 3]), [0, 0, 0])
        self.assertEqual(Solution().distance([1, 2, 3]), [0, 0, 0])
        self.assertEqual(Solution().distance([1, 1, 1]), [3, 2, 3])
        self.assertEqual(Solution().distance([1]), [0])

if __name__ == "__main__":
    unittest.main()