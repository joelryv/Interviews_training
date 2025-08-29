"""
https://leetcode.com/problems/alice-and-bob-playing-flower-game/description/?envType=daily-question&envId=2025-08-29
"""

class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        return (m * n) // 2
    
# Unittests
import unittest

class TestSolution(unittest.TestCase):
    
    def test_case_1(self):
        n, m = 2, 3
        expected = 3
        self.assertEqual(Solution().flowerGame(n, m), expected)
    
    def test_case_2(self):
        n, m = 1, 1
        expected = 0
        self.assertEqual(Solution().flowerGame(n, m), expected)
        
    def test_case_3(self):
        n, m = 4, 5
        expected = 10
        self.assertEqual(Solution().flowerGame(n, m), expected)
    
if __name__ == "__main__":
    unittest.main()