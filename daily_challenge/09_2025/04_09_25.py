"""
https://leetcode.com/problems/minimum-operations-to-make-the-integer-zero/description/?envType=daily-question&envId=2025-09-05
"""

class Solution:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        k = 1
        while True:
            x = num1 - num2 * k
            if x < k:
                return -1
            if k >= x.bit_count():
                return k
            k += 1

class Solution2:
    def makeTheIntegerZero(self, num1: int, num2: int) -> int:
        """
        m
        num1 = num2 * m + (x = 2^i + 2^(i') + ..) term -> m

        num1 - num2 * m =  
        """

        for i in range(61):
            target = num1 - num2 * i
            if target >= 0 and target.bit_count() <= i <= target:
                return i
        
        return -1

# Unit tests
import unittest

class TestMakeTheIntegerZero(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_makeTheIntegerZero(self):
        self.assertEqual(self.solution.makeTheIntegerZero(3, 2), 1)
        self.assertEqual(self.solution.makeTheIntegerZero(5, 3), 1)
        self.assertEqual(self.solution.makeTheIntegerZero(6, 1), 2)
        self.assertEqual(self.solution.makeTheIntegerZero(10, 3), 2)

if __name__ == "__main__":
    unittest.main()