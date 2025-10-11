"""
https://leetcode.com/problems/maximum-total-damage-with-spell-casting/?envType=daily-question&envId=2025-10-11
"""
from typing import List

class Solution:
    # once you cast a spell, disable spells with value -2 to +2
    # this is like delete and earn.
    #   - de is -1 to +1: either cur + 2ago or 1ago
    #   - this is -2 to +2: either cur + 3ago or 1ago
    def maximumTotalDamage(self, power: List[int]) -> int:
        count = {}
        for p in power:
            count[p] = count.get(p, 0) + 1
        strength = {k: k*count[k] for k in count}
        spells = [0, 0, 0] + sorted(list(strength.keys()))
        n = len(spells)
        dp = [0]*n
        for i in range(3, n):
            if spells[i] - spells[i-1] > 2:
                dp[i] = dp[i-1] + strength[spells[i]]
            elif spells[i] - spells[i-2] > 2:
                dp[i] = max(dp[i-1], dp[i-2] + strength[spells[i]])
            else:
                dp[i] = max(dp[i-1], dp[i-3] + strength[spells[i]])
        
        return dp[-1]
    
# Unit test
import unittest
class Test(unittest.TestCase):
    def test(self):
        s = Solution()
        self.assertEqual(s.maximumTotalDamage([2,2,3,3,3,4]), 9)
        self.assertEqual(s.maximumTotalDamage([1,1,1,2]), 3)
        self.assertEqual(s.maximumTotalDamage([3,4,2]), 4)
        self.assertEqual(s.maximumTotalDamage([8,10,4,9,1,3,5,9]), 24)
        self.assertEqual(s.maximumTotalDamage([1,2,3,4,5,6]), 9)
        self.assertEqual(s.maximumTotalDamage([100]), 100)
        self.assertEqual(s.maximumTotalDamage([1,1,1,1,1,1]), 6)

if __name__ == "__main__":
    unittest.main()