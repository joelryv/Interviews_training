"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/880/
"""
class Solution:
    def reverse(self, x: int) -> int:
        n=0
        if x<0:
            n=-int(str(-x)[::-1]) 
        else:
            n= int(str(x)[::-1])
        return n if n.bit_length()<32 else 0

# Unit tests    
import unittest
class TestSolution(unittest.TestCase):
    def test_reverse(self):
        solution = Solution()
        self.assertEqual(solution.reverse(123), 321)
        self.assertEqual(solution.reverse(-123), -321)
        self.assertEqual(solution.reverse(120), 21)
        self.assertEqual(solution.reverse(0), 0)
        self.assertEqual(solution.reverse(1534236469), 0)

if __name__ == "__main__":
    unittest.main()