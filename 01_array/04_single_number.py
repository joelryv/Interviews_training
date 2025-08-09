'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        c = dict()
        for num in nums:
            if num in c.keys():
                c[num] += 1
            else:
                c[num] = 1
        for key, value in c.items():
            if value == 1:
                return key
            
# Unit tests
import unittest
class TestSingleNumber(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_single_number(self):
        self.assertEqual(self.solution.singleNumber([4, 1, 2, 1, 2]), 4)
        self.assertEqual(self.solution.singleNumber([2, 2, 1]), 1)
        self.assertEqual(self.solution.singleNumber([1]), 1)
        self.assertEqual(self.solution.singleNumber([0, 0, -1]), -1)
        self.assertEqual(self.solution.singleNumber([-1, -1, -2]), -2)

if __name__ == "__main__":
    unittest.main()