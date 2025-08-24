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
    
