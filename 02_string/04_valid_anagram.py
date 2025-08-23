"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/882/
"""
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for c in t:
            d[c] = d.get(c, -1) - 1
        for key, value in d.items():
            if value != 0:
                return False
        return True

# Unittests
import unittest
class TestValidAnagram(unittest.TestCase):
    def test_example1(self):
        s = "anagram"
        t = "nagaram"
        expected = True
        self.assertEqual(Solution().isAnagram(s, t), expected)

    def test_example2(self):
        s = "rat"
        t = "car"
        expected = False
        self.assertEqual(Solution().isAnagram(s, t), expected)

    def test_empty_strings(self):
        s = ""
        t = ""
        expected = True
        self.assertEqual(Solution().isAnagram(s, t), expected)

    def test_different_lengths(self):
        s = "a"
        t = "ab"
        expected = False
        self.assertEqual(Solution().isAnagram(s, t), expected)

    def test_case_sensitivity(self):
        s = "aA"
        t = "Aa"
        expected = True
        self.assertEqual(Solution().isAnagram(s, t), expected)

    def test_special_characters(self):
        s = "a!b@c#"
        t = "c#b@a!"
        expected = True
        self.assertEqual(Solution().isAnagram(s, t), expected)

    def test_unicode_characters(self):
        s = "你好"
        t = "好你"
        expected = True
        self.assertEqual(Solution().isAnagram(s, t), expected)

if __name__ == "__main__":
    unittest.main()