"""
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = 1
        while i <= len(digits):
            if digits[-i] != 9:
                digits[-i] += 1
                return digits
            digits[-i] = 0
            i += 1
        digits = [1] + digits
        return digits

# Unit tests
import unittest
class TestPlusOne(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_plus_one(self):
        self.assertEqual(self.solution.plusOne([1, 2, 3]), [1, 2, 4])
        self.assertEqual(self.solution.plusOne([4, 3, 2, 1]), [4, 3, 2, 2])
        self.assertEqual(self.solution.plusOne([9]), [1, 0])
        self.assertEqual(self.solution.plusOne([1, 9, 9]), [2, 0, 0])
        self.assertEqual(self.solution.plusOne([0]), [1])

if __name__ == "__main__":
    unittest.main()