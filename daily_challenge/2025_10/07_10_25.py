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
    
# Unit test
import unittest

class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.successfulPairs([5,1,3],[1,2,3,4,5],7),[4,0,3])
        self.assertEqual(s.successfulPairs([3,1,2],[8,5,8],16),[2,0,2])
        self.assertEqual(s.successfulPairs([15,8,9,3,5,7,2,4,10,6,11,1,12,14,13],[1,2,3,4,5,6,7,8,9,10],30),[9, 7, 7, 1, 5, 6, 0, 3, 8, 6, 8, 0, 8, 8, 8])
        self.assertEqual(s.successfulPairs([1,2,3,4,5],[1,2,3,4,5],1),[5,5,5,5,5])

if __name__ == "__main__":
    unittest.main()