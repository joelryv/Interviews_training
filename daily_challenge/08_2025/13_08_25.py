"""
You are given a string num representing a large integer. An integer is good if it meets the following conditions:
It is a substring of num with length 3.
It consists of only one unique digit.
Return the maximum good integer as a string or an empty string "" if no such integer exists.
Note:
A substring is a contiguous sequence of characters within a string.
There may be leading zeroes in num or a good integer.
"""

class Solution(object):
    def largestGoodInteger(self, num):
        """
        :type num: str
        :rtype: str
        """
        max_good = ""
        for i in range(len(num) - 2):
            if num[i] == num[i + 1] == num[i + 2]:
                good_int = num[i:i + 3]
                if good_int > max_good:
                    max_good = good_int
        return max_good

# Unit tests
import unittest

class TestLargestGoodInteger(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_largest_good_integer(self):
        self.assertEqual(self.solution.largestGoodInteger("6777133339"), "777")
        self.assertEqual(self.solution.largestGoodInteger("2300019"), "000")
        self.assertEqual(self.solution.largestGoodInteger("42352338"), "")
        self.assertEqual(self.solution.largestGoodInteger("999"), "999")
        self.assertEqual(self.solution.largestGoodInteger("1234567890"), "")
        self.assertEqual(self.solution.largestGoodInteger("111222333444555666777888999000"), "999")

if __name__ == "__main__":
    unittest.main()