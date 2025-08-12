'''
https://leetcode.com/problems/ways-to-express-an-integer-as-sum-of-powers/description/
'''

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        """
        :type n: int
        :type x: int
        :rtype: int
        """
        MOD = 10**9 + 7
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        
        for i in range(1, n + 1):
            val = i ** x
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= val:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - val]) % MOD
        return dp[n][n]
    
# Unit tests
import unittest
class TestWaysToExpressIntegerAsSumOfPowers(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_numberOfWays(self):
        self.assertEqual(self.solution.numberOfWays(10, 2), 1)  # 3^2 + 1^2
        self.assertEqual(self.solution.numberOfWays(4, 1), 2)  # 4^1, 3^1 + 1^1

if __name__ == "__main__":
    unittest.main()