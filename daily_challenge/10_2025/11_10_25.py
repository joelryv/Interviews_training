"""
https://leetcode.com/problems/find-sum-of-array-product-of-magical-sequences/solutions/7267995/beats-99-explained/?envType=daily-question&envId=2025-10-12
"""

MOD = 10**9 + 7
from functools import lru_cache
import math
from typing import List

class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(remaining, odd_needed, index, carry):
            if remaining < 0 or odd_needed < 0 or remaining + carry.bit_count() < odd_needed:
                return 0
            if remaining == 0:
                return 1 if odd_needed == carry.bit_count() else 0
            if index >= len(nums):
                return 0
            
            ans = 0
            for take in range(remaining + 1):
                ways = math.comb(remaining, take) * pow(nums[index], take, MOD) % MOD
                new_carry = carry + take
                ans += ways * dfs(remaining - take, odd_needed - (new_carry % 2), index + 1, new_carry // 2)
                ans %= MOD
            return ans
        
        return dfs(m, k, 0, 0)
    
# Unit test
import unittest

class TestSolution(unittest.TestCase):
    def test_magicalSum(self):
        sol = Solution()
        self.assertEqual(sol.magicalSum(2,2,[5,4,3,2,1]),170)
        self.assertEqual(sol.magicalSum(5,5,[1,10,100,10000,1000000]), 991600007)
        self.assertEqual(sol.magicalSum(1,1,[28]),28)

if __name__ == "__main__":
    unittest.main()