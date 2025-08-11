'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
'''

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l1 = len(nums)
        return l1 > len(set(nums))
    
# Unit tests
import unittest
class TestContainsDuplicate(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_contains_duplicate(self):
        self.assertTrue(self.solution.containsDuplicate([1, 2, 3, 1]))
        self.assertFalse(self.solution.containsDuplicate([1, 2, 3, 4]))
        self.assertTrue(self.solution.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
        self.assertFalse(self.solution.containsDuplicate([]))
        self.assertFalse(self.solution.containsDuplicate([1]))

if __name__ == "__main__":
    unittest.main()