"""
https://leetcode.com/explore/interview/card/top-interview-questions-easy/127/strings/881/
"""
class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}
        for char in s:
            count[char] = count.get(char, 0) + 1
        for i, char in enumerate(s):
            if count[char] == 1:
                return i
        return -1
    
# Unittests
import unittest 
class TestFirstUniqueCharacter(unittest.TestCase):
    def test_example1(self):
        s = "leetcode"
        expected = 0
        self.assertEqual(Solution().firstUniqChar(s), expected)

    def test_example2(self):
        s = "loveleetcode"
        expected = 2
        self.assertEqual(Solution().firstUniqChar(s), expected)

    def test_example3(self):
        s = "aabb"
        expected = -1
        self.assertEqual(Solution().firstUniqChar(s), expected)

    def test_empty_string(self):
        s = ""
        expected = -1
        self.assertEqual(Solution().firstUniqChar(s), expected)

    def test_single_character(self):
        s = "z"
        expected = 0
        self.assertEqual(Solution().firstUniqChar(s), expected)

    def test_all_repeating_characters(self):
        s = "aaabbbccc"
        expected = -1
        self.assertEqual(Solution().firstUniqChar(s), expected)

    def test_first_character_unique(self):
        s = "zxyxzy"
        expected = -1
        self.assertEqual(Solution().firstUniqChar(s), expected)

    def test_last_character_unique(self):
        s = "xxyyzzp"
        expected = 6
        self.assertEqual(Solution().firstUniqChar(s), expected)

if __name__ == "__main__":
    unittest.main()