"""
https://leetcode.com/problems/number-of-zero-filled-subarrays/description/?envType=daily-question&envId=2025-08-19
"""

from typing import List
class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        def subarrayCount(n):
            count = 0
            while n > 0:
                count += n
                n -= 1
            return count
        current = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                current += 1
            else:
                total += subarrayCount(current)
                current = 0
        if current != 0:
            total += subarrayCount(current)
        return total
    
class Solution2:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        total = 0
        n = 0
        for num in nums:
            if num == 0:
                n += 1
            else:
                total += (n * (n + 1)) // 2
                n = 0
        total += (n * (n + 1)) // 2
        return total

# Unit tests for solution 1
def test_solution():
    sol = Solution()
    assert sol.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6
    assert sol.zeroFilledSubarray([0, 0, 0]) == 6
    assert sol.zeroFilledSubarray([1, 2, 3]) == 0
    assert sol.zeroFilledSubarray([0]) == 1
    assert sol.zeroFilledSubarray([]) == 0

# Unit tests for solution 2
def test_solution2():
    sol2 = Solution2()
    assert sol2.zeroFilledSubarray([1, 3, 0, 0, 2, 0, 0, 4]) == 6
    assert sol2.zeroFilledSubarray([0, 0, 0]) == 6
    assert sol2.zeroFilledSubarray([1, 2, 3]) == 0
    assert sol2.zeroFilledSubarray([0]) == 1
    assert sol2.zeroFilledSubarray([]) == 0

if __name__ == "__main__":
    test_solution()
    test_solution2()
    print("All tests passed!")