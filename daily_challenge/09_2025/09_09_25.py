"""
https://leetcode.com/problems/minimum-number-of-people-to-teach/description/?envType=daily-question&envId=2025-09-10
"""
from typing import List

class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        no_comm = {}
        for pair in friendships:
            comm = False
            for lan in languages[pair[0] - 1]:
                if lan in languages[pair[1] - 1]:
                    comm = True
                    break
            if comm == False:
                no_comm[pair[0] - 1] = 1
                no_comm[pair[1] - 1] = 1
        
        known_language = {}
        for key in no_comm.keys():
            for lan in languages[key]:
                known_language[lan] = known_language.get(lan, 0) + 1

        m_count = 0
        for key, value in known_language.items():
            if value > m_count:
                m_count = value

        return len(no_comm) - m_count
    
# Unit tests
import unittest

class TestMinimumTeachings(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_minimumTeachings(self):
        self.assertEqual(self.solution.minimumTeachings(2, [[1],[2],[1,2]], [[1,2],[1,3],[2,3]]), 1)
        self.assertEqual(self.solution.minimumTeachings(3, [[2],[1,3],[1,2],[3]], [[1,4],[1,2],[3,4],[2,3]]), 2)
        self.assertEqual(self.solution.minimumTeachings(3, [[1,2,3],[1,2,3],[1,2,3]], [[1,2],[2,3],[3,1]]), 0)
        self.assertEqual(self.solution.minimumTeachings(3, [[1],[2],[3]], [[1,2],[2,3],[3,1]]), 2)

if __name__ == "__main__":
    unittest.main()