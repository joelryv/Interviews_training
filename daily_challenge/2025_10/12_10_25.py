"""
https://leetcode.com/problems/find-resultant-array-after-removing-anagrams/description/?envType=daily-question&envId=2025-10-13
"""

from typing import List

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result = [words[0]]
        for i in range(1, len(words)):
            current = sorted(result[-1])
            if sorted(words[i]) != current:
                result.append(words[i])
        return result
    
# Unit test
import unittest

class TestSolution(unittest.TestCase):
    def test_removeAnagrams(self):
        sol = Solution()
        self.assertEqual(sol.removeAnagrams(["abba","baba","bbaa","cd","cd"]), ["abba","cd"])
        self.assertEqual(sol.removeAnagrams(["a","b","c","d","e"]), ["a","b","c","d","e"])
        self.assertEqual(sol.removeAnagrams(["a","a","a","b"]), ["a","b"])
        self.assertEqual(sol.removeAnagrams(["a"]), ["a"])
        self.assertEqual(sol.removeAnagrams(["ab","ba"]), ["ab"])
        self.assertEqual(sol.removeAnagrams(["abc","bca","cab","xyz","zyx"]), ["abc","xyz"])

if __name__ == "__main__":
    unittest.main()