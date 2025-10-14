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
    
