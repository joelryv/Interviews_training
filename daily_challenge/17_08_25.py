"""
https://leetcode.com/problems/24-game/?envType=daily-question&envId=2025-08-18
"""
from typing import List

class Solution:
    def judgePoint24(self, cards: List[int]) -> bool:
        EPS = 1e-6

        def dfs(nums: List[float]) -> bool:
            if len(nums) == 1:
                return abs(nums[0] - 24.0) < EPS

            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    next_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    a, b = nums[i], nums[j]
                    candidates = [a + b, a - b, b - a, a * b]
                    if abs(b) > EPS:
                        candidates.append(a / b)
                    if abs(a) > EPS:
                        candidates.append(b / a)

                    for val in candidates:
                        if dfs(next_nums + [val]):
                            return True
            return False

        return dfs([float(x) for x in cards])
    
# Unit tests
import unittest
class TestSolution(unittest.TestCase):
    def test_judgePoint24(self):
        sol = Solution()
        self.assertTrue(sol.judgePoint24([4, 1, 8, 7]))
        self.assertFalse(sol.judgePoint24([1, 2, 1, 2]))
        self.assertTrue(sol.judgePoint24([8, 1, 6, 6]))

if __name__ == "__main__":
    unittest.main()