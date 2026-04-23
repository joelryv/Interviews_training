"""
https://leetcode.com/problems/number-of-people-aware-of-a-secret/description/?envType=daily-question&envId=2025-09-09
"""

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        knows = [0] * n
        knows[0] = 1
        shared = 0
        total = 1

        for day in range(delay, forget):
            shared += knows[day - delay]
            total += shared
            knows[day] = shared 

        for day in range(forget, n):
            shared += knows[day - delay] - knows[day - forget]
            total += shared - knows[day - forget]
            knows[day] = shared
        
        return (total%(10**9+7))
    
# Unit tests
import unittest

class TestPeopleAwareOfSecret(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_peopleAwareOfSecret(self):
        self.assertEqual(self.solution.peopleAwareOfSecret(6, 2, 4), 5)
        self.assertEqual(self.solution.peopleAwareOfSecret(4, 1, 3), 6)
        self.assertEqual(self.solution.peopleAwareOfSecret(10, 1, 5), 416)

if __name__ == "__main__":
    unittest.main()