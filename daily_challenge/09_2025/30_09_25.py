"""
https://leetcode.com/problems/find-triangular-sum-of-an-array/?envType=daily-question&envId=2025-09-30
"""

from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        while n > 1:
            nums = [(nums[i] + nums[i+1])%10 for i in range(n-1)]
            n -= 1
        return nums[0]
    
