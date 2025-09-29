"""
https://leetcode.com/problems/largest-perimeter-triangle/description/?envType=daily-question
"""

from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        while len(nums) >= 3:
            if (nums[-3]+nums[-2]) > nums[-1]:
                return nums[-3] + nums[-2] + nums[-1]
            nums = nums[:-1]
        return 0