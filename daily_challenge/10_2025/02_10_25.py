"""
https://leetcode.com/problems/water-bottles-ii/submissions/1788889507/?envType=daily-question&envId=2025-10-02
"""

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty = 0
        totalDrunk = 0
        while numBottles > 0:
            totalDrunk += numBottles
            empty += numBottles
            numBottles = 0
            while empty >= numExchange:
                empty -= numExchange
                numExchange += 1
                numBottles += 1
        return totalDrunk
    

# Unit tests
import unittest
class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maxBottlesDrunk(self):
        self.assertEqual(self.solution.maxBottlesDrunk(9, 3), 11)
        self.assertEqual(self.solution.maxBottlesDrunk(15, 4), 18)
        self.assertEqual(self.solution.maxBottlesDrunk(5, 5), 6)
        self.assertEqual(self.solution.maxBottlesDrunk(2, 3), 2)
        self.assertEqual(self.solution.maxBottlesDrunk(6, 2), 8)
    
if __name__ == "__main__":
    unittest.main()