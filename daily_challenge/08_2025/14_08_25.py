"""
Given an integer n, return true if it is a power of four. Otherwise, return false.
An integer n is a power of four, if there exists an integer x such that n == 4x.
"""

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n == 0:
            return False
        n = bin(n)[2:]
        zs = len(n)-1
        if zs%2==0:
            if n[1:] == '0'*zs:
                return True
        return False
    
# Unit tests
import unittest
class TestPowerOfFour(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_is_power_of_four(self):
        self.assertTrue(self.solution.isPowerOfFour(16))
        self.assertFalse(self.solution.isPowerOfFour(5))
        self.assertTrue(self.solution.isPowerOfFour(1))
        self.assertFalse(self.solution.isPowerOfFour(0))
        self.assertTrue(self.solution.isPowerOfFour(64))

if __name__ == "__main__":
    unittest.main()