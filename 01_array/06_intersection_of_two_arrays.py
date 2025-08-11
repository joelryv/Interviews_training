"""
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        nums1.sort()
        nums2.sort()
        res = []
        i1 = i2 = 0
        times = min([len(nums1), len(nums2)])
        
        while i1 < times:
            if nums1[i1] == nums2[i2]:
                res.append(nums1[i1])
                i1 += 1
                i2 += 1
            elif nums1[i1] < nums2[i2]:
                i1 += 1
            else:
                i2 += 1
            if i2 == len(nums2):
                break
        return res
    
# Unit tests
import unittest
class TestIntersectionOfTwoArrays(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_intersect(self):
        self.assertEqual(self.solution.intersect([1, 2, 2, 1], [2, 2]), [2, 2])
        self.assertEqual(self.solution.intersect([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9])
        self.assertEqual(self.solution.intersect([], [1]), [])
        self.assertEqual(self.solution.intersect([1], []), [])
        self.assertEqual(self.solution.intersect([1, 2, 3], [4, 5, 6]), [])

if __name__ == "__main__":
    unittest.main()