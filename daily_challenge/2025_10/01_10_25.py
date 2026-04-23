"""
https://leetcode.com/problems/water-bottles/description/?envType=daily-question
"""

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        total = numBottles
        while True:
            exchange = numBottles//numExchange
            if exchange == 0:
                return total
            total += exchange
            residuo = numBottles%numExchange
            numBottles = exchange + residuo

# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numWaterBottles(self):
        self.assertEqual(self.solution.numWaterBottles(9, 3), 13)
        self.assertEqual(self.solution.numWaterBottles(15, 4), 19)
        self.assertEqual(self.solution.numWaterBottles(5, 5), 6)
        self.assertEqual(self.solution.numWaterBottles(2, 3), 2)
        self.assertEqual(self.solution.numWaterBottles(6, 2), 11)

if __name__ == "__main__":
    unittest.main()