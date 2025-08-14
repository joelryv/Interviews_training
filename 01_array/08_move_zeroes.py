"""
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
Note that you must do this in-place without making a copy of the array.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        pos = 0
        for j in range(len(nums)):
            if nums[j]!=0:
                nums[j],nums[pos]=nums[pos],nums[j]
                pos+=1
        return pos
    
# Unit tests
import unittest
class TestMoveZeroes(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_move_zeroes(self):
        nums1 = [0, 1, 0, 3, 12]
        self.solution.moveZeroes(nums1)
        self.assertEqual(nums1, [1, 3, 12, 0, 0])

        nums2 = [0]
        self.solution.moveZeroes(nums2)
        self.assertEqual(nums2, [0])

        nums3 = [1, 2, 3]
        self.solution.moveZeroes(nums3)
        self.assertEqual(nums3, [1, 2, 3])

        nums4 = [0, 0, 1]
        self.solution.moveZeroes(nums4)
        self.assertEqual(nums4, [1, 0, 0])

if __name__ == "__main__":
    unittest.main()