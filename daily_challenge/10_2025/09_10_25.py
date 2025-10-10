""""
https://leetcode.com/problems/taking-maximum-energy-from-the-mystic-dungeon/description/?envType=daily-question&envId=2025-10-10
"""

from typing import List

class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        for i in range(len(energy) - k - 1, -1, -1):
            energy[i] += energy[i + k]
        return max(energy)
    
# Unit test
import unittest
class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.maximumEnergy([1,-2,0,9,-1,-2], 3), 10)
        self.assertEqual(s.maximumEnergy([3,-1,-1,4,-1,5], 2), 9)
        self.assertEqual(s.maximumEnergy([-5,-3,-3,-2,-1], 2), -1)
        self.assertEqual(s.maximumEnergy([10,20,30], 1), 60)
        self.assertEqual(s.maximumEnergy([100], 1), 100)
        self.assertEqual(s.maximumEnergy([1,2,3,4,5,6], 3), 9)

if __name__ == "__main__":
    unittest.main()