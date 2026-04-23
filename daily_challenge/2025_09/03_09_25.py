"""
https://leetcode.com/problems/find-closest-person/description/?envType=daily-question&envId=2025-09-04
"""
class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        d1=abs(x-z)
        d2=abs(y-z)
        if d1<d2:
            return 1
        if d2<d1:
            return 2 
        else:
            return 0
        
# Unit tests
import unittest
class TestFindClosestPerson(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_findClosest(self):
        self.assertEqual(self.solution.findClosest(1, 2, 3), 2)
        self.assertEqual(self.solution.findClosest(2, 1, 3), 1)
        self.assertEqual(self.solution.findClosest(1, 2, 2), 2)

if __name__ == "__main__":
    unittest.main()