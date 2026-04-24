"""
You are given a string moves of length n consisting only of characters 'L', 'R', and '_'. The string represents your movement on a number line starting from the origin 0.

In the ith move, you can choose one of the following directions:

move to the left if moves[i] = 'L' or moves[i] = '_'
move to the right if moves[i] = 'R' or moves[i] = '_'
Return the distance from the origin of the furthest point you can get to after n moves.

https://leetcode.com/problems/furthest-point-from-origin/description/?envType=daily-question&envId=2026-04-24
"""

class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l = 0
        r = 0
        u = 0
        for move in moves:
            if move == 'L':
                l += 1
            elif move == 'R':
                r += 1
            else:
                u += 1
        return abs(l-r)+u
    
# Unit Tests
import unittest

class TestSolution(unittest.TestCase):
    def test_furthestDistanceFromOrigin(self):
        self.assertEqual(Solution().furthestDistanceFromOrigin("L_RL__R"), 3)
        self.assertEqual(Solution().furthestDistanceFromOrigin("______"), 6)
        self.assertEqual(Solution().furthestDistanceFromOrigin("LRLRLR"), 0)
        self.assertEqual(Solution().furthestDistanceFromOrigin("LLRR__"), 2)
        self.assertEqual(Solution().furthestDistanceFromOrigin("L_R_L_R_"), 4)

if __name__ == '__main__':
    unittest.main()