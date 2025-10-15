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