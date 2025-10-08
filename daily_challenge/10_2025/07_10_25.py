"""
https://leetcode.com/problems/successful-pairs-of-spells-and-potions/?envType=daily-question&envId=2025-10-08
"""

from typing import List

class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        out = [0]*len(spells)
        potions.sort()
        for i, spell in enumerate(spells):
            start = 0
            end = len(potions) -  1
            index = len(potions)
            while start <= end:
                mid = (start+end)//2
                if potions[mid]*spell >= success:
                    index = mid
                    end = mid - 1
                else:
                    start = mid + 1
            out[i] = len(potions) - index
        return out