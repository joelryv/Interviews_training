"""
https://leetcode.com/problems/smallest-missing-non-negative-integer-after-operations/submissions/1802972723/?envType=daily-question&envId=2025-10-16
"""

from typing import List

class Solution:
    def findSmallestInteger(self, nums: List[int], value: int) -> int:
        n = len(nums)
        mods = [0] * value
        for num in nums:
            mods[num % value] += 1
        min_i, min_mod = n + 1, n + 1
        for i, mod in enumerate(mods):
            if mod < min_mod:
                min_i = i
                min_mod = mod
        return min_mod * value + min_i