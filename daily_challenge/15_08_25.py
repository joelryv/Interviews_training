"""
You are given a positive integer num consisting only of digits 6 and 9.
Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        n = [c for c in str(num)]
        for i, c in enumerate(n):
            if c=='6':
                n[i] = '9'
                break
        res = int(''.join(n))
        return(res)
    
# Unit tests
import unittest
class TestMaximum69Number(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_maximum69Number(self):
        self.assertEqual(self.solution.maximum69Number(9669), 9969)
        self.assertEqual(self.solution.maximum69Number(9996), 9999)
        self.assertEqual(self.solution.maximum69Number(9999), 9999)
        self.assertEqual(self.solution.maximum69Number(6666), 9666)
        self.assertEqual(self.solution.maximum69Number(6969), 9969)

if __name__ == "__main__":
    unittest.main()