"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
class Solution:
    def rotate(self, nums, k):
        n=len(nums)
        k=k%n
        nums[:]= nums[-k:]+ nums[:-k]
        return
    
# Example usage:
sol = Solution()
arr = [1, 2, 3, 4, 5, 6, 7]
k = 3
sol.rotate(arr, k)
print(arr)  # Output: [5, 6, 7, 1, 2, 3, 4]
# This will rotate the array to the right by 3 steps.
# The function modifies the input list in place.
# Note: The function does not return anything as it modifies the input list directly.