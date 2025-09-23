"""
https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?envType=daily-question&envId=2025-09-22
"""
from typing import List

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1
        max_freq = max(freq.values())
        total = 0
        for value in freq.values():
            if value == max_freq:
                total += value

        return total