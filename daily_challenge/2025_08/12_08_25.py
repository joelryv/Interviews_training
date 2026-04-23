"""
https://leetcode.com/problems/power-of-three/description/
"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n < 1:
            return False
        while n % 3 == 0:
            n //= 3
        return n == 1
    
# Unit tests
import unittest
class TestPowerOfThree(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_isPowerOfThree(self):
        self.assertTrue(self.solution.isPowerOfThree(27))  # 3^3
        self.assertFalse(self.solution.isPowerOfThree(0))  # Not a power of three
        self.assertFalse(self.solution.isPowerOfThree(-1)) # Not a power of three
        self.assertTrue(self.solution.isPowerOfThree(1))   # 3^0

if __name__ == "__main__":
    unittest.main()