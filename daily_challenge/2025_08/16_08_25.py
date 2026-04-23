"""
Medium?
https://leetcode.com/problems/new-21-game/description/
"""
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        pp = [0] * (n + 1)
        pp[0] = 1
        tail = 1 if k > 0 else 0
        for i in range(1, n+1):
            pp[i] = tail/maxPts
            if i < k:
                tail += pp[i]
            if i - maxPts >= 0 and i - maxPts < k:
                tail -= pp[i - maxPts]
        return sum(pp[k:])
    
# Unit tests
import unittest
class TestNew21Game(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_new21Game(self):
        self.assertAlmostEqual(self.solution.new21Game(10, 1, 10), 1.0)
        self.assertAlmostEqual(self.solution.new21Game(6, 1, 10), 0.6)
        self.assertAlmostEqual(self.solution.new21Game(21, 17, 10), 0.73278)

if __name__ == '__main__':
    unittest.main()