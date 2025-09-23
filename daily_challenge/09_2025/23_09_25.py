"""
https://leetcode.com/problems/compare-version-numbers/description/?envType=daily-question&envId=2025-09-23
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = [int(x) for x in version1.split('.')]
        v2 = [int(x) for x in version2.split('.')]
        max_l = max([len(v1), len(v2)])
        while len(v1) < max_l:
            v1.append(0)
        while len(v2) < max_l:
            v2.append(0)

        for n1, n2 in zip(v1, v2):
            if n1 < n2:
                return -1
            if n1 > n2:
                return 1
        return 0
    
# Unittest
import unittest

class TestSolution(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_compareVersion(self):
        self.assertEqual(self.solution.compareVersion("1.01", "1.001"), 0)
        self.assertEqual(self.solution.compareVersion("1.0", "1.0.0"), 0)
        self.assertEqual(self.solution.compareVersion("0.1", "1.1"), -1)
        self.assertEqual(self.solution.compareVersion("1.0.1", "1"), 1)

if __name__ == "__main__":
    unittest.main()