"""
Write a function that reverses a string. The input string is given as an array of characters s.
You must do this by modifying the input array in-place with O(1) extra memory.
"""

from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

# Unit tests for the solution
def test_solution():
    sol = Solution()
    s1 = ["h", "e", "l", "l", "o"]
    sol.reverseString(s1)
    assert s1 == ["o", "l", "l", "e", "h"]

    s2 = ["H", "a", "n", "n", "a", "h"]
    sol.reverseString(s2)
    assert s2 == ["h", "a", "n", "n", "a", "H"]

    s3 = ["A"]
    sol.reverseString(s3)
    assert s3 == ["A"]

    s4 = []
    sol.reverseString(s4)
    assert s4 == []

    s5 = ["a", "b"]
    sol.reverseString(s5)
    assert s5 == ["b", "a"]

if __name__ == "__main__":
    test_solution()
    print("All tests passed!")