"""
https://leetcode.com/problems/avoid-flood-in-the-city/description/?envType=daily-question
"""

from sortedcontainers import SortedList
from typing import List

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        ans = [1] * len(rains)
        st = SortedList()
        mp = {}
        for i, rain in enumerate(rains):
            if rain == 0:
                st.add(i)
            else:
                ans[i] = -1
                if rain in mp:
                    it = st.bisect(mp[rain])
                    if it == len(st):
                        return []
                    ans[st[it]] = rain
                    st.discard(st[it])
                mp[rain] = i
        return ans
    
# Unit tests
import unittest

class TestSolution(unittest.TestCase):
    def test_1(self):
        rains = [1,2,3,4]
        expected = [-1,-1,-1,-1]
        self.assertEqual(Solution().avoidFlood(rains), expected)

    def test_2(self):
        rains = [1,2,0,0,2,1]
        expected = [-1,-1,2,1,-1,-1]
        self.assertEqual(Solution().avoidFlood(rains), expected)

    def test_3(self):
        rains = [1,2,0,1,2]
        expected = []
        self.assertEqual(Solution().avoidFlood(rains), expected)

    def test_4(self):
        rains = [69,0,0,0,69]
        expected = [-1,69,1,1,-1]
        self.assertEqual(Solution().avoidFlood(rains), expected)

    def test_5(self):
        rains = [10,20,20]
        expected = []
        self.assertEqual(Solution().avoidFlood(rains), expected)

if __name__ == "__main__":
    unittest.main()