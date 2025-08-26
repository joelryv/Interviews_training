"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/883/
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = ''.join(c.lower() for c in s if c.isalnum())
        return filtered == filtered[::-1]
    
# Unittests
import unittest
class TestSolution(unittest.TestCase):
    def test_isPalindrome1(self):
        s = "Anita lava la tina"
        expected = True
        self.assertEqual(Solution().isPalindrome(s), expected)
    
    def test_isPalindrome2(self):
        s = "Any other thing"
        expected = False
        self.assertEqual(Solution().isPalindrome(s), expected)

if __name__ == "__main__":
    unittest.main()