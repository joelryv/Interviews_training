"""
https://leetcode.com/problems/maximum-number-of-words-you-can-type/description/?envType=daily-question&envId=2025-09-15
"""

class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        brkn = {}
        for c in brokenLetters:
            brkn[c] = 1
        words = text.split()
        valid = len(words)
        for word in words:
            for l in word:
                if l in brkn.keys():
                    valid -= 1
                    break
        return valid
    
# Unit tests
import unittest

class TestCanBeTypedWords(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_canBeTypedWords(self):
        self.assertEqual(self.solution.canBeTypedWords("hello world", "ad"), 1)
        self.assertEqual(self.solution.canBeTypedWords("leet code", "lt"), 1)
        self.assertEqual(self.solution.canBeTypedWords("leet code", "e"), 0)
        self.assertEqual(self.solution.canBeTypedWords("a b c d e f g", "abcdefg"), 0)
        self.assertEqual(self.solution.canBeTypedWords("a b c d e f g", ""), 7)
        self.assertEqual(self.solution.canBeTypedWords("the quick brown fox jumps over the lazy dog", "aeiou"), 0)

if __name__ == "__main__":
    unittest.main()